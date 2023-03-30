init:
    image dv_ti = 'mods/four_horizons/spr/dv_tit.png'
    $ mods["credits_fh_2"]=u"Четыре горизонта. Титры"

label credits_fh_2:
    scene bg ext_aidpost_day:
        blur 16
    show dv_ti:
        xalign 0.0 ypos 2000
        linear 60 ypos -7700

    $ renpy.pause(20)
    

