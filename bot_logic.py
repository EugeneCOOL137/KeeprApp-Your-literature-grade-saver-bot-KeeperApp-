# bot_logic.py
import random
import pygame
import os
import sys
from content import (
    story, wrong_answers_ru, wrong_answers_en, difficulties,
    kostya_correct_ru, kostya_correct_en,
    kostya_error_ru, kostya_error_en
)
from legendary_content import (
    legendary_story, legendary_wrong_answers_ru, legendary_wrong_answers_en,
    legendary_difficulty
)
from database import get_player, save_player, reset_player, set_trophy

# Инициализация музыки
pygame.mixer.init()

# Пути к музыке
AUDIO_DIR = "audio"

def get_audio_path(filename):
    """Получает путь к аудиофайлу (ищем в _internal)"""
    if getattr(sys, 'frozen', False):
        exe_dir = os.path.dirname(sys.executable)
        base_path = os.path.join(exe_dir, '_internal', 'audio')
    else:
        base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
    
    full_path = os.path.join(base_path, filename)
    
    if not os.path.exists(full_path):
        print(f"❌ ОШИБКА: Музыка не найдена по пути: {full_path}")
    else:
        print(f"✅ Музыка найдена: {filename}")
        
    return full_path

def play_music(track_name):
    """Воспроизводит музыку (с правильными именами файлов)"""
    try:
        music_files = {
            "prologue": "prologue.mp3",
            "correct": "correct.mp3",
            "wrong": "wrong.mp3",
            "final_good": "good end.mp3",
            "final_bad": "bad end.mp3",
            "legendary_good": "epic good end.mp3",
            "legendary_bad": "epic bad end.mp3",
        }
        
        if track_name in music_files:
            filename = music_files[track_name]
            filepath = get_audio_path(filename)
            
            if os.path.exists(filepath):
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.play()
                print(f"🎵 Воспроизводится: {track_name} ({filename})")
            else:
                print(f"❌ ОШИБКА: Файл {filename} не найден по пути: {filepath}")
    except Exception as e:
        print(f"⚠️ Ошибка воспроизведения {track_name}: {e}")

# Маппинг английской раскладки на русскую
EN_TO_RU_LAYOUT = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы',
    'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
    'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.',
    'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г',
    'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ', 'A': 'Ф', 'S': 'Ы',
    'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д',
    ':': 'Ж', '"': 'Э', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И',
    'N': 'Т', 'M': 'Ь', '<': 'Б', '>': 'Ю', '?': ',',
}

def convert_to_russian(text):
    """Конвертирует текст с английской раскладки на русскую"""
    result = ''
    for char in text:
        result += EN_TO_RU_LAYOUT.get(char, char)
    return result

