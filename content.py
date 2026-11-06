# content.py
# Контент для режимов Easy, Medium, Hard, Extreme (15 вопросов)

import pygame
import os
import sys

# ================= МУЗЫКА =================
pygame.mixer.init()

AUDIO_DIR = "audio"

def get_audio_path(filename):
    """Получает путь к аудиофайлу (работает и в .exe, и в Python)"""
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, AUDIO_DIR, filename)

def play_music(track_name):
    """Воспроизводит музыку"""
    try:
        music_files = {
            "prologue": "prologue.mp3",
            "correct": "correct.mp3",
            "wrong": "wrong.mp3",
            "final_good": "final_good.mp3",
            "final_bad": "final_bad.mp3",
            "legendary_good": "legendary_good.mp3",
            "legendary_bad": "legendary_bad.mp3",
        }
        
        if track_name in music_files:
            filepath = get_audio_path(music_files[track_name])
            if os.path.exists(filepath):
                pygame.mixer.music.load(filepath)
                pygame.mixer.music.play()
                print(f"🎵 Воспроизводится: {track_name}")
            else:
                print(f"⚠️ Файл не найден: {filepath}")
    except Exception as e:
        print(f"⚠️ Ошибка воспроизведения: {e}")

# ================= НАСТРОЙКИ СЛОЖНОСТИ =================
difficulties = {
    "easy": {"options": 3, "death_first": False, "mid_death": None, "final_bad": 5},
    "medium": {"options": 4, "death_first": False, "mid_death": 3, "final_bad": 4},
    "hard": {"options": 5, "death_first": False, "mid_death": 2, "final_bad": 3},
    "extreme": {"options": 7, "death_first": True, "mid_death": None, "final_bad": None}
}

# ================= ФРАЗЫ КОСТИ =================
kostya_correct_ru = ["Костя: Вот так, бро.", "Костя: Красавчик.", "Костя: Сказки помнишь.", "Костя: Хорошо идём.", "Костя: Мир вздохнул легче."]
kostya_correct_en = ["Kostya: That's it, bro.", "Kostya: Beautiful.", "Kostya: You remember the tales.", "Kostya: We're doing great.", "Kostya: The world breathes easier."]
kostya_error_ru = ["Костя: Бро… это было не то.", "Костя: Осторожнее, мир трещит.", "Костя: Чувствую, сказкам больно.", "Костя: Эх… осколок треснул.", "Костя: Держись."]
kostya_error_en = ["Kostya: Bro... that wasn't it.", "Kostya: Careful, the world is cracking.", "Kostya: I can feel the tales hurting.", "Kostya: Sigh... a shard just cracked.", "Kostya: Hold on."]

