# legendary_content.py
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

# ================= НАСТРОЙКИ =================
legendary_difficulty = {
    "options": 7,
    "death_first": False,
    "mid_death": None,
    "final_bad": None,
    "lives": 3
}

# ================= ФРАЗЫ КОСТИ =================
kostya_correct_ru = ["Костя: Вот так, бро.", "Костя: Красавчик.", "Костя: Сказки помнишь.", "Костя: Хорошо идём.", "Костя: Мир вздохнул легче."]
kostya_correct_en = ["Kostya: That's it, bro.", "Kostya: Beautiful.", "Kostya: You remember the tales.", "Kostya: We're doing great.", "Kostya: The world breathes easier."]
kostya_error_ru = ["Костя: Бро… это было не то.", "Костя: Осторожнее, мир трещит.", "Костя: Чувствую, сказкам больно.", "Костя: Эх… осколок треснул.", "Костя: Держись."]
kostya_error_en = ["Kostya: Bro... that wasn't it.", "Kostya: Careful, the world is cracking.", "Kostya: I can feel the tales hurting.", "Kostya: Sigh... a shard just cracked.", "Kostya: Hold on."]

# ================= 100 ВОПРОСОВ =================
legendary_story = [
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
    },
    {
        "title_ru": "16. Репка", "title_en": "16. The Turnip (Repka)",
        "text_ru": "Перед вами огромная репка. Дед тянет, бабка тянет.\nКостя: «Бро, они не могут вытащить?»\n\nРепка спрашивает:\n«Кто помог вытащить меня последним?»",
        "text_en": "A giant turnip stands before you. The old man pulls, the old woman pulls.\nKostya: 'Bro, they can't pull it out?'\n\nThe turnip asks:\n'Who helped pull me out last?'",
        "correct_ru": "Мышка", "correct_en": "The mouse"
    },
    {
        "title_ru": "17. Курочка Ряба", "title_en": "17. Ryaba the Hen",
        "text_ru": "На полу лежит разбитое золотое яичко.\nКостя: «Бро, это же Курочка Ряба.»\n\nКурочка спрашивает:\n«Что я снесла вместо золотого?»",
        "text_en": "A broken golden egg lies on the floor.\nKostya: 'Bro, that's Ryaba the Hen.'\n\nThe hen asks:\n'What did I lay instead of the golden one?'",
        "correct_ru": "Простое яичко", "correct_en": "A simple egg"
    },
    {
        "title_ru": "18. Теремок", "title_en": "18. The Little Tower (Teremok)",
        "text_ru": "Перед вами маленький домик. Из него выглядывают звери.\nКостя: «Бро, там тесно.»\n\nМедведь спрашивает:\n«Что случилось с теремком?»",
        "text_en": "A small house stands before you. Animals peek out from it.\nKostya: 'Bro, it's crowded in there.'\n\nThe bear asks:\n'What happened to the little tower?'",
        "correct_ru": "Я его раздавил", "correct_en": "I crushed it"
    },
    {
        "title_ru": "19. Маша и Медведь", "title_en": "19. Masha and the Bear",
        "text_ru": "Вы в лесу. Перед вами большой медведь.\nКостя: «Бро, это же Машин медведь.»\n\nМедведь спрашивает:\n«Кого я нес домой в коробе?»",
        "text_en": "You are in the forest. A big bear stands before you.\nKostya: 'Bro, that's Masha's bear.'\n\nThe bear asks:\n'Whom did I carry home in the basket?'",
        "correct_ru": "Машу", "correct_en": "Masha"
    },
    {
        "title_ru": "20. Гуси-лебеди", "title_en": "20. The Geese-Swans",
        "text_ru": "По небу пролетают дикие гуси.\nКостя: «Бро, они уносят мальчика.»\n\nГуси спрашивают:\n«Кто спасает брата?»",
        "text_en": "Wild geese fly across the sky.\nKostya: 'Bro, they're taking the boy away.'\n\nThe geese ask:\n'Who is saving her brother?'",
        "correct_ru": "Сестрица Алёнушка", "correct_en": "Sister Alenushka"
    },
    {
        "title_ru": "21. Кот, Лиса и Петух", "title_en": "21. The Cat, the Fox, and the Rooster",
        "text_ru": "Перед вами петух в золотом гребешке.\nКостя: «Бро, лиса его опять утащит?»\n\nПетух спрашивает:\n«Кто меня спасает?»",
        "text_en": "A rooster with a golden crest stands before you.\nKostya: 'Bro, the fox will take him again?'\n\nThe rooster asks:\n'Who rescues me?'",
        "correct_ru": "Кот и пёс", "correct_en": "The cat and the dog"
    },
    {
        "title_ru": "22. Волк и семеро козлят", "title_en": "22. The Wolf and the Seven Kids",
        "text_ru": "Перед вами дверь. За ней слышны голоса.\nКостя: «Бро, это козлята.»\n\nВолк спрашивает:\n«Как коза узнала, что я не мама?»",
        "text_en": "A door stands before you. Voices are heard behind it.\nKostya: 'Bro, those are the kids.'\n\nThe wolf asks:\n'How did the goat know I wasn't their mother?'",
        "correct_ru": "По голосу и лапе", "correct_en": "By voice and paw"
    },
    {
        "title_ru": "23. Бычок — смоляной бочок", "title_en": "23. The Tar Bull",
        "text_ru": "Перед вами бычок, весь в смоле.\nКостя: «Бро, он липкий.»\n\nБычок спрашивает:\n«Кто прилип ко мне?»",
        "text_en": "A bull covered in tar stands before you.\nKostya: 'Bro, he's sticky.'\n\nThe bull asks:\n'Who got stuck to me?'",
        "correct_ru": "Волк, заяц, лиса", "correct_en": "Wolf, hare, fox"
    },
    {
        "title_ru": "24. Лиса и Журавль", "title_en": "24. The Fox and the Crane",
        "text_ru": "Перед вами лиса и журавль. На столе блюда.\nКостя: «Бро, они друг друга дурят.»\n\nЖуравль спрашивает:\n«Почему я не смог поесть у лисы?»",
        "text_en": "A fox and a crane stand before you. Dishes are on the table.\nKostya: 'Bro, they're tricking each other.'\n\nThe crane asks:\n'Why couldn't I eat at the fox's house?'",
        "correct_ru": "Каша была в плоской тарелке", "correct_en": "The porridge was in a flat plate"
    },
    {
        "title_ru": "25. Вершки и корешки", "title_en": "25. Tops and Roots",
        "text_ru": "Перед вами мужик и медведь. Они делят урожай.\nКостя: «Бро, медведь опять обманулся.»\n\nМедведь спрашивает:\n«Что я взял себе в этот раз?»",
        "text_en": "A peasant and a bear stand before you. They're dividing the harvest.\nKostya: 'Bro, the bear was tricked again.'\n\nThe bear asks:\n'What did I take for myself this time?'",
        "correct_ru": "Корешки (корни)", "correct_en": "The roots"
    },
    {
        "title_ru": "26. Сестрица Алёнушка и братец Иванушка", "title_en": "26. Sister Alenushka and Brother Ivanushka",
        "text_ru": "У ручья сидит козлёнок.\nКостя: «Бро, это же Иванушка.»\n\nКозлёнок спрашивает:\n«Во что я превратился, напившись из козьего копытца?»",
        "text_en": "A kid sits by the stream.\nKostya: 'Bro, that's Ivanushka.'\n\nThe kid asks:\n'What did I turn into after drinking from the goat's hoof?'",
        "correct_ru": "В козлёнка", "correct_en": "Into a kid"
    },
    {
        "title_ru": "27. По щучьему веленью", "title_en": "27. At the Pike's Command",
        "text_ru": "Перед вами мужик с ведром. Рядом щука.\nКостя: «Бро, это же Емеля.»\n\nЩука спрашивает:\n«Что я говорю Емеле, чтобы всё исполнялось?»",
        "text_en": "A peasant with a bucket stands before you. A pike is nearby.\nKostya: 'Bro, that's Yemelya.'\n\nThe pike asks:\n'What do I tell Yemelya to make everything come true?'",
        "correct_ru": "По щучьему веленью, по моему хотенью", "correct_en": "At the pike's command, at my desire"
    },
    {
        "title_ru": "28. Финист — Ясный Сокол", "title_en": "28. Finist the Bright Falcon",
        "text_ru": "Перед вами девушка, которая ищет своего жениха.\nКостя: «Бро, он же сокол.»\n\nДевушка спрашивает:\n«Во что превращается Финист ночью?»",
        "text_en": "A girl searching for her groom stands before you.\nKostya: 'Bro, he's a falcon.'\n\nThe girl asks:\n'What does Finist turn into at night?'",
        "correct_ru": "В сокола", "correct_en": "Into a falcon"
    },
    {
        "title_ru": "29. Кот и Лиса (изба)", "title_en": "29. The Cat and the Fox (The Hut)",
        "text_ru": "Перед вами ледяная избушка и лубяная избушка.\nКостя: «Бро, лиса зайца выгнала.»\n\nЗаяц спрашивает:\n«Кто мне помог вернуть избушку?»",
        "text_en": "An ice hut and a bark hut stand before you.\nKostya: 'Bro, the fox kicked the hare out.'\n\nThe hare asks:\n'Who helped me get my hut back?'",
        "correct_ru": "Медведь, волк и кот", "correct_en": "Bear, wolf, and cat"
    },
    {
        "title_ru": "30. Каша из топора", "title_en": "30. Porridge from an Axe",
        "text_ru": "Солдат идёт по дороге с топором.\nКостя: «Бро, он варит кашу?»\n\nСолдат спрашивает:\n«Из чего я варю кашу?»",
        "text_en": "A soldier walks down the road with an axe.\nKostya: 'Bro, is he cooking porridge?'\n\nThe soldier asks:\n'What am I cooking porridge from?'",
        "correct_ru": "Из топора (а баба добавляет крупу)", "correct_en": "From an axe (and the woman adds grain)"
    },
    {
        "title_ru": "31. Лиса и Волк (хвост в проруби)", "title_en": "31. The Fox and the Wolf (Tail in the Ice Hole)",
        "text_ru": "Перед вами прорубь. Из неё торчит хвост.\nКостя: «Бро, это волк.»\n\nВолк спрашивает:\n«Как лиса меня обманула?»",
        "text_en": "An ice hole stands before you. A tail sticks out from it.\nKostya: 'Bro, that's the wolf.'\n\nThe wolf asks:\n'How did the fox trick me?'",
        "correct_ru": "Сказала, что рыба сама ловится", "correct_en": "Said the fish catches itself"
    },
    {
        "title_ru": "32. Поп и работник Балда", "title_en": "32. The Priest and the Worker Balda",
        "text_ru": "Перед вами Балда с верёвкой.\nКостя: «Бро, он чертей перехитрил.»\n\nБалда спрашивает:\n«Что я потребовал у попа в награду?»",
        "text_en": "Balda stands before you with a rope.\nKostya: 'Bro, he outsmarted the devils.'\n\nBalda asks:\n'What did I demand from the priest as a reward?'",
        "correct_ru": "Три щелчка по лбу", "correct_en": "Three flicks on the forehead"
    },
    {
        "title_ru": "33. Умная дочка", "title_en": "33. The Wise Daughter",
        "text_ru": "Перед вами царь и крестьянская дочь.\nКостя: «Бро, она такая умная.»\n\nЦарь спрашивает:\n«Что я велел ей принести, чтобы доказать ум?»",
        "text_en": "A tsar and a peasant's daughter stand before you.\nKostya: 'Bro, she's so smart.'\n\nThe tsar asks:\n'What did I order her to bring to prove her wisdom?'",
        "correct_ru": "Ничего и всё (загадку)", "correct_en": "Nothing and everything (a riddle)"
    },
    {
        "title_ru": "34. Мужик и барин", "title_en": "34. The Peasant and the Landlord",
        "text_ru": "Перед вами поле. Мужик пашет.\nКостя: «Бро, барин опять хитрит.»\n\nМужик спрашивает:\n«Что барин забрал себе в этот раз?»",
        "text_en": "A field stands before you. A peasant is plowing.\nKostya: 'Bro, the landlord is tricky again.'\n\nThe peasant asks:\n'What did the landlord take for himself this time?'",
        "correct_ru": "Вершки (колосья)", "correct_en": "The tops (the ears of grain)"
    },
    {
        "title_ru": "35. Хавочка", "title_en": "35. Havochka (The Little Pig)",
        "text_ru": "Перед вами девочка с пятачком.\nКостя: «Бро, это же Хавочка.»\n\nХавочка спрашивает:\n«Кто меня спас от мачехи?»",
        "text_en": "A girl with a snout stands before you.\nKostya: 'Bro, that's Havochka.'\n\nHavochka asks:\n'Who saved me from the stepmother?'",
        "correct_ru": "Сестрица и волшебная яблоня", "correct_en": "Sister and the magic apple tree"
    },
    {
        "title_ru": "36. Баба-Яга", "title_en": "36. Baba Yaga",
        "text_ru": "Перед вами избушка на курьих ножках.\nКостя: «Бро, это же Баба-Яга.»\n\nБаба-Яга спрашивает:\n«На чём я летаю?»",
        "text_en": "A hut on chicken legs stands before you.\nKostya: 'Bro, that's Baba Yaga.'\n\nBaba Yaga asks:\n'What do I fly on?'",
        "correct_ru": "В ступе", "correct_en": "In a mortar"
    },
    {
        "title_ru": "37. Кощей Бессмертный", "title_en": "37. Koschei the Deathless",
        "text_ru": "Перед вами худой старик с цепями.\nКостя: «Бро, это же Кощей.»\n\nКощей спрашивает:\n«Где спрятана моя смерть?»",
        "text_en": "A thin old man with chains stands before you.\nKostya: 'Bro, that's Koschei.'\n\nKoschei asks:\n'Where is my death hidden?'",
        "correct_ru": "На конце иглы, в яйце", "correct_en": "On the tip of a needle, in an egg"
    },
    {
        "title_ru": "38. Василиса Прекрасная", "title_en": "38. Vasilisa the Beautiful",
        "text_ru": "Перед вами девушка с куклой в руках.\nКостя: «Бро, это Василиса.»\n\nВасилиса спрашивает:\n«Что мне дала мать перед смертью?»",
        "text_en": "A girl with a doll in her hands stands before you.\nKostya: 'Bro, that's Vasilisa.'\n\nVasilisa asks:\n'What did my mother give me before she died?'",
        "correct_ru": "Волшебную куклу", "correct_en": "A magic doll"
    },
    {
        "title_ru": "39. Царевна Несмеяна", "title_en": "39. The Tsarevna Who Couldn't Smile",
        "text_ru": "Перед вами грустная царевна.\nКостя: «Бро, она никогда не смеётся.»\n\nЦаревна спрашивает:\n«Что должно меня рассмешить?»",
        "text_en": "A sad tsarevna stands before you.\nKostya: 'Bro, she never smiles.'\n\nThe tsarevna asks:\n'What should make me laugh?'",
        "correct_ru": "Прыжки дурака в мешке", "correct_en": "A fool jumping in a sack"
    },
    {
        "title_ru": "40. Илья Муромец и Соловей-Разбойник", "title_en": "40. Ilya Muromets and the Nightingale Robber",
        "text_ru": "Перед вами богатырь на коне. В лесу свист.\nКостя: «Бро, это Соловей-Разбойник.»\n\nИлья спрашивает:\n«Как я победил Соловья?»",
        "text_en": "A bogatyr on a horse stands before you. A whistle in the forest.\nKostya: 'Bro, that's the Nightingale Robber.'\n\nIlya asks:\n'How did I defeat the Nightingale?'",
        "correct_ru": "Посадил в мешок и повёз в Киев", "correct_en": "Put him in a sack and took him to Kiev"
    },
    {
        "title_ru": "41. Белоснежка и семь гномов", "title_en": "41. Snow White and the Seven Dwarfs",
        "text_ru": "Перед вами девушка с кожей белой как снег.\nКостя: «Бро, это же Белоснежка.»\n\nБелоснежка спрашивает:\n«Что мне дала злая королева?»",
        "text_en": "A girl with skin white as snow stands before you.\nKostya: 'Bro, that's Snow White.'\n\nSnow White asks:\n'What did the evil queen give me?'",
        "correct_ru": "Отравленное яблоко", "correct_en": "A poisoned apple",
        "wrong_ru": ["Волшебное зеркало", "Золотое кольцо", "Серебряную корону", "Хрустальный башмачок", "Шёлковый платок", "Ядовитый цветок"],
        "wrong_en": ["A magic mirror", "A golden ring", "A silver crown", "A crystal slipper", "A silk scarf", "A poisonous flower"]
    },
    {
        "title_ru": "42. Рапунцель", "title_en": "42. Rapunzel",
        "text_ru": "Перед вами высокая башня. Из окна свисают длинные волосы.\nКостя: «Бро, это же Рапунцель.»\n\nРапунцель спрашивает:\n«Что я использовала вместо лестницы?»",
        "text_en": "A tall tower stands before you. Long hair hangs from the window.\nKostya: 'Bro, that's Rapunzel.'\n\nRapunzel asks:\n'What did I use instead of stairs?'",
        "correct_ru": "Свои волосы", "correct_en": "My hair",
        "wrong_ru": ["Верёвку", "Лестницу", "Канат", "Цепь", "Ветку дерева", "Шарф"],
        "wrong_en": ["A rope", "A ladder", "A cable", "A chain", "A tree branch", "A scarf"]
    },
    {
        "title_ru": "43. Русалочка", "title_en": "43. The Little Mermaid",
        "text_ru": "На камне сидит девушка с рыбьим хвостом.\nКостя: «Бро, это русалочка Андерсена.»\n\nРусалочка спрашивает:\n«Что я отдала морской ведьме?»",
        "text_en": "A girl with a fish tail sits on a rock.\nKostya: 'Bro, that's Andersen's mermaid.'\n\nThe mermaid asks:\n'What did I give to the sea witch?'",
        "correct_ru": "Свой голос", "correct_en": "My voice",
        "wrong_ru": ["Свою красоту", "Свой хвост", "Свои глаза", "Свою память", "Своё имя", "Свою молодость"],
        "wrong_en": ["My beauty", "My tail", "My eyes", "My memory", "My name", "My youth"]
    },
    {
        "title_ru": "44. Гадкий утёнок", "title_en": "44. The Ugly Duckling",
        "text_ru": "Перед вами большой белый лебедь.\nКостя: «Бро, он был таким маленьким и некрасивым.»\n\nЛебедь спрашивает:\n«Кем меня считали все в детстве?»",
        "text_en": "A big white swan stands before you.\nKostya: 'Bro, he was so small and ugly.'\n\nThe swan asks:\n'What did everyone think I was as a child?'",
        "correct_ru": "Гадким утёнком", "correct_en": "An ugly duckling",
        "wrong_ru": ["Цыплёнком", "Гусёнком", "Индюшонком", "Утёнком", "Птенцом", "Канарейкой"],
        "wrong_en": ["A chicken", "A gosling", "A turkey", "A duckling", "A chick", "A canary"]
    },
    {
        "title_ru": "45. Стойкий оловянный солдатик", "title_en": "45. The Steadfast Tin Soldier",
        "text_ru": "Перед вами оловянный солдатик с одной ногой.\nКостя: «Бро, он такой стойкий.»\n\nСолдатик спрашивает:\n«Во что я влюбился?»",
        "text_en": "A tin soldier with one leg stands before you.\nKostya: 'Bro, he's so steadfast.'\n\nThe soldier asks:\n'What did I fall in love with?'",
        "correct_ru": "В бумажную балерину", "correct_en": "A paper ballerina",
        "wrong_ru": ["В принцессу", "В куклу", "В фею", "В танцовщицу", "В актрису", "В певицу"],
        "wrong_en": ["A princess", "A doll", "A fairy", "A dancer", "An actress", "A singer"]
    },
    {
        "title_ru": "46. Спящая красавица", "title_en": "46. Sleeping Beauty",
        "text_ru": "Перед вами спящая принцесса в башне.\nКостя: «Бро, она спит уже сто лет.»\n\nПринцесса спрашивает:\n«Что меня укололо?»",
        "text_en": "A sleeping princess in a tower stands before you.\nKostya: 'Bro, she's been sleeping for a hundred years.'\n\nThe princess asks:\n'What pricked me?'",
        "correct_ru": "Веретено", "correct_en": "A spindle",
        "wrong_ru": ["Игла", "Шип розы", "Нож", "Кинжал", "Стрела", "Копьё"],
        "wrong_en": ["A needle", "A rose thorn", "A knife", "A dagger", "An arrow", "A spear"]
    },
    {
        "title_ru": "47. Красавица и Чудовище", "title_en": "47. Beauty and the Beast",
        "text_ru": "Перед вами ужасное чудовище.\nКостя: «Бро, он выглядит страшно.»\n\nЧудовище спрашивает:\n«Что я на самом деле?»",
        "text_en": "A terrible beast stands before you.\nKostya: 'Bro, he looks scary.'\n\nThe beast asks:\n'What am I really?'",
        "correct_ru": "Принцем", "correct_en": "A prince",
        "wrong_ru": ["Королём", "Колдуном", "Драконом", "Волком", "Медведем", "Великаном"],
        "wrong_en": ["A king", "A sorcerer", "A dragon", "A wolf", "A bear", "A giant"]
    },
    {
        "title_ru": "48. Пиноккио", "title_en": "48. Pinocchio",
        "text_ru": "Перед вами деревянный мальчик с длинным носом.\nКостя: «Бро, это же Пиноккио.»\n\nПиноккио спрашивает:\n«Что происходит с моим носом, когда я вру?»",
        "text_en": "A wooden boy with a long nose stands before you.\nKostya: 'Bro, that's Pinocchio.'\n\nPinocchio asks:\n'What happens to my nose when I lie?'",
        "correct_ru": "Он растёт", "correct_en": "It grows",
        "wrong_ru": ["Он укорачивается", "Он падает", "Он меняет цвет", "Он искривляется", "Он ломается", "Он исчезает"],
        "wrong_en": ["It shrinks", "It falls off", "It changes color", "It twists", "It breaks", "It disappears"]
    },
    {
        "title_ru": "49. Буратино", "title_en": "49. Buratino",
        "text_ru": "Перед вами деревянный мальчик с длинным носом.\nКостя: «Бро, это же Буратино.»\n\nБуратино спрашивает:\n«Кто меня сделал?»",
        "text_en": "A wooden boy with a long nose stands before you.\nKostya: 'Bro, that's Buratino.'\n\nBuratino asks:\n'Who made me?'",
        "correct_ru": "Папа Карло", "correct_en": "Papa Carlo",
        "wrong_ru": ["Джузеппе", "Карабас", "Дуремар", "Кот Базилио", "Лиса Алиса", "Мальвина"],
        "wrong_en": ["Giuseppe", "Karabas", "Duremar", "Cat Basilio", "Fox Alisa", "Malvina"]
    },
    {
        "title_ru": "50. Незнайка", "title_en": "50. Dunno (Neznayka)",
        "text_ru": "Перед вами коротышка в шляпе.\nКостя: «Бро, это же Незнайка.»\n\nНезнайка спрашивает:\n«Где я жил?»",
        "text_en": "A shorty in a hat stands before you.\nKostya: 'Bro, that's Dunno.'\n\nDunno asks:\n'Where did I live?'",
        "correct_ru": "В Цветочном городе", "correct_en": "In Flower City",
        "wrong_ru": ["В Солнечном городе", "В Лунном городе", "В Звёздном городе", "В Радужном городе", "В Весеннем городе", "В Летнем городе"],
        "wrong_en": ["In Sun City", "In Moon City", "In Star City", "In Rainbow City", "In Spring City", "In Summer City"]
    },
    {
        "title_ru": "51. Волшебник Изумрудного города", "title_en": "51. The Wizard of the Emerald City",
        "text_ru": "Перед вами девочка с собачкой.\nКостя: «Бро, это же Элли.»\n\nЭлли спрашивает:\n«Куда меня унесло?»",
        "text_en": "A girl with a dog stands before you.\nKostya: 'Bro, that's Ellie.'\n\nEllie asks:\n'Where was I taken?'",
        "correct_ru": "В Волшебную страну", "correct_en": "To the Magic Land",
        "wrong_ru": ["В Сказочную страну", "В Чудесную страну", "В Заколдованную страну", "В Таинственную страну", "В Древнюю страну", "В Неизвестную страну"],
        "wrong_en": ["To the Fairy Land", "To the Wonderful Land", "To the Enchanted Land", "To the Mysterious Land", "To the Ancient Land", "To the Unknown Land"]
    },
    {
        "title_ru": "52. Страшила", "title_en": "52. The Scarecrow",
        "text_ru": "Перед вами соломенное чучело.\nКостя: «Бро, это же Страшила.»\n\nСтрашила спрашивает:\n«Чего мне не хватает?»",
        "text_en": "A straw scarecrow stands before you.\nKostya: 'Bro, that's the Scarecrow.'\n\nThe Scarecrow asks:\n'What do I lack?'",
        "correct_ru": "Мозгов", "correct_en": "Brains",
        "wrong_ru": ["Сердца", "Смелости", "Силы", "Ловкости", "Зрения", "Слуха"],
        "wrong_en": ["A heart", "Courage", "Strength", "Agility", "Sight", "Hearing"]
    },
    {
        "title_ru": "53. Железный Дровосек", "title_en": "53. The Tin Woodman",
        "text_ru": "Перед вами человек из железа с топором.\nКостя: «Бро, это же Железный Дровосек.»\n\nДровосек спрашивает:\n«Чего мне не хватает?»",
        "text_en": "A man made of iron with an axe stands before you.\nKostya: 'Bro, that's the Tin Woodman.'\n\nThe Woodman asks:\n'What do I lack?'",
        "correct_ru": "Сердца", "correct_en": "A heart",
        "wrong_ru": ["Мозгов", "Смелости", "Силы", "Ловкости", "Зрения", "Слуха"],
        "wrong_en": ["Brains", "Courage", "Strength", "Agility", "Sight", "Hearing"]
    },
    {
        "title_ru": "54. Трусливый Лев", "title_en": "54. The Cowardly Lion",
        "text_ru": "Перед вами большой лев.\nКостя: «Бро, он боится всего.»\n\nЛев спрашивает:\n«Чего мне не хватает?»",
        "text_en": "A big lion stands before you.\nKostya: 'Bro, he's afraid of everything.'\n\nThe lion asks:\n'What do I lack?'",
        "correct_ru": "Смелости", "correct_en": "Courage",
        "wrong_ru": ["Мозгов", "Сердца", "Силы", "Ловкости", "Зрения", "Слуха"],
        "wrong_en": ["Brains", "A heart", "Strength", "Agility", "Sight", "Hearing"]
    },
    {
        "title_ru": "55. Гудвин", "title_en": "55. Goodwin",
        "text_ru": "Перед вами великий волшебник.\nКостя: «Бро, это же Гудвин.»\n\nГудвин спрашивает:\n«Где я живу?»",
        "text_en": "A great wizard stands before you.\nKostya: 'Bro, that's Goodwin.'\n\nGoodwin asks:\n'Where do I live?'",
        "correct_ru": "В Изумрудном городе", "correct_en": "In the Emerald City",
        "wrong_ru": ["В Золотом городе", "В Серебряном городе", "В Хрустальном городе", "В Алмазном городе", "В Рубиновом городе", "В Сапфировом городе"],
        "wrong_en": ["In the Golden City", "In the Silver City", "In the Crystal City", "In the Diamond City", "In the Ruby City", "In the Sapphire City"]
    },
    {
        "title_ru": "56. Садко", "title_en": "56. Sadko",
        "text_ru": "Перед вами гусляр на берегу моря.\nКостя: «Бро, это же Садко.»\n\nСадко спрашивает:\n«Кто забрал меня в подводное царство?»",
        "text_en": "A gusli player on the seashore stands before you.\nKostya: 'Bro, that's Sadko.'\n\nSadko asks:\n'Who took me to the underwater kingdom?'",
        "correct_ru": "Морской царь", "correct_en": "The Sea King",
        "wrong_ru": ["Водяной", "Нептун", "Посейдон", "Тритон", "Русалка", "Морская ведьма"],
        "wrong_en": ["The Water Spirit", "Neptune", "Poseidon", "Triton", "A mermaid", "A sea witch"]
    },
    {
        "title_ru": "57. Добрыня Никитич", "title_en": "57. Dobrynya Nikitich",
        "text_ru": "Перед вами богатырь с мечом.\nКостя: «Бро, это же Добрыня.»\n\nДобрыня спрашивает:\n«Кого я победил?»",
        "text_en": "A bogatyr with a sword stands before you.\nKostya: 'Bro, that's Dobrynya.'\n\nDobrynya asks:\n'Whom did I defeat?'",
        "correct_ru": "Змея Горыныча", "correct_en": "Zmey Gorynych",
        "wrong_ru": ["Кощея Бессмертного", "Соловья-Разбойника", "Идолище Поганое", "Тугарина Змеевича", "Жидовина", "Полкана"],
        "wrong_en": ["Koschei the Deathless", "The Nightingale Robber", "Idolishche", "Tugarin Zmeyevich", "Zhidovin", "Polkan"]
    },
    {
        "title_ru": "58. Алёша Попович", "title_en": "58. Alyosha Popovich",
        "text_ru": "Перед вами молодой богатырь.\nКостя: «Бро, это же Алёша.»\n\nАлёша спрашивает:\n«Кого я победил хитростью?»",
        "text_en": "A young bogatyr stands before you.\nKostya: 'Bro, that's Alyosha.'\n\nAlyosha asks:\n'Whom did I defeat with cunning?'",
        "correct_ru": "Тугарина Змеевича", "correct_en": "Tugarin Zmeyevich",
        "wrong_ru": ["Кощея Бессмертного", "Соловья-Разбойника", "Змея Горыныча", "Идолище Поганое", "Жидовина", "Полкана"],
        "wrong_en": ["Koschei the Deathless", "The Nightingale Robber", "Zmey Gorynych", "Idolishche", "Zhidovin", "Polkan"]
    },
    {
        "title_ru": "59. Никита Кожемяка", "title_en": "59. Nikita Kozhemyaka",
        "text_ru": "Перед вами сильный богатырь.\nКостя: «Бро, он такой мощный.»\n\nНикита спрашивает:\n«Кого я победил?»",
        "text_en": "A strong bogatyr stands before you.\nKostya: 'Bro, he's so powerful.'\n\nNikita asks:\n'Whom did I defeat?'",
        "correct_ru": "Змея-людоеда", "correct_en": "The man-eating dragon",
        "wrong_ru": ["Кощея Бессмертного", "Соловья-Разбойника", "Змея Горыныча", "Идолище Поганое", "Тугарина Змеевича", "Жидовина"],
        "wrong_en": ["Koschei the Deathless", "The Nightingale Robber", "Zmey Gorynych", "Idolishche", "Tugarin Zmeyevich", "Zhidovin"]
    },
    {
        "title_ru": "60. Змей Горыныч", "title_en": "60. Zmey Gorynych",
        "text_ru": "Перед вами трёхглавый дракон.\nКостя: «Бро, это же Горыныч.»\n\nГорыныч спрашивает:\n«Сколько у меня голов?»",
        "text_en": "A three-headed dragon stands before you.\nKostya: 'Bro, that's Gorynych.'\n\nGorynych asks:\n'How many heads do I have?'",
        "correct_ru": "Три", "correct_en": "Three",
        "wrong_ru": ["Две", "Четыре", "Пять", "Шесть", "Семь", "Девять"],
        "wrong_en": ["Two", "Four", "Five", "Six", "Seven", "Nine"]
    },
    {
        "title_ru": "61. Маугли", "title_en": "61. The Jungle Book",
        "text_ru": "Перед вами мальчик, которого воспитали волки.\nКостя: «Бро, это же Маугли.»\n\nМаугли спрашивает:\n«Кто научил меня Закону джунглей?»",
        "text_en": "A boy raised by wolves stands before you.\nKostya: 'Bro, that's Mowgli.'\n\nMowgli asks:\n'Who taught me the Law of the Jungle?'",
        "correct_ru": "Багира и Балу", "correct_en": "Bagheera and Baloo",
        "wrong_ru": ["Каа", "Шакал Табаки", "Шерхан", "Акела", "Ракша", "Хати"],
        "wrong_en": ["Kaa", "Tabaqui", "Shere Khan", "Akela", "Raksha", "Hathi"]
    },
    {
        "title_ru": "62. Винни-Пух", "title_en": "62. Winnie the Pooh",
        "text_ru": "Перед вами медвежонок в красной футболке.\nКостя: «Бро, он что-то ищет.»\n\nВинни-Пух спрашивает:\n«Что я люблю есть больше всего?»",
        "text_en": "A bear cub in a red shirt stands before you.\nKostya: 'Bro, he's looking for something.'\n\nWinnie the Pooh asks:\n'What do I love to eat the most?'",
        "correct_ru": "Мёд", "correct_en": "Honey",
        "wrong_ru": ["Сгущёнку", "Варенье", "Яблоки", "Орехи", "Траву", "Рыбу"],
        "wrong_en": ["Condensed milk", "Jam", "Apples", "Nuts", "Grass", "Fish"]
    },
    {
        "title_ru": "63. Карлсон", "title_en": "63. Karlsson-on-the-Roof",
        "text_ru": "На крыше стоит мужчина с пропеллером.\nКостя: «Бро, это же Карлсон.»\n\nКарлсон спрашивает:\n«Как я называю свои проделки?»",
        "text_en": "A man with a propeller stands on the roof.\nKostya: 'Bro, that's Karlsson.'\n\nKarlsson asks:\n'What do I call my pranks?'",
        "correct_ru": "Дело житейское", "correct_en": "A mere trifle",
        "wrong_ru": ["Варенье", "Печенье", "Мотор", "Шалости", "Игрушки", "Сюрпризы"],
        "wrong_en": ["Jam", "Cookies", "Motor", "Mischief", "Toys", "Surprises"]
    },
    {
        "title_ru": "64. Чиполлино", "title_en": "64. Cipollino",
        "text_ru": "Перед вами мальчик-луковка.\nКостя: «Бро, от него пахнет луком.»\n\nЧиполлино спрашивает:\n«Кто был моим главным врагом?»",
        "text_en": "An onion boy stands before you.\nKostya: 'Bro, he smells like onions.'\n\nCipollino asks:\n'Who was my main enemy?'",
        "correct_ru": "Принц Лимон", "correct_en": "Prince Lemon",
        "wrong_ru": ["Синьор Помидор", "Граф Вишенка", "Синьор Морковь", "Кавалер Редис", "Синьор Тыква", "Герцог Апельсин"],
        "wrong_en": ["Mr. Tomato", "Count Cherry", "Mr. Carrot", "Sir Radish", "Mr. Pumpkin", "Duke Orange"]
    },
    {
        "title_ru": "65. Бременские музыканты", "title_en": "65. Town Musicians of Bremen",
        "text_ru": "По дороге идут осёл, петух, кот и пёс.\nКостя: «Бро, они идут в город.»\n\nМузыканты спрашивают:\n«Кто шёл за нами по пятам?»",
        "text_en": "A donkey, a rooster, a cat, and a dog walk down the road.\nKostya: 'Bro, they are going to the city.'\n\nThe musicians ask:\n'Who followed us closely?'",
        "correct_ru": "Разбойники", "correct_en": "The robbers",
        "wrong_ru": ["Волк", "Медведь", "Лиса", "Охотник", "Король", "Дракон"],
        "wrong_en": ["The wolf", "The bear", "The fox", "The hunter", "The king", "The dragon"]
    },
    {
        "title_ru": "66. Маленький принц", "title_en": "66. The Little Prince",
        "text_ru": "Перед вами мальчик с золотыми волосами.\nКостя: «Бро, он с другой планеты.»\n\nМаленький принц спрашивает:\n«Что я просил нарисовать пилота?»",
        "text_en": "A boy with golden hair stands before you.\nKostya: 'Bro, he is from another planet.'\n\nThe Little Prince asks:\n'What did I ask the pilot to draw?'",
        "correct_ru": "Барашка", "correct_en": "A sheep",
        "wrong_ru": ["Самолёт", "Розу", "Змею", "Лиса", "Планету", "Звезду"],
        "wrong_en": ["An airplane", "A rose", "A snake", "A fox", "A planet", "A star"]
    },
    {
        "title_ru": "67. Простоквашино", "title_en": "67. Prostokvashino",
        "text_ru": "Перед вами деревенский дом. Из окна выглядывает кот.\nКостя: «Бро, это же Простоквашино.»\n\nКот спрашивает:\n«Как меня зовут?»",
        "text_en": "A country house stands before you. A cat peeks out of the window.\nKostya: 'Bro, that's Prostokvashino.'\n\nThe cat asks:\n'What is my name?'",
        "correct_ru": "Матроскин", "correct_en": "Matroskin",
        "wrong_ru": ["Мурзик", "Барсик", "Леопольд", "Базилио", "Гарфилд", "Том"],
        "wrong_en": ["Murzik", "Barsik", "Leopold", "Basilio", "Garfield", "Tom"]
    },
    {
        "title_ru": "68. Чёрная курица", "title_en": "68. Black Chicken",
        "text_ru": "Перед вами мальчик в подземном королевстве.\nКостя: «Бро, это же Алёша.»\n\nАлёша спрашивает:\n«Что я получил от Чёрной курицы за спасение?»",
        "text_en": "A boy in an underground kingdom stands before you.\nKostya: 'Bro, that's Alyosha.'\n\nAlyosha asks:\n'What did I receive from the Black Chicken for saving it?'",
        "correct_ru": "Конопляное зёрнышко", "correct_en": "A hemp seed",
        "wrong_ru": ["Золотую монету", "Волшебную палочку", "Ключ", "Кольцо", "Меч", "Корону"],
        "wrong_en": ["A gold coin", "A magic wand", "A key", "A ring", "A sword", "A crown"]
    },
    {
        "title_ru": "69. Старик Хоттабыч", "title_en": "69. Old Man Hottabych",
        "text_ru": "Перед вами старик в чалме, вырывающий волосы из бороды.\nКостя: «Бро, это же Хоттабыч.»\n\nХоттабыч спрашивает:\n«Как звали мальчика, которому я помогал?»",
        "text_en": "An old man in a turban plucking hairs from his beard stands before you.\nKostya: 'Bro, that's Hottabych.'\n\nHottabych asks:\n'What was the name of the boy I helped?'",
        "correct_ru": "Волька", "correct_en": "Volka",
        "wrong_ru": ["Гена", "Чебурашка", "Алёша", "Петя", "Саша", "Дима"],
        "wrong_en": ["Gena", "Cheburashka", "Alyosha", "Petya", "Sasha", "Dima"]
    },
    {
        "title_ru": "70. Приключения Электроника", "title_en": "70. Adventures of Electronics",
        "text_ru": "Перед вами робот-мальчик.\nКостя: «Бро, он же настоящий.»\n\nЭлектроник спрашивает:\n«Кто был моим двойником?»",
        "text_en": "A robot boy stands before you.\nKostya: 'Bro, he is real.'\n\nElectronics asks:\n'Who was my double?'",
        "correct_ru": "Сыроежкин", "correct_en": "Syroyezhkin",
        "wrong_ru": ["Гусь", "Чижиков", "Макаров", "Таратар", "Профессор Громов", "Учитель истории"],
        "wrong_en": ["Goose", "Chizhikov", "Makarov", "Taratar", "Professor Gromov", "History teacher"]
    },
    {
        "title_ru": "71. Алиса в Зазеркалье", "title_en": "71. Through the Looking-Glass",
        "text_ru": "Перед вами зеркало, в котором всё наоборот.\nКостя: «Бро, это не та страна чудес.»\n\nАлиса спрашивает:\n«Какой шахматной фигурой я стала в Зазеркалье?»",
        "text_en": "A mirror where everything is backwards stands before you.\nKostya: 'Bro, this isn't Wonderland.'\n\nAlice asks:\n'What chess piece did I become in the Looking-Glass?'",
        "correct_ru": "Пешкой", "correct_en": "A pawn",
        "wrong_ru": ["Королевой", "Королём", "Конём", "Слоном", "Ладьёй", "Тузом"],
        "wrong_en": ["A queen", "A king", "A knight", "A bishop", "A rook", "An ace"]
    },
    {
        "title_ru": "72. Питер Пэн", "title_en": "72. Peter Pan",
        "text_ru": "Перед вами мальчик, который не хочет взрослеть.\nКостя: «Бро, он умеет летать.»\n\nПитер Пэн спрашивает:\n«Что я потерял в доме Дарлингов?»",
        "text_en": "A boy who doesn't want to grow up stands before you.\nKostya: 'Bro, he can fly.'\n\nPeter Pan asks:\n'What did I lose at the Darlings' house?'",
        "correct_ru": "Свою тень", "correct_en": "My shadow",
        "wrong_ru": ["Свой меч", "Свою шляпу", "Свой крюк", "Свою фею", "Свой корабль", "Свой компас"],
        "wrong_en": ["My sword", "My hat", "My hook", "My fairy", "My ship", "My compass"]
    },
    {
        "title_ru": "73. Вий", "title_en": "73. Viy",
        "text_ru": "В церкви стоит гроб. Из-под него выглядывает страшное существо.\nКостя: «Бро, мне страшно.»\n\nВий спрашивает:\n«Что я кричал, когда меня привели к Хоме Бруту?»",
        "text_en": "A coffin stands in the church. A terrible creature peeks out from under it.\nKostya: 'Bro, I'm scared.'\n\nViy asks:\n'What did I shout when brought to Khoma Brut?'",
        "correct_ru": "«Поднимите мне веки!»", "correct_en": "\"Lift my eyelids!\"",
        "wrong_ru": ["«Убейте его!»", "«Сожгите его!»", "«Свяжите его!»", "«Прогоните его!»", "«Накажите его!»", "«Схватите его!»"],
        "wrong_en": ["\"Kill him!\"", "\"Burn him!\"", "\"Bind him!\"", "\"Chase him away!\"", "\"Punish him!\"", "\"Catch him!\""]
    },
    {
        "title_ru": "74. Ночь перед Рождеством", "title_en": "74. The Night Before Christmas",
        "text_ru": "Ночное небо. Чёрт сидит на месяце.\nКостя: «Бро, он украл его у кузнеца.»\n\nЧёрт спрашивает:\n«Что я украл у кузнеца Вакулы?»",
        "text_en": "The night sky. A devil sits on the moon.\nKostya: 'Bro, he stole it from the blacksmith.'\n\nThe devil asks:\n'What did I steal from the blacksmith Vakula?'",
        "correct_ru": "Месяц", "correct_en": "The moon",
        "wrong_ru": ["Солнце", "Звезду", "Подкову", "Молот", "Душу", "Сердце"],
        "wrong_en": ["The sun", "A star", "A horseshoe", "A hammer", "A soul", "A heart"]
    },
    {
        "title_ru": "75. Руслан и Людмила", "title_en": "75. Ruslan and Lyudmila",
        "text_ru": "Перед вами гигантская голова и спящая богатырша.\nКостя: «Бро, это же Пушкин.»\n\nЧерномор спрашивает:\n«Кто отрубил мне голову?»",
        "text_en": "A giant head and a sleeping heroine stand before you.\nKostya: 'Bro, that's Pushkin.'\n\nChernomor asks:\n'Who cut off my head?'",
        "correct_ru": "Руслан", "correct_en": "Ruslan",
        "wrong_ru": ["Ратмир", "Фарлаф", "Наина", "Финн", "Святослав", "Олег"],
        "wrong_en": ["Ratmir", "Farlaf", "Naina", "Finn", "Svyatoslav", "Oleg"]
    },
    {
        "title_ru": "76. Сказка о царе Салтане", "title_en": "76. The Tale of Tsar Saltan",
        "text_ru": "Из морской пены выходят богатыри.\nКостя: «Бро, их ровно тридцать три.»\n\nБогатыри спрашивают:\n«Кто вышел из моря вместе с нами?»",
        "text_en": "Bogatyrs emerge from the sea foam.\nKostya: 'Bro, there are exactly thirty-three of them.'\n\nThe bogatyrs ask:\n'Who emerged from the sea along with us?'",
        "correct_ru": "Царевна Лебедь", "correct_en": "The Swan Princess",
        "wrong_ru": ["Русалка", "Золотая рыбка", "Морская царевна", "Волна", "Жемчужина", "Чайка"],
        "wrong_en": ["A mermaid", "A golden fish", "A sea princess", "A wave", "A pearl", "A seagull"]
    },
    {
        "title_ru": "77. Сивка-Бурка", "title_en": "77. Sivka-Burka",
        "text_ru": "Перед вами поле. Мальчик свистит.\nКостя: «Бро, сейчас прибежит конь.»\n\nМальчик спрашивает:\n«Что нужно сделать, чтобы вызвать Сивку-Бурку?»",
        "text_en": "A field stands before you. A boy whistles.\nKostya: 'Bro, the horse will run here now.'\n\nThe boy asks:\n'What must be done to summon Sivka-Burka?'",
        "correct_ru": "Свистнуть и позвать его", "correct_en": "Whistle and call him",
        "wrong_ru": ["Спеть песню", "Ударить в бубен", "Зажечь огонь", "Постучать в бубен", "Поклониться", "Заплакать"],
        "wrong_en": ["Sing a song", "Beat a tambourine", "Light a fire", "Knock on a drum", "Bow", "Cry"]
    },
    {
        "title_ru": "78. Летучий корабль", "title_en": "78. The Flying Ship",
        "text_ru": "Перед вами царь и простой парень.\nКостя: «Бро, он выполнил все условия.»\n\nЦарь спрашивает:\n«Что ты должен был принести мне, чтобы жениться на царевне?»",
        "text_en": "A tsar and a simple guy stand before you.\nKostya: 'Bro, he met all the conditions.'\n\nThe tsar asks:\n'What did you have to bring me to marry the princess?'",
        "correct_ru": "Летучий корабль", "correct_en": "A flying ship",
        "wrong_ru": ["Золотое яблоко", "Живую воду", "Чудо-юдо", "Ковёр-самолёт", "Меч-кладенец", "Перо жар-птицы"],
        "wrong_en": ["A golden apple", "Living water", "A monster", "A magic carpet", "A magic sword", "A firebird's feather"]
    },
    {
        "title_ru": "79. Дикие лебеди", "title_en": "79. The Wild Swans",
        "text_ru": "Девушка молча плетёт что-то из колючих растений.\nКостя: «Бро, её руки в кровь.»\n\nЭльза спрашивает:\n«Из чего я плела рубашки для своих братьев?»",
        "text_en": "A girl silently weaves something from prickly plants.\nKostya: 'Bro, her hands are bleeding.'\n\nEliza asks:\n'What did I weave the shirts for my brothers from?'",
        "correct_ru": "Из крапивы", "correct_en": "From nettles",
        "wrong_ru": ["Из шёлка", "Из шерсти", "Из льна", "Из хлопка", "Из золота", "Из перьев"],
        "wrong_en": ["From silk", "From wool", "From flax", "From cotton", "From gold", "From feathers"]
    },
    {
        "title_ru": "80. Огниво", "title_en": "80. The Tinderbox",
        "text_ru": "Перед вами солдат и три огромные собаки.\nКостя: «Бро, у них глаза как тарелки.»\n\nСолдат спрашивает:\n«Сколько глаз было у собаки, охранявшей медь?»",
        "text_en": "A soldier and three huge dogs stand before you.\nKostya: 'Bro, their eyes are like saucers.'\n\nThe soldier asks:\n'How many eyes did the dog guarding the copper have?'",
        "correct_ru": "Как колёса у телеги", "correct_en": "Like carriage wheels",
        "wrong_ru": ["Как чайные чашки", "Как блюдца", "Как звёзды", "Как монеты", "Как пуговицы", "Как орехи"],
        "wrong_en": ["Like teacups", "Like saucers", "Like stars", "Like coins", "Like buttons", "Like nuts"]
    },
    {
        "title_ru": "81. Новые наряды короля", "title_en": "81. The Emperor's New Clothes",
        "text_ru": "Перед вами король, который гордо шагает по улице.\nКостя: «Бро, он же голый!»\n\nКороль спрашивает:\n«Из чего сделан мой новый наряд?»",
        "text_en": "A king proudly walks down the street.\nKostya: 'Bro, he's naked!'\n\nThe king asks:\n'What is my new suit made of?'",
        "correct_ru": "Ни из чего (он невидимый)", "correct_en": "Nothing (it is invisible)",
        "wrong_ru": ["Из шёлка", "Из золота", "Из бархата", "Из серебра", "Из пурпура", "Из шерсти"],
        "wrong_en": ["Silk", "Gold", "Velvet", "Silver", "Purple", "Wool"]
    },
    {
        "title_ru": "82. Храбрый портняжка", "title_en": "82. The Brave Little Tailor",
        "text_ru": "Перед вами маленький портной с поясом.\nКостя: «Бро, он победил великанов.»\n\nПортняжка спрашивает:\n«Что было написано на моём поясе?»",
        "text_en": "A little tailor with a belt stands before you.\nKostya: 'Bro, he defeated giants.'\n\nThe tailor asks:\n'What was written on my belt?'",
        "correct_ru": "Семерых одним махом", "correct_en": "Seven at one blow",
        "wrong_ru": ["Одного великана", "Двух драконов", "Трёх медведей", "Четырёх волков", "Пять разбойников", "Шесть львов"],
        "wrong_en": ["One giant", "Two dragons", "Three bears", "Four wolves", "Five robbers", "Six lions"]
    },
    {
        "title_ru": "83. Гамельнский крысолов", "title_en": "83. The Pied Piper of Hamelin",
        "text_ru": "Перед вами человек с дудочкой.\nКостя: «Бро, он увёл всех детей.»\n\nКрысолов спрашивает:\n«Кого я сначала вывел из города?»",
        "text_en": "A man with a pipe stands before you.\nKostya: 'Bro, he led all the children away.'\n\nThe piper asks:\n'Who did I lead out of the town first?'",
        "correct_ru": "Крыс", "correct_en": "Rats",
        "wrong_ru": ["Мышей", "Котов", "Собак", "Жуков", "Пауков", "Змей"],
        "wrong_en": ["Mice", "Cats", "Dogs", "Beetles", "Spiders", "Snakes"]
    },
    {
        "title_ru": "84. Золотой гусь", "title_en": "84. The Golden Goose",
        "text_ru": "Перед вами гусь, за которым тянется вереница людей.\nКостя: «Бро, они все прилипли.»\n\nГусь спрашивает:\n«Что происходило с теми, кто меня касался?»",
        "text_en": "A goose with a line of people trailing behind it stands before you.\nKostya: 'Bro, they are all stuck.'\n\nThe goose asks:\n'What happened to those who touched me?'",
        "correct_ru": "Они прилипали", "correct_en": "They got stuck",
        "wrong_ru": ["Они летали", "Они богатели", "Они говорили", "Они пели", "Они исчезали", "Они превращались в золото"],
        "wrong_en": ["They flew", "They got rich", "They spoke", "They sang", "They disappeared", "They turned to gold"]
    },
    {
        "title_ru": "85. Румпельштильцхен", "title_en": "85. Rumpelstiltskin",
        "text_ru": "Перед вами маленький странный старичок.\nКостя: «Бро, он прядёт золото.»\n\nСтаричок спрашивает:\n«Что должна была угадать королева, чтобы забрать ребёнка?»",
        "text_en": "A strange little old man stands before you.\nKostya: 'Bro, he spins gold.'\n\nThe old man asks:\n'What did the queen have to guess to keep her child?'",
        "correct_ru": "Моё имя", "correct_en": "My name",
        "wrong_ru": ["Мой возраст", "Мою силу", "Мой дом", "Мою профессию", "Мой цвет", "Мою тень"],
        "wrong_en": ["My age", "My strength", "My home", "My profession", "My color", "My shadow"]
    },
    {
        "title_ru": "86. Двенадцать месяцев", "title_en": "86. The Twelve Months",
        "text_ru": "Перед вами заснеженный лес и девочка с корзиной.\nКостя: «Бро, сейчас зима.»\n\nДевочка спрашивает:\n«Какие цветы я должна была найти в январе?»",
        "text_en": "A snowy forest and a girl with a basket stand before you.\nKostya: 'Bro, it's winter now.'\n\nThe girl asks:\n'What flowers was I supposed to find in January?'",
        "correct_ru": "Подснежники", "correct_en": "Snowdrops",
        "wrong_ru": ["Розы", "Тюльпаны", "Ромашки", "Ландыши", "Сирень", "Пионы"],
        "wrong_en": ["Roses", "Tulips", "Daisies", "Lilies of the valley", "Lilacs", "Peonies"]
    },
    {
        "title_ru": "87. Снегурочка", "title_en": "87. The Snow Maiden",
        "text_ru": "Перед вами прекрасная девушка из снега.\nКостя: «Бро, ей нельзя греться.»\n\nСнегурочка спрашивает:\n«От чего я растаяла?»",
        "text_en": "A beautiful girl made of snow stands before you.\nKostya: 'Bro, she can't get warm.'\n\nThe Snow Maiden asks:\n'What made me melt?'",
        "correct_ru": "От прыжка через костёр (солнечного луча)", "correct_en": "Jumping over a bonfire (a sunbeam)",
        "wrong_ru": ["От дождя", "От ветра", "От холода", "От старости", "От злого слова", "От громкой музыки"],
        "wrong_en": ["Rain", "Wind", "Cold", "Old age", "A mean word", "Loud music"]
    },
    {
        "title_ru": "88. Жар-птица", "title_en": "88. The Firebird",
        "text_ru": "В клетке сидит птица, освещающая всё вокруг.\nКостя: «Бро, она горит, но не сгорает.»\n\nЖар-птица спрашивает:\n«Что я обронила в саду царя?»",
        "text_en": "A bird that illuminates everything sits in a cage.\nKostya: 'Bro, it burns but doesn't burn out.'\n\nThe Firebird asks:\n'What did I drop in the tsar's garden?'",
        "correct_ru": "Одно золотое перо", "correct_en": "A single golden feather",
        "wrong_ru": ["Клюв", "Коготь", "Яйцо", "Крыло", "Глаз", "Хвост"],
        "wrong_en": ["A beak", "A claw", "An egg", "A wing", "An eye", "A tail"]
    },
    {
        "title_ru": "89. Сказка о мёртвой царевне", "title_en": "89. The Tale of the Dead Princess",
        "text_ru": "Перед вами спящая царевна и семь богатырей.\nКостя: «Бро, это пушкинская версия.»\n\nЦаревна спрашивает:\n«Чем меня отравила мачеха?»",
        "text_en": "A sleeping princess and seven bogatyrs stand before you.\nKostya: 'Bro, this is the Pushkin version.'\n\nThe princess asks:\n'What did my stepmother poison me with?'",
        "correct_ru": "Яблоком", "correct_en": "An apple",
        "wrong_ru": ["Грушей", "Персиком", "Вишней", "Сливой", "Гранатом", "Апельсином"],
        "wrong_en": ["A pear", "A peach", "A cherry", "A plum", "A pomegranate", "An orange"]
    },
    {
        "title_ru": "90. Сказка о золотом петушке", "title_en": "90. The Tale of the Golden Cockerel",
        "text_ru": "На спице сидит золотая птица.\nКостя: «Бро, он предупреждает об опасности.»\n\nПетушок спрашивает:\n«Что я должен был кричать при тревоге?»",
        "text_en": "A golden bird sits on a spire.\nKostya: 'Bro, he warns of danger.'\n\nThe cockerel asks:\n'What was I supposed to crow when there was danger?'",
        "correct_ru": "Кири-ку-ку", "correct_en": "Cock-a-doodle-doo (Kiri-ku-ku)",
        "wrong_ru": ["Кукареку", "Спеть песню", "Ударить в барабан", "Свистнуть", "Хлопнуть в ладоши", "Топнуть ногой"],
        "wrong_en": ["Cock-a-doodle-doo", "Sing a song", "Beat a drum", "Whistle", "Clap hands", "Stomp a foot"]
    },
    {
        "title_ru": "91. Каменный цветок", "title_en": "91. The Stone Flower",
        "text_ru": "Перед вами мастер, смотрящий на идеальный цветок из малахита.\nКостя: «Бро, это работа Данилы.»\n\nДанила спрашивает:\n«Кто показал мне этот цветок?»",
        "text_en": "A craftsman looking at a perfect malachite flower stands before you.\nKostya: 'Bro, this is Danila's work.'\n\nDanila asks:\n'Who showed me this flower?'",
        "correct_ru": "Хозяйка Медной горы", "correct_en": "The Mistress of the Copper Mountain",
        "wrong_ru": ["Снежная королева", "Русалка", "Баба-Яга", "Царевна-лягушка", "Золотая рыбка", "Василиса Премудрая"],
        "wrong_en": ["The Snow Queen", "A mermaid", "Baba Yaga", "The Frog Princess", "The Golden Fish", "Vasilisa the Wise"]
    },
    {
        "title_ru": "92. Алые паруса", "title_en": "92. Scarlet Sails",
        "text_ru": "Девушка смотрит на море.\nКостя: «Бро, корабль уже плывёт.»\n\nАссоль спрашивает:\n«Какого цвета были паруса корабля, который меня забрал?»",
        "text_en": "A girl looks out at the sea.\nKostya: 'Bro, the ship is already sailing.'\n\nAssol asks:\n'What color were the sails of the ship that came for me?'",
        "correct_ru": "Алые", "correct_en": "Scarlet",
        "wrong_ru": ["Белые", "Золотые", "Синие", "Чёрные", "Зелёные", "Пурпурные"],
        "wrong_en": ["White", "Golden", "Blue", "Black", "Green", "Purple"]
    },
    {
        "title_ru": "93. Счастливый принц", "title_en": "93. The Happy Prince",
        "text_ru": "Перед вами статуя принца, покрытая сусальным золотом.\nКостя: «Бро, он плачет.»\n\nПринц спрашивает:\n«Что было внутри моей статуи, когда её переплавили?»",
        "text_en": "A statue of a prince covered in gold leaf stands before you.\nKostya: 'Bro, he is crying.'\n\nThe prince asks:\n'What was inside my statue when it was melted down?'",
        "correct_ru": "Свинцовое сердце", "correct_en": "A leaden heart",
        "wrong_ru": ["Золотое сердце", "Серебряное сердце", "Хрустальное сердце", "Каменное сердце", "Деревянное сердце", "Стеклянное сердце"],
        "wrong_en": ["A golden heart", "A silver heart", "A crystal heart", "A stone heart", "A wooden heart", "A glass heart"]
    },
    {
        "title_ru": "94. Щелкунчик", "title_en": "94. The Nutcracker",
        "text_ru": "Перед вами деревянная игрушка-солдатик.\nКостя: «Бро, он победил мышей.»\n\nЩелкунчик спрашивает:\n«Кто был моим главным врагом?»",
        "text_en": "A wooden toy soldier stands before you.\nKostya: 'Bro, he defeated the mice.'\n\nThe Nutcracker asks:\n'Who was my main enemy?'",
        "correct_ru": "Мышиный король", "correct_en": "The Mouse King",
        "wrong_ru": ["Крысиный король", "Кошачий король", "Собачий король", "Лисий король", "Волчий король", "Медвежий король"],
        "wrong_en": ["The Rat King", "The Cat King", "The Dog King", "The Fox King", "The Wolf King", "The Bear King"]
    },
    {
        "title_ru": "95. Кот в сапогах", "title_en": "95. Puss in Boots",
        "text_ru": "Перед вами хитрый кот в высоких сапогах.\nКостя: «Бро, он сделал из хозяина маркиза.»\n\nКот спрашивает:\n«Какое имя я придумал для своего хозяина?»",
        "text_en": "A cunning cat in tall boots stands before you.\nKostya: 'Bro, he made his master a marquis.'\n\nThe cat asks:\n'What name did I invent for my master?'",
        "correct_ru": "Маркиз де Карабас", "correct_en": "Marquis of Carabas",
        "wrong_ru": ["Граф де Монте-Кристо", "Барон де Мюнхгаузен", "Герцог де Ришельё", "Принц де Конде", "Король де Франс", "Сеньор де Помидор"],
        "wrong_en": ["Count of Monte Cristo", "Baron Munchausen", "Duke of Richelieu", "Prince de Condé", "King of France", "Lord Tomato"]
    },
    {
        "title_ru": "96. Джек и бобовый стебель", "title_en": "96. Jack and the Beanstalk",
        "text_ru": "Перед вами огромный стебель, уходящий в облака.\nКостя: «Бро, наверху живёт великан.»\n\nДжек спрашивает:\n«За что я продал нашу корову?»",
        "text_en": "A giant stalk reaching into the clouds stands before you.\nKostya: 'Bro, a giant lives up there.'\n\nJack asks:\n'What did I sell our cow for?'",
        "correct_ru": "За волшебные бобы", "correct_en": "Magic beans",
        "wrong_ru": ["За золотые монеты", "За серебряные ключи", "За волшебные семена", "За хрустальные шарики", "За алмазные кольца", "За изумрудные камешки"],
        "wrong_en": ["Gold coins", "Silver keys", "Magic seeds", "Crystal balls", "Diamond rings", "Emerald stones"]
    },
    {
        "title_ru": "97. Синяя Борода", "title_en": "97. Bluebeard",
        "text_ru": "Перед вами богатый замок и связка ключей.\nКостя: «Бро, не открывай ту дверь.»\n\nСиняя Борода спрашивает:\n«Что я дал своей жене с одним строгим запретом?»",
        "text_en": "A rich castle and a bunch of keys stand before you.\nKostya: 'Bro, don't open that door.'\n\nBluebeard asks:\n'What did I give my wife with one strict prohibition?'",
        "correct_ru": "Ключ от запретной комнаты", "correct_en": "The key to the forbidden room",
        "wrong_ru": ["Меч", "Кольцо", "Корону", "Книгу", "Зеркало", "Карту"],
        "wrong_en": ["A sword", "A ring", "A crown", "A book", "A mirror", "A map"]
    },
    {
        "title_ru": "98. Принцесса на горошине", "title_en": "98. The Princess and the Pea",
        "text_ru": "Перед вами замок и мокрая девушка.\nКостя: «Бро, она не могла уснуть.»\n\nПринцесса спрашивает:\n«Что лежало подо мной ночью?»",
        "text_en": "A castle and a wet girl stand before you.\nKostya: 'Bro, she couldn't sleep.'\n\nThe princess asks:\n'What was under me at night?'",
        "correct_ru": "Горошина (под 20 тюфяками и 20 перинами)", "correct_en": "A pea (under 20 mattresses and 20 feather beds)",
        "wrong_ru": ["Золотая монета", "Серебряная ложка", "Алмазное кольцо", "Хрустальный шар", "Шёлковая лента", "Перо павлина"],
        "wrong_en": ["A gold coin", "A silver spoon", "A diamond ring", "A crystal ball", "A silk ribbon", "A peacock feather"]
    },
    {
        "title_ru": "99. Двенадцать танцующих принцесс", "title_en": "99. The Twelve Dancing Princesses",
        "text_ru": "Перед вами спальня с двенадцатью кроватями.\nКостя: «Бро, их башмаки всегда изношены.»\n\nСтаршая принцесса спрашивает:\n«Почему наши башмаки каждое утро были истёрты до дыр?»",
        "text_en": "A bedroom with twelve beds stands before you.\nKostya: 'Bro, their shoes are always worn out.'\n\nThe eldest princess asks:\n'Why were our shoes worn to holes every morning?'",
        "correct_ru": "Мы танцевали в подземном замке", "correct_en": "We danced in an underground castle",
        "wrong_ru": ["Мы работали в поле", "Мы бегали от волков", "Мы искали клады", "Мы строили дома", "Мы стирали бельё", "Мы готовили еду"],
        "wrong_en": ["We worked in the fields", "We ran from wolves", "We searched for treasure", "We built houses", "We washed laundry", "We cooked food"]
    },
    {
        "title_ru": "100. Хранитель Сказок (Финал)", "title_en": "100. Keeper of Tales (The Finale)",
        "text_ru": "Перед тобой сияет восстановленный Кристалл. Костя улыбается.\nКостя: «Бро, мы сделали это. Все 100 сказок спасены.»\n\nКристалл спрашивает:\n«Что на самом деле спасло мир сказок?»",
        "text_en": "The restored Crystal shines before you. Kostya smiles.\nKostya: 'Bro, we did it. All 100 tales are saved.'\n\nThe Crystal asks:\n'What actually saved the world of tales?'",
        "correct_ru": "Память и любовь к историям", "correct_en": "Memory and love for stories",
        "wrong_ru": ["Золото и богатство", "Магия и чары", "Мечи и доспехи", "Короны и троны", "Заклинания и книги", "Кристаллы и камни"],
        "wrong_en": ["Gold and wealth", "Magic and spells", "Swords and armor", "Crowns and thrones", "Spells and books", "Crystals and stones"]
    }
]

