
# database.py
import sqlite3
import os
import sys

# Определяем путь к базе данных (работает и в .exe, и в Python)
if getattr(sys, 'frozen', False):
    DB_PATH = os.path.join(os.path.dirname(sys.executable), "bot_data.db")
else:
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bot_data.db")

def init_db():
    """Инициализация базы данных"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Таблица игроков
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS players (
            user_id INTEGER PRIMARY KEY,
            language TEXT DEFAULT 'ru',
            difficulty TEXT,
            step INTEGER,
            errors INTEGER,
            perfect BOOLEAN,
            trophy BOOLEAN DEFAULT 0
        )
    ''')
    
    # Таблица сообщений чата
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            sender TEXT,
            text TEXT,
            timestamp TEXT
        )
    ''')
    
    try:
        cursor.execute("ALTER TABLE players ADD COLUMN trophy BOOLEAN DEFAULT 0")
        conn.commit()
    except:
        pass
    
    conn.close()

def get_player(uid):
    """Получить данные игрока"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT language, difficulty, step, errors, perfect, trophy FROM players WHERE user_id = ?", (uid,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return {
            "language": result[0] or 'ru',
            "difficulty": result[1],
            "step": result[2],
            "errors": result[3],
            "perfect": bool(result[4]),
            "trophy": bool(result[5])
        }
    return None

def save_player(uid, language, difficulty, step, errors, perfect, trophy=False):
    """Сохранить данные игрока"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO players (user_id, language, difficulty, step, errors, perfect, trophy)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (uid, language, difficulty, step, errors, int(perfect), int(trophy)))
    conn.commit()
    conn.close()

def reset_player(uid):
    """Сбросить данные игрока"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT trophy FROM players WHERE user_id = ?", (uid,))
    result = cursor.fetchone()
    trophy = bool(result[0]) if result else False
    cursor.execute("DELETE FROM players WHERE user_id = ?", (uid,))
    conn.commit()
    conn.close()
    return trophy

def set_trophy(uid):
    """Установить трофей"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE players SET trophy = 1 WHERE user_id = ?", (uid,))
    conn.commit()
    conn.close()

# ================= НОВЫЕ ФУНКЦИИ ДЛЯ ЧАТА =================

def save_message(uid, sender, text, timestamp):
    """Сохранить сообщение в базу"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (user_id, sender, text, timestamp)
        VALUES (?, ?, ?, ?)
    ''', (uid, sender, text, timestamp))
    conn.commit()
    conn.close()

def get_messages(uid):
    """Получить все сообщения пользователя"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT sender, text, timestamp FROM messages 
        WHERE user_id = ? 
        ORDER BY id ASC
    ''', (uid,))
    results = cursor.fetchall()
    conn.close()
    return [{"sender": r[0], "text": r[1], "timestamp": r[2]} for r in results]

def clear_messages(uid):
    """Очистить историю чата"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages WHERE user_id = ?", (uid,))
    conn.commit()
    conn.close()