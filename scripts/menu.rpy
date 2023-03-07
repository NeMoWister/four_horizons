init:
    image main_img = im.Scale("mods/four_horizons/cg/dance_night.png", 1920, 1080)
    $ mods["menu_fh"]=u"Четыре горизонта. Меню."
    
    
init python:
    
    
    style.fhs = Style(style.default)
    style.fhs.size = 60
    style.fhs.color = "#FFFAFA"
    style.fhs.hover_color = "#9b870c"
    style.fhs.font = "mods/four_horizons/VinSlabPro-LightItalic.ttf"
    
    class CutM(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "mods/four_horizons/cutm.png"

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
    alpha 0 xalign 1.3
    ease 2.5 alpha 1.0 xalign 0.9
    
        
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
        spacing 20
        xalign 0.9
        yalign .5
        textbutton "Начать" at fh_button:
            style "fhs"
            text_style "fhs"
            action (Hide("menu_main", Dissolve(1.0)), Return())
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
            action Quit()
            
            
    
label menu_fh:
    call screen sova_main with dissolve
    jump four_horizons