# ================= 15 ВОПРОСОВ =================
story = [
    {
        "title_ru": "1. Лукоморье", "title_en": "1. Lukomorye (The Learned Cat)",
        "text_ru": "Ты и Костя выходите к огромному дубу. По золотой цепи ходит кот учёный.\nКостя: «Бро… он реально ходит по цепи.»\n\nКот спрашивает:\n«Что я делаю у этого дуба?»",
        "text_en": "You and Kostya approach a giant oak tree. A learned cat walks along a golden chain.\nKostya: 'Bro... he's actually walking on a chain.'\n\nThe cat asks:\n'What am I doing by this oak tree?'",
        "correct_ru": "Хожу по цепи", "correct_en": "Walking on a chain"
    },
    {
        "title_ru": "2. Колобок", "title_en": "2. Kolobok (The Round Bun)",
        "text_ru": "Вы выходите на лесную тропинку. По дороге катится Колобок.\nКостя: «Бро, он живой.»\n\nКолобок спрашивает:\n«От кого я убежал первым?»",
        "text_en": "You step onto a forest path. A round, baked creature is rolling down the road.\nKostya: 'Bro, it's alive.'\n\nKolobok asks:\n'Who did I run away from first?'",
        "correct_ru": "От деда и бабы", "correct_en": "From the old man and the old woman"
    },
    {
        "title_ru": "3. Золушка", "title_en": "3. Cinderella",
        "text_ru": "Вы оказываетесь у дворца. Карета сияет.\nКостя: «Бро, тут прям бал.»\n\nЗолушка спрашивает:\n«Что я потеряла на балу?»",
        "text_en": "You find yourselves at a grand palace. The carriage is shining.\nKostya: 'Bro, this is literally a ball.'\n\nCinderella asks:\n'What did I lose at the ball?'",
        "correct_ru": "Хрустальную туфельку", "correct_en": "The glass slipper"
    },
    {
        "title_ru": "4. Красная Шапочка", "title_en": "4. Little Red Riding Hood",
        "text_ru": "Лес становится гуще. Навстречу выходит девочка в красной шапочке.\nКостя: «Бро, это она.»\n\nОна спрашивает:\n«К кому я иду?»",
        "text_en": "The forest grows denser. A girl in a red hood approaches you.\nKostya: 'Bro, that's her.'\n\nShe asks:\n'Whose house am I going to?'",
        "correct_ru": "К бабушке", "correct_en": "Grandmother's house"
    },
    {
        "title_ru": "5. Три поросёнка", "title_en": "5. The Three Little Pigs",
        "text_ru": "Перед вами три домика.\nКостя: «Бро, я это помню… вроде.»\n\nПоросёнок спрашивает:\n«Какой дом выдержит волка?»",
        "text_en": "Three small houses stand before you.\nKostya: 'Bro, I remember this one... I think.'\n\nThe pig asks:\n'Which house can withstand the wolf?'",
        "correct_ru": "Дом из кирпича", "correct_en": "The brick house"
    },
    {
        "title_ru": "6. Алиса в Стране Чудес", "title_en": "6. Alice in Wonderland",
        "text_ru": "Мир вокруг становится странным. Мимо пробегает Белый Кролик, сверяясь с часами.\nКостя: «Бро, он опаздывает.»\n\nКролик спрашивает:\n«За кем ты должен идти?»",
        "text_en": "The world around you becomes strange. A White Rabbit runs past, checking his pocket watch.\nKostya: 'Bro, he's late.'\n\nThe Rabbit asks:\n'Who must you follow?'",
        "correct_ru": "За Белым Кроликом", "correct_en": "The White Rabbit"
    },
    {
        "title_ru": "7. Дюймовочка", "title_en": "7. Thumbelina",
        "text_ru": "На цветке сидит маленькая девочка.\nКостя: «Бро, она крошечная.»\n\nОна спрашивает:\n«Кто мне помогает?»",
        "text_en": "A tiny girl is sitting on a flower petal.\nKostya: 'Bro, she's microscopic.'\n\nShe asks:\n'Who helps me?'",
        "correct_ru": "Ласточка", "correct_en": "The swallow"
    },
    {
        "title_ru": "8. Снежная королева", "title_en": "8. The Snow Queen",
        "text_ru": "Становится холоднее. Снег искрится.\nКостя: «Бро, тут мороз.»\n\nГерда спрашивает:\n«Кого я ищу?»",
        "text_en": "It grows colder. The snow sparkles sharply.\nKostya: 'Bro, it's freezing.'\n\nGerda asks:\n'Who am I looking for?'",
        "correct_ru": "Кая", "correct_en": "Kai"
    },
    {
        "title_ru": "9. Сказка о рыбаке и рыбке", "title_en": "9. The Fisherman and the Golden Fish",
        "text_ru": "Вы выходите к морю. Волны ведут себя странно.\nКостя: «Бро, море злится.»\n\nРыбка спрашивает:\n«Чего хочет старуха?»",
        "text_en": "You reach the sea. The waves are behaving strangely.\nKostya: 'Bro, the sea is angry.'\n\nThe Golden Fish asks:\n'What does the old woman want?'",
        "correct_ru": "Всё больше богатства и власти", "correct_en": "More and more wealth and power"
    },
    {
        "title_ru": "10. Конёк-Горбунок", "title_en": "10. The Little Humpbacked Horse",
        "text_ru": "Перед вами маленький волшебный конёк.\nКостя: «Бро, он милый.»\n\nКонёк спрашивает:\n«Кому я служу?»",
        "text_en": "A tiny, magical horse stands before you.\nKostya: 'Bro, he's cute.'\n\nThe horse asks:\n'Whom do I serve?'",
        "correct_ru": "Ивану", "correct_en": "Ivan"
    },
    {
        "title_ru": "11. Аленький цветочек", "title_en": "11. The Scarlet Flower",
        "text_ru": "Вы в саду. Цветок сияет.\nКостя: «Бро, он светится.»\n\nГолос спрашивает:\n«Что нужно беречь?»",
        "text_en": "You are in a magical garden. A flower is glowing brightly.\nKostya: 'Bro, it's glowing.'\n\nA voice asks:\n'What must be protected?'",
        "correct_ru": "Аленький цветочек", "correct_en": "The scarlet flower"
    },
    {
        "title_ru": "12. Серебряное копытце", "title_en": "12. Silver Hoof",
        "text_ru": "Перед вами козочка.\nКостя: «Бро, камни появляются.»\n\nОна спрашивает:\n«Что я выбиваю копытцем?»",
        "text_en": "A small goat stands before you.\nKostya: 'Bro, gems are appearing.'\n\nShe asks:\n'What do I strike with my hoof?'",
        "correct_ru": "Драгоценные камни", "correct_en": "Precious stones"
    },
    {
        "title_ru": "13. Морозко", "title_en": "13. Father Frost (Morozko)",
        "text_ru": "Становится холодно. Появляется Морозко.\nКостя: «Бро, он добрый… вроде.»\n\nОн спрашивает:\n«Что я люблю в людях?»",
        "text_en": "It becomes bitterly cold. Father Frost appears.\nKostya: 'Bro, he's kind... I think.'\n\nHe asks:\n'What do I love in people?'",
        "correct_ru": "Терпение и доброту", "correct_en": "Patience and kindness"
    },
    {
        "title_ru": "14. Иван-Царевич и Серый Волк", "title_en": "14. Ivan Tsarevich and the Grey Wolf",
        "text_ru": "Перед вами стоит Серый Волк.\nКостя: «Бро, финал.»\n\nВолк спрашивает:\n«Кто мой спутник?»",
        "text_en": "The Grey Wolf stands before you.\nKostya: 'Bro, the finale.'\n\nThe Wolf asks:\n'Who is my companion?'",
        "correct_ru": "Иван-Царевич", "correct_en": "Ivan Tsarevich"
    },
    {
        "title_ru": "15. Царевна-лягушка", "title_en": "15. The Frog Princess",
        "text_ru": "На пне сидит лягушка и держит стрелу.\nКостя: «Бро, только не стреляй.»\n\nЛягушка спрашивает:\n«Кем я обернулась на балу?»",
        "text_en": "A frog sits on a stump, holding an arrow.\nKostya: 'Bro, don't shoot it.'\n\nThe Frog asks:\n'What did I turn into at the ball?'",
        "correct_ru": "Василисой Премудрой", "correct_en": "Vasilisa the Wise"
    }
]

