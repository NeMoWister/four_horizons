init:
    image main_img = im.Scale("mods/four_horizons/bg/ext_boathouse_alt_night_7dl.jpg", 1920, 1080)
    image us_main = im.Scale("mods/four_horizons/cg/IMG_7046.png", 1920, 1080)
    image dv_main = im.Scale("mods/four_horizons/cg/dv_sem.png", 1920, 1080)
    image sl_main = im.Scale("mods/four_horizons/cg/IMG_7353.png", 1920, 1080)
    image un_main = im.Scale("mods/four_horizons/cg/dance_night.png", 1920, 1080)
    $ mods["menu_fh"]=u"Четыре горизонта. Меню."
    $ config.developer = True
    $ credits_fh = '{color=#ff0000}{size=120}Дисклеймер{/color}{/size}.\nВсе истории и персонажи является фантазией сценариста.\nЛюбое совпадение с реальностью - чистая случайность.'
    $ credits_fh_v = '{color=#ff0000}{size=60}Дисклеймер{/color}{/size}\n\n{size=40}Перед началом игры, пожалуйста, ознакомьтесь с данной информацией.\n\nЭта игра предназначена только для развлекательных целей и не имеет никакой связи с реальностью.\nВсе персонажи, события и диалоги являются вымышленными и не являются настоящими.{/size}'




    
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
    tag test
    modal True
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
            action (Hide('menu_main', dissolve), Stop("music"), Return())


screen fh_ch:
    tag test
    modal True
    imagemap:
        idle 'mods/four_horizons/bg/idle.jpg'
        hover 'mods/four_horizons/bg/hover.jpg'

        hotspot (0, 0, 480, 1080) action Jump('Four_horizons_Maxim_story_prologue'), Stop("music"), Hide('menu_main', dissolve), Hide('fh_ch', dissolve)
        hotspot (481, 0, 480, 1080) action Jump('four_horizons_dv'), Stop("music"), Hide('menu_main', dissolve), Hide('fh_ch', dissolve)
        hotspot (961, 0, 480, 1080) action Jump('Four_horizons_Kirril_story_prologue'), Stop("music"), Hide('menu_main', dissolve), Hide('fh_ch', dissolve)
        hotspot (1441, 0, 480, 1080) action Jump('four_horizons'), Stop("music"), Hide('menu_main', dissolve), Hide('fh_ch', dissolve)

        key "K_ESCAPE" action Return()

            

label menu_fh:
    play music "mods/four_horizons/music/Z FEEL-Z-Hear The Wind-kissvk.com.mp3" fadein 3
    call screen menu_main with dissolve
    stop music fadeout 3
    return

label credits_fh:
    stop music fadeout 0.5
    scene black with dissolve
    show text credits_fh_v at truecenter with dissolve
    $renpy.pause(10)
    return