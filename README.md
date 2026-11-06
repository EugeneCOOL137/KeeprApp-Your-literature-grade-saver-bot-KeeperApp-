# KeeprApp-Your-literature-grade-saver-bot-KeeperApp-
Your literature coach in the form of an app./Твой литературный тренер в форме приложения
# 🔮 Keeper of Tales — Хранитель Сказок

[🇷🇺 Русский](#русский) | [🇬🇧 English](#english)

---

<a id="русский"></a>
## 🇷🇺 Русский

Интерактивная игра-квест на Python, где ты спасаешь мир сказок, отвечая на вопросы о любимых историях.

### 🎮 Особенности

- 5 режимов сложности (от лёгкого до легендарного)
- 115 уникальных вопросов
- Секретная концовка
- Авторская музыка
- Красивый интерфейс с картинками
- Поддержка русского и английского языков
- Сохранение прогресса и истории чата

### ⚠️ ВАЖНО: Структура файлов

**Файл `KeeperApp.exe` и папка `_internal` должны лежать в ОДНОЙ папке!** Иначе приложение работать не будет.

Правильная структура:
```
📁 KeeperApp/
├── 📄 KeeperApp.exe          ← запускаемый файл
└── 📁 _internal/             ← ОБЯЗАТЕЛЬНО рядом с exe!
    ├── 📁 assets/
    │   ├── 📁 icons/
    │   └── 📁 backgrounds/
    ├── 📁 audio/
    ├── content.py
    ├── legendary_content.py
    ├── bot_logic.py
    └── database.py
```

❌ **НЕЛЬЗЯ:**
- Перемещать `KeeperApp.exe` отдельно от `_internal`
- Копировать только exe без папки `_internal`
- Распаковывать файлы в разные папки

✅ **МОЖНО:**
- Перемещать всю папку `KeeperApp` целиком куда угодно
- Копировать всю папку на флешку или другу

### 🚀 Как запустить

1. Скачай все файлы из репозитория
2. Убедись, что `KeeperApp.exe` и папка `_internal` лежат в одной папке
3. Запусти `KeeperApp.exe` двойным кликом
4. Наслаждайся игрой! 🔮

> 💡 **Примечание:** Если антивирус ругается на exe — это ложная тревога. Добавь папку в исключения.

### 🎯 Управление

| Команда | Описание |
|---------|----------|
| `/start` | Начать игру |
| `/menu` | Меню |
| `/lang` | Сменить язык |
| `/easy` | Лёгкий режим (3 варианта) |
| `/medium` | Средний режим (4 варианта) |
| `/hard` | Сложный режим (5 вариантов) |
| `/extreme` | Экстрим (7 вариантов, мгновенная смерть) |
| `/legendary` | Легендарный (100 вопросов, 3 жизни) |
| `/keeper` | Секретная концовка |
| `Ctrl+C` | Копировать текст |
| `Ctrl+V` | Вставить текст |
| `F5` | Очистить чат |

### 📦 Сборка из исходного кода

Если хочешь собрать приложение сам:

1. Установи Python 3.8+
2. Установи зависимости:
```bash
pip install pygame Pillow pyinstaller
```
3. Собери exe:
```bash
python -m PyInstaller --console --icon=icon_logo.ico --collect-all pygame --collect-all PIL --add-data "content.py;." --add-data "legendary_content.py;." --add-data "bot_logic.py;." --add-data "database.py;." --add-data "audio;audio" --add-data "assets;assets" --name "KeeperApp" App.py --noconfirm
```

### 🛠 Технологии

- Python 3.8
- Tkinter (интерфейс)
- Pygame (музыка)
- Pillow (картинки)
- SQLite (база данных)
- PyInstaller (сборка в .exe)

---

<a id="english"></a>
## 🇬🇧 English

An interactive Python quest game where you save the world of tales by answering questions about your favorite stories.

### 🎮 Features

- 5 difficulty modes (from easy to legendary)
- 115 unique questions
- Secret ending
- Original music
- Beautiful interface with images
- Russian and English language support
- Progress and chat history saving

### ⚠️ IMPORTANT: File Structure

**The `KeeperApp.exe` file and the `_internal` folder MUST be in the SAME folder!** Otherwise, the application will not work.

Correct structure:
```
📁 KeeperApp/
├── 📄 KeeperApp.exe          ← executable file
└── 📁 _internal/             ← MUST be next to exe!
    ├── 📁 assets/
    │   ├── 📁 icons/
    │   └── 📁 backgrounds/
    ├── 📁 audio/
    ├── content.py
    ├── legendary_content.py
    ├── bot_logic.py
    └── database.py
```

❌ **DO NOT:**
- Move `KeeperApp.exe` separately from `_internal`
- Copy only exe without the `_internal` folder
- Extract files into different folders

✅ **YOU CAN:**
- Move the entire `KeeperApp` folder anywhere
- Copy the entire folder to a USB drive or share with a friend

### 🚀 How to Run

1. Download all files from the repository
2. Make sure `KeeperApp.exe` and the `_internal` folder are in the same directory
3. Run `KeeperApp.exe` with a double click
4. Enjoy the game! 🔮

> 💡 **Note:** If antivirus warns about the exe — it's a false positive. Add the folder to exceptions.

### 🎯 Controls

| Command | Description |
|---------|-------------|
| `/start` | Start the game |
| `/menu` | Menu |
| `/lang` | Change language |
| `/easy` | Easy mode (3 options) |
| `/medium` | Medium mode (4 options) |
| `/hard` | Hard mode (5 options) |
| `/extreme` | Extreme (7 options, instant death) |
| `/legendary` | Legendary (100 questions, 3 lives) |
| `/keeper` | Secret ending |
| `Ctrl+C` | Copy text |
| `Ctrl+V` | Paste text |
| `F5` | Clear chat |

### 📦 Build from Source

If you want to build the application yourself:

1. Install Python 3.8+
2. Install dependencies:
```bash
pip install pygame Pillow pyinstaller
```
3. Build the exe:
```bash
python -m PyInstaller --console --icon=icon_logo.ico --collect-all pygame --collect-all PIL --add-data "content.py;." --add-data "legendary_content.py;." --add-data "bot_logic.py;." --add-data "database.py;." --add-data "audio;audio" --add-data "assets;assets" --name "KeeperApp" App.py --noconfirm
```

### 🛠 Technologies

- Python 3.8
- Tkinter (interface)
- Pygame (music)
- Pillow (images)
- SQLite (database)
- PyInstaller (exe build)

### 📄 License

MIT License — see [LICENSE](LICENSE) file for details.

---

Made with ❤️ by [EugeneCOOL137]
