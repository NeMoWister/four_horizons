label imGAY(cgn, bgn, spn, dayn):
    scene black with dissolve
    pause 1
    scene expression cgn:
        xpos -700
    show expression AlphaMask(bgn, 'mods/four_horizons/huynya2.png'):
        blur 10
    show expression spn:
        xpos 1070
    show text '{font=mods/four_horizons/GothicRus2.ttf}{size=90}{color=#8B00FF}[dayn]{/size}{/font}{/color}':
        xalign 0.99
        yalign 0.8
    with dissolve2
    pause 3
    show black with moveinright
    return
