label Four_horizons_Kirril_story_day4:
    $ save_name = ('Четыре горизонта.\nИстория Кирилла.\nДень 4.\nНаша команда.')
    window hide
    $ renpy.pause(2)
    scene int_house_of_sl_day
    hide blink
    show unblink
    $ day_time()
    $ persistent.sprite_time = "day"
    window show
    play ambience ambience_int_cabin_day fadein 2
    "Я проснулся чуть раньше будильника. Судя по заправленной кровати напротив, было ясно, что Славя ушла на пробежку. На стульчике весела её форма."
    play sound sfx_blanket_off_stand
    "Я встал с постели и сразу же принялся одеваться, пока моей соседки не было дома."
    "Хотел уже пойти умываться и чистить зубы, но вспомнил вчерашние слова Шурика."
    stop ambience fadeout 2
    window hide
    show prologue_dream with dissolve
    $ renpy.pause(1)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    scene int_dining_hall_sunset
    show sh serious pioneer
    show prologue_dream
    with dissolve
    window show
    sh "Алиса и Электроник сговорились, чтобы подставить тебя и Женю перед вожатой. Только, в какой день они это сделают, неизвестно."
    window hide
    $ renpy.pause(1)
    $ day_time()
    scene int_house_of_sl_day with dissolve
    $ persistent.sprite_time = "day"
    window show
    play ambience ambience_int_cabin_day fadein 2
    th "Теперь одному идти опасно, будут провокации."
    th "Об этом нужно будет всем собраться и поговорить."
    "Поэтому я стал ждать прихода Слави."
    th "Отличная всё-таки у меня теперь возможность всё выяснить поближе. Взаимны мои чувства или нет? Как всё-таки ко мне относится Славя после всех этих десяти лет учёбы в одном классе?"
    th "Ведь я знаю все её страхи и даже такие подробности, которые неизвестны больше никому."
    play sound sfx_open_door_1
    "Из моих размышлений меня отвлекла открывающаяся дверь."
    show sl smile sport with dissolve
    "На пороге стояла Славя в своей спортивной форме."
    show sl smile2 sport with dspr
    sl "Привет, сосед! А ты чего не умылся?"
    ki "Привет! Тебя ждал, без тебя не хочу идти умываться."
    show sl surprise sport with dspr
    sl "Почему?"
    ki "На то есть свои причины, на завтраке расскажу. Надо только места на шесть человек занять."
    sl "Мы же впятером договорились собраться."
    ki "Возможно, и вшестером, если вы все проголосуете за."
    show sl tender sport with dspr
    sl "Я сделаю так, как ты считаешь нужным. Я тебе в этом плане доверяю."
    ki "Лучше всё равно послушать. Иногда моё мнение может быть ошибочным, а ты можешь иногда меня подправить."
    show sl smile sport with dspr
    sl "Ладно, договорились. А теперь…{nw}"
    show sl smile2 sport with dspr
    ki "Ничего не говори, я уже выхожу."
    scene ext_house_of_sl_day with dissolve
    play sound sfx_close_door_1
    stop ambience fadeout 2
    play music music_list["everyday_theme"] fadein 2
    "Славя хихикнула, а я вышел из домика."
    "Утро уже успела встретить меня светлыми, а главное тёплыми лучами своего солнца."
    th "Чудесный сегодня денёк начинается!"
    "Теперь осталось дождаться соседку и можно пойти умываться."
    show us smile pioneer with dissolve
    play sound sfx_slavya_run
    "Пока я ждал Славю на улице, ко мне подбежала Ульяна."
    us "Привет, зануда!"
    ki "Привет, а почему я зануда?"
    us "Да потому, что не спортивный парень. Ни в футбол не играешь, ни спортом не занимаешься."
    show us sad pioneer with dspr
    us "Да и шутки не воспринимаешь, как шутки."
    ki "Ульяна, я ни с кем ссориться или ругаться не хочу, но всякие шутки, которые могут реально обидеть или навредить, я не потерплю. Так и можешь передать своей рыжей подруге."
    "Девочка не ждала, что я отреагирую именно так, как отреагировал."
    us "Ты думаешь, это она меня послала сюда?"
    ki "Я ничего не думаю. Ты могла и по своей инициативе, ничего не сказав Алисе, сюда прийти. Я ни с кем не желаю портить отношения, поэтому лучше просто оставьте меня и тех, с кем я общаюсь, в покое. В лагере и без меня полно народу."
    show us smile pioneer with dspr
    us "Ладно, лично я к тебе не буду приставать. Пока!"
    hide us with dissolve
    play sound sfx_run_forest
    "Ульяна побежала в сторону площади."
    th "Фух..отстала…"
    show sl normal pioneer with dissolve
    play sound sfx_close_door_1
    "Из этого разговора я даже не заметил, что Славя уже вышла."
    sl "Ну что, пойдём?"
    ki "Пошли."
    scene ext_houses_day
    show sl normal pioneer
    with dissolve
    "По дороге к умывальникам некоторые пионеры обратили на нас внимание и даже кто-то сплетничал."
    th "Неужели уже весь лагерь в курсе, что я переехал к Славе?"
    th "Или опять рыжая сказки сочиняет?"
    th "Плевать, пускай завидуют."
    show sl smile pioneer with dspr
    sl "Кажется, по поводу нас уже слухи или сплетни идут."
    scene ext_washstand_day
    show sl normal pioneer
    with dissolve
    "Заговорила Славя, когда мы подошли к умывальникам."
    ki "А мне всё равно, что будут думать все по поводу нас. Главное, чтобы наши друзья и ты сама о нас плохо не думали."
    show sl smile2 pioneer with dspr
    "Она улыбнулась, и мы принялись за водные процедуры."
    scene ext_washstand2_day with dissolve
    play sound_loop sfx_water_sink_stream
    "Я быстренько почистил зубы и умылся."
    th "Ледяной водичкой не стоит злоупотреблять."
    play sound sfx_close_water_sink
    stop sound_loop
    scene ext_houses_day
    show sl normal pioneer
    with dissolve
    "Закончив, мы отправились обратно в домик."
    show sl smile2 pioneer with dspr
    sl "Ты теперь везде будешь со мной ходить?"
    ki "А ты против?"
    "Засмеялся я."
    show sl laugh pioneer with dspr
    "Она хихикнула в ответ."
    scene ext_house_of_sl_day
    show sl smile2 pioneer
    with dissolve
    "Дойдя до домика, Славя сказала:"
    sl "Я только за!"
    ki "Ну вот и решено значит."
    show sl laugh pioneer with dspr
    sl "Давай сюда свои принадлежности, дурень!"
    show sl smile2 pioneer with dspr
    "Я отдал ей свою зубную щётку и пасту. Она положила их в свой пакет."
    sl "Раз мы теперь живём и будем находиться вместе, тогда и пакет у нас будет общий."
    ki "Я не возражаю."
    hide sl with dissolve
    play sound sfx_open_door_1
    "Она вошла в домик, чтобы оставить там наш пакетик."
    th "Не знаю, сколько я ещё раз скажу у себя в голове, но Славя, какая ты хорошая."
    th "Как хорошо, что нет людей, которые могут читать чужие мысли. А то такие люди точно поломались, если бы попытались прочитать мои мысли"
    th "Ведь там только Славя, Славя, Славя, Славя и никого кроме неё."
    show sl smile2 pioneer with dissolve
    play sound sfx_close_door_1
    "Через минуту она вышла, закрыв дверь на замок, она взялась за мою ручку. Я покраснел, но не стал пытаться вырваться с её ручки."
    ki "Пошли получать задание от вожатой."
    sl "Да, я уверена, она заставит нас перед походом поработать."
    ki "А может нам как-то отдельно туда пойти?"
    show sl surprise pioneer with dspr
    sl "В смысле?"
    ki "В прямом, занять не одну полянку, а две. Там, вроде, где мы искали Шурика, есть две полянки."
    ki "Одну пускай занимают все ребята, а мы впятером или в вшестером, займём другую."
    show sl smile pioneer with dspr
    sl "Слушай, а это отличная мысль. Тем более, если с вами буду я, то точно разрешат. Ведь костёр нормально могут развести только двое: я и Ольга Дмитриевна."
    ki "Вот и отлично."
    stop ambience fadeout 2
    play music music_list["get_to_know_me_better"] fadein 2
    scene ext_square_day with dissolve
    "Мы, придя на площадь, тут же встали в строй."
    scene expression 'mods/four_horizons/cg/lineup_mi.png' with dissolve
    "Через пару минут пришла Ольга Дмитриевна."
    mt "Доброе утро, отряд, сегодня у нас по плану назначен поход. Сразу после обеда, чтобы к отбою успеть вернуться."
    mt "Но перед этим, лагерь нуждается в вашей помощи, и сейчас я разобью вас по парам, кто чем заниматься будет."
    "Я особо старался не слушать, только то, что касалось нашей команды, если закончим раньше, то предложить сходить им помочь."
    "Меня и Славю оставляют на уборке площади. Тут не так много работы."
    "Женю и Семёна отправили на уборку в библиотеке."
    "Лену отправили помочь Шурику, так как у него Электроника забрали на помощь Мику."
    "Как идеально всё сошлось."
    mt "Если всем всё понятно – разойтись!"
    play sound sfx_run_forest
    scene ext_square_day with dissolve
    stop ambience fadeout 2
    play ambience ambience_camp_center_day fadein 2
    "Лена сразу же побежала в столовую. Видать, нам занять место."
    show sl normal pioneer at right
    show mt normal panama pioneer at left
    with dissolve
    stop ambience fadeout 2
    "Мы же подошли к вожатой."
    sl "Ольга Дмитриевна, можно обратиться с предложением?"
    show mt smile panama pioneer at left with dspr
    mt "Слушаю вас, мои самые ответственные пионеры."
    sl "Мы хотим устроить два костра. На втором будут 6 человек."
    show mt normal panama pioneer at left with dspr
    mt "Это на соседней поляне от той, где мы обычно разводим?"
    sl "Да, на ней."
    mt "И кто там будет на ней?"
    ki "Я, Славя, Женя, Семён, Лена и Шурик."
    show sl surprise pioneer at right with dspr
    "Славя удивилась, когда я назвал имя Шурика."
    show sl normal pioneer at right with dspr
    mt "Я не возражаю. Главное, соблюдайте меры осторожности."
    show sl smile pioneer at right with dspr
    sl "Не волнуйтесь, Ольга Дмитриевна, ведь с ними буду я."
    show mt smile panama pioneer at left with dspr
    mt "Именно поэтому я и разрешила вам организовать второй костёр. Только в порядок площадь приведите."
    play sound sfx_dinner_horn_processed
    "Прозвучал горн на завтрак."
    mt "Идите кушать."
    scene ext_dining_hall_away_day
    show sl normal pioneer
    with dissolve
    "Мы в очередной раз благодарные нашей вожатой отправились завтракать."
    scene int_dining_hall_sunset
    show sl normal pioneer
    with dissolve
    "Народу у столовой было не так много, поэтому мы зашли туда быстро."
    scene int_dining_hall_day
    show sl normal pioneer
    with dissolve
    stop ambience fadeout 2
    play ambience ambience_dining_hall_empty fadein 2
    "Взяв наши порции, я заметил, что Лена действительно прибежала раньше всех и заняла столик для нас."
    ki "Пошли к Лене, вон уже сидит, нас ждёт."
    "Славя лишь молча кивнула, и мы подошли к Лене."
    hide sl
    show sl normal pioneer at fleft
    show un normal pioneer at cleft
    with dissolve
    ki "Привет художникам!"
    show un scared pioneer at cleft with dspr
    "Лена чуть не подпрыгнула от испуга."
    show un shy pioneer at cleft with dspr
    un "Ой, это вы! Привет-привет!"
    show sl smile pioneer at fleft with dspr
    sl "Специально пораньше для нас место заняла?"
    show un smile pioneer at cleft with dspr
    "Лена хихикнула."
    un "Конечно, я же раньше всех прихожу в столовую всегда, чтобы получше местечко занять."
    un "Вот. Только тут стул один будет лишний."
    ki "Не лишний. К нам ещё один человек подсядет, кто пока не скажу кто. Славя, молчи, сохраняем интригу."
    sl "Хорошо."
    show mz smile glasses pioneer at right
    show se smile at fright
    with dissolve
    mz "А вот и мы! Привет, друзья! Как спалось, Кирилл, на моём месте?"
    ki "Привет, Женя! Здорово, Семён!"
    "Мы поприветствовали друг друга рукопожатием."
    ki "Спалось замечательно, а тебе как спалось на моём месте?"
    mz "Восхитительно!"
    me "Мы аж чуть не проспали линейку."
    sl "Долго обнимались?"
    show sl laugh pioneer at fleft
    show un laugh pioneer at cleft
    show mz laugh glasses pioneer at right
    show se smile at fright
    with dspr
    "Мы все засмеялись. Однако надо было прерывать веселье."
    show sl normal pioneer at fleft
    show un smile pioneer at cleft
    show mz normal glasses pioneer at right
    show se normal at fright
    with dspr
    ki "Ребята, в общем, есть новость неприятная одна, сейчас к нам подсядет ещё один человек и всё расскажет."
    me "И кто же это?"
    "Сзади к нам уже подходил Шурик."
    show sh normal pioneer at center with dspr
    sh "Это буду я. Приветствую всех, я с миром."
    ki "Ты так говоришь, как будто мы тут банда хулиганов каких-то. Садись."
    "Шурик сел рядом с Леной."
    ki "Вчера мне Шурик сказал очень интересную информацию, за которую, я считаю, мы должны считать его своим другом."
    me "Пускай вначале озвучит. Лично я против него ничего не имею."
    show sh serious pioneer at center with dspr
    stop ambience fadeout 2
    play music music_list["into_the_unknown"] fadein 2
    sh "Это сообщение, по большей части, касается Жени и Кирилла, но раз у вас друг от друга тайн нет, тогда ладно, слушайте все."
    "Шурик отпил из своего стакана чай и продолжил."
    sh "Против Кирилла и Жени образовался союз недоброжелателей. Первому хотят просто испортить лагерные каникулы, вторую лишить права на личное счастье."
    show se angry at fright with dspr
    me "Дай угадаю. Опять Электроник всё никак не успокоится?"
    sh "Да, ещё и с Алисой договорился."
    show sl scared pioneer at fleft
    show un shocked pioneer at cleft
    show mz normal glasses pioneer at right
    with dspr
    "Все девушки были шокированы."
    show un normal pioneer at cleft with dspr
    un "А этой чего неймётся? Опять кому-то жизнь хочет испортить?"
    sh "Нет, она хочет отомстить Кириллу за то, что он рассказал всё вожатой и испортил ей день репетиции. А Жене за то, что бегала за ней с арматурой в руках."
    show sl sad pioneer at fleft with dspr
    sl "Ну и дела! Я знала, конечно, что Алиса злопамятная, но чтобы настолько?"
    show mz rage glasses pioneer at right with dspr
    mz "Я ей в глаз дам или вообще убью, если помешает мне быть вместе с Семёном!"
    sh "И Электроник, придурок, влюбился в Женю. Она сказала «нет», у неё есть другой, ну и оставь ты девушку в покое! Так нет, они ещё и меня постарались втянуть в это."
    show se normal at fright with dspr
    me "А что планировал он ещё сделать?"
    sh "Он хотел во время твоего дежурства в медпункте отключить свет, соответственно, пока там всё наладили бы в холодильнике некоторые препараты могли бы прийти в негодность, а потом сделать так, чтобы ты был виновником в отключении электричества. Тебя бы наказали."
    un "А ты что?"
    sh "А я отказывался. Говорил ему, что я не крыса, чтобы просто так парня без причины подставлять, тем более, что он меня пару раз перед Ольгой Дмитриевной отмазывал."
    show sl surprise pioneer at fleft with dspr
    sl "Это в чём он тебя отмазывал?"
    sh "Я пару раз ходил без спроса в старый лагерь."
    show mz bukal glasses pioneer at right with dspr
    mz "Славя, давай не будем его наказывать. Он всё-таки нам интересную новость принёс, а за такую новость, наоборот, человека надо ценить."
    show sl normal pioneer at fleft with dspr
    sl "А я не собиралась Ольге Дмитриевне ничего говорить о нём. Шурик, хоть иногда и бывает занудным, но он добрый человек."
    ki "Я предлагаю всё-таки Шурика вписать в нашу дружескую компанию."
    show un smile pioneer at cleft with dspr
    un "Я согласна, хороших людей надо держать рядом."
    show mz normal glasses pioneer at right with dspr
    mz "Даже если кто-то выскажется против, отныне, этот парень – мой союзник."
    "Семён просто пожал руку Шурику."
    me "Это говорит лучше всех слов."
    sl "А я как все."
    stop music fadeout 2
    play ambience ambience_dining_hall_empty fadein 2
    ki "Ну, значит, решено. За нашего нового товарища в команде – Шурика!"
    "Это прозвучало как тост, и мы чокнулись стаканами."
    sl "Ладно, ребята, нам пора, если мы закончим раньше, придём вам помогать."
    un "Аналогично. Где мы соберёмся?"
    mz "Предлагаю в библиотеке. Сегодня мы там убираемся, а завтра нас раскидают подежурить весь день напоследок."
    me "Очень надеюсь, что раскидают по парам."
    show sh normal pioneer at center with dspr
    sh "Мне без разницы, один я буду или с кем-то из вас. Но, конечно, лучше с вами."
    ki "Ладно, мы пошли. Если что, собираемся в библиотеке перед походом."
    scene ext_depot
    show sl normal pioneer
    with dissolve
    stop ambience fadeout 2
    play ambience ambience_camp_center_day fadein 2
    "Выйдя из столовой, Славя взяла меня за руку и повела в сторону складов."
    ki "А нам там много надо будет убирать?"
    sl "Нет. Мы собираем кучку листвы и всякого мусора, протрём памятник со скамейками и всё."
    ki "Вчера же Алиса тут должна была убираться."
    sl "Так она весь мусор из-под скамеек собирала."
    ki "Ясненько. Тогда давай мне веник, я сразу пойду подметать, пока ты ходишь за водой, а там вместе всё быстро сделаем."
    sl "Лучше не торопиться, а то ещё начудим что-нибудь."
    ki "Хорошо, торопиться не будем."
    play sound sfx_unlock_door_campus
    "Славя открыла склад и дала мне метлу."
    sl "Ты пока что иди, а я за водой. Начну со скамеек."
    ki "Как прикажешь, товарищ сержант!"
    "Отдал ей честь, словно она мой командир."
    show sl laugh pioneer with dspr
    "Славя засмеялась, но тоже в шутливой форме отдала честь."
    "Я отправился на площадь с метлой."
    scene ext_square_day with dissolve
    "Оказавшись на площади, и оценив фронт работ, я осознал, что дел тут не так уж и много, как могло показаться сначала."
    play sound_loop sfx_broom_sweep
    "Я стал потихоньку подметать территорию возле памятников."
    "Поскольку дождя уже давно тут не было, пыли скопилось очень много, и чтобы сильно не пылить я аккуратно подметал территорию."
    show sl normal pioneer far with dissolve
    "К тому моменту на площади уже была и Славя, которая мыла скамейки."
    "Среди листвы и пыли, которую я подметал, было ещё несколько фантиков конфет."
    th "Просто немыслимо, чтобы в деревне или у нас в районе так мусорили."
    th "Уверен, что это проделки рыжих!"
    "Это меня злило, но не мешало выполнить то, что мне было сказано сделать."
    stop sound_loop
    "Примерно через десять минут я закончил подметать. Славя также освободилась."
    show sl normal pioneer with dissolve
    sl "Ну что? Передохнем или сразу отмоем памятник и пойдём отдыхать?"
    ki "Давай лучше сразу отмоем и пойдём."
    show sl smile pioneer with dspr
    sl "Вот это правильно, сразу лучше всё сделать, чтобы потом больше отдыхать, если работы не будет."
    ki "Ты прямо трудоголик!"
    "Мы приступили мыть памятник Генде."
    show sl happy pioneer with dspr
    sl "Ой, кто бы говорил! А сам-то на субботниках больше всех работал, меньше всех отдыхал."
    ki "А ты откуда знаешь?"
    sl "Я не дура, с вами же тогда выходили, просто на другие участки, и я часто замечала, как многие баловались и отдыхали, а ты один берёшь и честно подметаешь."
    ki "Славя, нас будет сегодня ждать ещё один разговор."
    show sl smile pioneer with dspr
    sl "Хорошо, я только рада с тобой поговорить."
    show sl normal pioneer with dspr
    "Дальше мы молча мыли памятник. Он не сильно страдал от пыли, поэтому мы смогли быстро управиться и с ним."
    show mi smile pioneer far at fright with dissolve2
    hide mi with dissolve2
    "Мимо нас пробегала Мику, и всё, что она успела сделать, это помахать нам ручкой. Мы помахали в ответ, но она этого, к сожалению, не увидела."
    scene Slavya_and_Kirill_on_the_bench with dissolve
    stop ambience fadeout 2
    play music music_list["forest_maiden"] fadein 2
    "Закончив мыть памятник, мы ненадолго присели на лавочку чтобы отдохнуть."
    "Мы сели рядышком, но то, что произошло дальше повергло меня в шок."
    "Славя видать так сильно устала, что она положила свою голову прямо к моей."
    th "Обычно в таких сценах, это первый признак симпатии или даже любви."
    th "Неужели все эти годы я всё-таки был симпатичен Слави, но из-за своей нерешительности не знал, как ей это сказать!"
    th "Дурак!"
    "Но мне было сейчас всё равно на свои мысли, которые меня стыдили, сейчас любимая девочка сидит рядышком, дышит, никуда не вырывается и не хочет уходить. "
    th "Ей явно это сцена тоже очень приятна."
    "Пару минут так и царила тишина на площади. Только звуки ветра, нашего дыхания и стук моего сердца нарушали эту гробовую тишину."
    sl "Пускай не очень красиво, но хоть так поприветствовала нас."
    "Внезапно нарушила тишину Славя."
    ki "Жалко она только не увидела, что мы ей тоже помахали в ответ."
    sl "Она это почувствовала, она знает, что мы добрые люди."
    ki "Ну что, будем тут отдыхать, или пойдём сразу в библиотеку?"
    sl "Раньше бы я сказала, а давай пойдём, попросим ещё работы, чтобы день быстрее и с пользой прошёл."
    ki "И что изменилось?"
    sl "Ты приехал и всё поменялось. Пойдём лучше в библиотеку и там с ребятами отдохнём до обеда."
    ki "Ну, пошли."
    sl "Ты пока иди туда, я сейчас закину всё на склад и приду."
    scene ext_square_day
    show sl normal pioneer with dissolve
    stop music fadeout 2
    play ambience ambience_camp_center_day fadein 2
    "Мы встали со скамейки, и моя соседка тут же приступила к сбору всего того, что мы взяли со склада."
    ki "Может, тебе помочь?"
    show sl smile2 pioneer with dspr
    sl "Сама справлюсь."
    ki "Давай, я буду ждать."
    scene ext_library_day with dissolve
    "Я отправился в библиотеку."
    show se normal with dissolve
    "Подойдя к библиотеке, я встретился с Семёном, который заканчивал протирать окна."
    ki "Как уборка идёт?"
    show se smile with dspr
    me "Вы уже закончили?"
    ki "Да, сейчас Славя подойдёт."
    me "Здорово! Лена с Шуриком тоже должны скоро закончить."
    ki "У меня к тебе есть просьба."
    show se normal with dspr
    me "Какая?"
    ki "Я хочу со Славей уйти пораньше, чтобы обсудить кое-какие вопросы перед сном."
    me "Не проблема, остальным потом скажу."
    ki "Только вот какое оправдание придумать?"
    show se smile with dspr
    "Семён тут же ухмыльнулся."
    me "Это легко. Скажи, что ногу подвернул и хочешь пойти домой. Главное, прихрамывать не забывай."
    ki "Был опыт симуляции?"
    me "Есть такое."
    ki "Ладно, спасибо."
    "Перед тем, как зайти в библиотеку я пожал руку Семёну."
    th "Хороший парень, добрый и выручаешь чем можешь."
    scene int_library_day with dissolve
    "Я зашёл в библиотеку."
    "Женя тут же обратила на меня внимание."
    show mz normal glasses pioneer with dissolve
    mz "Кирилл, если хочешь, можешь пока подремать в кабинете, где мы стенгазету оформляем. Я тебя разбужу."
    ki "А если искать будут?"
    show mz smile glasses pioneer with dspr
    mz "Скажу, что вы закончили раньше и решили передохнуть просто."
    show mz normal glasses pioneer with dspr
    ki "Спасибо."
    show mz smile glasses pioneer with dspr
    mz "Это тебе спасибо."
    "Я отправился в тот самый кабинет."
    ##Фон класса в библиотеки утро
    "Сев за столик, я положил пару книжек как подушку."
    show blink
    "Закрыв глаза, я практически моментально упал в мир снов."
    play music music_list["drown"] fadein 2
    "Мне снился сон."
    "Он был о возможных проблемах в будущем."
    "В моем сне произошло ужаснейшее событие для всей нашей любимой страны. А именно развал СССР. Весь Союз разделился на 15 различных территорий."
    "Самая огромная из них чуть не уничтожила саму себя изнутри. Бесконечные жестокие войны между народами, которые, казалось, совсем недавно сражались плечом к плечу."
    "В этом ужасном мире был и я. Я пережил эти ужасные события без особого труда, у нас был свой дачный домик, где я сидел и смотрел, как горит огонь в печи и рядом со мной сидит маленький человечек, очень сильно похожий на меня. "
    th "Это мой сын? Или просто мальчишка, очень похожий на меня? Это не могло быть моим прошлым."
    th "Неужели это сон будущего? Или же просто моя фантазия решила подарить мне странный сон, чтобы время летело быстрее?"
    "Ответ на этот вопрос я, к сожалению, не узнаю никогда."
    "Вскоре я услышал горн на обед и почувствовал, что меня толкали в плечо."
    un "Эй, сладкая парочка, просыпайтесь!"
    stop music fadeout 2
    play ambience ambience_int_cabin_day fadein 2
    hide blink
    show unblink
    "Я открыл глаза."
    show sl sad pioneer close:
        xcenter 0.90 ycenter 0.50
    show un cry_smile pioneer at center
    show se normal:
        xcenter 0.12 ycenter 0.50
    show mz shy glasses pioneer at left
    with dissolve
    "Возле меня спала Славя."
    th "Так близко…"
    "Я сразу же покраснел."
    sl "А, уже обед?"
    "Лениво потягиваясь сказала она."
    show mz smile glasses pioneer at left with dspr
    mz "Да, пока вы спали, мы всё для похода приготовили."
    me "Раньше это делала всегда Славя, но теперь ей нужно отдохнуть хотя бы раз по-настоящему."
    show sl shy pioneer close:
        xcenter 0.90 ycenter 0.50
    with dspr
    "Славя хотела сделать недовольное лицо, но прикоснувшаяся моя рука к её руке сразу разрушила все её планы."
    scene ext_library_day
    show sl normal pioneer:
        xcenter 0.90 ycenter 0.50
    show un smile pioneer at center
    show se normal:
        xcenter 0.12 ycenter 0.50
    show mz normal glasses pioneer at left
    with dissolve
    stop ambience fadeout 2
    play ambience ambience_camp_center_day fadein 2
    "Мы все вышли из библиотеки и направились в столовую."
    scene ext_dining_hall_away_day
    show sl normal pioneer:
        xcenter 0.90 ycenter 0.50
    show un smile pioneer at center
    show se normal:
        xcenter 0.12 ycenter 0.50
    show mz normal glasses pioneer at left
    with dissolve
    "Подойдя к столовой, Лена сразу же обратила на себя наше внимание."
    un "За наше место не волнуйтесь. Там уже Шурик сидит."
    me "Оперативно вы."
    scene ext_dining_hall_near_day
    show sl normal pioneer:
        xcenter 0.90 ycenter 0.50
    show un smile pioneer at center
    show se normal:
        xcenter 0.12 ycenter 0.50
    show mz normal glasses pioneer at left
    with dissolve
    un "Я просто тоже захотела чуток поспать."
    "Мы зашли в столовую."
    scene int_dining_hall_day with dissolve
    stop ambience fadeout 2
    play ambience ambience_dining_hall_empty fadein 2
    "Слова Лены оказались правдой. Шурик действительно занял для нас столик и даже, как он сказал, отогнал Электроника."
    scene bg int_dining_hall_day
    show sl normal pioneer:
        xcenter 0.90 ycenter 0.50
    show sh normal pioneer at center
    show un smile pioneer:
        xcenter 0.74 ycenter 0.50
    show se normal:
        xcenter 0.12 ycenter 0.50
    show mz normal glasses pioneer at left
    with dissolve
    "Мы все подсели к нему."
    "На обед у нас был борщ и компот."
    me "Что он хотел?"
    sh "Поговорить. Я ему сказал: «Хочешь поговорить, завтра всё обсудим»."
    mz "Не нравится мне всё это."
    ki "Так, ребятки, давайте мы сейчас не будем друг другу аппетит портить. А то нам ещё до завтрака надо будет продержаться."
    show sl smile pioneer:
        xcenter 0.90 ycenter 0.50
    with dspr
    sl "Ну почему же? Нам разрешат взять с собой булочки и термос чая."
    show un cry_smile pioneer:
        xcenter 0.74 ycenter 0.50
    with dspr
    un "Как будто вчерашний пикник."
    show un smile pioneer:
        xcenter 0.74 ycenter 0.50
    with dspr
    show sh normal_smile pioneer at center with dspr
    sh "Только меня с вами не было."
    ki "Ничего, мы не кусаемся."
    show sl laugh pioneer:
        xcenter 0.90 ycenter 0.50
    show sh normal_smile pioneer at center
    show un laugh pioneer:
        xcenter 0.74 ycenter 0.50
    show se smile:
        xcenter 0.12 ycenter 0.50
    show mz laugh glasses pioneer at left
    with dspr
    "Мы все посмеялись."
    show sl normal pioneer:
        xcenter 0.90 ycenter 0.50
    show sh normal pioneer at center
    show un smile pioneer:
        xcenter 0.74 ycenter 0.50
    show se normal:
        xcenter 0.12 ycenter 0.50
    show mz bukal glasses pioneer at left
    with dspr
    mz "Все наши сумки уже у Слави на складе. Сходите, парни, возьмёте их, и пойдём в поход."
    show sl smile2 pioneer:
        xcenter 0.90 ycenter 0.50
    with dspr
    sl "А может, мне с ними?"
    mz "Хватит переживать так за свой склад. Тем более, там будет Кирилл. Хочешь, можешь даже ему ключи от склада отдать."
    sl "А я ведь так и сделаю."
    un "Мы тогда вас подождём на площади."
    play sound sfx_keys_rattle
    "Славя отдала мне ключи от склада."
    ki "Обещаю вернуть их в целости и сохранности."
    un "Отлично, теперь давайте есть."
    "Дальше мы решили пообедать молча."
    "Закончив есть, мы вышли со столовой."
    scene ext_dining_hall_near_day
    show se normal at right
    show sh normal pioneer at left
    with dissolve
    stop ambience fadeout 2
    play ambience ambience_camp_center_day fadein 2
    "Оказавшись на улице все стали расходится по своим местам."
    scene ext_depot
    show se normal at right
    show sh normal pioneer at left
    with dissolve
    "Мы втроём пришли на склад и открыли дверь."
    scene int_depot with dissolve
    show se normal at right
    show sh normal pioneer at left
    with dissolve
    play sound sfx_open_door_1
    stop ambience fadeout 2
    "Так, у нас были два пакета и одна сумка."
    "По тяжести они все были одинаковы, поэтому было без разницы кто, что возьмёт с собой."
    "Каждый взял себе по грузу и вышел со склада."
    scene ext_depot
    show se normal at right
    show sh normal pioneer at left
    with dissolve
    play ambience ambience_camp_center_day fadein 2
    play sound sfx_close_door_1
    "Закрыв склад, мы пошли на площадь."
    scene ext_houses_day
    show se normal at right
    show sh normal pioneer at left
    with dissolve
    sh "Нам Ольга-то разрешила отдельно быть от всех?"
    ki "Да, мы со Славей специально на линейке задержались."
    me "Это здорово. Но Шурику придётся рассказать о себе кое-что."
    ki "Но он о нас ничего не знает."
    me "А мы повторим процедуру, как раз это тоже поможет скоротать время."
    scene ext_square_day
    show se normal at right
    show sh normal pioneer at left
    with dissolve
    "Мы пришли на площадь."
    hide se
    hide sh
    show mt normal panama pioneer
    with dissolve
    "Все уже стояли и ждали команды от вожатой, которая стояла прямо перед нами."
    mt "Так, пионеры! Становись!"
    "Мы все встали, как на линейку. Только с нами ещё был младший отряд."
    mt "Слушать мою команду! По парам разбиться: мальчик – девочка и выстраиваемся в колонну за мной. Кирилл и Славя замыкают колонну."
    th "Как удачно попались."
    th "Или же это специальное решение Ольги Дмитриевны?"
    th "Не важно…"
    show sl smile pioneer close at fleft with dissolve
    "Мы переглянулись друг с другом и оба улыбнулись и взялись за ручку."
    mt "Костёр без меня или Славяны не разводить. А теперь, за мной шагом марш!"
    hide mt with dissolve
    scene ext_path_day with dissolve
    stop ambience fadeout 2
    play ambience ambience_forest_day fadein 2
    "И ребята, все как один, отправились за вожатой в путь. Наша команда из шести человек шла последней."
    show sh normal pioneer far at right
    show un normal pioneer far at left
    with dissolve
    "Шурик шёл в паре с Леной."
    hide sh
    hide un
    show mz laugh glasses pioneer at left
    show se smile at right
    with dissolve
    "Женя с Семёном."
    hide mz
    hide se
    show sl smile pioneer close at left
    with dissolve
    sl "Хоть какое-то разнообразие, а то устала в походе быть на одном и том же месте."
    ki "Такое ощущение, что после моего приезда в твоей жизни настали одни плюсы."
    show sl smile2 pioneer close at left with dspr
    "Она хитро посмотрела на меня."
    sl "Всё возможно."
    show sl surprise pioneer close at left with dspr
    "Славя шла неаккуратно, запнулась и чуть не упала. Благо я рядом был и вовремя среагировал."
    "Её плечи лежат на моих руках и очень лениво они подняли хозяйку в стоячее положение."
    show sl shy pioneer close at left with dspr
    sl "С-спасибо."
    ki "Не дам я тебе упасть."
    "Она тихонько хихикнула."
    "Нам пришлось чуть ускорить свой шаг, чтобы догнать ребят."
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    stop ambience fadeout 2
    play ambience ambience_forest_evening fadein 2
    scene ext_polyana_sunset with dissolve
    "Придя на первую поляну, Ольга Дмитриевна дала нам жестом понять, что мы можем идти, а сама стала заниматься своим отрядом."
    "…"
    show black with dissolve
    hide black with dissolve
    "Мы же прошли ещё минуту и оказались на своей поляне."
    show sl normal pioneer with dissolve
    sl "Итак, ребятки, значит, действуем так: мальчики ищут дрова и хворост, мы подготавливаем место для привала. Как они соберут хворост, я разведу костёр."
    hide sl
    show sh normal pioneer at right
    show se normal at left
    with dissolve
    "Мы отправились собирать хворост и дрова."
    scene ext_forest_sunset
    show sh normal pioneer at right
    show se normal at left
    with dissolve
    sh "Как думаете, что будет завтра?"
    me "Уверен, нас раскидают по объектам. Я слышал только, что Виоле надо куда-то уехать до вечера, и кто-то вместо неё с утра дежурить будет. "
    ki "Если верить слухам, Ольга хочет чтобы мы завтра последний день плотно поработали, а всем остальным будут заниматься потом младшие отряды."
    me "То есть через день..."
    ki "Старший отряд хочет освободить от всех видов работ, перед последним днём пребывания в лагере."
    "Парней обрадовало моё дополнение к высказыванию Семёна."
    show sh normal_smile pioneer at right
    show se smile at left
    with dspr
    me "Это же просто замечательно!"
    sh "Согласен!"
    ki "Аналогично."
    show sh normal pioneer at right
    show se normal at left
    with dspr
    sh "Ладно, думаю, мы достаточно набрали хвороста для костра, давайте возвращаться."
    scene ext_polyana_sunset
    show sl normal pioneer far:
        xcenter 0.90 ycenter 0.50
    show sh normal pioneer at center
    show un smile pioneer far:
        xcenter 0.74 ycenter 0.50
    show se normal:
        xcenter 0.12 ycenter 0.50
    show mz normal glasses pioneer far at left
    with dissolve
    stop ambience fadeout 2
    play music music_list["dance_of_fireflies"] fadein 2
    "Мы вернулись назад."
    "Девушки уже всё приготовили, и сидели, разговаривая о чём-то своём."
    show sl normal pioneer:
        xcenter 0.90 ycenter 0.50
    show un smile pioneer:
        xcenter 0.74 ycenter 0.50
    show mz normal glasses pioneer at left
    with dissolve
    ki "А вот и мы! Славя, твой выход!"
    show sl smile pioneer:
        xcenter 0.90 ycenter 0.50
    with dspr
    "Девушка молча кивнула и подошла к месту возведения костра."
    sl "Сюда кладите."
    "У неё с собой были спички и немного бензина. Она аккуратно вылила пару капель и подожгла костёр."
    "Мы присели вокруг."
    scene ext_polyana_sunset with dissolve
    window hide
    pause(1)
    $ set_mode_nvl()
    nvl show dissolve
    ki_nvl "А теперь, Шурик должен пройти просвещение. А именно, мы вчера все рассказывали, чем увлекаемся и кем хотим стать."
    "Каждый повторил свой рассказ с острова. Некоторые кое-что добавляли, другие что-то умолчали."
    sh "Я понял. Ну, ладно. Я очень люблю инженерию, физику и информатику. Меня так и тянет к созданию чего-нибудь нового. Хочу выучиться на инженера-конструктора и создавать какие-нибудь классные вещи, которые будут улучшать и упрощать человеческую жизнь."
    sh "Люблю плавать, читать книги, изучать что-то новое."
    me "Ну, вот, другое дело, теперь ты – наш человек!"
    "Дальше время шло очень быстро."
    "Мы разговаривали на различные темы."
    "Рассказывали друг другу истории из нашей бурной юношеской жизни."
    "Играли в карты, где чаще всего победителем выходил либо я, либо Семён."
    "Обсуждали различную музыку."
    th "Никогда не подумал бы, что Алисе и Лене нравится одна и та же музыка. Только художница скрывает это очень активно."
    "Всё это мы делали на фоне горящего костра, поедая вкусные булочки из столовой."
    "Если бы мы взяли палатку, то можно было бы тут даже заночевать. Прекрасное место! Да и компания душевная и искренняя у нас."
    "Славя призналась, что впервые видит таких Лену и Женю. Она никогда не видела, чтобы Лена так легко общалась и так часто улыбалась, тоже самое касалось и Жени. Ведь Женя часто всем дерзила и хамила. Даже могла посоревноваться в этом плане с Алисой и, наверное, выиграла бы."
    "Семён стал развлекать всех длинным рассказом, а для нас со Славей это стало отличным поводом, чтобы уединиться. Да и Славя, наверняка, устала."
    nvl hide dissolve
    pause(1)
    $ set_mode_adv()
    window show
    show sl normal pioneer with dissolve
    ki "Ты устала? Может, пойдём домой?"
    sl "А как же ребята?"
    ki "Думаю, они сами скоро пойдут."
    "Я взял один из наших пакетов."
    sl "Да, пойдём домой. Поговорим там."
    ki "Может, тебя на руках понести?"
    show sl happy pioneer with dspr
    "Она тихонько захихикала и начала потихоньку краснеть."
    show sl shy pioneer with dspr
    sl "Не стоит, правда. Я не до такой степени уставшая."
    "Я махнул рукой Семёну, что мы ушли."
    window hide
    $ night_time()
    $ persistent.sprite_time = "night"
    stop music fadeout 2
    play ambience ambience_forest_night fadein 2
    scene ext_path_night
    show sl smile pioneer close
    with dissolve
    window show
    "Мы шли аккуратно. Было не так светло, но дорогу мы видели."
    "Я решил не отпускать руку Слави, пока не дойдём до дома, так как один раз она чуть не упала."
    th "Нет уж, упасть я тебе не позволю."
    "Мы молча шли до домика."
    stop ambience fadeout 2
    play ambience ambience_camp_center_night fadein 2
    scene ext_house_of_sl_night
    show sl normal pioneer
    with dissolve
    "Дойдя до нашего место проживания, Славя сделала шаг вперёд, а я отпустил её руку и остался стоять на месте."
    ki "Так, ты пока переоденься в ночнушку, или в чем ты спишь, а потом меня позовёшь."
    sl "Ладно."
    hide sl with dissolve
    play sound sfx_open_door_1
    "Она вошла в домик. "
    "Сейчас попробую хотя бы начать этот разговор. А завтра продолжить. Ко дню танцев я должен уже выяснить, взаимны ли наши чувства."
    "Или же это обычная симпатия и не более."
    sl "Заходи."
    scene int_house_of_sl_light_night with dissolve
    play sound sfx_open_door_1
    stop ambience fadeout 2
    "Услышав голос своей соседки, я зашёл в помещение."
    "Оказавшись внутри, было сразу видно, что Славя уже лежит под одеялом и смотрит на потолок."
    "Первым делом я быстренько разделся и укутался в одеяло, чтобы не смущать Славю."
    sl "Так о чём ты хотел поговорить?"
    ki "Славя, я не знаю, правильно ли я поступаю. Может, я вообще сую нос не в своё дело…"
    scene int_house_of_sl_night with dissolve
    play sound turning_on_light
    play music music_list["blow_with_the_fires"] fadein 2
    "Я волновался и выключил свет в домике, перед тем, как снова сесть на свою кровать."
    sl "Я всё выслушаю спокойно."
    ki "Скажи мне, пожалуйста, тебе кто-то нравится из нашей школы?"
    sl "Ну, есть один молодой человек. Правда, он не всегда замечает мои намёки. Или может, я неправильно их подаю?"
    ki "Хорошо, понял. Ну, спрашивать кто он – довольно грубо будет, а?"
    sl "Я могу только дать тебе подсказку."
    ki "Ну, давай."
    sl "Он добрый и необщительный, всегда помогает и не требует ничего взамен. Готов пожертвовать своим здоровьем и не даст тебе упасть. Постарается удержать в настроении тебя, даже если у самого настроение плохое."
    ki "Сколько у меня времени на разгадку этого ребуса?"
    sl "Завтра перед умывальниками спрошу, догадался или нет. Доброй ночи, соседушка!"
    ki "Сладких снов!"
    "Я лёг на кровать и задумался."
    th "Неужели у неё кто-то есть? Но кто? В нашем классе мало добрых парней было, и то, в основном, все общительные. Помогает и не требует ничего взамен... Ну, есть такие… точнее, делают вид, что такие."
    "Но тем временем где-то там, в глубине, тускло светилась маленькая искорка. Пусть и маленькая, она слегка кидала щёки в жар, не давала спокойно уснуть, хоть меня очень сильно тянуло в сон…"
    th "Так, ладно, я поставлю свой будильник на пять минут позже, чем просыпается Славя и подумаю лучше утром на свежую голову."
    "Утро вечера мудренее."
    "Именно на этой ноте я и уснул."
    stop music fadeout 2
    jump Four_horizons_Kirril_story_day5
