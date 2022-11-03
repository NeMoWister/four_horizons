define test = ImageDissolve('huynya2.png', 10.0)
define test2 = AlphaDissolve('huynya2.png', 10.0)

init:
    image h = 'mods/four_horizons/huynya2.png'
    image bg alex_room_day = 'alex_room_day.jpg'
    image cg 1022 = '1022-2.jpg'

init python:
    def f_trans(cgn, bgn, spn):
        renpy.scene(cgn)
        renpy.scene(bgn)
        renpy.show(spn)
        renpy.with_statement(test2)

    def f_trans2(cgn, bgn, spn):
        renpy.jump('f_trans3')

# Игра начинается здесь:
label f_trans3:
    scene cgn
    scene bgn
    show spn:
        xalign 0.8
    with test2
    scene black with pixellate
    return