# ================= НЕПРАВИЛЬНЫЕ ОТВЕТЫ (Вопросы 1-40) =================
legendary_wrong_answers_ru = {
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
    "Василисой Премудрой": ["Царевной", "Королевой", "Ведьмой", "Лебедью", "Птицей", "Феей"],
    "Мышка": ["Дед", "Бабка", "Жучка", "Внучка", "Кошка", "Лошадь"],
    "Простое яичко": ["Серебряное", "Бриллиантовое", "Платиновое", "Деревянное", "Каменное", "Хрустальное"],
    "Я его раздавил": ["Они его сожгли", "Они его утопили", "Они его разобрали", "Они его продали", "Они его спрятали", "Они его закопали"],
    "Машу": ["Дедушку", "Бабушку", "Медвежонка", "Зайца", "Лису", "Волка"],
    "Сестрица Алёнушка": ["Братец Иванушка", "Матушка", "Батюшка", "Бабушка", "Дедушка", "Тётушка"],
    "Кот и пёс": ["Только кот", "Только пёс", "Медведь", "Лиса", "Волк", "Заяц"],
    "По голосу и лапе": ["По запаху", "По цвету шерсти", "По размеру", "По глазам", "По ушам", "По хвосту"],
    "Волк, заяц, лиса": ["Только волк", "Только лиса", "Медведь и волк", "Заяц и лиса", "Кот и пёс", "Дед и бабка"],
    "Каша была в плоской тарелке": ["Каша была в кувшине", "Каша была в миске", "Каша была в кастрюле", "Каша была в сковороде", "Каша была в ведре", "Каша была в бочке"],
    "Корешки (корни)": ["Вершки (листья)", "Стебли", "Цветы", "Плоды", "Семена", "Кору"],
    "В козлёнка": ["В медвежонка", "В волчонка", "В зайчонка", "В лисёнка", "В поросёнка", "В телёнка"],
    "По щучьему веленью, по моему хотенью": ["По моему слову", "По моему желанию", "По щучьему слову", "По велению царя", "По воле бога", "По моему приказу"],
    "В сокола": ["В орла", "В ястреба", "В ворона", "В лебедя", "В гуся", "В утку"],
    "Медведь, волк и кот": ["Только кот", "Только медведь", "Заяц и лиса", "Дед и бабка", "Поп и Балда", "Царь и царевна"],
    "Из топора (а баба добавляет крупу)": ["Из камня", "Из дерева", "Из железа", "Из глины", "Из песка", "Из воды"],
    "Сказала, что рыба сама ловится": ["Сказала, что это для царя", "Сказала, что это для обеда", "Сказала, что это для детей", "Сказала, что это для праздника", "Сказала, что это для гостей", "Сказала, что это для продажи"],
    "Три щелчка по лбу": ["Три мешка золота", "Три бочки мёда", "Три коня", "Три дома", "Три коровы", "Три овцы"],
    "Ничего и всё (загадку)": ["Золото", "Серебро", "Хлеб", "Воду", "Землю", "Камень"],
    "Вершки (колосья)": ["Корешки (корни)", "Стебли", "Листья", "Цветы", "Семена", "Солому"],
    "Сестрица и волшебная яблоня": ["Только сестрица", "Только яблоня", "Мачеха", "Царь", "Медведь", "Волк"],
    "В ступе": ["На метле", "На ковре-самолёте", "На коне", "На лодке", "На санях", "На телеге"],
    "На конце иглы, в яйце": ["В сундуке", "Под дубом", "В море", "В огне", "В земле", "На дереве"],
    "Волшебную куклу": ["Волшебный клубок", "Волшебное зеркало", "Волшебную палочку", "Волшебное кольцо", "Волшебный меч", "Волшебный щит"],
    "Прыжки дурака в мешке": ["Песни петуха", "Танцы медведя", "Шутки царя", "Сказки бабушки", "Игры детей", "Стихи поэта"],
    "Посадил в мешок и повёз в Киев": ["Отрубил голову", "Сжёг в огне", "Утопил в море", "Заморозил во льду", "Запер в башне", "Превратил в камень"]
}

