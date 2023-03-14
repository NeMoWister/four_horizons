init:
    
    #Персонажи
    $ ung = Character(u'Девушка', color="B956FF", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ usg_nvl = Character(u'Девушка', kind=nvl, color="FF3200", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ mig = Character(u'Девушка', color="#00DEFF", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ elb = Character(u'Парень', color="#FFFF00", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ shb = Character(u'Парень', color="#FFFF00", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ mzg = Character(u'Девушка', color="#72A0FF", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ csn = Character(u'…', color="#A5A5FF", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    
    $ un_and_us = Character(u'Лена и Ульяна', color="FF56FF", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    
    $ golos_fizruka = Character(u'Голос', color="555555", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ trener = Character(u'Тренер', color="555555", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ Se_Vi = Character(u'Сергей Витальевич', color="555555", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ Se_Vi_nvl = Character('Сергей Витальевич: ', kind=nvl, color="555555", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ max = Character(u'Максим', color="00F0C8", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ max_nvl = Character('Максим: ', kind=nvl, color="00F0C8", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ all_voices = Character(u'Все', color="0000FF", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ voditel = Character(u'Водитель', color="F5DEB3", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ father_nvl = Character(u'Отец: ', kind=nvl, color="555555", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ prepod_nvl = Character(u'Преподаватель: ', kind=nvl, color="555555", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    
    
    
    
    
    #Спрайты персонажей
    
    
    
    #Физрук
    image fiz normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_normal.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_normal.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/fizruk/fizruk_normal.png" )
    
    image fiz smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_smile.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_smile.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/fizruk/fizruk_smile.png" )
    
    image fiz int = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_int.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_int.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/fizruk/fizruk_int.png" )

    image fiz angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_angry.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/fizruk/fizruk_angry.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/fizruk/fizruk_angry.png" )
    
    
    
    #Семён
    image se normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Normal.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Normal.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_Normal.png" )
    
    image se smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_smile.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_smile.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_smile.png" )
    
    image se grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Grin.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Grin.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_Grin.png" )
    
    image se shocked = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Shocked.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Shocked.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_Shocked.png" )
    
    image se angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Angry.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Angry.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_Angry.png" )
    
    image se sure = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Sure.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Sure.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_Sure.png" )
    
    image se surprise = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_surprise.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_surprise.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_surprise.png" )
    
    image se surprise = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_surprise.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_surprise.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_surprise.png" )
    
    image se upset = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Upset.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/spr/sem/se_Upset.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/spr/sem/se_Upset.png" )
    
    
    
    
    
    
    
    
    
    
    #БГ
    image int_Maxims_flat = "mods/four_horizons/bg/int_Maxim's_flat.jpg"
    image int_cloakroom = "mods/four_horizons/bg/int_cloakroom.jpg"
    image ext_stadion = "mods/four_horizons/bg/ext_stadion.jpg"
    image ext_bus_busstop_summer = "mods/four_horizons/bg/bus_busstop_summer_day1.jpg"
    image ext_Maxim_house_day = "mods/four_horizons/bg/ext_Maxim_house_day.jpg"
    image ext_Maxim_house_sunset = "mods/four_horizons/bg/ext_Maxim_house_sunset.jpg"
    image ext_Maxim_house_night = "mods/four_horizons/bg/ext_Maxim_house_night.jpg"
    image int_Maxim_house_day = "mods/four_horizons/bg/int_Maxim_house_day.jpg"
    image int_Maxim_house_sunset = "mods/four_horizons/bg/int_Maxim_house_sunset.jpg"
    image int_Maxim_house_night = "mods/four_horizons/bg/int_Maxim_house_night.jpg"
    image int_Maxim_house_night_light = "mods/four_horizons/bg/int_Maxim_house_night_light.jpg"
    image ext_depot_day = "mods/four_horizons/bg/ext_depot.jpg"
    image ext_depot_sunset = "mods/four_horizons/bg/ext_depot_sunset.jpg"
    image ext_depot_night = "mods/four_horizons/bg/ext_depot_night.jpg"
    image ext_playground_sunset = "mods/four_horizons/bg/ext_playground_sunset.png"
    image ext_houses_night = "mods/four_horizons/bg/ext_houses_night.png"
    image int_depot_sunset = "mods/four_horizons/bg/int_depot_sunset.jpg"
    image ext_aidpost_sunset = "mods/four_horizons/bg/ext_aidpost_sunset.png"
    image Maxim_and_Ulyana_at_bus_stop = "mods/four_horizons/cg/Maxim_and_Ulyana_at_bus_stop.png"
    
    
    
    
    
    #ЦГ
    image map = "mods/four_horizons/cg/map.jpg"
    image Maxim_reflection = "mods/four_horizons/cg/Maxim_reflection.jpg"
    image cg_line = "mods/four_horizons/cg/cg_line.jpg"
    image Maxim_and_Ulyana_peel_potatoes = "mods/four_horizons/cg/Maxim_and_Ulyana_peel_potatoes.jpg"
    image Maxim_and_Ulyana_intensively_peel_potatoes = "mods/four_horizons/cg/Maxim_and_Ulyana_intensively_peel_potatoes.jpg"
    image Ulyana_and_Maxim_with_book = "mods/four_horizons/cg/Ulyana_and_Maxim_with_book.png"
    image Maxim_and_Ulyana_boat = "mods/four_horizons/cg/Maxim_and_Ulyana_boat.jpg"
    image Maxim_and_Ulyana_hug_catacombs = "mods/four_horizons/cg/Maxim_and_Ulyana_hug_catacombs.jpeg"
    
    
    
    
    
    #Звуки
    $ sound_of_running = "mods/four_horizons/sounds/sound_of_running.mp3"
    $ doused_with_water = "mods/four_horizons/sounds/doused_with_water.mp3"
    $ door_handle = "mods/four_horizons/sound/door_handle.mp3"
    $ sfx_unlock_door = "mods/four_horizons/sounds/sfx_unlock_door.mp3"
    $ sfx_alisa_falls_novoice = "mods/four_horizons/sounds/sfx_alisa_falls_novoice.ogg"