init:
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


    #спрайты
    image se angry = "mods/four_horizons/spr/sem/se_Angry.png"
    image se grin = "mods/four_horizons/spr/sem/se_Grin.png"
    image se normal = "mods/four_horizons/spr/sem/se_Normal.png"
    image se shocked = "mods/four_horizons/spr/sem/se_Shocked.png"
    image se smile = "mods/four_horizons/spr/sem/se_smile.png"
    image se sure = "mods/four_horizons/spr/sem/se_Sure.png"
    image se surprise = "mods/four_horizons/spr/sem/se_surprise.png"
    image se upset = "mods/four_horizons/spr/sem/se_Upset.png"
    image un1 cry_smile = im.MatrixColor('mods/four_horizons/spr/un/normal/un_2_sleep_4hor_cry_smile.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 shy = im.MatrixColor('mods/four_horizons/spr/un/normal/un_1_sleep_4hor_shy.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 smile = im.MatrixColor('mods/four_horizons/spr/un/normal/un_1_sleep_4hor_smile.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 laugh = im.MatrixColor('mods/four_horizons/spr/un/normal/un_3_sleep_4hor_laugh.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 smile2 = im.MatrixColor('mods/four_horizons/spr/un/normal/un_1_sleep_4hor_smile2.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 smile3 = im.MatrixColor('mods/four_horizons/spr/un/normal/un_3_sleep_4hor_smile3.png', im.matrix.tint(0.63, 0.78, 0.82))
    image un1 grin = im.MatrixColor('mods/four_horizons/spr/un/normal/un_3_sleep_4hor_grin.png', im.matrix.tint(0.63, 0.78, 0.82))


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

init python:
    heart = 'mods/four_horizons/Музыка/ambi/heart.mp3'
    mgs = 'mods/four_horizons/Музыка/ambi/mgs.mp3'

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
    show text '{font=mods/four_horizons/GothicRus2.ttf}{size=90}{color=#8B00FF}[dayn]{/size}{/font}{/color}':
        xalign fix2
        yalign 0.8
    with dissolve2
    pause 3
    show black with moveinright
    return