# ================= НЕПРАВИЛЬНЫЕ ОТВЕТЫ =================
wrong_answers_ru = {
    "Хожу по цепи": ["Сижу под деревом", "Сплю на ветке", "Ловлю мышей", "Читаю книги", "Охраняю дуб", "Пою песни"],
    "От деда и бабы": ["От зайца", "От медведя", "От лисы", "От волка", "От охотника", "От мельника"],
    "Хрустальную туфельку": ["Серебряную туфельку", "Лунную туфельку", "Хрустальный браслет", "Золотое кольцо", "Шёлковый веер", "Бархатный плащ"],
    "К бабушке": ["К маме", "К тёте", "К подруге", "К сестре", "В школу", "На рынок"],
    "Дом из кирпича": ["Дом из дерева", "Дом из соломы", "Дом из глины", "Каменный дом", "Ледяной дом", "Стальной дом"],
    "За Белым Кроликом": ["За Чёрным Кроликом", "За Серым Кроликом", "За Лисой", "За Гусеницей", "За Болванщиком", "За Чеширским Котом"],
    "Ласточка": ["Стрекоза", "Синица", "Голубка", "Воробей", "Сова", "Пчела"],
    "Кая": ["Герду", "Мальчика", "Девочку", "Короля", "Разбойницу", "Принца"],
    "Всё больше богатства и власти": ["Молодости", "Красоты", "Силы", "Саму золотую рыбку", "Свободы", "Новый дворец"],
    "Ивану": ["Царю", "Князю", "Купцу", "Богатырю", "Царице", "Кощею"],
    "Аленький цветочек": ["Синий цветочек", "Лунный цветочек", "Волшебный цветочек", "Золотой бутон", "Серебряный лист", "Красную розу"],
    "Драгоценные камни": ["Сияющие камни", "Волшебные камни", "Синие камни", "Золотые монеты", "Серебряные слитки", "Алмазы"],
    "Терпение и доброту": ["Смелость и честность", "Трудолюбие", "Вежливость", "Силу", "Ум", "Хитрость"],
    "Иван-Царевич": ["Добрыня Никитич", "Алёша Попович", "Серый Волк", "Илья Муромец", "Царь Берендей", "Кощей Бессмертный"],
    "Василисой Премудрой": ["Царевной", "Королевой", "Ведьмой", "Лебедью", "Птицей", "Феей"]
}

