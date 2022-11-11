label Four_horizons_Kirril_story_prologue:
    $ save_name = ('Четыре горизонта.\nИстория Кирилла.\nПролог.\nПодарок дедушки.')
    $ prolog_time()
    $ persistent.sprite_time = "day"
    "У каждого есть своя история любви."
    "У кого-то она началась с первого взгляда, у кого-то с дружбы, а у кого-то с первого класса школы."
    "Позвольте мне поделиться своей историей."
    scene int_countryhouse_day with dissolve
    window hide
    pause(1)
    $ set_mode_nvl()
    nvl show dissolve
    play music music_list["farewell_to_the_past_edit"] fadein 2
    "На дворе стояло лето 1987 года."
    "Меня зовут Кирилл, мне 17 лет. Я обычный советский подросток с чувством неразделённой любви, хорошист, которому уже на следующий год грозит поступать в ВУЗ."
    "С самого детства я учился в одном классе с прекрасной девушкой, которую я в тайне прозвал «Воплощение природы в одном лице»."
    "Звали её Славяна, но она всех просила называть её просто Славей."
    "Добрая девушка, которая никому не отказывала в помощи, но и ни с кем особо не контактировала. Пообщаться могла, но вот лучших друзей или же парня у неё вовсе не было."
    "Она очень любила биологию и труды. Особенно, если на трудах они что-то вязали. Славя меня знала как человека, на которого можно положиться, но особо близко мы никогда не общались."
    "Каждый вечер, каждую ночь я засыпаю с мыслями о ней."
    "Это любовь. Любовь с первого класса."
    "Но из-за своей замкнутости, я не могу ей признаться в чувствах, ибо боюсь это поставит жирный крест на нашей дружбе."
    "Если я вообще являюсь для неё другом."
    "Примерно 4 года назад я узнал, что она любит ездить летом в один и тот же пионерлагерь под названием «Совёнок». Я каждый год просил родителей устроить мне поездку в этот лагерь, но всякий раз это заканчивалась неудачей."
    "И вот наступила последняя возможность съездить в лагерь, но родителей не было рядом. Они уехали в командировку, а меня отправили к дедушке."
    nvl clear
    "Мой дедушка был мне не просто дедом, он был мне как старший брат, даже больше, чем отец. Он прекрасно знал о моем желании попасть в этот лагерь. Я ему рассказывал, что не ровно дышу к одной девушке, но не могу ей признаться в своих чувствах. В сердце была надежда на то, что она ответит мне взаимностью, но неизвестность пожирала меня."
    nvl hide dissolve
    pause(1)
    $ set_mode_adv()
    window show
    stop music fadeout 2
    play ambience ambience_int_cabin_day fadein 2
    "И вот настало новое утро."
    "Как обычно я смотрел в окно и думал об одном и том же…"
    "О Славе…"
    th "Как там она интересно поживает в своём лагере?"
    "Однако этот день принимал совершенно нестандартный поворот событий."
    "Дед позвал меня к себе."
    ded "Кирилл, подойди-ка сюда!"
    "Я пришёл на кухню, где меня ждал уже мой дед."
    show ded normal daily with dissolve
    "Я всегда слушался родителей, а деда я любил больше всего на свете, поэтому по малейшему его зову я прибегал к нему."
    ki "Да, дедушка, ты меня звал?"
    ded "Ты отличный внук! Если честно, даже лучше моего сына. Скорее всего, ты пошёл в свою маму или же в меня."
    show ded smile2 daily with dspr
    "Дед засмеялся."
    show ded normal daily with dspr
    ki "В общем, давай ближе к делу. Ты же меня не просто так позвал."
    ded "Толковый парень! Помнишь, ты однажды мне рассказывал, что был влюблён в свою одноклассницу и постоянно рвался в один лагерь?"
    ki "Да, просил родителей выбить путёвку, но им всё отказывали."
    show ded smile daily with dspr
    ded "Им надо было пойти сразу ко мне! А о твоей истории я узнал только год назад."
    ki "Ну, дальше что?"
    ded "Собирайся! Ты едешь в этот лагерь!"
    stop ambience
    play music Stigmata_September fadein 2
    with hpunch
    play sound sfx_body_bump
    "Ноги подкосились, я хотел плюхнуться в кресло, но оно было слишком далеко. Мои расчёты оказались ложными, и я повалился на пол, но тут же вскочил."
    ki "Ты шутишь?!"
    show ded smile3 daily with dspr
    ded "Я когда-нибудь такими вещами шутил?"
    show ded normal daily with dspr
    "Дед положил на стол путёвку."
    "Я не мог поверить ни своим глазам, ни своим ушам то что вижу и слышу."
    ded "Тебе повезло, что одна путёвка освободилась, правда, ты только на неделю туда сможешь приехать."
    ki "Мне этого будет достаточно, чтобы попытать свой шанс."
    show ded smile daily with dspr
    ded "Тогда собирай вещи, возьми все необходимое, и мы отправляемся."
    ki "Разве я не должен буду ехать на автобусе?"
    ded "Ради тебя одного целый автобус отправлять не будут. Я сам тебя на своей «волге» отвезу."
    ki "Я тебе это говорил уже кучу раз и скажу ещё: я тебя люблю, дедушка!"
    show ded smile2 daily with dspr
    ded "Я знаю, я тебя тоже, внучок! Собирайся, я буду ждать тебя в машине."
    hide ded with dissolve
    "Дед тут же вышел на улицу."
    "Я взял путёвку в руки и по-прежнему не мог поверить своим глазам."
    th "Та самая путёвка. В тот самый пионерлагерь «Совёнок», в который постоянно ездит Славя."
    "Держа путёвку в своих руках, я отправился в свою комнату."
    "Придя в свою комнату, я тут же начал собирать свои вещи."
    th "Никогда у меня не было настолько большого желание выбраться из дома. Тем более отправится в путешествие."
    "Взяв свой рюкзак, я решил сложить всё самое необходимое: плавки, средства гигиены, спортивную одежду на всякий случай и пару книг, если будет совсем нечем заняться."
    th "Правда главной моей целью является не чтение книг, а признаться Славе в своих чувствах."
    th "А самое главное, ответит ли она взаимностью? Или же это невзаимная любовь."
    "Собрав вещи, я вышел на улицу."
    scene countryhouse
    show ded smile daily
    with dissolve
    "Дед стоял у машины и уже заканчивал курить."
    ded "Ну что, рыцарь, готов к подвигу?"
    ki "Всегда готов!"
    ded "Садись в машину, сейчас закрою дом и ворота и поедем."
    stop music fadeout 4
    play music Gruppa_krovi fadein 2
    scene int_old_car_forest with dissolve
    "Я сел в машину и спустя пару минут сел дедушка."
    ded "Ну что, поехали?"
    ki "Да! Я готов!"
    "Громко и гордо ответил я и мы тут же отправились в путь."
    "Дед тронул педаль газа, и машина тронулась на встречу нашим приключениям."
    "Дедушка не любил быструю езду, поэтому он ехал спокойно, не превышая скорости даже там, где это можно было сделать."
    "У деда в машине играла отличная, душевная, однако не слишком популярная у нас музыка."
    ded "Не мешает музыка?"
    ki "Нет, нисколько."
    ded "Не забудь, у тебя ровно неделя, чтобы признаться девочке в своих чувствах, но только не делай этого сразу же."
    ki "А что надо делать?"
    "Ведь до этого я никогда не пытался так разговаривать с девушками. Точнее, не как одноклассник с одноклассницей, а парень с девушкой. Ну или по-дружески."
    ded "Покажи ей, что тебе она интересна, как человек, а самое главное, докажи ей, что ты пойдёшь на всё, чтобы добиться её."
    "Дед отвечал с пониманием, ведь он прекрасно знал все мои тайны."
    ki "Спасибо за совет."
    ded "Возвращаться будешь вместе с ней в одном автобусе. Я тебя встречу, как мне позвонит вожатая."
    ki "А как её зовут?"
    ded "Ольга Дмитриевна. Это дочка моей подруги из университета. Взрослая девушка, правда, очень строгая."
    th "Теперь понятно, как деду удалось сделать то, что не сделали мои родители."
    th "Если они вообще пытались достать путёвку в этот лагерь."
    "Наслаждаясь какое-то время летним пейзажем, я почувствовал, что меня потянуло в сон."
    ki "Славя, я иду…"
    ded "Вот этот настрой! Мне нравится! Будь смелее!"
    th "Неужели я с ней встречусь без одноклассников?"
    th "Неужели у меня появился шанс признаться в своих чувствах той, которую люблю?"
    th "Мне нельзя терять этот шанс впустую!"
    show blink
    "И с этими последними словами я окончательно уснул."
    stop music fadeout 2
    jump Four_horizons_Kirril_story_day1