legendary_wrong_answers_en = {
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
    "Vasilisa the Wise": ["A princess", "A queen", "A witch", "A swan", "A bird", "A fairy"],
    "The mouse": ["The old man", "The old woman", "The dog", "The granddaughter", "The cat", "The horse"],
    "A simple egg": ["A silver egg", "A diamond egg", "A platinum egg", "A wooden egg", "A stone egg", "A crystal egg"],
    "I crushed it": ["They burned it", "They drowned it", "They dismantled it", "They sold it", "They hid it", "They buried it"],
    "Masha": ["The grandfather", "The grandmother", "The bear cub", "The hare", "The fox", "The wolf"],
    "Sister Alenushka": ["Brother Ivanushka", "The mother", "The father", "The grandmother", "The grandfather", "The aunt"],
    "The cat and the dog": ["Only the cat", "Only the dog", "The bear", "The fox", "The wolf", "The hare"],
    "By voice and paw": ["By smell", "By fur color", "By size", "By eyes", "By ears", "By tail"],
    "Wolf, hare, fox": ["Only the wolf", "Only the fox", "Bear and wolf", "Hare and fox", "Cat and dog", "Old man and old woman"],
    "The porridge was in a flat plate": ["The porridge was in a jug", "The porridge was in a bowl", "The porridge was in a pot", "The porridge was in a pan", "The porridge was in a bucket", "The porridge was in a barrel"],
    "The roots": ["The tops (leaves)", "The stems", "The flowers", "The fruits", "The seeds", "The bark"],
    "Into a kid": ["Into a bear cub", "Into a wolf cub", "Into a hare cub", "Into a fox cub", "Into a piglet", "Into a calf"],
    "At the pike's command, at my desire": ["At my word", "At my wish", "At the pike's word", "At the tsar's command", "At God's will", "At my order"],
    "Into a falcon": ["Into an eagle", "Into a hawk", "Into a raven", "Into a swan", "Into a goose", "Into a duck"],
    "Bear, wolf, and cat": ["Only the cat", "Only the bear", "Hare and fox", "Old man and old woman", "Priest and Balda", "Tsar and tsarina"],
    "From an axe (and the woman adds grain)": ["From stone", "From wood", "From iron", "From clay", "From sand", "From water"],
    "Said the fish catches itself": ["Said it's for the tsar", "Said it's for dinner", "Said it's for the children", "Said it's for the holiday", "Said it's for the guests", "Said it's for sale"],
    "Three flicks on the forehead": ["Three bags of gold", "Three barrels of honey", "Three horses", "Three houses", "Three cows", "Three sheep"],
    "Nothing and everything (a riddle)": ["Gold", "Silver", "Bread", "Water", "Land", "Stone"],
    "The tops (the ears of grain)": ["The roots", "The stems", "The leaves", "The flowers", "The seeds", "The straw"],
    "Sister and the magic apple tree": ["Only the sister", "Only the apple tree", "The stepmother", "The tsar", "The bear", "The wolf"],
    "In a mortar": ["On a broom", "On a magic carpet", "On a horse", "On a boat", "On a sleigh", "On a cart"],
    "On the tip of a needle, in an egg": ["In a chest", "Under the oak", "In the sea", "In fire", "In the ground", "On a tree"],
    "A magic doll": ["A magic ball of yarn", "A magic mirror", "A magic wand", "A magic ring", "A magic sword", "A magic shield"],
    "A fool jumping in a sack": ["Rooster songs", "Bear dances", "Tsar jokes", "Grandmother tales", "Children games", "Poet verses"],
    "Put him in a sack and took him to Kiev": ["Cut off his head", "Burned him in fire", "Drowned him in the sea", "Froze him in ice", "Locked him in a tower", "Turned him to stone"]
}