# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")
define test = ImageDissolve('huynya2.png', 10.0)
define test2 = AlphaDissolve('huynya2.png', 10.0)
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

init:
    image h = 'huynya2.png'
    image bg alex_room_day = 'alex_room_day.jpg'
    image cg 1022 = '1022-2.jpg'

# Игра начинается здесь:
label start:

    scene cg 1022
    '.'
    show h
    '.'
    show bg alex_room_day
    '.'


    scene cg 1022
    '.'
    scene bg alex_room_day
    show eileen happy at right
    with test2
    e "Вы создали новую игру Ren'Py."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    return
