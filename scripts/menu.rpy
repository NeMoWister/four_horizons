init:
    image FH_menu_bg = "mods/four_horizons/images/bg/ext_boathouse_alt_night_7dl.jpg"
    $ mods["FH_start"]="{font=[FH_Maki_Sans]}{color=0F1766}Четыре Горизонта{/color}{/font}"
    $ config.developer = True
    $ FH_discplaimer_text = '{font=[FH_Maki_Sans]}{color=#ff0000}{size=60}Дисклеймер{/color}{/size}\n\n{size=40}Перед началом игры, пожалуйста, ознакомьтесь с данной информацией.\n\nЭта игра предназначена только для развлекательных целей и не имеет никакой связи с реальностью.\nВсе персонажи, события и диалоги являются вымышленными и не являются настоящими.{/size}{/font}'

    python:
        # Превью для табличного списка модов 
        try:
            modsImages["FH_start"] = ("mods/four_horizons/images/misc/preview.png", False)
        except:
            pass

init python:
    
    style.fhs = Style(style.default)
    style.fhs.size = 60
    style.fhs.color = "#89a8b8"
    style.fhs.hover_color = "#9b870c"
    style.fhs.font = "mods/four_horizons/fonts/VinSlabPro-LightItalic.ttf"
    
    class FH_CutM(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = []
            self.rd = "mods/four_horizons/images/misc/firedrop.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    
transform fh_menu:
    alpha 0 xalign -0.5
    ease 2.5 alpha 1.0 xalign 0.05
    
transform fh_title:
    alpha 0 xalign 1.5
    ease 2.5 alpha 1.0 xalign 0.95

transform fh_button:
    on idle:
        ease .75 zoom 1 alpha .8
    on hover:
        ease .75 zoom 1.2 alpha 1.0
    
screen FH_menu_main():
    tag test
    modal True
    add "FH_menu_bg"
    add (FH_CutM().sm)
    vbox at fh_title:
        area (0.6, 0.0, 0.4, 0.2)
        text "Четыре":
            font FH_Montserrat
            size 80
            color "92c6e5"
            xalign 0.0
        text "Горизонта":
            font FH_Montserrat
            size 80
            color "92c6e5"
            xalign 1.0
    vbox at fh_menu:
        spacing 30
        xalign 0.1
        yalign .5
        textbutton "Начать" at fh_button:
            style "fhs"
            text_style "fhs"
            action Jump('FH_chapter_select')
        textbutton "Загрузить" at fh_button:
            style "fhs"
            text_style "fhs"
            action ShowMenu("load", dissolve)
        textbutton "Галерея" at fh_button:
            style "fhs"
            text_style "fhs"
            action Jump("FH_gallery_start")
        textbutton "Новости" at fh_button:
            style "fhs"
            text_style "fhs"
            action OpenURL("https://vk.com/vitotheknyazzpublic")
        if persistent.FH_ending["dv"] and persistent.FH_ending["sl"] and persistent.FH_ending["un"] and persistent.FH_ending["us"]:
            textbutton "Послесловие" at fh_button:
                style "fhs"
                text_style "fhs"
                action OpenURL("https://vk.com/@vitotheknyazzpublic-vselennaya-chetyre-gorizonta-vnutri-igrovogo-soobschestva-be")
        textbutton "Выход" at fh_button:
            style "fhs"
            text_style "fhs"
            action [Hide("FH_menu_main", dissolve), Return()]

screen FH_chapter_selector():
    tag test
    modal True
    hbox:
        imagebutton auto "mods/four_horizons/images/misc/menu/us_%s.jpg" action [Hide('FH_menu_main', dissolve), Hide('FH_chapter_selector', dissolve), Return("us")]
        imagebutton auto "mods/four_horizons/images/misc/menu/dv_%s.jpg" action [Hide('FH_menu_main', dissolve), Hide('FH_chapter_selector', dissolve), Return("dv")]
        imagebutton auto "mods/four_horizons/images/misc/menu/sl_%s.jpg" action [Hide('FH_menu_main', dissolve), Hide('FH_chapter_selector', dissolve), Return("sl")]
        imagebutton auto "mods/four_horizons/images/misc/menu/un_%s.jpg" action [Hide('FH_menu_main', dissolve), Hide('FH_chapter_selector', dissolve), Return("un")]
    imagebutton auto get_image("gui/dialogue_box/prologue/backward_%s.png") xalign 0.01 yalign 0.97 action (Hide("FH_chapter_selector"), Hide("FH_menu_main"), Return("menu"))
    
label FH_chapter_select:
    scene expression "mods/four_horizons/images/misc/menu/idle.jpg" with dissolve
    call screen FH_chapter_selector with dissolve
    if _return == "menu":
        scene FH_menu_bg with dissolve
        call screen FH_menu_main with dissolve
    stop music fadeout 3
    if _return == "us":
        show expression "mods/four_horizons/images/misc/menu/us_hover.jpg":
            xpos 0
        pause 2
        call FH_discplaimer
        jump Four_horizons_Maxim_story_prologue
    elif _return == "dv":
        show expression "mods/four_horizons/images/misc/menu/dv_hover.jpg":
            xpos 481
        pause 2
        call FH_discplaimer
        jump four_horizons_dv
    elif _return == "sl":
        show expression "mods/four_horizons/images/misc/menu/sl_hover.jpg":
            xpos 961
        pause 2
        call FH_discplaimer
        jump Four_horizons_Kirril_story_prologue
    elif _return == "un":
        show expression "mods/four_horizons/images/misc/menu/un_hover.jpg":
            xpos 1441
        pause 2
        call FH_discplaimer
        jump four_horizons_un
    scene bg black with dissolve2
    return

label FH_gallery_start:
    $ persistent.sprite_time = "night"
    scene expression "mods/four_horizons/images/bg/ext_un_hideout_night_7dl.jpg" with dissolve
    $ FH_mode = "bg"
    $ FH_cg_char = "none"
    $ FH_gal_list = "none"
    call screen FH_gallery with dissolve
    if _return == "menu":
        if not renpy.music.get_playing() == "mods/four_horizons/music/Z FEEL-Z-Hear The Wind-kissvk.com.mp3":
            play music "mods/four_horizons/music/Z FEEL-Z-Hear The Wind-kissvk.com.mp3" fadeout 1 fadein 3
        scene FH_menu_bg with dissolve
        call screen FH_menu_main with dissolve
    stop music fadeout 3
    scene bg black with dissolve2
    return

style FH_gallery_style:
    font FH_Montserrat
    size 50
    color "#B956FF"
    idle_color "#FFF"
    hover_color "#B956FF"
    outlines [(3, '#000', 0, 0)]
    
style FH_mroom:
    font FH_Zekton
    size 50
    idle_color "#FFF"
    hover_color "#B956FF"
    selected_color "#B956FF"
    insensitive_color "#888"
    
init python:
    FH_music_list = [
        ("83Crutch – OST Глухарь. Возвращение", "mods/four_horizons/music/83Crutch_-_GLUHAR_3_Vozvracshenie_Cover_(Zvyki.com).mp3"),
        ("[[AMATORY] – Дыши со мной", "mods/four_horizons/music/-AMATORY--Дыши со мной-kissvk.com.mp3"),
        ("[[AMATORY] – Слишком поздно", "mods/four_horizons/music/amatory-slishkom-pozdno-underbiz_mix_(Krolik.biz).mp3"),
        ("[[AMATORY] – Теряешь меня", "mods/four_horizons/music/[AMATORY] — Теряешь меня.mp3"),
        ("Bobstor – Heart-eater Strikes Again (OST Love, Money, RocknRoll)", "mods/four_horizons/music/Bobstor (Love, Money, RocknRoll OST) — Heart-eater Strikes Again (www.lightaudio.ru).mp3"),
        ("Bobstor – Ultraviolet Stream (OST Love, Money, RocknRoll)", "mods/four_horizons/music/Bobstor (Love, Money, RocknRoll OST) — Ultraviolet Stream (www.lightaudio.ru).mp3"),
        ("BrainStorm - Ветер", "mods/four_horizons/music/Brainstorm - Ветер.mp3"),
        ("Disturbed – Sound Of Silence", "mods/four_horizons/music/Disturbed_Sound_Of_Silence_MINUS_www.lightaudio.ru.mp3"),
        ("Klavier Gavin – Love Love Guilty (OST Ace Attorney - Apollo Justice)", "mods/four_horizons/music/Apollo Justice_ Ace Attorney OST — Klavier Gavin ~ Love Love Guilty (www.lightaudio.ru).mp3"),
        ("LUMEN - Не надо снов", "mods/four_horizons/music/Lumen - Не надо снов.mp3"),
        ("Nautilus Pompilius - Утро Полины", "mods/four_horizons/music/Nautilus Pompilius - Утро Полины.mp3"),
        ("Nautilus Pompilius - Черные птицы", "mods/four_horizons/music/Nautilus Pompilius - Черные птицы.mp3"),
        ("NemesisTheory – Rose At Twilight", "mods/four_horizons/music/NemesisTheory — Rose At Twilight (ID_ 193466) (www.lightaudio.ru).mp3"),
        ("OST Ace Attorney - Cross Examination Allegro", "mods/four_horizons/music/OST Ace Attorney - Cross Examination Allegro.mp3"),
        ("OST Ace Attorney - Pursuit_Cornered", "mods/four_horizons/music/OST Ace_Attorney - Pursuit_Cornered.mp3"),
        ("OST God Eater 2 Rage Burst – God and Man Resolution", "mods/four_horizons/music/God Eater 2 Rage Burst OST - God and Man Resolution (www.hotplayer.ru).mp3"),
        ("OST PAYDAY 2 – Fuse Box", "mods/four_horizons/music/PayDay 2 - Fuse Box OST.mp3"),
        ("OST Puss in boots - Dance Cat", "mods/four_horizons/music/OST Puss in boots - Танец кота.mp3"),
        ("OST Rice Driver GRID – Battle", "mods/four_horizons/music/Race Driver_ Grid OST - Battle.mp3"),
        ("OST Sickness – Main", "mods/four_horizons/music/prolog.mp3"),
        ("OST Space Rangers HD: A War Apart – Depth (Тема Анархистов)", "mods/four_horizons/music/Space Rangers HD Full OST — Depth (www.lightaudio.ru).mp3"),
        ("OST Space Rangers HD: A War Apart – Квестовая", "mods/four_horizons/music/OST_Space Rangers.mp3"),
        ("OST Интерны - Latino", "mods/four_horizons/music/OST Интерны - Latino.mp3"),
        ("Papa Roach - Take Me", "mods/four_horizons/music/Papa Roach-Take Me-kissvk.com.mp3"),
        ("PW3 – The Fragrance of Dark Coffee (Guitar Cover)", "mods/four_horizons/music/PW3-Godot.mp3"),
        ("Rammstein - Amour", "mods/four_horizons/music/LeRoxey-Rammstein - Amour -На русском--kissvk.com.mp3"),
        ("RedMountain – Fractal Alley (OST Love, Money, RocknRoll)", "mods/four_horizons/music/RedMountain (Love, Money, RocknRoll OST) — Fractal Alley (www.lightaudio.ru).mp3"),
        ("ROCK PRIVET - Этот Город (Cover на Браво/Nickelback)", "mods/four_horizons/music/ROCK PRIVET-Этот Город 2021 -Cover на Браво - Nickelback--kissvk.com.mp3"),
        ("Static-X - New Pain", "mods/four_horizons/music/Static-X — New Pain (Instrumental Cover) (www.lightaudio.ru).mp3"),
        ("STIGMATA - Дыши со мной", "mods/four_horizons/music/Stigmata - Сентябрь.mp3"),
        ("Three Days Grace - I Hate Everything About You", "mods/four_horizons/music/Three Days Grace - I Hate Everything About You.mp3"),
        ("Three Days Grace – Never Too Late", "mods/four_horizons/music/Three_Days_Grace_-_Never_Too_Late_Instrumental_audiohunter.ru.mp3"),
        ("Yan Shpitalnik - Secret (OST Четыре Горизонта)", "mods/four_horizons/music/Yan Shpitalnik - Secret (OST Четыре Горизонта).mp3"),
        ("Yan Shpitalnik - Two (OST Четыре Горизонта)", "mods/four_horizons/music/Yan Shpitalnik - Two.mp3"),
        ("Z FEEL-Z – Hear The Wind (OST Love, Money, RocknRoll)", "mods/four_horizons/music/Z FEEL-Z-Hear The Wind-kissvk.com.mp3"),
        ("АнимациЯ  – Родина", "mods/four_horizons/music/АнимациЯ - Родина.mp3"),
        ("БИ-2 - Счастье", "mods/four_horizons/music/БИ-2 - Счастье.mp3"),
        ("Город 312 – Останусь", "mods/four_horizons/music/Город 312-Останусь-kissvk.com.mp3"),
        ("Григорий Лепс – Зачем тебе Я?", "mods/four_horizons/music/лепс — Зачем тебе Я (минуc).mp3"),
        ("Инкогнито - Бесконечность", "mods/four_horizons/music/Инкогнито-Бесконечность-kissvk.com.mp3"),
        ("Кино - Восьмиклассница", "mods/four_horizons/music/Кино - Восьмиклассница.mp3"),
        ("Кино - Группа крови", "mods/four_horizons/music/Кино - Группа крови.mp3"),
        ("Кино - Звезда по имени Солнце", "mods/four_horizons/music/Кино - Звезда по имени Солнце.mp3"),
        ("Кино - Малыш (Vocal-Remix)", "mods/four_horizons/music/Кино - Малыш (голос).mp3"),
        ("Кино - Малыш", "mods/four_horizons/music/Кино - Малыш.mp3"),
        ("Кино - Пачка Сигарет", "mods/four_horizons/music/Кино - Пачка Сигарет.mp3"),
        ("Кино - Спокойная ночь", "mods/four_horizons/music/Кино - Спокойная ночь.mp3"),
        ("КолиZей - Имя твоё", "mods/four_horizons/music/КолиZей - Имя твоё.mp3"),
        ("Король и Шут - Девушка и Граф", "mods/four_horizons/music/Король и Шут - Девушка и Граф.mp3"),
        ("Король и Шут - Лесник", "mods/four_horizons/music/Король и Шут - Лесник.mp3"),
        ("ЛЮБЭ  – Давай за жизнь", "mods/four_horizons/music/Любэ - Давай за...mp3"),
        ("Потомучто - Жизнь и Смерть", "mods/four_horizons/music/Потомучто - Жизнь и Смерть.mp3"),
        ("Сектор Газа - Бомж", "mods/four_horizons/music/Сектор Газа - Бомж.mp3"),
        ("Сектор Газа - Лирика", "mods/four_horizons/music/Сектор Газа - Лирика.mp3"),
        ("СЛОТ - Круги на воде", "mods/four_horizons/music/СЛОТ - Круги на воде.mp3"),
        ("СЛОТ - Мертвые Звезды", "mods/four_horizons/music/Слот - Мертвые Звезды.mp3"),
        ("СПЛИН  – Мы сидели и курили", "mods/four_horizons/music/Сплин - Мы сидели и курили.mp3"),
        ("ТАНЦЫ МИНУС - Половинка", "mods/four_horizons/music/Танцы минус - Половинка.mp3"),
        ]

    FH_mr = MusicRoom(fadeout=1.0)
    
    for name, filename in FH_music_list:
        FH_mr.add(filename)

    FH_gallery_list_bg = [
        "FH_alex_room_night",
        "FH_class",
        "FH_countryhouse",
        "FH_ext_aidpost_sunset",
        "FH_ext_boathouse_sunset",
        "FH_ext_bus_busstop_summer",
        "FH_ext_cafe",
        "FH_ext_clubs_sunset",
        "FH_ext_forest_sunset",
        "FH_ext_house_of_dv_sunset",
        "FH_ext_house_of_sl_night",
        "FH_ext_house_of_sl_sunset",
        "FH_ext_house_of_un_night_7dl",
        "FH_ext_house_of_un_night_light",
        "FH_ext_houses_night_moonlight",
        "FH_ext_in_debar",
        "FH_ext_island_night_uv",
        "FH_ext_island_sunset",
        "FH_ext_kirill_house_day",
        "FH_ext_kirill_house_night",
        "FH_ext_kirill_house_sunset",
        "FH_ext_library_sunset",
        "FH_ext_musclub_night_7dl",
        "FH_ext_musclub_verandah_sunset",
        "FH_ext_playground_sunset",
        "FH_ext_stadion",
        "FH_ext_stage_big_day",
        "FH_ext_street_night",
        "FH_ext_un_house_sunset",
        "FH_ext_warehouse_day_7dl",
        "FH_ext_warehouse_sunset_7dl",
        "FH_int_aidpost_sunset",
        "FH_int_cafe",
        "FH_int_class_day",
        "FH_int_cloakroom",
        "FH_int_clubs_male_night_7dl",
        "FH_int_countryhouse_day",
        "FH_int_depot",
        "FH_int_depot_sunset",
        "FH_int_dining_hall_people_sunset",
        "FH_int_house_of_dv_night_no_light_7dl",
        "FH_int_house_of_sl_light_night",
        "FH_int_house_of_sl_night",
        "FH_int_house_of_un_rain",
        "FH_int_house_of_un_sunset",
        "FH_int_kh_room",
        "FH_int_kirill_house_day",
        "FH_int_kirill_house_night",
        "FH_int_kirill_house_night_light",
        "FH_int_kirill_house_sunset",
        "FH_int_kitchen_7dl",
        "FH_int_liaz_city",
        "FH_int_mt_sam_room_7dl",
        "FH_int_mt_sam_room_night_7dl",
        "FH_int_musclub_mattresses_day",
        "FH_int_musclub_mattresses_night",
        "FH_int_musclub_mattresses_sunset",
        "FH_int_old_car_forest",
        "FH_int_semen_room_clean",
        "FH_int_semen_room_night",
        "FH_park",
        "FH_underwater",
    ]
    
    FH_gallery_list_dv = [
        "d2_mirror",
        ["d2_miku_piano2", "d2_miku_piano"],
        "FH_un_dv_punch",
        ["d6_dv_fight", "d6_dv_fight_2"],
        "FH_Lena_i_Alisa",
        "FH_lineup",
        "FH_din_dv_un",
        "FH_dv_alex_guitar",
        ["FH_dv_guitar", "FH_sem_guitar"],
        "d4_mi_guitar",
        "FH_un_dv_boat_day",
        "FH_island_night_un_dv",
        "FH_un_dv_boat_night",
        "FH_dv_alex",
        ["FH_alisa1", "FH_alisa2", "FH_alisa3"],
        ["FH_alicemusic1", "FH_alicemusic2"],
        ["FH_rocklove1", "FH_rocklove2", "FH_rocklove3"],
        "epilogue_uv_dv",
        ["FH_finalalice1", "FH_finalalice2"],
        "FH_d7_dv_epilogue_kiss"
    ]
    
    FH_gallery_list_sl = [
        "d3_sl_library",
        ["d1_sl_dinner", "d1_sl_dinner_0"],
        "FH_Kirill_reflection",
        "FH_lineup",
        "d4_catac_sl",
        "d4_sh_sit",
        "d5_boat",
        "d6_sl_forest_2",
        "FH_Slavya_and_Kirill_at_the_table",
        "FH_evil_Kirill_and_Slavya",
        "d3_sl_dance",
        "d3_sl_evening",
        "FH_Kirill_and_Slavya_kiss",
        "FH_Kirill_and_Slavya_outside_camp",
        ["FH_Slavya_and_Kirill_hug_open_eyes", "FH_Slavya_and_Kirill_hug_close_eyes"],
    ]
    
    FH_gallery_list_un = [
        "FH_un_hugs",
        ["alb1", "persistent.FH_un_album1", "pic1", "pic2", "pic3"],
        "FH_lineup",
        "d4_mi_sing",
        "FH_boh_un",
        "FH_dance_night",
        "epilogue_uv_un",
        ["bg ext_boathouse_day", "persistent.FH_un_d3_kiss", "cg FH_kiss_un_2", "cg FH_kiss_un_1"],
        "FH_un_vi_boa",
        "FH_bo_un",
        "FH_lena_night",
        ["bg int_house_of_un_day", "persistent.FH_un_d4_kiss", "cg FH_kiss_un_2", "cg FH_kiss_un_1"],
        "d3_un_dance",
        "FH_un_hug",
        ["FH_sun_un", "FH_un_winter1", "FH_un_winter2"],
        "FH_Obnimashki2",
        ["bg FH_int_house_of_un_rain", "persistent.FH_un_d5_kiss", "cg FH_kiss_un_2", "cg FH_kiss_un_1"],
        ["alb2", "persistent.FH_un_album2", "d5pic1", "d5pic2", "d5pic3", "d5pic4", "vi_sis"],
        "FH_un_under",
        "FH_sl_sleep",
        "d5_boat",
        "FH_guitar_un",
        "d6_un_evening_1",
        "FH_un_sqr",
        ["FH_lena1", "FH_lena2", "FH_lena3"],
        ["FH_ho_c", "FH_ho_o"],
        "FH_wed_un",
        "FH_un_winter3",
        "FH_un_ep"
    ]
    
    FH_gallery_list_us = [
        "d1_grasshopper",
        "FH_Kirill_reflection",
        "FH_lineup",
        ["FH_Maxim_and_Ulyana_peel_potatoes", "FH_Maxim_and_Ulyana_intensively_peel_potatoes"],
        "FH_Ulyana_and_Maxim_with_book",
        "FH_us_soccer_sunset",
        "d6_un_evening_1",
        "epilogue_uv_us",
        "d4_mi_guitar",
        "FH_max_ulya",
        "FH_Maxim_and_Ulyana_boat",
        "FH_d6_ostrov",
        "d6_us_film",
        "d5_us_sit",
        "FH_Maxim_and_Ulyana_hug_catacombs",
        "d4_catac_us_2",
        "d5_us_kiss",
        "d7_pioneers_leaving",
        "FH_Maxim_and_Ulyana_at_bus_stop"
    ]
    
    FH_g = Gallery()
    FH_g.transition = fade
    FH_g.locked_button = get_image("gui/gallery/not_opened_idle.png")
    FH_g.unlocked_button = get_image("gui/gallery/blank.png")
    
    for item in FH_gallery_list_dv:
        if type(item) is list:
            FH_g.button(item[0])
            for img in item:
                FH_g.unlock_image("cg " + img)
        else:
            FH_g.button(item)
            FH_g.unlock_image("cg " + item)
        
    for item in FH_gallery_list_sl:
        if type(item) is list:
            FH_g.button(item[0])
            for img in item:
                FH_g.unlock_image("cg " + img)
        else:
            FH_g.button(item)
            FH_g.unlock_image("cg " + item)
        
    for item in FH_gallery_list_un:
        if type(item) is list:
            if item[0].startswith("bg"):
                FH_g.button(item[0])
                FH_g.condition(item[1])
                FH_g.image(item[0],item[2])
                FH_g.image(item[0],item[3])
            elif item[0].startswith("alb"):
                if item[2] == "pic1":
                    FH_g.button(item[2])
                    FH_g.condition(item[1])
                    FH_g.image("stars", "cg FH_" + item[2])
                    FH_g.transform(None, truecenter)
                    FH_g.image("stars", "cg FH_" + item[3])
                    FH_g.transform(None, truecenter)
                    FH_g.image("stars", "cg FH_" + item[4])
                    FH_g.transform(None, truecenter)
                if item[2] == "d5pic1":
                    FH_g.button(item[2])
                    FH_g.condition(item[1])
                    FH_g.image("stars", "cg FH_" + item[2])
                    FH_g.transform(None, truecenter)
                    FH_g.image("stars", "cg FH_" + item[3])
                    FH_g.transform(None, truecenter)
                    FH_g.image("stars", "cg FH_" + item[4])
                    FH_g.transform(None, truecenter)
                    FH_g.image("stars", "cg FH_" + item[5])
                    FH_g.transform(None, truecenter)
                    FH_g.image("stars", "cg FH_" + item[6])
                    FH_g.transform(None, truecenter)
            else:
                FH_g.button(item[0])
                for img in item:
                    FH_g.unlock_image("cg " + img)
        else:
            FH_g.button(item)
            FH_g.unlock_image("cg " + item)
        
    for item in FH_gallery_list_us:
        if type(item) is list:
            FH_g.button(item[0])
            for img in item:
                FH_g.unlock_image("cg " + img)
        else:
            FH_g.button(item)
            FH_g.unlock_image("cg " + item)
        
    for item in FH_gallery_list_bg:
        FH_g.button(item)
        FH_g.unlock_image("bg " + item)
        
    def FH_gall_list(girl):
        if girl == "dv":
            return FH_gallery_list_dv
        if girl == "sl":
            return FH_gallery_list_sl
        if girl == "un":
            return FH_gallery_list_un
        if girl == "us":
            return FH_gallery_list_us

screen FH_gallery:
    add "mods/four_horizons/images/bg/ext_un_hideout_night_7dl.jpg"
    if FH_mode == "bg":
        $ len_table = len(FH_gallery_list_bg)
        text "Фоны":
            style "FH_gallery_style"
            xalign 0.5 yalign 0.05
        textbutton "Музыка":
            style "FH_gallery_style" text_style "FH_gallery_style"
            xalign 0.05 yalign 0.05
            action (SetVariable("FH_mode", "music"), Show("FH_gallery", dissolve) )
        textbutton "Иллюстрации":
            style "FH_gallery_style" text_style "FH_gallery_style"
            xalign 0.95 yalign 0.05
            action (SetVariable("FH_mode", "cg"), SetVariable("FH_cg_char", "none"), Show("FH_gallery", dissolve) )
        $ cells = 12
        grid 4 3:
            xalign 0.5 ypos 0.2
            
            $ cg_displayed = 0
            $ next_page = page + 1
            if next_page > int(len_table/cells):
                $ next_page = 0
            $ FH_gal_list = FH_gallery_list_bg
            for n in range(0, len_table):
                if n < (page+1)*cells and n>=page*cells:
                    python:
                        if renpy.loadable("mods/four_horizons/images/bg/" + FH_gal_list[n][3:] + ".jpg"):
                            imgp = "mods/four_horizons/images/bg/" + FH_gal_list[n][3:] + ".jpg"
                        else:
                            imgp = "mods/four_horizons/images/bg/" + FH_gal_list[n][3:] + ".png"
                        _t = im.Crop(imgp, (0,0,1920,1080))
                        th = im.Scale(_t, 320, 180)
                        img = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image(get_image("gui/gallery/thumbnail_idle.png")))
                        imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image(get_image("gui/gallery/thumbnail_hover.png")))
                    add FH_g.make_button(FH_gal_list[n], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                    $ cg_displayed += 1
                    
                    if n+1 == len_table:
                        $ next_page = 0

            for j in range(0, 12-cg_displayed):
                null

        grid 3 1:
            xalign 0.48 ypos 0.85
            if page != 0:
                imagebutton auto get_image("gui/dialogue_box/prologue/backward_%s.png") action (SetVariable('page', page-1), Show("FH_gallery", dissolve))
            else:
                null width 116
            python:
                def abc(n,k):
                    l = float(n)/float(k)
                    if l-int(l) > 0:
                        return int(l)+1
                    else:
                        return l
                pages = str(page+1)+"/"+str(int(abc(len_table,cells)))
            text pages style "FH_gallery_style" color "FFF" yalign 0.5 xalign 0.5
            if next_page == 0:
                null width 116
            else:
                imagebutton auto get_image("gui/dialogue_box/prologue/forward_%s.png") action (SetVariable('page', next_page), Show("FH_gallery", dissolve))

    if FH_mode == "cg":
        if FH_cg_char == "dv":
            $ len_table = len(FH_gal_list)
            add "dv smile FH_dress":
                xpos -0.05
        if FH_cg_char == "sl":
            $ len_table = len(FH_gal_list)
            add "sl happy dress":
                xpos -0.05
        if FH_cg_char == "un":
            $ len_table = len(FH_gal_list)
            add "un grin dress":
                xpos -0.05
        if FH_cg_char == "us":
            $ len_table = len(FH_gal_list)
            add "us laugh2 dress":
                xpos -0.05
        text "Иллюстрации":
            style "FH_gallery_style"
            xalign 0.5 yalign 0.05
        textbutton "Фоны":
            style "FH_gallery_style" text_style "FH_gallery_style"
            xalign 0.05 yalign 0.05
            action (SetVariable("FH_mode", "bg"), SetVariable("page", 0), Show("FH_gallery", dissolve) )
        textbutton "Музыка":
            style "FH_gallery_style" text_style "FH_gallery_style"
            xalign 0.95 yalign 0.05
            action (SetVariable("FH_mode", "music"), Show("FH_gallery", dissolve) )
        hbox:
            xalign 0.5 yalign 0.12
            textbutton "Сангвиник":
                style "FH_gallery_style" text_style "FH_gallery_style"
                text_hover_color "#00F0C8" text_selected_color "#00F0C8"
                action (SelectedIf(SetVariable("FH_cg_char", "us")), SetVariable("FH_gal_list", FH_gall_list("us")), SetVariable("page", 0), Show("FH_gallery", dissolve))
            null width 50
            textbutton "Холерик":
                style "FH_gallery_style" text_style "FH_gallery_style"
                text_hover_color "#919191" text_selected_color "#919191"
                action (SelectedIf(SetVariable("FH_cg_char", "dv")), SetVariable("FH_gal_list", FH_gall_list("dv")), SetVariable("page", 0), Show("FH_gallery", dissolve))
            null width 50
            textbutton "Флегматик":
                style "FH_gallery_style" text_style "FH_gallery_style"
                text_hover_color "#8093FE" text_selected_color "#8093FE"
                action (SelectedIf(SetVariable("FH_cg_char", "sl")), SetVariable("FH_gal_list", FH_gall_list("sl")), SetVariable("page", 0), Show("FH_gallery", dissolve))
            null width 50
            textbutton "Меланхолик":
                style "FH_gallery_style" text_style "FH_gallery_style"
                text_hover_color "#1E7628" text_selected_color "#1E7628"
                action (SelectedIf(SetVariable("FH_cg_char", "un")), SetVariable("FH_gal_list", FH_gall_list("un")), SetVariable("page", 0), Show("FH_gallery", dissolve))
        if FH_cg_char in ["sl", "dv", "un", "us"]:
            $ cells = 9
            grid 3 3:
                xpos 0.3 ypos 0.2
                
                $ cg_displayed = 0
                $ next_page = page + 1
                if next_page > int(len_table/cells):
                    $ next_page = 0
                $ FH_gal_list = FH_gall_list(FH_cg_char)
                for n in range(0, len_table):
                    if n < (page+1)*cells and n>=page*cells:
                        python:
                            nocrop = False
                            if type(FH_gal_list[n]) is list:
                                if FH_gal_list[n][0] in gallery_cg:
                                    imgp = "images/cg/" + FH_gal_list[n][0] + ".jpg"
                                else:
                                    if FH_gal_list[n][0].startswith("bg FH_"):
                                        imgp = im.Composite((1920, 1080),
                                        (0,0), ("mods/four_horizons/images/bg/" + FH_gal_list[n][0][6:] + ".jpg"),
                                        (0,0), ("mods/four_horizons/images/cg/kiss_un_1.png"))
                                    elif FH_gal_list[n][0].startswith("bg"):
                                        imgp = im.Composite((1920, 1080),
                                        (0,0), ("images/bg/" + FH_gal_list[n][0][3:] + ".jpg"),
                                        (0,0), ("mods/four_horizons/images/cg/kiss_un_1.png"))
                                    elif FH_gal_list[n][0].startswith("alb"):
                                        imgp = "mods/four_horizons/images/misc/" + FH_gal_list[n][0] + ".png"
                                        nocrop = True
                                    elif renpy.loadable("mods/four_horizons/images/cg/" + FH_gal_list[n][0][3:] + ".jpg"):
                                        imgp = "mods/four_horizons/images/cg/" + FH_gal_list[n][0][3:] + ".jpg"
                                    else:
                                        imgp = "mods/four_horizons/images/cg/" + FH_gal_list[n][0][3:] + ".png"
                            else:
                                if FH_gal_list[n] in gallery_cg:
                                    imgp = "images/cg/" + FH_gal_list[n] + ".jpg"
                                else:
                                    if renpy.loadable("mods/four_horizons/images/cg/" + FH_gal_list[n][3:] + ".jpg"):
                                        imgp = "mods/four_horizons/images/cg/" + FH_gal_list[n][3:] + ".jpg"
                                    else:
                                        imgp = "mods/four_horizons/images/cg/" + FH_gal_list[n][3:] + ".png"
                            if nocrop:
                                th = imgp
                            else:
                                _t = im.Crop(imgp, (0,0,1920,1080))
                                th = im.Scale(_t, 320, 180)
                            img = im.Composite((336,196),(8,8),im.Alpha(th,0.9),(0,0),im.Image(get_image("gui/gallery/thumbnail_idle.png")))
                            imgh = im.Composite((336,196),(8,8),th,(0,0),im.Image(get_image("gui/gallery/thumbnail_hover.png")))
                        if type(FH_gal_list[n]) is list:
                            if FH_gal_list[n][0].startswith("alb"):
                                add FH_g.make_button(FH_gal_list[n][2], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                            else:
                                add FH_g.make_button(FH_gal_list[n][0], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                        else:
                            add FH_g.make_button(FH_gal_list[n], get_image("gui/gallery/blank.png"), None, imgh, img, style="blank_button", bottom_margin=50, right_margin=50)
                        $ cg_displayed += 1
                        
                        if n+1 == len_table:
                            $ next_page = 0

                for j in range(0, 9-cg_displayed):
                    null

            grid 3 1:
                xpos 0.505 ypos 0.85
                if page != 0:
                    imagebutton auto get_image("gui/dialogue_box/prologue/backward_%s.png") action (SetVariable('page', page-1), Show("FH_gallery", dissolve))
                else:
                    null width 116
                python:
                    def abc(n,k):
                        l = float(n)/float(k)
                        if l-int(l) > 0:
                            return int(l)+1
                        else:
                            return l
                    pages = str(page+1)+"/"+str(int(abc(len_table,cells)))
                text pages style "FH_gallery_style" color "FFF" yalign 0.5 xalign 0.5
                if next_page == 0:
                    null width 116
                else:
                    imagebutton auto get_image("gui/dialogue_box/prologue/forward_%s.png") action (SetVariable('page', next_page), Show("FH_gallery", dissolve))

                

    if FH_mode == "music":
        text "Музыка":
            style "FH_gallery_style"
            xalign 0.5 yalign 0.05
        textbutton "Иллюстрации":
            style "FH_gallery_style" text_style "FH_gallery_style"
            xalign 0.05 yalign 0.05
            action (SetVariable("FH_mode", "cg"), SetVariable("FH_cg_char", "none"), Show("FH_gallery", dissolve) )
        textbutton "Фоны":
            style "FH_gallery_style" text_style "FH_gallery_style"
            xalign 0.95 yalign 0.05
            action (SetVariable("FH_mode", "bg"), SetVariable("page", 0), Show("FH_gallery", dissolve) )

        side "c r":
            area (0.05, 0.15, 0.9, 0.74)
            viewport id "music_box":
                draggable True
                mousewheel True
                scrollbars None

                has grid 1 len(FH_music_list)
                for name, file in FH_music_list:
                    if renpy.seen_audio(file):
                        textbutton name:
                            style "FH_mroom"
                            text_style "FH_mroom"
                            action FH_mr.Play(file)
                    else:
                        textbutton "???":
                            style "FH_mroom"
                            text_style "FH_mroom"
            $ vbar_null = Frame(get_image("gui/settings/vbar_null.png"),0,0)

            vbar value YScrollValue("music_box") bottom_bar vbar_null top_bar vbar_null thumb "images/gui/settings/vthumb.png" thumb_offset -12

    imagebutton auto get_image("gui/dialogue_box/prologue/backward_%s.png") xalign 0.01 yalign 0.97 action (Hide("FH_gallery", dissolve), Hide("FH_menu_main"), Return("menu"))

label FH_start:
    scene FH_menu_bg
    with fade2
    $ prolog_time()
    play music "mods/four_horizons/music/Z FEEL-Z-Hear The Wind-kissvk.com.mp3" fadein 3
    call screen FH_menu_main with dissolve
    stop music fadeout 3
    scene bg black with dissolve2
    return

label FH_discplaimer:
    scene black with dissolve
    show text FH_discplaimer_text at truecenter with dissolve
    pause 5
    return