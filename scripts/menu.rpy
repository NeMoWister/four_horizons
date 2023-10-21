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
            font "mods/four_horizons/fonts/Montserrat.ttf"
            size 80
            color "92c6e5"
            xalign 0.0
        text "Горизонта":
            font "mods/four_horizons/fonts/Montserrat.ttf"
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
            
label returner:
    return

label FH_chapter_select:
    scene expression "mods/four_horizons/images/misc/menu/idle.jpg" with dissolve
    call screen FH_chapter_selector with dissolve
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
    return


label FH_start:
    scene FH_menu_bg
    with fade2
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