wrong_answers_en = {
    "Walking on a chain": ["Sitting under the tree", "Sleeping on a branch", "Chasing a mouse", "Reading a book", "Guarding the tree", "Singing a song"],
    "From the old man and the old woman": ["From the hare", "From the bear", "From the fox", "From the wolf", "From the hunter", "From the miller"],
    "The glass slipper": ["The silver shoe", "The moon shoe", "The glass bracelet", "The golden ring", "The silk fan", "The velvet cloak"],
    "Grandmother's house": ["To her mother", "To her aunt", "To her friend", "To her sister", "To school", "To the market"],
    "The brick house": ["The wooden house", "The straw house", "The clay house", "The stone house", "The ice house", "The steel house"],
    "The White Rabbit": ["The Black Rabbit", "The Grey Rabbit", "The Fox", "The Caterpillar", "The Mad Hatter", "The Cheshire Cat"],
    "The swallow": ["The dragonfly", "The titmouse", "The dove", "The sparrow", "The owl", "The bee"],
    "Kai": ["Gerda", "The boy", "The girl", "The king", "The robber girl", "The prince"],
    "More and more wealth and power": ["Youth", "Beauty", "Strength", "The golden fish itself", "Freedom", "A new palace"],
    "Ivan": ["The Tsar", "The Prince", "The Merchant", "The Bogatyr", "The Tsarina", "Koschei"],
    "The scarlet flower": ["The blue flower", "The moon flower", "The magic flower", "The golden bud", "The silver leaf", "The red rose"],
    "Precious stones": ["Shining stones", "Magic stones", "Blue stones", "Gold coins", "Silver bars", "Diamonds"],
    "Patience and kindness": ["Courage and honesty", "Hard work", "Politeness", "Strength", "Intelligence", "Cunning"],
    "Ivan Tsarevich": ["Dobrynya", "Alyosha Popovich", "The Grey Wolf", "Ilya Muromets", "Tsar Berendey", "Koschei"],
    "Vasilisa the Wise": ["A princess", "A queen", "A witch", "A swan", "A bird", "A fairy"]
}