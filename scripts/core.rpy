init:
    $ mods["Four_horizons_Kirril_story_prologue"]=u"Четыре горизонта (История Кирилла)"
    #персонажи
    $ mom = Character(u'Мама', color="#e9ff57", what_color="E2C778")
    $ doc = Character(u'Доктор', color="#454545", what_color="E2C778")
    $ doc1 = Character(u'Медсестра', color="#247ba6", what_color="E2C778")
    $ vi = Character(u'Виталий', color="#013d00", what_color="E2C778")
    $ vito = Character(u'Вито', color="#042604", what_color="E2C778")#042604
    $ va = Character(u'Вадим', color="#ffffff", what_color="E2C778")
    $ v = Character(u'Голоса', color="#E6E6FA", what_color="E2C778", kind=nvl)
    $ vi_n = Character(u'Виталий:', color="#013d00", what_color="E2C778", kind=nvl, ctc="ctc_animation_nvl", ctc_position="fixed")
    $ ge = Character(u'Георгий:', color="#331d01", what_color="E2C778", kind=nvl, ctc="ctc_animation_nvl", ctc_position="fixed")
    $ re = Character(u'Регистратор', color="#331d01", what_color="E2C778")

    $ al = Character(u'Алексей', color="#013d00", what_color="E2C778")
    $ vas = Character(u'Василий', color="#013d00", what_color="E2C778")
    $ al_n = Character(u'Алексей:', color="#013d00", what_color="E2C778", kind=nvl, ctc="ctc_animation_nvl", ctc_position="fixed")
    $ vas_n = Character(u'Василий:', color="#013d00", what_color="E2C778", kind=nvl, ctc="ctc_animation_nvl", ctc_position="fixed")



    $ ded = Character(u'Дед', color="#E6E6FA", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ ki = Character(u'Кирилл', color="#E6E6FA", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ ki_nvl = Character('Кирилл: ', kind=nvl, color="#E6E6FA", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ shb = Character(u'Парень', color="#E6E600", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ meb = Character(u'Парень', color="#E6E6FA", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ pap_ki = Character(u'Папа: ', kind=nvl, color="#E6E6FA", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ mam_ki = Character(u'Мама: ', kind=nvl, color="#E6E6FA", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ pap_sl = Character(u'Папа Слави: ', kind=nvl, color="#FFD200", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ mam_sl_nvl = Character(u'Мама Слави: ', kind=nvl, color="#FFD200", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")
    $ mam_sl = Character(u'Мама Слави', color="#FFD200", what_color="E2C778", drop_shadow = [ (2, 2) ],drop_shadow_color = "#000",what_drop_shadow = [ (2, 2) ],what_drop_shadow_color = "#000")

    #спрайты
    image se angry = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Angry.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Angry.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_Angry.png" )

    image se grin = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Grin.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Grin.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_Grin.png" )

    image se normal = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Normal.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Normal.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_Normal.png" )

    image se shocked = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Shocked.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Shocked.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_Shocked.png" )

    image se smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_smile.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_smile.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_smile.png" )

    image se sure = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Sure.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Sure.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_Sure.png" )

    image se surprise = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_surprise.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_surprise.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_surprise.png" )

    image se upset = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Upset.png", im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( "mods/four_horizons/Дополнительные спрайты/sem/se_Upset.png", im.matrix.tint(0.63, 0.78, 0.82) ),
    True, "mods/four_horizons/Дополнительные спрайты/sem/se_Upset.png" )


    image un1 cry_smile = im.MatrixColor('mods/four_horizons/spr/un/normal/un_2_sleep_4hor_cry_smile.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 shy = im.MatrixColor('mods/four_horizons/spr/un/normal/un_1_sleep_4hor_shy.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 smile = im.MatrixColor('mods/four_horizons/spr/un/normal/un_1_sleep_4hor_smile.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 laugh = im.MatrixColor('mods/four_horizons/spr/un/normal/un_3_sleep_4hor_laugh.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 smile2 = im.MatrixColor('mods/four_horizons/spr/un/normal/un_1_sleep_4hor_smile2.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 smile3 = im.MatrixColor('mods/four_horizons/spr/un/normal/un_3_sleep_4hor_smile3.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 grin = im.MatrixColor('mods/four_horizons/spr/un/normal/un_3_sleep_4hor_grin.png', im.matrix.tint(0.63, 0.78, 0.82))



    image ded smile daily = "mods/four_horizons/Дополнительные спрайты/ded/ded/ded_1.png"
    image ded smile2 daily = "mods/four_horizons/Дополнительные спрайты/ded/ded/ded_2.png"
    image ded smile3 daily = "mods/four_horizons/Дополнительные спрайты/ded/ded/grigory_idle_b.png"
    image ded dissatisfied daily = "mods/four_horizons/Дополнительные спрайты/ded/ded/grigory_moody_b.png"
    image ded normal daily = "mods/four_horizons/Дополнительные спрайты/ded/ded/grigory_sad_b.png"
    image ded wink daily = "mods/four_horizons/Дополнительные спрайты/ded/ded/grigory_wink_b.png"

    #фоны
    image bg int_din_sunset = 'mods/four_horizons/bg/int_din_sunset.jpg'
    image bg obs_int_musclub_mattresses_night = 'mods/four_horizons/bg/obs_int_musclub_mattresses_night.png'
    image bg ext_house_of_un_night_7dl = 'mods/four_horizons/bg/ext_house_of_un_night_7dl.jpg'
    image bg ext_un_house_sunset = 'mods/four_horizons/bg/ext_un_house_sunset.png'
    image bg ext_houses_night_moonlight = 'mods/four_horizons/bg/ext_houses_night_moonlight.jpg'
    image bg ext_stage_big_night = 'mods/four_horizons/bg/ext_stage_big_night.jpg'
    image bg int_musclub_sunset = 'mods/four_horizons/bg/int_musclub_sunset.png'
    image bg obs_ext_musclub_verandah_sunset = 'mods/four_horizons/bg/obs_ext_musclub_verandah_sunset.png'
    image bg ext_musclub_night_7dl = 'mods/four_horizons/bg/ext_musclub_night_7dl.jpg'
    image bg int_musclub_night_light = 'mods/four_horizons/bg/int_musclub_night_light.png'
    image bg d5_musclub1_night = 'mods/four_horizons/bg/d5_musclub1_night.jpg'
    image bg 1022-2 = "mods/four_horizons/bg/1022-2.jpg"
    image bg alex_room_day = "mods/four_horizons/bg/alex_room_day.jpg"
    image bg alex_room_night = "mods/four_horizons/bg/alex_room_night.jpg"
    image bg bedroom = "mods/four_horizons/bg/bedroom.jpg"
    image bg bus_busstop_summer_day1 = "mods/four_horizons/bg/bus_busstop_summer_day1.jpg"
    image bg cafe = "mods/four_horizons/bg/cafe.jpg"
    image bg class = "mods/four_horizons/bg/class.jpg"
    image bg ext_boathouse_alt_day_7dl = "mods/four_horizons/bg/ext_boathouse_alt_day_7dl.jpg"
    image bg ext_boathouse_alt_night_7dl = "mods/four_horizons/bg/ext_boathouse_alt_night_7dl.jpg"
    image bg ext_boathouse_sunset = "mods/four_horizons/bg/ext_boathouse_sunset.jpg"
    image bg ext_bus1 = "mods/four_horizons/bg/ext_bus1.jpg"
    image bg ext_busstop_summer_day = "mods/four_horizons/bg/ext_busstop_summer_day.jpg"
    image bg ext_home_day = "mods/four_horizons/bg/ext_home_day.jpg"
    image bg ext_house_of_to_sunset = "mods/four_horizons/bg/ext_house_of_to_sunset.jpg"
    image bg ext_island = "mods/four_horizons/bg/ext_island.jpg"
    image bg ext_pier_day = "mods/four_horizons/bg/ext_pier_day.jpg"
    image bg ext_pier_sunset = "mods/four_horizons/bg/ext_pier_sunset.jpg"
    image bg ext_street_night = "mods/four_horizons/bg/ext_street_night.jpg"
    image bg ext_warehouse_day_7dl = "mods/four_horizons/bg/ext_warehouse_day_7dl.jpg"
    image bg ext_warehouse_night_7dl = "mods/four_horizons/bg/ext_warehouse_night_7dl.jpg"
    image bg fon_PapaKarlo = "mods/four_horizons/bg/fon-gotovy-debarkader_PapaKarlo.jpg"
    image bg home_night2 = "mods/four_horizons/bg/home_night2.jpg"
    image bg int_house_of_str_day = "mods/four_horizons/bg/int_house_of_str_day.jpg"
    image bg int_house_of_to_night_noflower = "mods/four_horizons/bg/int_house_of_to_night_noflower.jpg"
    image bg int_house_of_to_sunset = "mods/four_horizons/bg/int_house_of_to_sunset.jpg"
    image bg int_house_of_un_sunset = "mods/four_horizons/bg/int_house_of_un_sunset.jpg"
    image bg int_kitchen = "mods/four_horizons/bg/int_kitchen.jpg"
    image bg int_mt_sam_room_night_7dl = "mods/four_horizons/bg/int_mt_sam_room_night_7dl.jpg"
    image bg int_room_dedleny = "mods/four_horizons/bg/int_room_dedleny.jpg"
    image bg int_semen_room2_night = "mods/four_horizons/bg/int_semen_room2_night.jpg"
    image bg int_semen_room_clean = "mods/four_horizons/bg/int_semen_room_clean.jpg"
    image bg park = "mods/four_horizons/bg/park.jpg"
    image bg stadion = "mods/four_horizons/bg/stadion.jpg"
    image bg stadion2 = "mods/four_horizons/bg/stadion2.jpg"



    image ext_depot = "mods/four_horizons/bg/ext_depot.jpg"
    image int_depot = "mods/four_horizons/bg/int_depot.png"
    image countryhouse = "mods/four_horizons/bg/countryhouse.jpg"
    image int_countryhouse_day = "mods/four_horizons/bg/int_countryhouse1.jpg"
    image int_kirill_house_day = "mods/four_horizons/bg/int_kirill_house_day.jpg"
    image int_kirill_house_sunset = "mods/four_horizons/bg/int_kirill_house_sunset.jpg"
    image int_kirill_house_night = "mods/four_horizons/bg/int_kirill_house_night.jpg"
    image ext_kirill_house_day = "mods/four_horizons/bg/ext_kirill_house_day.jpg"
    image ext_kirill_house_sunset = "mods/four_horizons/bg/ext_kirill_house_sunset.jpg"
    image ext_kirill_house_night = "mods/four_horizons/bg/ext_kirill_house_night.jpg"
    image ext_clubs_sunset = "mods/four_horizons/bg/ext_clubs_sunset.jpg"
    image ext_houses_night = "mods/four_horizons/bg/ext_houses_night.png"
    image ext_island_reverse_day = "mods/four_horizons/bg/ext_island_reverse_day.jpg"
    image ext_boathouse_sunset = "mods/four_horizons/bg/ext_boathouse_sunset.jpg"
    image ext_island_sunset = "mods/four_horizons/bg/ext_island_sunset.jpg"
    image int_dining_hall_people_sunset = "mods/four_horizons/bg/int_dining_hall_people_sunset.jpg"
    image ext_house_of_sl_sunset = "mods/four_horizons/bg/ext_house_of_sl_sunset.png"
    image ext_house_of_sl_night = "mods/four_horizons/bg/ext_house_of_sl_night.png"
    image int_house_of_sl_light_night = "mods/four_horizons/bg/int_house_of_sl_light_night.jpg"
    image int_house_of_sl_night = "mods/four_horizons/bg/int_house_of_sl_night.png"
    image ext_forest_sunset = "mods/four_horizons/bg/ext_forest10_sunset.jpg"
    image ext_library_sunset = "mods/four_horizons/bg/ext_library_sunset.png"
    image ext_depot_sunset = "mods/four_horizons/bg/ext_depot_sunset.jpg"

    #ЦГ
    image int_old_camp_car = "mods/four_horizons/bg/int_old_camp_car.jpg"
    image int_old_car_forest = "mods/four_horizons/bg/int_old_car_forest.png"
    image cg_line = "mods/four_horizons/cg/cg_line.jpg"
    image door_in_old_camp = "mods/four_horizons/bg/door_in_old_camp.jpg"
    image door_in_old_camp_open = "mods/four_horizons/bg/door_in_old_camp_open.jpg"
    image Slavya_and_Kirill_on_the_bench = "mods/four_horizons/cg/Slavya and Kirill on the bench.jpg"
    image Kirill_reflection = "mods/four_horizons/cg/Kirill_reflection.jpg"
    image Slavya_and_Kirill_at_the_table = "mods/four_horizons/Наше/Slavya_and_Kirill_at_the_table.jpg"
    image evil_Kirill_and_Slavya = "mods/four_horizons/cg/evil_Kirill_and_Slavya.jpg"
    image Kirill_and_Slavya_dance = "mods/four_horizons/cg/EverlastingSummer-Scene-74.jpg"
    image Kirill_and_Slavya_kiss = "mods/four_horizons/cg/1454001594158369927.png"
    image Kirill_and_Slavya_outside_camp = "mods/four_horizons/Наше/Kirill_and_Slavya_outside_camp.png"
    image Slavya_and_Kirill_hug_open_eyes = "mods/four_horizons/cg/Slavya_and_Kirill_hug_open_eyes.jpg"
    image Slavya_and_Kirill_hug_close_eyes = "mods/four_horizons/cg/Slavya_and_Kirill_hug_close_eyes.jpg"

init python:
    heart = 'mods/four_horizons/Музыка/ambi/heart.mp3'
    mgs = 'mods/four_horizons/Музыка/ambi/mgs.mp3'
    #Звуки
    sound_of_zhiguli_leaving = "mods/four_horizons/Музыка/ambi/sound_of_zhiguli_leaving.mp3"
    pull_handle_of_door = "mods/four_horizons/Музыка/ambi/pull_handle_of_door.mp3"
    doused_with_water = "mods/four_horizons/Музыка/ambi/doused_with_water.mp3"
    turning_on_light = "mods/four_horizons/Музыка/ambi/turning_on_light.mp3"
    sfx_unlock_door = "mods/four_horizons/Музыка/ambi/sfx_unlock_door.mp3"
    sound_of_running = "mods/four_horizons/Музыка/ambi/sound_of_running.mp3"

    #Музыка
    Stigmata_September = "mods/four_horizons/Музыка/Stigmata -Сентябрь.mp3"
    Yan_Shpitalnik_Two = "mods/four_horizons/Музыка/Yan Shpitalnik - Two.mp3"
    Cross_Examination_Allegro = "mods/four_horizons/Музыка/OST Ace Attorney - Cross Examination Allegro.mp3"
    Pursuit_Cornered = "mods/four_horizons/Музыка/OST Ace_Attorney - Pursuit_Cornered.mp3"
    Klavier_Gavin_Guilty_Love = "mods/four_horizons/Музыка/Toshihiko_Horiyama_-_Klavier_Gavin_Guilty_Love.mp3"
    quiet_night = "mods/four_horizons/Музыка/Кино - Спокойная ночь.mp3"

style imgay_style:
    outlines [(absolute(3),"#00ff00",absolute(2),absolute(2))]
    font 'mods/four_horizons/VinSlabPro-LightItalic.ttf'
    color '#FFFFFF'
    size 90


label imGAY(cgn, bgn, spn, dayn, cgpos, textpos):
    $ fix, fix2 = int(cgpos), float(textpos)
    scene black with dissolve
    pause 1
    scene expression cgn:
        xpos -fix
    show expression AlphaMask(bgn, 'mods/four_horizons/huynya2.png'):
        blur 10
    show expression spn:
        xpos 1070
    show text '{=imgay_style}[dayn]{/imgay_style}':
        xalign fix2
        yalign 0.8
    with dissolve2
    pause 3
    show black with moveinright
    return