class BotLogic:
    def __init__(self, user_id=1):
        self.user_id = user_id
        self.messages = []
        self.current_options = []
        
    def get_difficulty_settings(self, diff):
        if diff == "legendary":
            return legendary_difficulty
        return difficulties.get(diff, difficulties["easy"])

    def get_story_and_wrong(self, diff, lang):
        if diff == "legendary":
            wrong = legendary_wrong_answers_ru if lang == 'ru' else legendary_wrong_answers_en
            return legendary_story, wrong
        else:
            wrong = wrong_answers_ru if lang == 'ru' else wrong_answers_en
            return story, wrong

    def gen_options(self, scene, diff, lang):
        correct_key = f"correct_{lang}"
        correct = scene[correct_key]
        wrong_key = f"wrong_{lang}"
        if wrong_key in scene:
            pool = scene[wrong_key]
        else:
            _, wrong_answers = self.get_story_and_wrong(diff, lang)
            pool = wrong_answers.get(correct, [])
        cfg = self.get_difficulty_settings(diff)
        total = cfg["options"]
        wrongs = random.sample(pool, min(len(pool), total - 1))
        opts = wrongs + [correct]
        random.shuffle(opts)
        return opts

    def process_message(self, text):
        """Обработка сообщения и возврат списка ответов"""
        self.messages = []
        
        # Конвертируем английскую раскладку в русскую
        text_ru = convert_to_russian(text)
        text = text.strip().lower()
        text_ru = text_ru.strip().lower()
        
        st = get_player(self.user_id)
        
        # Проверяем команды (оригинал + конвертированная версия)
        if text in ['/start', '/меню', '/menu', 'начать', 'start'] or \
           text_ru in ['/start', '/меню', '/menu', 'начать', 'start']:
            return self.cmd_start(st)
        elif text == '/lang' or text_ru == '/lang':
            return self.cmd_lang()
        elif text in ['русский', 'russian'] or text_ru in ['русский', 'russian']:
            return self.cmd_set_lang('ru', st)
        elif text in ['english', 'английский'] or text_ru in ['english', 'английский']:
            return self.cmd_set_lang('en', st)
        elif text in ['/keeper', '/кипер'] or text_ru in ['/keeper', '/кипер']:
            return self.cmd_keeper(st)
        elif text in ['/easy', '/medium', '/hard', '/extreme', '/legendary'] or \
             text_ru in ['/easy', '/medium', '/hard', '/extreme', '/legendary']:
            diff = text[1:] if text.startswith('/') else text_ru[1:]
            return self.cmd_start_game(diff, st)
        
        # Игровые ответы
        if not st or not st["difficulty"]:
            return ["Сначала напишите /start, чтобы начать игру."]
        
        return self.handle_answer(text, st)
    
    def add_msg(self, text):
        """Добавить сообщение в список"""
        self.messages.append(text)
    
    def cmd_start(self, st):
        trophy = reset_player(self.user_id)
        existing_lang = st["language"] if st else 'ru'
        save_player(self.user_id, existing_lang, None, 0, 0, False, trophy)
        
        trophy_text = ""
        if trophy:
            if existing_lang == 'ru':
                trophy_text = "\n\n🏆 У вас есть трофей: Хранитель Сказок 🏆"
            else:
                trophy_text = "\n\n🏆 You have a trophy: Keeper of Tales 🏆"
        
        if existing_lang == 'ru':
            self.add_msg(
                "Голубой кристалл зовёт в мир сказок." + trophy_text + "\n\n"
                "Выберите сложность:\n"
                "/easy — лёгкий путь (3 варианта)\n"
                "/medium — путь искателя (4 варианта)\n"
                "/hard — путь на грани (5 вариантов)\n"
                "/extreme — без права на ошибку (7 вариантов)\n"
                "/legendary — легендарный путь (100 вопросов, 3 жизни)\n\n"
                "🌐 /lang — сменить язык\n"
                "💡 /menu — вернуться в это меню\n\n"
                "keeper-???"
            )
        else:
            self.add_msg(
                "The blue crystal calls you to the world of tales." + trophy_text + "\n\n"
                "Choose difficulty:\n"
                "/easy — the easy path (3 options)\n"
                "/medium — the seeker's path (4 options)\n"
                "/hard — on the edge (5 options)\n"
                "/extreme — no room for error (7 options)\n"
                "/legendary — legendary path (100 questions, 3 lives)\n\n"
                "🌐 /lang — change language\n"
                "💡 /menu — return to this menu\n\n"
                "keeper-???"
            )
        return self.messages
    
    def cmd_lang(self):
        self.add_msg("Выберите язык / Choose language:\n\nрусский / english")
        return self.messages
    
    def cmd_set_lang(self, lang, st):
        trophy = st["trophy"] if st else False
        if st:
            save_player(self.user_id, lang, st["difficulty"], st["step"], st["errors"], st["perfect"], trophy)
        else:
            save_player(self.user_id, lang, None, 0, 0, False, trophy)
        
        if lang == 'ru':
            self.add_msg("Язык изменён на русский.\nНапиши /start или /menu")
        else:
            self.add_msg("Language changed to English.\nType /start or /menu")
        return self.messages
    
    def cmd_keeper(self, st):
        # Проверяем, что игра завершена успешно
        if not st or st.get("perfect") is not True or st.get("difficulty") != "extreme":
            if st and st["language"] == 'en':
                self.add_msg("The crystal is silent. It is closed to you.\n(Pass /extreme with zero errors first.)")
            else:
                self.add_msg("Кристалл молчит. Он закрыт для тебя.\n(Сначала пройди /extreme без единой ошибки.)")
            return self.messages
        
        # Дополнительная проверка: step должен быть равен len(current_story)
        current_story, _ = self.get_story_and_wrong(st["difficulty"], st["language"])
        if st.get("step") < len(current_story):
            if st["language"] == 'en':
                self.add_msg("The crystal is silent. Finish the path first.")
            else:
                self.add_msg("Кристалл молчит. Сначала заверши путь.")
            return self.messages
        
        lang = st["language"]
        if lang == 'ru':
            self.add_msg(
                "Кристалл раскрывается. Свет становится холодным и глубоким.\n"
                "Перед тобой появляется Первый Хранитель.\n\n"
                "«Ты прошёл путь без единой трещины. Значит, ты готов услышать правду.»\n\n"
                "Он поднимает руку — и мир вокруг меняется.\n"
                "Ты видишь, как сказки рушились:\n"
                "— К коту учёному пришли люди, забрали цепь, а самого кота чуть не застрелили.\n"
                "— Серебряное копытце схватили охотники и требовали выбивать камни.\n"
                "— Герда блуждала в пустоте, где снег превращался в пепел.\n"
                "— Рыбку поймали сети, и море стало чёрным.\n\n"
                "«Чтобы остановить хаос, я создал кристалл — щит, защищающий мир сказок.\n"
                "Но Тень украла меня. Осталось только тело… а кристалл без Хранителя стал разрушаться.»\n\n"
                "Он смотрит прямо в тебя:\n"
                "«Теперь ты знаешь правду. И только ты решаешь, что будет дальше.»\n\n"
                "Секретная концовка.\nНапиши /start"
            )
        else:
            self.add_msg(
                "The crystal opens. The light becomes cold and deep.\n"
                "The First Keeper appears before you.\n\n"
                "'You passed the path without a single crack. You are ready to hear the truth.'\n\n"
                "He raises his hand — and the world around changes.\n"
                "You see how the tales were destroyed:\n"
                "— People came to the learned cat, took the chain, and almost shot the cat.\n"
                "— Hunters caught Silver Hoof and demanded gems.\n"
                "— Gerda wandered in emptiness where snow turned to ash.\n"
                "— The Fish was caught in nets, and the sea turned black.\n\n"
                "'To stop the chaos, I created the crystal — a shield protecting the world of tales.\n"
                "But the Shadow stole me. Only the body remains... and the crystal without a Keeper began to crumble.'\n\n"
                "He looks straight into you:\n"
                "'Now you know the truth. And only you decide what happens next.'\n\n"
                "Secret ending.\nType /start"
            )
        reset_player(self.user_id)
        return self.messages
    
    def cmd_start_game(self, diff, st):
        lang = st["language"] if st else 'ru'
        trophy = st["trophy"] if st else False
        reset_player(self.user_id)
        save_player(self.user_id, lang, diff, 0, 0, False, trophy)
        
        # Пролог
        if diff == "extreme":
            self.add_prologue_extreme(lang)
        elif diff == "legendary":
            self.add_prologue_legendary(lang)
        else:
            self.add_prologue_common(lang)
        
        play_music("prologue")
        
        # Первый вопрос
        self.add_question()
        return self.messages
    
    def add_prologue_common(self, lang):
        if lang == 'ru':
            self.add_msg("Поздний вечер. Вы с Костей гуляете возле дома.")
            self.add_msg("Костя: «Бро, смотри, что там блестит?»")
            self.add_msg("В траве лежит голубой кристалл. Ты поднимаешь его — и он оживает.")
            self.add_msg("Голос: «Мир сказок трескается. Он исчезает. Мне нужны те, кто помнит истории.»")
            self.add_msg("Костя: «Бро, это про нас. Давай попробуем.»")
        else:
            self.add_msg("Late evening. You and Kostya are walking near the house.")
            self.add_msg("Kostya: 'Bro, look, what's shining over there?'")
            self.add_msg("A blue crystal lies in the grass. You pick it up — and it comes alive.")
            self.add_msg("Voice: 'The world of tales is cracking. It is disappearing. I need those who remember the stories.'")
            self.add_msg("Kostya: 'Bro, this is about us. Let's try.'")

    def add_prologue_extreme(self, lang):
        if lang == 'ru':
            self.add_msg("Поздний вечер. Воздух вокруг будто стал тяжелее.")
            self.add_msg("Костя останавливается: «Бро… ты тоже это чувствуешь?»")
            self.add_msg("В траве вспыхивает голубой свет. Кристалл дрожит, словно боится рассыпаться.")
            self.add_msg("Ты поднимаешь его — трещины вспыхивают холодным светом.")
            self.add_msg("Голос: «Мир сказок держится на последней нити. Ошибок не будет прощено.»")
            self.add_msg("Костя: «Бро… здесь не будет права на ошибку. Держись.»")
        else:
            self.add_msg("Late evening. The air around feels heavier.")
            self.add_msg("Kostya stops: 'Bro... do you feel it too?'")
            self.add_msg("A blue light flashes in the grass. The crystal trembles, as if afraid to shatter.")
            self.add_msg("You pick it up — cracks flash with cold light.")
            self.add_msg("Voice: 'The world of tales hangs by a last thread. No mistakes will be forgiven.'")
            self.add_msg("Kostya: 'Bro... there won't be any room for error here. Hold on.'")

    def add_prologue_legendary(self, lang):
        if lang == 'ru':
            self.add_msg("Поздний вечер. Кристалл пульсирует необычным светом.")
            self.add_msg("Костя: «Бро… он будто зовёт нас куда-то дальше.»")
            self.add_msg("Голос: «Ты прошёл испытание. Но готов ли ты к легендарному пути?»")
            self.add_msg("Костя: «Сто сказок… Бро, это будет эпично.»")
            self.add_msg("Голос: «У тебя будет три жизни. Используй их мудро.»")
        else:
            self.add_msg("Late evening. The crystal pulses with unusual light.")
            self.add_msg("Kostya: 'Bro... it seems to be calling us somewhere further.'")
            self.add_msg("Voice: 'You passed the test. But are you ready for the legendary path?'")
            self.add_msg("Kostya: 'A hundred tales... Bro, this will be epic.'")
            self.add_msg("Voice: 'You will have three lives. Use them wisely.'")
    
    def add_question(self):
        """Добавить текущий вопрос"""
        st = get_player(self.user_id)
        if not st:
            return
        
        diff = st["difficulty"]
        if not diff:
            return
        
        current_story, _ = self.get_story_and_wrong(diff, st["language"])
        step = st["step"]
        
        if step >= len(current_story):
            self.final()
            return
        
        scene = current_story[step]
        lang = st["language"]
        opts = self.gen_options(scene, diff, lang)
        
        # Сохраняем варианты для проверки ответа
        self.current_options = opts
        
        title = scene[f"title_{lang}"]
        text = scene[f"text_{lang}"]
        
        if diff == "legendary":
            lives = 3 - st["errors"]
            if lang == 'ru':
                text = f"❤️ Жизней: {lives}\n\n{text}"
            else:
                text = f"❤️ Lives: {lives}\n\n{text}"
        
        # Формируем сообщение с вариантами
        msg = f"{title}\n\n{text}\n\n" + "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(opts)])
        self.add_msg(msg)
    
    def handle_answer(self, text, st):
        """Обработка ответа"""
        step = st["step"]
        lang = st["language"]
        diff = st["difficulty"]
        cfg = self.get_difficulty_settings(diff)
        current_story, _ = self.get_story_and_wrong(diff, lang)
        
        # Проверка: если step >= len(current_story), значит игра уже завершена
        if step >= len(current_story):
            return ["Игра завершена. Напиши /start, чтобы начать заново."]
        
        scene = current_story[step]
        correct_key = f"correct_{lang}"
        correct = scene[correct_key]
        
        # Проверяем, является ли ответ номером варианта
        is_correct = False
        if text.isdigit():
            num = int(text) - 1
            if 0 <= num < len(self.current_options):
                selected = self.current_options[num]
                is_correct = (selected.lower() == correct.lower())
            else:
                self.add_msg(f"❌ Нет такого варианта. Выберите число от 1 до {len(self.current_options)}.")
                return self.messages
        else:
            # Проверяем текстовый ответ
            is_correct = (text == correct.lower())
        
        # Мгновенная смерть в Extreme
        if cfg.get("death_first") and not is_correct:
            if lang == 'ru':
                self.add_msg("В воздухе появляется разбитый осколок. Кристалл не выдерживает.\nМир сказок трескается и гаснет.\n\nНапиши /start")
            else:
                self.add_msg("A broken shard appears in the air. The crystal cannot hold.\nThe world of tales cracks and fades.\n\nType /start")
            play_music("wrong")
            reset_player(self.user_id)
            return self.messages
        
        # Проверка ответа
        kostya_correct = kostya_correct_ru if lang == 'ru' else kostya_correct_en
        kostya_error = kostya_error_ru if lang == 'ru' else kostya_error_en
        
        if not is_correct:
            new_errors = st["errors"] + 1
            if diff == "legendary" and new_errors >= 3:
                if lang == 'ru':
                    self.add_msg("Все три жизни потеряны. Мир сказок гаснет.\n\nНапиши /start, чтобы начать заново.")
                else:
                    self.add_msg("All three lives lost. The world of tales fades.\n\nType /start to try again.")
                play_music("legendary_bad")
                reset_player(self.user_id)
                return self.messages
            
            save_player(self.user_id, lang, diff, step, new_errors, st["perfect"], st["trophy"])
            if lang == 'ru':
                self.add_msg("В воздухе появляется разбитый осколок. Трещина проходит по кристаллу.")
                if diff == "legendary":
                    lives_left = 3 - new_errors
                    self.add_msg(f"Осталось жизней: {lives_left}")
            else:
                self.add_msg("A broken shard appears in the air. A crack runs through the crystal.")
                if diff == "legendary":
                    lives_left = 3 - new_errors
                    self.add_msg(f"Lives remaining: {lives_left}")
            play_music("wrong")
            self.add_msg(random.choice(kostya_error))
        else:
            if lang == 'ru':
                self.add_msg("В воздухе вспыхивает свет. Перед тобой появляется целый осколок.")
            else:
                self.add_msg("Light flashes in the air. A whole shard appears before you.")
            play_music("correct")
            self.add_msg(random.choice(kostya_correct))
        
        # Проверка смерти в середине
        if step == 6:
            current_errors = get_player(self.user_id)["errors"]
            if diff in ("medium", "hard") and cfg.get("mid_death") is not None and current_errors >= cfg["mid_death"]:
                if lang == 'ru':
                    self.add_msg("Кристалл вспыхивает и трескается. Слишком много разбитых осколков.\nМир сказок гаснет.\n\nНапиши /start")
                else:
                    self.add_msg("The crystal flashes and cracks. Too many broken shards.\nThe world of tales fades.\n\nType /start")
                play_music("final_bad")
                reset_player(self.user_id)
                return self.messages
        
        # Следующий шаг
        new_step = step + 1
        current_errors = get_player(self.user_id)["errors"]
        save_player(self.user_id, lang, diff, new_step, current_errors, st["perfect"], st["trophy"])
        
        if new_step >= len(current_story):
            self.final()
            return self.messages
        
        self.add_question()
        return self.messages
    
    def final(self):
        """Финал игры"""
        st = get_player(self.user_id)
        if not st:
            return
        lang = st["language"]
        diff = st["difficulty"]
        if not diff:
            return
        cfg = self.get_difficulty_settings(diff)
        errors = st["errors"]
        
        if diff in ["extreme", "legendary"]:
            if errors == 0:
                if diff == "legendary":
                    set_trophy(self.user_id)
                save_player(self.user_id, lang, diff, st["step"], 0, True, st["trophy"])
                if lang == 'ru':
                    if diff == "legendary":
                        self.add_msg("🏆 ТРОФЕЙ ПОЛУЧЕН: Хранитель Сказок 🏆\n\nТы прошёл легендарный путь без единой ошибки!\nВсе 100 сказок спасены. Кристалл сияет вечным светом.\nТы — настоящий Хранитель!")
                        play_music("legendary_good")
                    else:
                        self.add_msg("Ты прошёл путь без единой трещины.\nКристалл сияет чистым светом. Мир сказок восстановлен.\nНо он будто ждёт твоего решения…")
                        play_music("final_good")
                    if diff == "extreme":
                        self.add_msg("Кристалл шепчет: «Если ты слышишь меня… попробуй вспомнить слово кипер.»")
                else:
                    if diff == "legendary":
                        self.add_msg("🏆 TROPHY UNLOCKED: Keeper of Tales 🏆\n\nYou passed the legendary path without a single error!\nAll 100 tales are saved. The crystal shines with eternal light.\nYou are a true Keeper!")
                        play_music("legendary_good")
                    else:
                        self.add_msg("You passed the path without a single crack.\nThe crystal shines with pure light. The world of tales is restored.\nBut it seems to be waiting for your decision...")
                        play_music("final_good")
                    if diff == "extreme":
                        self.add_msg("The crystal whispers: 'If you hear me... try to remember the word keeper.'")
                return
            else:
                if lang == 'ru':
                    if diff == "legendary":
                        self.add_msg(f"Ты дошёл до конца, но совершил {errors} ошибок.\nМир сказок выжил, но трещины остались.\nОшибок: {errors}\n\nНапиши /start, чтобы начать заново.")
                        play_music("legendary_bad")
                    else:
                        self.add_msg("Ты дошёл до конца, но трещины оказались смертельными.\nМир сказок не выдерживает и гаснет.\n\nНапиши /start, чтобы начать заново.")
                        play_music("final_bad")
                else:
                    if diff == "legendary":
                        self.add_msg(f"You reached the end, but made {errors} errors.\nThe world of tales survived, but cracks remain.\nErrors: {errors}\n\nType /start to try again.")
                        play_music("legendary_bad")
                    else:
                        self.add_msg("You reached the end, but the cracks were fatal.\nThe world of tales cannot hold and fades away.\n\nType /start to try again.")
                        play_music("final_bad")
                reset_player(self.user_id)
                return
        
        is_bad = errors >= cfg["final_bad"]
        if lang == 'ru':
            if diff == "easy":
                msg = "Слишком много разбитых осколков. Кристалл тускнеет, сказки медленно гаснут.\nПлохая концовка." if is_bad else "Ты прошёл путь. Целых осколков больше, чем трещин.\nКристалл удерживает мир сказок.\nХорошая концовка."
            elif diff == "medium":
                msg = "Кристалл вспыхивает и рассыпается на осколки.\nМир сказок гаснет.\nПлохая концовка." if is_bad else "Кристалл становится чистым и спокойным.\nМир стабилизируется, сказки оживают.\nХорошая концовка."
            elif diff == "hard":
                msg = "Мир не выдерживает накопившихся трещин.\nСказки рассыпаются в тишине.\nПлохая концовка." if is_bad else "Ты прошёл тяжёлый путь.\nМир сказок держится на грани, но всё ещё жив.\nХорошая концовка."
            if not is_bad:
                msg += f"\nОшибок: {errors}"
            msg += "\n\nНапиши /start, чтобы начать заново."
        else:
            if diff == "easy":
                msg = "Too many broken shards. The crystal dims, tales slowly fade.\nBad ending." if is_bad else "You passed the path. Whole shards outnumber the cracks.\nThe crystal holds the world of tales.\nGood ending."
            elif diff == "medium":
                msg = "The crystal flashes and shatters into pieces.\nThe world of tales fades.\nBad ending." if is_bad else "The crystal becomes clear and calm.\nThe world stabilizes, tales come alive.\nGood ending."
            elif diff == "hard":
                msg = "The world cannot withstand the accumulated cracks.\nTales scatter in silence.\nBad ending." if is_bad else "You passed a hard path.\nThe world of tales hangs by a thread, but is still alive.\nGood ending."
            if not is_bad:
                msg += f"\nErrors: {errors}"
            msg += "\n\nType /start to play again."
        
        play_music("final_good" if not is_bad else "final_bad")
        self.add_msg(msg)
        reset_player(self.user_id)