# 🔮 Keeper of Tales — Хранитель Сказок

[🇷🇺 Русский](#русский) | [🇬🇧 English](#english)

---

<a id="русский"></a>
## 🇷🇺 Русский

Интерактивная игра-квест, где ты спасаешь мир сказок, отвечая на вопросы о любимых историях.

### 🎮 Особенности
- 5 режимов сложности (от лёгкого до легендарного)
- 115+ уникальных вопросов
- Секретная концовка
- Авторская музыка и красивый интерфейс
- Поддержка русского и английского языков
- Сохранение прогресса и истории чата

### 🚀 Как запустить (Исходный код)
Этот репозиторий содержит исходный код проекта. Чтобы запустить его:

1. Нажми зелёную кнопку **Code** сверху → **Download ZIP**.
2. Распакуй архив в любую папку.
3. Установи **Python 3.x** (работает на любых современных версиях, включая **3.15**).
4. Открой терминал в папке с проектом и установи библиотеки:
   ```bash
   pip install pygame Pillow
   ```
5. Запусти игру:
   ```bash
   python App.py
   ```

### 📦 Как получить готовую игру (.exe)
Если ты не хочешь возиться с Python, скачай готовую версию:
1. Перейди в раздел **Releases** (справа на странице репозитория).
2. Скачай архив с последней версией игры.
3. ⚠️ **ВАЖНО:** После распаковки файл `KeeperApp.exe` и папка `_internal` **должны лежать в одной папке**. Не перемещай `.exe` отдельно! Иначе игра не найдёт свои ресурсы и не запустится.

### 🎯 Управление в игре
| Команда | Описание |
|---------|----------|
| `/start` | Начать игру |
| `/menu` | Вернуться в меню |
| `/lang` | Сменить язык (русский / english) |
| `/extreme` | Режим "Экстрим" (7 вариантов, цена ошибки) |
| `/keeper` | Секретная концовка (доступна после идеального прохождения /extreme) |
| `F5` | Очистить чат |

### 🛠 Сборка своего .exe
Если хочешь собрать приложение самостоятельно:
```bash
pip install pyinstaller
python -m PyInstaller --console --icon=icon_logo.ico --collect-all pygame --collect-all PIL --add-data "content.py;." --add-data "legendary_content.py;." --add-data "bot_logic.py;." --add-data "database.py;." --add-data "audio;audio" --add-data "assets;assets" --name "KeeperApp" App.py --noconfirm
```

---

<a id="english"></a>
## 🇬🇧 English

An interactive quest game where you save the world of tales by answering questions about your favorite stories.

### 🎮 Features
- 5 difficulty modes (from easy to legendary)
- 115+ unique questions
- Secret ending
- Original music and beautiful interface
- Russian and English language support
- Progress and chat history saving

### 🚀 How to Run (Source Code)
This repository contains the source code. To run it:

1. Click the green **Code** button at the top → **Download ZIP**.
2. Extract the archive to any folder.
3. Install **Python 3.x** (works on any modern version, including **3.15**).
4. Open a terminal in the project folder and install dependencies:
   ```bash
   pip install pygame Pillow
   ```
5. Run the game:
   ```bash
   python App.py
   ```

### 📦 How to Get the Ready-to-Play Game (.exe)
If you don't want to deal with Python, download the pre-built version:
1. Go to the **Releases** section (on the right side of the repository page).
2. Download the archive with the latest game version.
3. ⚠️ **IMPORTANT:** After extraction, the `KeeperApp.exe` file and the `_internal` folder **MUST be in the same directory**. Do not move the `.exe` file separately! Otherwise, the game won't find its resources and will crash.

### 🎯 In-Game Controls
| Command | Description |
|---------|-------------|
| `/start` | Start the game |
| `/menu` | Return to menu |
| `/lang` | Change language (русский / english) |
| `/extreme` | Extreme mode (7 options, high stakes) |
| `/keeper` | Secret ending (available after perfect /extreme run) |
| `F5` | Clear chat |

### 🛠 Build Your Own .exe
If you want to compile the application yourself:
```bash
pip install pyinstaller
python -m PyInstaller --console --icon=icon_logo.ico --collect-all pygame --collect-all PIL --add-data "content.py;." --add-data "legendary_content.py;." --add-data "bot_logic.py;." --add-data "database.py;." --add-data "audio;audio" --add-data "assets;assets" --name "KeeperApp" App.py --noconfirm
```

---

### 📄 License
MIT License — см. файл [LICENSE](LICENSE) / see [LICENSE](LICENSE) file for details.

Made with ❤️
