init:
    image main_img = im.Scale("mods/four_horizons/bg/ext_boathouse_alt_night_7dl.jpg", 1920, 1080)
    image us_main = im.Scale("mods/four_horizons/cg/IMG_7046.png", 1920, 1080)
    image dv_main = im.Scale("mods/four_horizons/cg/dv_sem.png", 1920, 1080)
    image sl_main = im.Scale("mods/four_horizons/cg/IMG_7353.png", 1920, 1080)
    image un_main = im.Scale("mods/four_horizons/cg/dance_night.png", 1920, 1080)
    $ mods["menu_fh"]=u"Четыре горизонта. Меню."

    $ credits_fh = '{color='#ff0000'}Дисклеймер{/color}.\nВсе истории и персонажи является фантазией сценариста.\nЛюбое совпадение с реальностью - чистая случайность.'
    $ credits_fh_v2 = '''
    Дисклеймер.
    Перед началом игры, пожалуйста, ознакомьтесь с данной информацией.

    Эта игра предназначена только для развлекательных целей и не имеет никакой связи с реальностью.\nВсе персонажи, события и диалоги являются вымышленными и не являются настоящими.

    Игра может содержать материалы, которые могут оказаться неуместными для некоторых игроков, включая сцены насилия, жестокости, сексуальные сцены или нецензурную лексику.\nИгроки, которые не желают видеть такие материалы, должны прекратить игру.
    '''




    
init python:
    
    
    style.fhs = Style(style.default)
    style.fhs.size = 60
    style.fhs.color = "#FFFAFA"
    style.fhs.hover_color = "#9b870c"
    style.fhs.font = "mods/four_horizons/VinSlabPro-LightItalic.ttf"
    
    class CutM(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = []
            self.rd = "mods/four_horizons/firedrop.png"

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
    renpy.image("cutm", CutM().sm)
    
transform fh_menu:
    alpha 0 xalign -0.5
    ease 2.5 alpha 1.0 xalign 0.05

transform fh_mn:
    alpha 0.0
    on appear:
        alpha 1.0
    on show:
        linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 1.0
        
transform fh_button:
    on idle:
        ease .75 zoom 1 alpha .8
    on hover:
        ease .75 zoom 1.2 alpha 1.0
    

screen menu_main():
    timer 0.00001 action Play("music", "mods/four_horizons/music/Z FEEL-Z-Hear The Wind-kissvk.com.mp3")
    add "main_img"
    add (CutM().sm)
    vbox at fh_menu:
        spacing 30
        xalign 0.1
        yalign .5
        textbutton "Начать" at fh_button:
            style "fhs"
            text_style "fhs"
            action ShowMenu('fh_ch')
        textbutton "Загрузить" at fh_button:
            style "fhs"
            text_style "fhs"
            action ShowMenu("load", dissolve)
        textbutton "Новости" at fh_button:
            style "fhs"
            text_style "fhs"
            action OpenURL("https://vk.com/vitotheknyazzpublic")
        textbutton "Выход" at fh_button:
            style "fhs"
            text_style "fhs"
            action (Hide('menu_main'), Stop("music"), Call('main'))


screen fh_ch:
    modal True
    vbox at fh_menu:
        default n = 0
        spacing 30
        xalign 0.1
        yalign 0.5
        textbutton 'Лена' at fh_button:
            style 'fhs'
            text_style 'fhs'
            hovered SetScreenVariable(n, 1)
        textbutton 'Алиса' at fh_button:
            style 'fhs'
            text_style 'fhs'
            hovered SetScreenVariable(n, 2)
        textbutton 'Ульяна' at fh_button:
            style 'fhs'
            text_style 'fhs'
            hovered SetScreenVariable(n, 3)
        textbutton 'Славя' at fh_button:
            style 'fhs'
            text_style 'fhs'
            hovered SetScreenVariable(n, 4)
        textbutton 'Назад' at fh_button:
            style 'fhs'
            text_style 'fhs'
            hovered SetScreenVariable(n, 0)
            #hover_background '':
                #xalign 0.0 yalign 0.0
    showif n == 0:
        pass
        add 'main_img' at fh_mn
    elif n == 1:
        add 'un_main' at fh_mn
    elif n == 2:
        add 'dv_main' at fh_mn
    elif n == 3:
        add 'us_main' at fh_mn
    elif n == 4:
        add 'sl_main' at fh_mn
            

label menu_fh:
    call screen menu_main with dissolve
    jump four_horizons

label credits_fh:
    scene black with dissolve
    text credits_fh at truecenter with dissolve:
        size 100
    return