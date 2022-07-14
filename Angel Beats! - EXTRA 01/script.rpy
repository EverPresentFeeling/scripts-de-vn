



image movie = Movie(size=(320, 240), xpos=475, ypos=50, xanchor=0, yanchor=0)





label splashscreen:
    $ show_button_game_menu = False
    $ renpy.pause(0, hard=True)
    scene bg black01
    show text "Angel Beats! Visual Project presenta:"
    with fade
    with Pause(1.2)
    scene bg black01
    show text "Una historia de Angel Beats!"
    with fade
    with Pause(1.2)
    scene bg black01
    show text "Disfrútala..."
    with fade
    with Pause(0.5)

    $ renpy.pause(0, hard=True)
    scene title
    with fade
    with Pause(1.2)

    $ renpy.pause(0.5, hard=True)
    show title2
    hide text
    with dissolve

    return





init:
    $ e = Character(" ",
                        color="#c8ffc8",
                        what_slow_cps=70)
    $ e2 = Character("???????? ",
                        color="#c8ffc8",
                        what_slow_cps=70)
    $ everyone = Character("Everyone",
                        color="#c8ffc8",
                        what_slow_cps=70)
    $ K = Character("Kinoshita ",
                        color="#c8ffc8",
                        what_slow_cps=70)
    $ H = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70)
    $ H1 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako01.png", xalign=0.0, yalign=1.0))
    $ H2 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako02.png", xalign=0.0, yalign=1.0))
    $ H3 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako03.png", xalign=0.0, yalign=1.0))
    $ H4 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako04.png", xalign=0.0, yalign=1.0))
    $ H5 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako05.png", xalign=0.0, yalign=1.0))
    $ H6 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako06.png", xalign=0.0, yalign=1.0))
    $ H7 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako07.png", xalign=0.0, yalign=1.0))
    $ H8 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako08.png", xalign=0.0, yalign=1.0))
    $ H9 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako09.png", xalign=0.0, yalign=1.0))
    $ H10 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako10.png", xalign=0.0, yalign=1.0))
    $ H11 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako11.png", xalign=0.0, yalign=1.0))
    $ H12 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako12.png", xalign=0.0, yalign=1.0))
    $ H13 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako13.png", xalign=0.0, yalign=1.0))
    $ H14 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako14.png", xalign=0.0, yalign=1.0))
    $ H15 = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Hisako15.png", xalign=0.0, yalign=1.0))
    $ I = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=70)
    $ I1 = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Iwasawa01.png", xalign=0.0, yalign=1.0))
    $ I2 = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Iwasawa02.png", xalign=0.0, yalign=1.0))
    $ I3 = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Iwasawa03.png", xalign=0.0, yalign=1.0))
    $ I4 = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Iwasawa04.png", xalign=0.0, yalign=1.0))
    $ I5 = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Iwasawa05.png", xalign=0.0, yalign=1.0))
    $ I6 = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Iwasawa06.png", xalign=0.0, yalign=1.0))
    $ S = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70)
    $ S1 = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Sekine01.png", xalign=0.0, yalign=1.0))
    $ S2 = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Sekine02.png", xalign=0.0, yalign=1.0))
    $ S3 = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Sekine03.png", xalign=0.0, yalign=1.0))
    $ S4 = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Sekine04.png", xalign=0.0, yalign=1.0))
    $ S5 = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Sekine05.png", xalign=0.0, yalign=1.0))
    $ S6 = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Sekine06.png", xalign=0.0, yalign=1.0))
    $ S7 = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Sekine07.png", xalign=0.0, yalign=1.0))
    $ IR = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=70)
    $ IR1 = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Irie01.png", xalign=0.0, yalign=1.0))
    $ IR2 = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Irie02.png", xalign=0.0, yalign=1.0))
    $ IR3 = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Irie03.png", xalign=0.0, yalign=1.0))
    $ IR4 = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Irie04.png", xalign=0.0, yalign=1.0))
    $ IR5 = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Irie05.png", xalign=0.0, yalign=1.0))
    $ IR6 = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Irie06.png", xalign=0.0, yalign=1.0))
    $ Hslow = Character("Hisako",
                        color="#9E3F00",
                        what_slow_cps=50)
    $ Islwo = Character("Iwasawa",
                        color="#AF446E",
                        what_slow_cps=50)
    $ Sslow = Character("Sekine",
                        color="#FCB573",
                        what_slow_cps=50)
    $ IRslow = Character("Irie",
                        color="#9479BC",
                        what_slow_cps=50)
    $ F = Character("Fujimaki",
                        color="#7F7F7F",
                        what_slow_cps=70)
    $ F1 = Character("Fujimaki",
                        color="#7F7F7F",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Fujimaki01.png", xalign=0.0, yalign=1.0))
    $ F2 = Character("Fujimaki",
                        color="#7F7F7F",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Fujimaki02.png", xalign=0.0, yalign=1.0))
    $ F3 = Character("Fujimaki",
                        color="#7F7F7F",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Fujimaki03.png", xalign=0.0, yalign=1.0))
    $ F4 = Character("Fujimaki",
                        color="#7F7F7F",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("Fujimaki04.png", xalign=0.0, yalign=1.0))
    $ O = Character("Ooyama",
                        color="#90576A",
                        what_slow_cps=70)
    $ O1 = Character("Ooyama",
                        color="#90576A",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("oyyama01.png", xalign=0.0, yalign=1.0))
    $ O2 = Character("Ooyama",
                        color="#90576A",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("oyyama02.png", xalign=0.0, yalign=1.0))
    $ O3 = Character("Ooyama",
                        color="#90576A",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("oyyama03.png", xalign=0.0, yalign=1.0))
    $ O4 = Character("Ooyama",
                        color="#90576A",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("oyyama04.png", xalign=0.0, yalign=1.0))
    $ TK = Character("T.K.",
                        color="#E10000",
                        what_slow_cps=70)
    $ TK1 = Character("T.K.",
                        color="#E10000",
                        what_slow_cps=70,
                        window_left_padding=160,
                        show_side_image=Image("TK01.png", xalign=0.0, yalign=1.0))

    $ subtitle = Character(None,
                            what_size=28,
                            what_outlines=[(3, "#F3F1F2", 2, 2), (3, "#F3F1F2", 0, 0)],
                            what_layout="subtitle",
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5)





    image bg black01 = "Blackout 01.jpg"
    image title = "title.jpg"
    image title2 = "title2.jpg"
    image bg Concerthall = "Concert hall.jpg"
    image bg Emptyclassroom = "Empty classroom.jpg"
    image bg corridoor1 = "Corridor - Day - 01.jpg"
    image bg corridoor2 = "Corridor - Day - 02.jpg"
    image bg corridoor3 = "Corridor - Day - 03.jpg"
    image bg class1 = "Classroom - Day - 15.jpg"
    image bg window1 = "Window - 01.jpg"
    image bg irie = "Irie.jpg"
    image bg Chapter = "Chapter.jpg"
    image bg ground01 = "ground01.jpg"
    image bg ground02 = "ground02.jpg"
    image bg ground03 = "ground03.jpg"
    image bg ground04 = "ground04.jpg"
    image GDM = "GDM.jpg"
    image bg sekine = "Sekine Introduction.jpg"
    image bg sekine2 = "Sekine Introduction 2.jpg"
    image bg sekine3 = "Sekine Introduction 3.jpg"
    image bg sunset01 = "sunset01.jpg"
    image bg sunset02 = "sunset02.jpg"
    image oyamaowned = "Oyamaowned.jpg"
    image bg Iwasawa = "Iwasawa.jpg"
    image bg dorm = "dormsekine.jpg"
    image bg outside = "outsideband.jpg"
    image bg gang = "gang.jpg"





    image Hisako = "Hisako.png"
    image Hisakohng = "Hisakohng.png"
    image Hisakohuh = "Hisakohuh.png"
    image Hisakolargemouth = "Hisakolargemouth.png"
    image Hisakooh = "Hisakooh.png"
    image Hisakosmile = "Hisakosmile.png"
    image Hisakotalk = "Hisakotalk.png"
    image Hisako2 = "Hisako2.png"
    image Hisakohng2 = "Hisakohng2.png"
    image Hisakohuh2 = "Hisakohuh2.png"
    image Hisakolargemouth2 = "Hisakolargemouth2.png"
    image Hisakooh2 = "Hisakooh2.png"
    image Hisakosmile2 = "Hisakosmile2.png"
    image Hisakotalk2 = "Hisakotalk2.png"

    image Sekine = "Sekine.png"
    image Sekinegeh = "Sekinegeh.png"
    image Sekinesad = "Sekinesad.png"
    image Sekinesmile = "Sekinesmile.png"
    image Sekinetalk = "Sekinetalk.png"
    image Sekinetalkangry = "Sekinetalkangry.png"
    image Sekineyellangry = "Sekineyellangry.png"
    image Sekinesuprised = "Sekinesuprised.png"
    image Sekine2 = "Sekine2.png"
    image Sekinegeh2 = "Sekinegeh2.png"
    image Sekinesad2 = "Sekinesad2.png"
    image Sekinesmile2 = "Sekinesmile2.png"
    image Sekinetalk2 = "Sekinetalk2.png"
    image Sekinetalkangry2 = "Sekinetalkangry2.png"
    image Sekineyellangry2 = "Sekineyellangry2.png"
    image Sekinesuprised2 = "Sekinesuprised2.png"
    image Sekineangry = "Sekineangry.png"
    image Sekineangry2 = "Sekineangry2.png"

    image Irie = "Irie.png"
    image Iriehuh = "Iriehuh.png"
    image Iriesad = "Iriesad.png"
    image Iriesmile = "Iriesmile.png"
    image Iriesmileb = "Iriesmileb.png"
    image Irietalk = "Irietalk.png"
    image Irie2 = "Irie2.png"
    image Iriehuh2 = "Iriehuh2.png"
    image Iriesad2 = "Iriesad2.png"
    image Iriesmile2 = "Iriesmile2.png"
    image Iriesmileb2 = "Iriesmileb2.png"
    image Irietalk2 = "Irietalk2.png"
    image Iriehappytalk = "Iriehappytalk.png"
    image Iriehappytalk2 = "Iriehappytalk2.png"
    image Iriehuhb = "Iriehuhb.png"
    image Iriehuhb2 = "Iriehuhb2.png"

    image Iwasawa = "Iwasawa.png"
    image Iwasawasmile = "Iwasawasmile.png"
    image Iwasawahappy = "Iwasawahappy.png"
    image Iwasawacool = "Iwasawacool.png"
    image Iwasawatalk = "Iwasawatalk.png"

    image TK = "TK.png"
    image TKyell = "TKyell.png"
    image TK2 = "TK2.png"
    image TKyell2 = "TKyell2.png"

    image oyama = "Oyama.png"
    image Oyamageh = "Oyamageh.png"
    image Oyamahm = "Oyamahm.png"
    image Oyamatalk = "Oyamatalk.png"

    image fujimaki = "Fujimaki.png"
    image Fujimakisad = "Fujimakisad.png"
    image Fujimakihah = "Fujimakihah.png"
    image Fujimaki2 = "Fujimaki2.png"
    image Fujimakisad2 = "Fujimakisad2.png"
    image Fujimakihah2 = "Fujimakihah2.png"                





label start:
    stop music

    window hide

    scene bg black01
    with fade

    window show dissolve
    $ show_button_game_menu = True
    with dissolve

    e "Angel Beats! Visual Project presenta:"

    e "Un proyecto traducido por Ever Present Feeling."

    e "Capítulo Extra 01: Girl's Dead Monster."

    e "Disfrútenlo."

    window hide dissolve
    $ show_button_game_menu = False
    with dissolve

    scene bg Chapter
    with fade

    subtitle "..."

    scene bg black01
    with fade



    scene bg ground01
    with fade

    $ result = renpy.imagemap("ground01.jpg", "hover.jpg", [
        (88, 454, 200, 495, "Sekine"),
        ], focus="imagemap")





    if result == "Sekine":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        window show dissolve
        $ show_button_game_menu = True
        with dissolve

        Sslow "... ...... ............"

        S3 "Ummm..."

        S7 "¿Por dónde debería empezar?"

        S1 "¿Qué de que habló? "

        S1 "De mis compañeras de Girls Dead Monster. A veces nos hacemos llamar Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabías, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mía y de nadie más."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compañeras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un día le dije en broma a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''¡Esas dos son unas monstruos! ¡Huye, Miyukichi! Escapa cómo puedas, ¡no te preocupes por mí!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzó a formar parte de nuestra banda."

        S7 "Supongo que también puedo hablar un poco más de las otras miembros..."

        S1 "Honestamente, espero que disfrutes lo que estoy por contarte."

        S3 "..."

        S2 "¿Empezamos?"

        S "Comencemos con Hisako-senpai."

    window hide





label set2:

    $ renpy.block_rollback()    

    scene bg black01
    with fade

    e "Seleccionar Historia."

    window hide None

    $ result = renpy.imagemap("ground02.jpg", "hover.jpg", [
        (88, 454, 200, 495, "Sekine"),
        (270, 344, 376, 392, "Hisako"), 
        ], focus="imagemap")

    window show None





    if result == "Sekine":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        window show dissolve
        $ show_button_game_menu = True
        with dissolve

        Sslow "... ...... ............"

        S3 "Ummm..."

        S7 "¿Por dónde debería empezar?"

        S1 "¿Qué de que habló? "

        S1 "De mis compañeras de Girls Dead Monster. A veces nos hacemos llamar Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabías, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mía y de nadie más."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compañeras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un día le dije en broma a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''¡Esas dos son unas monstruos! ¡Huye, Miyukichi! Escapa cómo puedas, ¡no te preocupes por mí!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzó a formar parte de nuestra banda."

        S7 "Supongo que también puedo hablar un poco más de las otras miembros..."

        S1 "Honestamente, espero que disfrutes lo que estoy por contarte."

        S3 "..."

        jump set2





    elif result == "Hisako":

        $ renpy.block_rollback()    

        play music "04 - girl's hop.mp3" fadeout 1.0 fadein 1.0

        S1 "Primero se las presentaré."

        S1 "Está es Hisako-senpai."

        S1 "Y cómo puedes intuir, es mi superior."

        S1 "Hisako es la guitarrista principal de nuestra banda."

        S1 "Puede parecer extraño, pero tiene un pequeño problema:"

        S1 "Ella es una jugadora compulsiva."

        S7 "Para ser más específica: es una jugadora compulsiva... que hace trampas."

        S7 "Un día tuve mucha suerte y pude ver con mis propios ojos lo habilidosos que eran sus trucos."

        scene bg sunset02
        with fade

        S "Ese día estaba jugando a las escondidas con Miyukichi. Me había encerrado en un casillero."

        S "El sol estaba comenzando a ocultarse, así que comencé a preguntarme si debía salir."

        scene bg black01

        stop music fadeout 1.0

        play sound "bosu36.wav" 

        e "*GOLPE*" with vpunch

        scene bg sunset01
        with dissolve

        S "Las luces se encendieron. Y, una voz muy familiar entró al salón y dijo:"

        play sound "bosu36.wav" 

        e2 "¡Hagámoslo!" with vpunch

        S "Y se sentó cerca de una mesa."

        S "Yo pude verlo todo desde las ventilas del casillero."

        S "Me quedé encerrada, no quería salir del casillero delante de tanta gente como si fuese lo más normal del mundo."

        S "No lo sabía en ese momento, pero esa iba a ser la primera vez que vería el lado más divertido de Hisako."

        S "Los cuatro que estaban sentados alrededor de la mesa eran Fujimaki, TK, Ooyama, y Hisako. "

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S "Ellos comenzaron mezclando y repartiendo las tablas de Mahjong."

        S "Las reglas del Mahjong son simples, tienen que formar una mano en la que tengan un par de tablas que sean iguales, y cuatro grupos de tres tablas iguales."

        S "El primero en formar una mano completa, gana. El ganador puede juntar los puntos de todos los demás."

        S "Siendo honesta, no sé mucho de Mahjong. Aún hay muchas reglas que se me escapan."

        show Hisakotalk at right with dissolve

        H13 "¡Empecemos!"

        hide Hisakotalk
        show Hisako at right

        S "Hisako formó una jugada de mil puntos en la mesa, mostrando que estaba a una tabla de formar una mano completa."

        show Fujimaki2 at left with dissolve

        F2 "Bien… ¡Vamos! "

        hide Hisako with dissolve
        show Hisako2 at right with dissolve

        H14 "Gano por pura suerte, tan simple que solo necesité un tiro."

        H14 "Oh, con esta Dora, todos los puntos van para mí. "

        hide Hisako2
        show Hisakohng2 at right

        S "Fue como una pequeña guerra."

        S "Pero era obvio que la mano de Hisako no tenía suficientes tablas."

        S "Debería de haber trece, pero ella solo tenía diez."

        S "Escondiendo las otras tres en su mano, ganó formando tres filas en vez de cuatro."

        hide Fujimaki2
        show Fujimakihah2 at left 

        F3 "Tsk… Mierda."

        hide Fujimakihah2 with fade

        hide Hisakohng2
        show Hisako2 at right

        S "Fujimaki fue tan idiota que no se dio cuenta."

        stop music fadeout 1.0

        S "Solo le quedó juntar sus pequeñas tablas con obediencia."

        S "La estrategia de Hisako era imbatible."

        S "Haciendo eso, siempre formaría una mano mucho más rápido que cualquiera."

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        show TK2 at left with dissolve

        hide Hisako2 with dissolve
        show Hisakosmile at right with dissolve

        H13 "Terminé. Bien, gané descartando. Ni un solo puntero, más la Dora que está en el medio."

        H14 "Ah, saqué el máximo otra vez."

        hide TK2
        show TKyell2 at left

        play sound "bosu36.wav"

        TK1 "¡Ah! ¡Fuck me! " with vpunch

        S "TK fue un poco idiota también, así que tampoco se percató de ello."

        S "No sé mucho de inglés, pero... para que TK diga eso, estoy segura que se enojó muchísimo."

        stop music fadeout 1.0

        hide TKyell2 with fade

        show oyama at left with dissolve

        O2 "Terminé. "

        hide Hisakosmile
        show Hisakohuh2 at right

        play music "25 - let's operation.mp3" fadeout 1.0 fadein 1.0

        S "Aunque esa vez, Ooyama casi vence a Hisako."

        S "Tan solo llegaron al tercer turno, pero..."

        S "No podía ganar incluso teniendo solo diez fichas en la mesa."

        S "Entonces, Hisako decidió hacer algo aún más descarado."

        S "Escondió otras tres fichas en su mano."

        S "Ahora solo quedan siete, de las cuales solo dos son puentes."

        hide Hisakohuh2 with dissolve
        show Hisakosmile at right with dissolve

        H14 "¡Yo también terminé!"

        S "Dijo sin miedo."

        S "Pero eso fue demasiado obvio. Solo tenía la mitad de las fichas a diferencia de Ooyama."

        S "Aparentemente Ooyama no lo aguantó más y se quejó de ello."

        S "Bueno, se quejó lo más fuerte que pudo hacerlo."

        hide oyama
        show Oyamatalk at left

        O1 "¿Estás segura que tienes trece fichas?"

        hide Hisakosmile
        show Hisakotalk at right

        H13 "Síp."

        hide Hisakotalk
        show Hisakosmile at right

        hide Oyamatalk
        show Oyamageh at left

        play sound "bosu36.wav"

        stop music fadeout 1.0

        O4 "… ¡¿Quééééééé?!" with vpunch

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        S "Incluso desde el casillero pude oír su grito ahogado."

        S "Pensándolo bien, el casillero era el escondite perfecto."

        S "Con una vista perfecta de toda la mesa.~"

        S "Pero como nadie más dijo nada, el pobre Ooyama se quedó quieto y tomó otra ficha."

        hide Oyamageh
        show Oyamatalk at left

        play sound "bosu36.wav" 

        O3 "¡Quiero ganar…! ¡Mierda! ¡Esta ficha no sirve! " with vpunch

        S "Pero él ya dijo que había terminado, así que no podía hacer nada."

        O3 "¡Muévete! "

        hide Oyamatalk
        show Oyamahm at left

        hide Hisakosmile with dissolve
        show Hisakosmile2 at right with dissolve

        H11 "Oh, no servirá."

        H11 "Gano por descarte."

        hide Hisakosmile2 with dissolve
        show Hisakosmile at right with dissolve

        H11 "Gané el mano a mano; todas parejas y ningún puntero. Todo en una misma cadena y con dos Doras. Ah, también hay que contar la Dora del medio… "

        H14 "¿Cuánto es eso…? "

        H13 "Un múltiplo de trece, ¿eh? Un nuevo máximo, ja. "

        stop music fadeout 1.0

        hide Oyamahm with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamahm at center with dissolve

        F2 "Oh, por Dios… Eso fue genial, Hisako… "

        S "Fujimaki quedó absolutamente asombrado. "

        hide Fujimakihah2 with dissolve
        hide Oyamahm with dissolve

        show Oyamatalk at left with dissolve

        O1 "¡Espera, espera un poco! ¡¿Dices que eso es genial?!"

        play sound "bosu36.wav" 

        O1 "¡Cualquiera puede hacerlo solo con siete tablas! " with vpunch

        hide Oyamatalk
        show oyama at left

        hide Hisakosmile with dissolve
        show Hisakohng2 at right with dissolve

        H12 "Te dije que son trece. En fin, juguemos otra... ¡Empecemos!"

        S "Mezcló todas las fichas en el centro para ocultar la evidencia."

        hide oyama
        show Oyamatalk at left

        O4 "¡Eres una tramposa! ¡Muy bien, yo también lo haré! ¡Terminé! "

        hide Oyamatalk
        show oyama at left

        hide Hisakohng2
        show Hisakosmile2 at right

        S "Ooyama escondió tres fichas en su mano y la atacó con nueve tablas, teniendo una fila menos que una mano completa."

        hide oyama with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamageh at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        F3 "Espera, Ooyama, maldito estúpido, ¿cuántas fichas tienes? "

        hide Oyamageh
        show oyama at center

        hide Fujimakihah2
        show Fujimakisad2 at left

        S "Fujimaki las miró y empezó a contar."

        hide Fujimakisad2
        show Fujimakihah2 at left

        F1 "¿Ves? ¡Te faltan tres! Tú no juegas más, idiota. "

        hide oyama
        hide Fujimakihah2
        show Oyamatalk at center
        show Fujimakisad2 at left

        play sound "bosu36.wav" 

        O4 "¡¿Qué demo-?! ¡¿Por qué soy el único al que le sale mal?!" with vpunch

        hide Fujimakisad2 with dissolve
        hide Oyamatalk

        show oyama at left with dissolve

        S "Fue obligado a devolver la ficha que tomó de la pila."

        hide Hisakosmile2 with dissolve
        show Hisakolargemouth at right with dissolve

        stop music fadeout 1.0

        H13 "Gané por descarte. "

        hide Hisakolargemouth
        show Hisakosmile at right

        S "Dijo Hisako. "

        O1 "¿Eh? ¿Quién ganó por descarte? "

        hide oyama
        show Oyamageh at left

        hide Hisakosmile
        show Hisakohng at right with dissolve

        H14 "Yo gané gracias a ti. "

        play sound "bosu34.wav" 

        e "*FLOP*" with vpunch

        scene oyamaowned
        with fade

        S "Ella mostró sus fichas. "

        S "Los cuatro vientos más los tres dragones. "

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        O3 "¿Qué demonios es eso…? "

        H13 "Trece deseos, el puntaje máximo pero multiplicado por dos."

        play sound "bosu36.wav" 

        O1 "¡¿Trece deseos con solo siete tablas?! ¡¿No ven que hay algo raro?!" with vpunch

        H14 "Ah, y todo en la primera mano. Entonces será por tres."

        play sound "bosu36.wav" 

        O4 "¡¿Quéééééé?! " with vpunch

        F1 "Guau… nunca vi a alguien reunir los trece deseos en la primera mano…"

        play sound "bosu36.wav" 

        O3 "¡Porque es literalmente imposible!" with vpunch

        scene bg sunset01
        with fade

        S "Y con eso, Ooyama entró en cólera… "

        show oyama at left with dissolve
        show Hisakosmile at right with dissolve

        H12 "Muy bien, entréguenme todos los boletos de comida que me deben."

        hide oyama
        show Oyamahm at left

        O4 "Oh, vamos… "

        S6 "Alguien sin misericordia, con una arrogancia en su estado más puro."

        S6 "Esa es nuestra Hisako; una embustera. La encarnación perfecta del Diablo en persona."

        stop music fadeout 1.0

        scene bg black01
        with fade

        e "¡Sigamos con Irie!"

    window hide





label set3:

    $ renpy.block_rollback()    

    scene bg black01
    with fade

    e "Seleccionar Historia."

    window hide None






    $ result = renpy.imagemap("ground03.jpg", "hover.jpg", [
        (88, 454, 200, 495, "Sekine"),
        (270, 344, 376, 392, "Hisako"), 
        (719, 443, 796, 481, "Irie"),    
        ], focus="imagemap")





    window show None





    if result == "Sekine":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        window show dissolve
        $ show_button_game_menu = True
        with dissolve

        Sslow "... ...... ............"

        S3 "Ummm..."

        S7 "¿Por dónde empiezo?"

        S1 "¿Qué de que habló?"

        S1 "De mis compañeras de Girls Dead Monster. A veces nos llamamos Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabías, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mía y de nadie más."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compañeras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un día le dije bromeando a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''¡Esas dos son unas monstruos! ¡Huye, Miyukichi! Escapa cómo puedas, ¡no te preocupes por mí!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzó a formar parte de nuestra banda."

        S3 "..."

        jump set2





    elif result == "Hisako":

        $ renpy.block_rollback()    

        play music "04 - girl's hop.mp3" fadeout 1.0 fadein 1.0

        S1 "Primero se las presentaré."

        S1 "Está es Hisako-senpai."

        S1 "Y cómo puedes intuir, es mi superior."

        S1 "Hisako es la guitarrista principal de nuestra banda."

        S1 "Puede parecer extraño, pero tiene un pequeño problema: "

        S1 "Ella es una jugadora compulsiva."

        S7 "Para ser más específica: es una jugadora compulsiva... que hace trampas."

        S7 "Un día tuve mucha suerte y pude ver con mis propios ojos lo habilidosos que eran sus trucos."

        scene bg sunset02
        with fade

        S "Ese día estaba jugando a las escondidas con Miyukichi. Me había encerrado en un casillero."

        S "El sol estaba comenzando a ocultarse, así que comencé a preguntarme si debía salir."

        scene bg black01

        stop music fadeout 1.0

        play sound "bosu36.wav" 

        e "*GOLPE*" with vpunch

        scene bg sunset01
        with dissolve

        S "Las luces se encendieron. Y, una voz muy familiar entró al salón y dijo:"

        play sound "bosu36.wav" 

        e2 "¡Hagámoslo!" with vpunch

        S "Y se sentó cerca de una mesa."

        S "Yo pude verlo todo desde las ventilas del casillero."

        S "Me quedé encerrada, no quería salir del casillero delante de tanta gente como si fuese lo más normal del mundo."

        S "No lo sabía en ese momento, pero esa iba a ser la primera vez que vería el lado más divertido de Hisako."

        S "Los cuatro que estaban sentados alrededor de la mesa eran Fujimaki, TK, Ooyama, y Hisako. "

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S "Ellos comenzaron mezclando y repartiendo las tablas de Mahjong."

        S "Las reglas del Mahjong son simples, tienen que formar una mano en la que tengan un par de tablas que sean iguales, y cuatro grupos de tres tablas iguales."

        S "El primero en formar una mano completa, gana. El ganador puede juntar los puntos de todos los demás."

        S "Siendo honesta, no sé mucho de Mahjong. Aún hay muchas reglas que se me escapan."

        show Hisakotalk at right with dissolve

        H13 "¡Empecemos!"

        hide Hisakotalk
        show Hisako at right

        S "Hisako formó una jugada de mil puntos en la mesa, mostrando que estaba a una tabla de formar una mano completa."

        show Fujimaki2 at left with dissolve

        F2 "Bien… ¡Vamos! "

        hide Hisako with dissolve
        show Hisako2 at right with dissolve

        H14 "Gano por pura suerte, tan simple que solo necesité un tiro."

        H14 "Oh, con esta Dora, todos los puntos van para mí. "

        hide Hisako2
        show Hisakohng2 at right

        S "Fue como una pequeña guerra."

        S "Pero era obvio que la mano de Hisako no tenía suficientes tablas."

        S "Debería de haber trece, pero ella solo tenía diez."

        S "Escondiendo las otras tres en su mano, ganó formando tres filas en vez de cuatro."

        hide Fujimaki2
        show Fujimakihah2 at left 

        F3 "Tsk… Mierda."

        hide Fujimakihah2 with fade

        hide Hisakohng2
        show Hisako2 at right

        S "Fujimaki fue tan idiota que no se dio cuenta."

        stop music fadeout 1.0

        S "Solo le quedó juntar sus pequeñas tablas con obediencia."

        S "La estrategia de Hisako era imbatible."

        S "Haciendo eso, siempre formaría una mano mucho más rápido que cualquiera."

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        show TK2 at left with dissolve

        hide Hisako2 with dissolve
        show Hisakosmile at right with dissolve

        H13 "Terminé. Bien, gané descartando. Ni un solo puntero, más la Dora que está en el medio."

        H14 "Ah, saqué el máximo otra vez."

        hide TK2
        show TKyell2 at left

        play sound "bosu36.wav"

        TK1 "¡Ah! ¡Fuck me! " with vpunch

        S "TK fue un poco idiota también, así que tampoco se percató de ello."

        S "No sé mucho de inglés, pero... para que TK diga eso, estoy segura que se enojó muchísimo."

        stop music fadeout 1.0

        hide TKyell2 with fade

        show oyama at left with dissolve

        O2 "Terminé. "

        hide Hisakosmile
        show Hisakohuh2 at right

        play music "25 - let's operation.mp3" fadeout 1.0 fadein 1.0

        S "Aunque esa vez, Ooyama casi vence a Hisako."

        S "Tan solo llegaron al tercer turno, pero..."

        S "No podía ganar incluso teniendo solo diez fichas en la mesa."

        S "Entonces, Hisako decidió hacer algo aún más descarado."

        S "Escondió otras tres fichas en su mano."

        S "Ahora solo quedan siete, de las cuales solo dos son puentes."

        hide Hisakohuh2 with dissolve
        show Hisakosmile at right with dissolve

        H14 "¡Yo también terminé!"

        S "Dijo sin miedo."

        S "Pero eso fue demasiado obvio. Solo tenía la mitad de las fichas a diferencia de Ooyama."

        S "Aparentemente Ooyama no lo aguantó más y se quejó de ello."

        S "Bueno, se quejó lo más fuerte que pudo hacerlo."

        hide oyama
        show Oyamatalk at left

        O1 "¿Estás segura que tienes trece fichas?"

        hide Hisakosmile
        show Hisakotalk at right

        H13 "Síp."

        hide Hisakotalk
        show Hisakosmile at right

        hide Oyamatalk
        show Oyamageh at left

        play sound "bosu36.wav"

        stop music fadeout 1.0

        O4 "… ¡¿Quééééééé?!" with vpunch

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        S "Incluso desde el casillero pude oír su grito ahogado."

        S "Pensándolo bien, el casillero era el escondite perfecto."

        S "Con una vista perfecta de toda la mesa.~"

        S "Pero como nadie más dijo nada, el pobre Ooyama se quedó quieto y tomó otra ficha."

        hide Oyamageh
        show Oyamatalk at left

        play sound "bosu36.wav" 

        O3 "¡Quiero ganar…! ¡Mierda! ¡Esta ficha no sirve! " with vpunch

        S "Pero él ya dijo que había terminado, así que no podía hacer nada."

        O3 "¡Muévete! "

        hide Oyamatalk
        show Oyamahm at left

        hide Hisakosmile with dissolve
        show Hisakosmile2 at right with dissolve

        H11 "Oh, no servirá."

        H11 "Gano por descarte."

        hide Hisakosmile2 with dissolve
        show Hisakosmile at right with dissolve

        H11 "Gané el mano a mano; todas parejas y ningún puntero. Todo en una misma cadena y con dos Doras. Ah, también hay que contar la Dora del medio… "

        H14 "¿Cuánto es eso…? "

        H13 "Un múltiplo de trece, ¿eh? Un nuevo máximo, ja. "

        stop music fadeout 1.0

        hide Oyamahm with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamahm at center with dissolve

        F2 "Oh, por Dios… Eso fue genial, Hisako… "

        S "Fujimaki quedó absolutamente asombrado. "

        hide Fujimakihah2 with dissolve
        hide Oyamahm with dissolve

        show Oyamatalk at left with dissolve

        O1 "¡Espera, espera un poco! ¡¿Dices que eso es genial?!"

        play sound "bosu36.wav" 

        O1 "¡Cualquiera puede hacerlo solo con siete tablas! " with vpunch

        hide Oyamatalk
        show oyama at left

        hide Hisakosmile with dissolve
        show Hisakohng2 at right with dissolve

        H12 "Te dije que son trece. En fin, juguemos otra... ¡Empecemos!"

        S "Mezcló todas las fichas en el centro para ocultar la evidencia."

        hide oyama
        show Oyamatalk at left

        O4 "¡Eres una tramposa! ¡Muy bien, yo también lo haré! ¡Terminé! "

        hide Oyamatalk
        show oyama at left

        hide Hisakohng2
        show Hisakosmile2 at right

        S "Ooyama escondió tres fichas en su mano y la atacó con nueve tablas, teniendo una fila menos que una mano completa."

        hide oyama with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamageh at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        F3 "Espera, Ooyama, maldito estúpido, ¿cuántas fichas tienes? "

        hide Oyamageh
        show oyama at center

        hide Fujimakihah2
        show Fujimakisad2 at left

        S "Fujimaki las miró y empezó a contar."

        hide Fujimakisad2
        show Fujimakihah2 at left

        F1 "¿Ves? ¡Te faltan tres! Tú no juegas más, idiota. "

        hide oyama
        hide Fujimakihah2
        show Oyamatalk at center
        show Fujimakisad2 at left

        play sound "bosu36.wav" 

        O4 "¡¿Qué demo-?! ¡¿Por qué soy el único al que le sale mal?!" with vpunch

        hide Fujimakisad2 with dissolve
        hide Oyamatalk

        show oyama at left with dissolve

        S "Fue obligado a devolver la ficha que tomó de la pila."

        hide Hisakosmile2 with dissolve
        show Hisakolargemouth at right with dissolve

        stop music fadeout 1.0

        H13 "Gané por descarte. "

        hide Hisakolargemouth
        show Hisakosmile at right

        S "Dijo Hisako. "

        O1 "¿Eh? ¿Quién ganó por descarte? "

        hide oyama
        show Oyamageh at left

        hide Hisakosmile
        show Hisakohng at right with dissolve

        H14 "Yo gané gracias a ti. "

        play sound "bosu34.wav" 

        e "*FLOP*" with vpunch

        scene oyamaowned
        with fade

        S "Ella mostró sus fichas. "

        S "Los cuatro vientos más los tres dragones. "

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        O3 "¿Qué demonios es eso…? "

        H13 "Trece deseos, el puntaje máximo pero multiplicado por dos."

        play sound "bosu36.wav" 

        O1 "¡¿Trece deseos con solo siete tablas?! ¡¿No ven que hay algo raro?!" with vpunch

        H14 "Ah, y todo en la primera mano. Entonces será por tres."

        play sound "bosu36.wav" 

        O4 "¡¿Quéééééé?! " with vpunch

        F1 "Guau… nunca vi a alguien reunir los trece deseos en la primera mano…"

        play sound "bosu36.wav" 

        O3 "¡Porque es literalmente imposible!" with vpunch

        scene bg sunset01
        with fade

        S "Y con eso, Ooyama entró en cólera… "

        show oyama at left with dissolve
        show Hisakosmile at right with dissolve

        H12 "Muy bien, entréguenme todos los boletos de comida que me deben."

        hide oyama
        show Oyamahm at left

        O4 "Oh, vamos… "

        S6 "Alguien sin misericordia, con una arrogancia en su estado más puro."

        S6 "Esa es nuestra Hisako; una embustera. La encarnación perfecta del Diablo en persona."

        stop music fadeout 1.0

        scene bg black01
        with fade

        jump set3





    elif result == "Irie":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        e "La siguiente es nuestra baterista, Irie; aunque nosotras la llamamos Miyukichi. Se unió a la banda al mismo tiempo que yo."

        e "Si Hisako era el Diablo, entonces Miyukichi es su versión en miniatura."

        e "Es muy débil físicamente, pero realmente es una demonio. Suele tentar a los demás estudiantes, los NPCs, a hacer cosas muy peligrosas solo para ver hasta dónde puede influenciarlos. Verdaderamente es una demonio."

        scene bg corridoor2
        with fade

        show Sekinesad at center with dissolve
        show Iriesmile at left with dissolve

        play music "15 - study time.mp3" fadeout 1.0 fadein 1.0

        IR6 "Oye, oye, ¿conoces a ese chico, uh… Kinoshita, el NPC? ¡Pues él... está enamorado de mí!"

        IR6 "Cuando estábamos en clase, ¡cruzamos miradas y su cara se volvió completamente roja!"

        show Iriesmileb at left

        IR3 "¡Oh, por Dios, es muy obvio! "

        e "Un día se jacto de ello."

        hide Iriesmileb
        show Iriesmile at left

        IR6 "Así que ayer, le dije que a mí me gustaban más los chicos, eh... 'rebeldes'; como los de esas series de los 90s. Cuando lo vi hoy por la mañana, ¡estaba usando unos pantalones holgados!"

        IR1 "¡No estoy mintiendo! "

        hide Iriesmile
        show Iriehappytalk at left

        IR6 "¡Estaba usando su chaqueta del uniforme con esos pantalones holgados! ¡Oh, por Dios, no podía parar de reírme!"

        IR2 "Estos NPCs son demasiado geniales."

        IR2 "¡¿Cómo se las arregló para conseguirlos?!"

        IR2 "¿Se desveló haciéndolos?"

        IR6 "Cuando me vio empezó a actuar salvajemente. '¿Qué miran, idiotas?' , fue lo que dijo a todos sus compañeros. ¡Pero era obvio que con eso solo lo mirarían más! "

        play sound "bosu36.wav" 

        IR "¡Ja, ja, ja, ja!" with vpunch

        hide Iriehappytalk
        show Irie at left

        IR2 "¡Lo más gracioso de todo es que lo hizo para tratar de conquistarme!"

        scene bg corridoor1
        with dissolve

        show Irie at center with dissolve

        e "Podríamos ser amigas de él, pero teníamos que decírselo apropiadamente."

        e "Incluso si eran NPCs, me sentía mal por ellos."

        hide Irie
        show Irie2 with dissolve

        IR4 "Entonces, Shiorin, ¿qué deberíamos pedirle ahora? Hará cualquier cosa, ¡estoy segura de ello!"

        show Sekinetalkangry at right with dissolve

        S6 "Dios, Miyukichi, ¿no sabes cuándo parar?"

        S6 "Ya lo molestaste demasiado."

        hide Sekinetalkangry
        show Sekineangry at right

        e "Intenté provocar alguna pizca de piedad en ella."

        e "Era tan humana como todos nosotros, así que supuse que debía tenerla en alguna parte."

        hide Irie2 with dissolve
        show Irietalk at left with dissolve

        IR6 "¿Pero no te da curiosidad qué tan lejos pueden llegar? Después de todo, ¡somos espías del escuadrón del más allá!"

        hide Irietalk
        show Iriesmile at left

        e "¿Desde cuándo te volviste una espía?"

        e "¿Y qué es eso del escuadrón del más allá?"

        e "Qué nombre más raro... "

        e "¿Acaso intentaste darle tu propia versión a la SSS?"

        e "Aunque, la SSS siempre la integraron un montón de idiotas."

        e "Es imposible que lleguen a tener miembros tan inteligentes como yo o Miyukichi."

        hide Iriesmile
        show Iriehappytalk at left 

        IR4 "¡¿Qué te parece un afro?! Si le digo que a mí me gustan los chicos que tienen un afro, ¡estoy segura que mañana vendrá con uno! ¡Oh, por Dios, no puedo parar de reír! "

        hide Iriehappytalk
        show Iriesmileb at left 

        hide Sekineangry
        show Sekinetalk at right

        S7 "Deberías dejarlo. Los pantalones holgados ya fueron más que suficiente."

        S7 "Un poco más y creo que enfadarás al pobre NPC."

        hide Sekinetalk
        show Sekine at right

        hide Iriesmileb
        show Iriehuh2 at left with dissolve

        stop music fadeout 1.0

        IR4 "¡Pero ese es el punto!"

        IR4 "¡Quiero saber hasta dónde pueden llegar!"

        IR4 "Está bien, me decidí. ¡Mañana, Kinoshita tendrá un afro! "

        scene bg black01
        with fade

        e "Al día siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekine at left with dissolve

        play sound "bosu36.wav" 

        IR "¡Oh, por Dios, ese es Kinoshita!" with vpunch

        hide Sekine with dissolve
        show Sekine2 at left with dissolve

        e "Quería practicar mi bajo en paz, así que me fui a un aula vacía. Cuando, Miyukichi entró corriendo al salón."

        e "Luego de que finalmente parara de reír, ella dijo:"

        show Iriehappytalk at right with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        IR2 "¡Lo hizo, vino con un maldito afro! ¡No te estoy mintiendo! ¡Dios, no tenía idea de que nuestra escuela tuviese a un peluquero con tanto talento! ¡Qué desperdicio! " with vpunch

        e "De hecho, estoy segura de que eso es imposible. No importa lo que hagas, no puedes hacerte crecer un afro en solo una noche."

        hide Iriehappytalk
        show Iriesmile at right 

        hide Sekine2
        show Sekinetalk2 at left

        S3 "Yo también lo vi, era muy fácil de identificar. Pude adivinar quién era apenas me lo crucé por el pasillo; pobre chico."

        hide Sekinetalk2
        show Sekine2 at left

        hide Iriesmile with dissolve
        show Iriesmile2 at right with dissolve

        IR6 "Entonces, ¿qué sigue? ¡Él verdaderamente hará cualquier cosa que le pida!"

        IR6 "¡Oh, por Dios, es demasiado gracioso!"

        hide Iriesmile2 with dissolve
        show Iriesmileb2 at center with dissolve

        show Sekinetalkangry2 at left 

        stop music fadeout 1.0

        S4 "Sí… ¿Qué pasó con tu meta principal? Ahora lo único que quieres es reírte."

        show Sekineangry2 at left

        scene bg corridoor3
        with fade

        show Iriehappytalk at center with dissolve

        play music "27 - moment of rest.mp3" fadeout 1.0 fadein 1.0

        IR6 "¡No, no es así! Esto es algo verdaderamente serio… Je, je, je.~"

        hide Iriehappytalk
        show Iriesmile

        e "Es muy difícil de creer cuando lo dices tú, ¿sabes?"

        scene bg corridoor1
        with dissolve

        show Iriesmileb at center with dissolve

        IR3 "Oye, la próxima vez... ¡¿Qué te parece si le pido que se ponga brochetas en su afro?!"

        hide Iriesmileb with dissolve
        show Iriesmileb2 at center with dissolve

        IR3 "El café hará brochetas esta noche."

        IR6 "¡Así que haremos que él aparezca con un montón de ellas en su afro!"

        IR2 "Je, je, je.~"

        scene bg corridoor2
        with dissolve

        show Sekinesad at right with dissolve
        show Irie at center with dissolve

        S4 "Al menos el afro es un estilo de verdad, ¿pero brochetas?"

        show Sekinetalk at right

        S4 "¿Cómo piensas pedírselo?"

        show Sekine at right

        hide Irie with dissolve
        show Iriehappytalk2 at left with dissolve

        IR2 "Fácil. Cuando me lo encuentre le diré algo como... "

        IR2 "Oh, si tan solo tuvieras algunas brochetas en tu afro, Kinoshita.~ Se que caería rendida a los pies de cualquiera que lo tuviese así.~ Ah, llevo fijándome en ti desde hace mucho tiempo.~ Je, je, je.~"

        hide Iriehappytalk2
        show Iriesmile2 at left 

        show Sekinesad

        stop music fadeout 1.0

        e "Qué mujer… "

        scene bg black01
        with fade

        e "Y luego de que se fuera, seguí practicando en el aula."

        e "Al día siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekinesad with dissolve

        play sound "bosu36.wav" 

        IR "¡Oh, por Dios! ¡Oh, por Dios! ¡De verdad se clavó brochetas en su afro!" with vpunch

        scene bg irie
        with fade

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        e "Estaba a punto de estallar en lágrimas de risa. No tengo dudas de que se rio en todo el camino hasta aquí."

        S7 "Sí, lo vi. Te creo."

        IR3 "Es genial, ¡¿verdad?! Y uno de sus amigos le dijo: '¡Dame una!' Pero el respondió enojado: '¡No me toques!' ¡JA, JA, JA, JA, JA! ¡Santos cielos!"

        S3 "Entonces, ¿te comiste una? "

        IR2 "¡Iugh, claro que no! ¡Eran de ayer y estaban muy frías!"

        IR2 "¡Y estoy segura que fue al baño con ellas! ¡Asqueroso!"

        scene bg Emptyclassroom
        with fade

        show Sekinesad2 with dissolve
        show Iriesmileb at right with dissolve

        stop music fadeout 1.0

        e "Oh, hombre. Miyukichi fue demasiado lejos… "

        e "Este mundo transforma a las personas… "

        e "Y, a pesar de todo, aún hay gente que se toma la vida en serio y hacen lo imposible para pelear contra Dios."

        scene bg class1
        with fade

        IR4 "¡Oooh, hagamos que mañana camine con uno de esos aros de natación!"

        IR6 "No los usará para nadar, ¡pero estoy segura que andará por todos lados con eso!"

        IR2 "¡Pantalones holgados, un afro con brochetas clavadas en él y un aro de natación!"

        IR2 "¡JA, JA! ¡Ese NPC tendrá mucha más personalidad que todos nosotros!"

        scene bg black01

        play sound "hit_p07.wav" 

        e "*GOLPE* " with vpunch

        scene bg Emptyclassroom
        with fade

        show Iriehuhb2 at right with dissolve

        IR "¡...!"

        e "Le di una bofetada con todas mis fuerzas."

        e "Miyukichi mantuvo su mirada fija, mirando a la nada."

        e "Se quedó completamente paralizada."

        show Sekinetalkangry2 at center with dissolve

        play sound "bosu36.wav" 

        S6 "Quizás los NPCs no tengan un alma como sí tenemos nosotros, ¡pero siguen siendo personas! " with vpunch

        S6 "¡Ellos tienen sentimientos! Y por encima de todo, ¡Kinoshita es demasiado dulce e inocente!"

        S6 "A menos que le pidas que se suicide, ¡estoy segura que hará cualquier cosa que le pidas!"

        S3 "¡Pero todo lo que haces es aprovecharte de eso y sigues burlándote de él! ¡¿No tienes vergüenza?!"

        hide Sekinetalkangry2 with dissolve
        show Sekineangry with dissolve

        hide Iriehuhb2
        show Iriehuh2 at right

        IR5 "P- Pero… pensé que tú también estabas divirtiéndote… "

        hide Iriehuh2
        show Iriehuhb at right

        hide Sekinetalkangry2
        hide Sekineangry
        show Sekineyellangry2

        play sound "bosu36.wav" 

        S6 "¡¿Cómo podría divertirme con algo así?! " with vpunch

        S6 "¡Kinoshita es mucho más humano que tú! "

        show Sekineangry2

        hide Iriehuhb
        show Iriesad at right with dissolve

        e "Su rostro se oscureció de repente."

        e "Para cualquier integrante de la SSS, ser comparado con un NPC es mucho más ofensivo que cualquier otro insulto que te puedas imaginar."

        IR5 "¿Tú crees… que un NPC es mejor persona que yo...?"

        hide Sekineangry2
        show Sekinetalkangry2

        S7 "Sí. Y creo que deberías pensar sobre ello."

        hide Sekinetalkangry2
        show Sekineangry2

        IR5 "S- Sollozo… "

        e "Los hombros de Miyukichi comenzaron a temblar…"

        hide Iriesad with dissolve

        play sound "bosu36.wav" 

        IR "¡Guaaaaaah!" with vpunch

        show Sekineangry2 with fade

        e "Salió corriendo mientras cubría su rostro con sus manos."

        show Sekinetalkangry2

        S4 "Sheesh… "

        hide Sekinetalkangry2

        scene bg Concerthall
        with fade

        e "Más tarde, se lo expliqué todo a Kinoshita."

        e "Ocultando la parte de que era un NPC, obviamente."

        e "Incluso si lo hubiera hecho, se habría confundido tanto que olvidaría todo lo que le dije."

        show Sekine with dissolve

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        S7 "Lo siento."

        hide Sekine
        show Sekinetalk

        S1 "Hiciste absolutamente todo lo que te pidió, pero esto se te fue de las manos."

        hide Sekinetalk
        show Sekine

        K "Entonces, eso significa que… yo fui el único que sintió amor de verdad… "

        e "No apartó la mirada del suelo, completamente abatido. "

        hide Sekine
        show Sekinesad

        S3 "Sí… supongo que tienes razón… "

        K "Ya veo, pero no voy a llorar por esto. Porque, ¡encontré a mi nuevo amor!"

        e "Sus ojos brillaron cómo nunca antes y alzó a lo alto su puño cerrado."

        hide Sekinesad
        show Sekinesmile

        S1 "¿Eh? ¡Eso es genial!"

        K "¡Tú!"

        hide Sekinesmile
        show Sekinegeh

        stop music fadeout 1.0

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        S5 "¡¿Qué?! ¡¿Yo?! " with vpunch

        K "¡Sí, tú! ¡Tú siempre te preocupaste por un pobre sujeto como yo! "

        K "¡Estoy verdaderamente enamorado de ti! "

        hide Sekinegeh
        show Sekinegeh2

        S5 "¿D- De verdad?"

        K "¡Por favor, salga conmigo, señorita Sekine!"

        hide Sekinegeh2
        show Sekinesad

        S5 "Espera, no estoy segura de esto…"

        K "¡¿Te gustan los afros?! ¿O brochetas? ¡Quizás te vayan los chicos rebeldes!"

        hide Sekinesad
        show Sekinegeh

        S5 "No, uh… a mí no me van todas esas cosas raras… "

        K "¡¿Entonces te gusto tal y cómo soy?! " with vpunch

        hide Sekinegeh
        show Sekinegeh2

        stop music fadeout 1.0

        S5 "Uh… espera… eso no es lo que… ¡Adiós! "

        hide Sekinegeh2 with dissolve

        e "Escapé lo más rápido que pude." with vpunch

        scene bg black01
        with fade

        e "Al final, Miyukichi no era tan malvada como yo creía; tan solo disfrutaba demasiado jugando con los pobres NPCs. Aunque no se puede negar que es cruel."

        e "Y por último, nos queda Iwasawa."

    window hide





label set4:

    $ renpy.block_rollback()    

    scene bg black01
    with fade

    e "Seleccionar Historia."

    window hide None

    $ result = renpy.imagemap("ground04.jpg", "hover.jpg", [
        (88, 454, 200, 495, "Sekine"),
        (270, 344, 376, 392, "Hisako"), 
        (570, 510, 698, 546, "Iwasawa"),
        (719, 443, 796, 481, "Irie"),    
        ], focus="imagemap")

    window show None





    if result == "Sekine":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        window show dissolve
        $ show_button_game_menu = True
        with dissolve

        Sslow "... ...... ............"

        S3 "Umm..."

        S7 "¿Por dónde empiezo?"

        S1 "¿Qué de que hablo? "

        S1 "De mis compañeras de Girls Dead Monster. A veces lo llamamos Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabías, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mía y de nadie más."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compañeras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un día le dije bromeando a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''¡Esas dos son unas monstruos! ¡Huye, Miyukichi! Escapa cómo puedas, ¡no te preocupes por mí!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzó a formar parte de nuestra banda."

        S3 "..."

        jump set2





    elif result == "Hisako":

        $ renpy.block_rollback()    

        play music "04 - girl's hop.mp3" fadeout 1.0 fadein 1.0

        S1 "Primero se las presentaré. "

        S1 "Está es Hisako-senpai."

        S1 "Y cómo puedes intuir, es mi superior."

        S1 "Hisako es la guitarrista principal de nuestra banda."

        S1 "Puede parecer extraño, pero tiene un pequeño problema: "

        S1 "Ella es una jugadora compulsiva."

        S7 "Para ser más específica: es una jugadora compulsiva... que hace trampas."

        S7 "Un día tuve mucha suerte y pude ver con mis propios ojos lo habilidosos que eran sus trucos."

        scene bg sunset02
        with fade

        S "Ese día estaba jugando a las escondidas con Miyukichi. Me había encerrado en un casillero."

        S "El sol estaba comenzando a ocultarse, así que comencé a preguntarme si debía salir."

        scene bg black01

        stop music fadeout 1.0

        play sound "bosu36.wav" 

        e "*GOLPE*" with vpunch

        scene bg sunset01
        with dissolve

        S "Las luces se encendieron. Y, una voz muy familiar entró al salón y dijo:"

        play sound "bosu36.wav" 

        e2 "¡Hagámoslo!" with vpunch

        S "Y se sentó cerca de una mesa."

        S "Yo pude verlo todo desde las ventilas del casillero."

        S "Me quedé encerrada, no quería salir del casillero delante de tanta gente como si fuese lo más normal del mundo."

        S "No lo sabía en ese momento, pero esa iba a ser la primera vez que vería el lado más divertido de Hisako."

        S "Los cuatro que estaban sentados alrededor de la mesa eran Fujimaki, TK, Ooyama, y Hisako. "

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S "Ellos comenzaron mezclando y repartiendo las tablas de Mahjong."

        S "Las reglas del Mahjong son simples, tienen que formar una mano en la que tengan un par de tablas que sean iguales, y cuatro grupos de tres tablas iguales."

        S "El primero en formar una mano completa, gana. El ganador puede juntar los puntos de todos los demás."

        S "Siendo honesta, no sé mucho de Mahjong. Aún hay muchas reglas que se me escapan."

        show Hisakotalk at right with dissolve

        H13 "¡Empecemos!"

        hide Hisakotalk
        show Hisako at right

        S "Hisako formó una jugada de mil puntos en la mesa, mostrando que estaba a una tabla de formar una mano completa."

        show Fujimaki2 at left with dissolve

        F2 "Bien… ¡Vamos! "

        hide Hisako with dissolve
        show Hisako2 at right with dissolve

        H14 "Gano por pura suerte, tan simple que solo necesité un tiro."

        H14 "Oh, con esta Dora, todos los puntos van para mí. "

        hide Hisako2
        show Hisakohng2 at right

        S "Fue como una pequeña guerra."

        S "Pero era obvio que la mano de Hisako no tenía suficientes tablas."

        S "Debería de haber trece, pero ella solo tenía diez."

        S "Escondiendo las otras tres en su mano, ganó formando tres filas en vez de cuatro."

        hide Fujimaki2
        show Fujimakihah2 at left 

        F3 "Tsk… Mierda."

        hide Fujimakihah2 with fade

        hide Hisakohng2
        show Hisako2 at right

        S "Fujimaki fue tan idiota que no se dio cuenta."

        stop music fadeout 1.0

        S "Solo le quedó juntar sus pequeñas tablas con obediencia."

        S "La estrategia de Hisako era imbatible."

        S "Haciendo eso, siempre formaría una mano mucho más rápido que cualquiera."

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        show TK2 at left with dissolve

        hide Hisako2 with dissolve
        show Hisakosmile at right with dissolve

        H13 "Terminé. Bien, gané descartando. Ni un solo puntero, más la Dora que está en el medio."

        H14 "Ah, saqué el máximo otra vez."

        hide TK2
        show TKyell2 at left

        play sound "bosu36.wav"

        TK1 "¡Ah! ¡Fuck me! " with vpunch

        S "TK fue un poco idiota también, así que tampoco se percató de ello."

        S "No sé mucho de inglés, pero... para que TK diga eso, estoy segura que se enojó muchísimo."

        stop music fadeout 1.0

        hide TKyell2 with fade

        show oyama at left with dissolve

        O2 "Terminé. "

        hide Hisakosmile
        show Hisakohuh2 at right

        play music "25 - let's operation.mp3" fadeout 1.0 fadein 1.0

        S "Aunque esa vez, Ooyama casi vence a Hisako."

        S "Tan solo llegaron al tercer turno, pero..."

        S "No podía ganar incluso teniendo solo diez fichas en la mesa."

        S "Entonces, Hisako decidió hacer algo aún más descarado."

        S "Escondió otras tres fichas en su mano."

        S "Ahora solo quedan siete, de las cuales solo dos son puentes."

        hide Hisakohuh2 with dissolve
        show Hisakosmile at right with dissolve

        H14 "¡Yo también terminé!"

        S "Dijo sin miedo."

        S "Pero eso fue demasiado obvio. Solo tenía la mitad de las fichas a diferencia de Ooyama."

        S "Aparentemente Ooyama no lo aguantó más y se quejó de ello."

        S "Bueno, se quejó lo más fuerte que pudo hacerlo."

        hide oyama
        show Oyamatalk at left

        O1 "¿Estás segura que tienes trece fichas?"

        hide Hisakosmile
        show Hisakotalk at right

        H13 "Síp."

        hide Hisakotalk
        show Hisakosmile at right

        hide Oyamatalk
        show Oyamageh at left

        play sound "bosu36.wav"

        stop music fadeout 1.0

        O4 "… ¡¿Quééééééé?!" with vpunch

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        S "Incluso desde el casillero pude oír su grito ahogado."

        S "Pensándolo bien, el casillero era el escondite perfecto."

        S "Con una vista perfecta de toda la mesa.~"

        S "Pero como nadie más dijo nada, el pobre Ooyama se quedó quieto y tomó otra ficha."

        hide Oyamageh
        show Oyamatalk at left

        play sound "bosu36.wav" 

        O3 "¡Quiero ganar…! ¡Mierda! ¡Esta ficha no sirve! " with vpunch

        S "Pero él ya dijo que había terminado, así que no podía hacer nada."

        O3 "¡Muévete! "

        hide Oyamatalk
        show Oyamahm at left

        hide Hisakosmile with dissolve
        show Hisakosmile2 at right with dissolve

        H11 "Oh, no servirá."

        H11 "Gano por descarte."

        hide Hisakosmile2 with dissolve
        show Hisakosmile at right with dissolve

        H11 "Gané el mano a mano; todas parejas y ningún puntero. Todo en una misma cadena y con dos Doras. Ah, también hay que contar la Dora del medio… "

        H14 "¿Cuánto es eso…? "

        H13 "Un múltiplo de trece, ¿eh? Un nuevo máximo, ja. "

        stop music fadeout 1.0

        hide Oyamahm with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamahm at center with dissolve

        F2 "Oh, por Dios… Eso fue genial, Hisako… "

        S "Fujimaki quedó absolutamente asombrado. "

        hide Fujimakihah2 with dissolve
        hide Oyamahm with dissolve

        show Oyamatalk at left with dissolve

        O1 "¡Espera, espera un poco! ¡¿Dices que eso es genial?!"

        play sound "bosu36.wav" 

        O1 "¡Cualquiera puede hacerlo solo con siete tablas! " with vpunch

        hide Oyamatalk
        show oyama at left

        hide Hisakosmile with dissolve
        show Hisakohng2 at right with dissolve

        H12 "Te dije que son trece. En fin, juguemos otra... ¡Empecemos!"

        S "Mezcló todas las fichas en el centro para ocultar la evidencia."

        hide oyama
        show Oyamatalk at left

        O4 "¡Eres una tramposa! ¡Muy bien, yo también lo haré! ¡Terminé! "

        hide Oyamatalk
        show oyama at left

        hide Hisakohng2
        show Hisakosmile2 at right

        S "Ooyama escondió tres fichas en su mano y la atacó con nueve tablas, teniendo una fila menos que una mano completa."

        hide oyama with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamageh at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        F3 "Espera, Ooyama, maldito estúpido, ¿cuántas fichas tienes? "

        hide Oyamageh
        show oyama at center

        hide Fujimakihah2
        show Fujimakisad2 at left

        S "Fujimaki las miró y empezó a contar."

        hide Fujimakisad2
        show Fujimakihah2 at left

        F1 "¿Ves? ¡Te faltan tres! Tú no juegas más, idiota. "

        hide oyama
        hide Fujimakihah2
        show Oyamatalk at center
        show Fujimakisad2 at left

        play sound "bosu36.wav" 

        O4 "¡¿Qué demo-?! ¡¿Por qué soy el único al que le sale mal?!" with vpunch

        hide Fujimakisad2 with dissolve
        hide Oyamatalk

        show oyama at left with dissolve

        S "Fue obligado a devolver la ficha que tomó de la pila."

        hide Hisakosmile2 with dissolve
        show Hisakolargemouth at right with dissolve

        stop music fadeout 1.0

        H13 "Gané por descarte. "

        hide Hisakolargemouth
        show Hisakosmile at right

        S "Dijo Hisako. "

        O1 "¿Eh? ¿Quién ganó por descarte? "

        hide oyama
        show Oyamageh at left

        hide Hisakosmile
        show Hisakohng at right with dissolve

        H14 "Yo gané gracias a ti. "

        play sound "bosu34.wav" 

        e "*FLOP*" with vpunch

        scene oyamaowned
        with fade

        S "Ella mostró sus fichas. "

        S "Los cuatro vientos más los tres dragones. "

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        O3 "¿Qué demonios es eso…? "

        H13 "Trece deseos, el puntaje máximo pero multiplicado por dos."

        play sound "bosu36.wav" 

        O1 "¡¿Trece deseos con solo siete tablas?! ¡¿No ven que hay algo raro?!" with vpunch

        H14 "Ah, y todo en la primera mano. Entonces será por tres."

        play sound "bosu36.wav" 

        O4 "¡¿Quéééééé?! " with vpunch

        F1 "Guau… nunca vi a alguien reunir los trece deseos en la primera mano…"

        play sound "bosu36.wav" 

        O3 "¡Porque es literalmente imposible!" with vpunch

        scene bg sunset01
        with fade

        S "Y con eso, Ooyama entró en cólera… "

        show oyama at left with dissolve
        show Hisakosmile at right with dissolve

        H12 "Muy bien, entréguenme todos los boletos de comida que me deben."

        hide oyama
        show Oyamahm at left

        O4 "Oh, vamos… "

        S6 "Alguien sin misericordia, con una arrogancia en su estado más puro."

        S6 "Esa es nuestra Hisako; una embustera. La encarnación perfecta del Diablo en persona."

        stop music fadeout 1.0

        scene bg black01
        with fade

        jump set3





    elif result == "Irie":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        e "La siguiente es nuestra baterista, Irie; aunque nosotras la llamamos Miyukichi. Se unió a la banda al mismo tiempo que yo."

        e "Si Hisako era el Diablo, entonces Miyukichi es su versión en miniatura."

        e "Es muy débil físicamente, pero realmente es una demonio. Suele tentar a los demás estudiantes, los NPCs, a hacer cosas muy peligrosas solo para ver hasta dónde puede influenciarlos. Verdaderamente es una demonio."

        scene bg corridoor2
        with fade

        show Sekinesad at center with dissolve
        show Iriesmile at left with dissolve

        play music "15 - study time.mp3" fadeout 1.0 fadein 1.0

        IR6 "Oye, oye, ¿conoces a ese chico, uh… Kinoshita, el NPC? ¡Pues él... está enamorado de mí!"

        IR6 "Cuando estábamos en clase, ¡cruzamos miradas y su cara se volvió completamente roja!"

        show Iriesmileb at left

        IR3 "¡Oh, por Dios, es muy obvio! "

        e "Un día se jacto de ello."

        hide Iriesmileb
        show Iriesmile at left

        IR6 "Así que ayer, le dije que a mí me gustaban más los chicos, eh... 'rebeldes'; como los de esas series de los 90s. Cuando lo vi hoy por la mañana, ¡estaba usando unos pantalones holgados!"

        IR1 "¡No estoy mintiendo! "

        hide Iriesmile
        show Iriehappytalk at left

        IR6 "¡Estaba usando su chaqueta del uniforme con esos pantalones holgados! ¡Oh, por Dios, no podía parar de reírme!"

        IR2 "Estos NPCs son demasiado geniales."

        IR2 "¡¿Cómo se las arregló para conseguirlos?!"

        IR2 "¿Se desveló haciéndolos?"

        IR6 "Cuando me vio empezó a actuar salvajemente. '¿Qué miran, idiotas?' , fue lo que dijo a todos sus compañeros. ¡Pero era obvio que con eso solo lo mirarían más! "

        play sound "bosu36.wav" 

        IR "¡Ja, ja, ja, ja!" with vpunch

        hide Iriehappytalk
        show Irie at left

        IR2 "¡Lo más gracioso de todo es que lo hizo para tratar de conquistarme!"

        scene bg corridoor1
        with dissolve

        show Irie at center with dissolve

        e "Podríamos ser amigas de él, pero teníamos que decírselo apropiadamente."

        e "Incluso si eran NPCs, me sentía mal por ellos."

        hide Irie
        show Irie2 with dissolve

        IR4 "Entonces, Shiorin, ¿qué deberíamos pedirle ahora? Hará cualquier cosa, ¡estoy segura de ello!"

        show Sekinetalkangry at right with dissolve

        S6 "Dios, Miyukichi, ¿no sabes cuándo parar?"

        S6 "Ya lo molestaste demasiado."

        hide Sekinetalkangry
        show Sekineangry at right

        e "Intenté provocar alguna pizca de piedad en ella."

        e "Era tan humana como todos nosotros, así que supuse que debía tenerla en alguna parte."

        hide Irie2 with dissolve
        show Irietalk at left with dissolve

        IR6 "¿Pero no te da curiosidad qué tan lejos pueden llegar? Después de todo, ¡somos espías del escuadrón del más allá!"

        hide Irietalk
        show Iriesmile at left

        e "¿Desde cuándo te volviste una espía?"

        e "¿Y qué es eso del escuadrón del más allá?"

        e "Qué nombre más raro... "

        e "¿Acaso intentaste darle tu propia versión a la SSS?"

        e "Aunque, la SSS siempre la integraron un montón de idiotas."

        e "Es imposible que lleguen a tener miembros tan inteligentes como yo o Miyukichi."

        hide Iriesmile
        show Iriehappytalk at left 

        IR4 "¡¿Qué te parece un afro?! Si le digo que a mí me gustan los chicos que tienen un afro, ¡estoy segura que mañana vendrá con uno! ¡Oh, por Dios, no puedo parar de reír! "

        hide Iriehappytalk
        show Iriesmileb at left 

        hide Sekineangry
        show Sekinetalk at right

        S7 "Deberías dejarlo. Los pantalones holgados ya fueron más que suficiente."

        S7 "Un poco más y creo que enfadarás al pobre NPC."

        hide Sekinetalk
        show Sekine at right

        hide Iriesmileb
        show Iriehuh2 at left with dissolve

        stop music fadeout 1.0

        IR4 "¡Pero ese es el punto!"

        IR4 "¡Quiero saber hasta dónde pueden llegar!"

        IR4 "Está bien, me decidí. ¡Mañana, Kinoshita tendrá un afro! "

        scene bg black01
        with fade

        e "Al día siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekine at left with dissolve

        play sound "bosu36.wav" 

        IR "¡Oh, por Dios, ese es Kinoshita!" with vpunch

        hide Sekine with dissolve
        show Sekine2 at left with dissolve

        e "Quería practicar mi bajo en paz, así que me fui a un aula vacía. Cuando, Miyukichi entró corriendo al salón."

        e "Luego de que finalmente parara de reír, ella dijo:"

        show Iriehappytalk at right with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        IR2 "¡Lo hizo, vino con un maldito afro! ¡No te estoy mintiendo! ¡Dios, no tenía idea de que nuestra escuela tuviese a un peluquero con tanto talento! ¡Qué desperdicio! " with vpunch

        e "De hecho, estoy segura de que eso es imposible. No importa lo que hagas, no puedes hacerte crecer un afro en solo una noche."

        hide Iriehappytalk
        show Iriesmile at right 

        hide Sekine2
        show Sekinetalk2 at left

        S3 "Yo también lo vi, era muy fácil de identificar. Pude adivinar quién era apenas me lo crucé por el pasillo; pobre chico."

        hide Sekinetalk2
        show Sekine2 at left

        hide Iriesmile with dissolve
        show Iriesmile2 at right with dissolve

        IR6 "Entonces, ¿qué sigue? ¡Él verdaderamente hará cualquier cosa que le pida!"

        IR6 "¡Oh, por Dios, es demasiado gracioso!"

        hide Iriesmile2 with dissolve
        show Iriesmileb2 at center with dissolve

        show Sekinetalkangry2 at left 

        stop music fadeout 1.0

        S4 "Sí… ¿Qué pasó con tu meta principal? Ahora lo único que quieres es reírte."

        show Sekineangry2 at left

        scene bg corridoor3
        with fade

        show Iriehappytalk at center with dissolve

        play music "27 - moment of rest.mp3" fadeout 1.0 fadein 1.0

        IR6 "¡No, no es así! Esto es algo verdaderamente serio… Je, je, je.~"

        hide Iriehappytalk
        show Iriesmile

        e "Es muy difícil de creer cuando lo dices tú, ¿sabes?"

        scene bg corridoor1
        with dissolve

        show Iriesmileb at center with dissolve

        IR3 "Oye, la próxima vez... ¡¿Qué te parece si le pido que se ponga brochetas en su afro?!"

        hide Iriesmileb with dissolve
        show Iriesmileb2 at center with dissolve

        IR3 "El café hará brochetas esta noche."

        IR6 "¡Así que haremos que él aparezca con un montón de ellas en su afro!"

        IR2 "Je, je, je.~"

        scene bg corridoor2
        with dissolve

        show Sekinesad at right with dissolve
        show Irie at center with dissolve

        S4 "Al menos el afro es un estilo de verdad, ¿pero brochetas?"

        show Sekinetalk at right

        S4 "¿Cómo piensas pedírselo?"

        show Sekine at right

        hide Irie with dissolve
        show Iriehappytalk2 at left with dissolve

        IR2 "Fácil. Cuando me lo encuentre le diré algo como... "

        IR2 "Oh, si tan solo tuvieras algunas brochetas en tu afro, Kinoshita.~ Se que caería rendida a los pies de cualquiera que lo tuviese así.~ Ah, llevo fijándome en ti desde hace mucho tiempo.~ Je, je, je.~"

        hide Iriehappytalk2
        show Iriesmile2 at left 

        show Sekinesad

        stop music fadeout 1.0

        e "Qué mujer… "

        scene bg black01
        with fade

        e "Y luego de que se fuera, seguí practicando en el aula."

        e "Al día siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekinesad with dissolve

        play sound "bosu36.wav" 

        IR "¡Oh, por Dios! ¡Oh, por Dios! ¡De verdad se clavó brochetas en su afro!" with vpunch

        scene bg irie
        with fade

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        e "Estaba a punto de estallar en lágrimas de risa. No tengo dudas de que se rio en todo el camino hasta aquí."

        S7 "Sí, lo vi. Te creo."

        IR3 "Es genial, ¡¿verdad?! Y uno de sus amigos le dijo: '¡Dame una!' Pero el respondió enojado: '¡No me toques!' ¡JA, JA, JA, JA, JA! ¡Santos cielos!"

        S3 "Entonces, ¿te comiste una? "

        IR2 "¡Iugh, claro que no! ¡Eran de ayer y estaban muy frías!"

        IR2 "¡Y estoy segura que fue al baño con ellas! ¡Asqueroso!"

        scene bg Emptyclassroom
        with fade

        show Sekinesad2 with dissolve
        show Iriesmileb at right with dissolve

        stop music fadeout 1.0

        e "Oh, hombre. Miyukichi fue demasiado lejos… "

        e "Este mundo transforma a las personas… "

        e "Y, a pesar de todo, aún hay gente que se toma la vida en serio y hacen lo imposible para pelear contra Dios."

        scene bg class1
        with fade

        IR4 "¡Oooh, hagamos que mañana camine con uno de esos aros de natación!"

        IR6 "No los usará para nadar, ¡pero estoy segura que andará por todos lados con eso!"

        IR2 "¡Pantalones holgados, un afro con brochetas clavadas en él y un aro de natación!"

        IR2 "¡JA, JA! ¡Ese NPC tendrá mucha más personalidad que todos nosotros!"

        scene bg black01

        play sound "hit_p07.wav" 

        e "*GOLPE* " with vpunch

        scene bg Emptyclassroom
        with fade

        show Iriehuhb2 at right with dissolve

        IR "¡...!"

        e "Le di una bofetada con todas mis fuerzas."

        e "Miyukichi mantuvo su mirada fija, mirando a la nada."

        e "Se quedó completamente paralizada."

        show Sekinetalkangry2 at center with dissolve

        play sound "bosu36.wav" 

        S6 "Quizás los NPCs no tengan un alma como sí tenemos nosotros, ¡pero siguen siendo personas!" with vpunch

        S6 "¡Ellos tienen sentimientos! Y por encima de todo, ¡Kinoshita es demasiado dulce e inocente!"

        S6 "A menos que le pidas que se suicide, ¡estoy segura que hará cualquier cosa que le pidas!"

        S3 "¡Pero todo lo que haces es aprovecharte de eso y sigues burlándote de él! ¡¿No tienes vergüenza?!"

        hide Sekinetalkangry2 with dissolve
        show Sekineangry with dissolve

        hide Iriehuhb2
        show Iriehuh2 at right

        IR5 "P- Pero… pensé que tú también estabas divirtiéndote… "

        hide Iriehuh2
        show Iriehuhb at right

        hide Sekinetalkangry2
        hide Sekineangry
        show Sekineyellangry2

        play sound "bosu36.wav" 

        S6 "¡¿Cómo podría divertirme con algo así?! " with vpunch

        S6 "¡Kinoshita es mucho más humano que tú! "

        show Sekineangry2

        hide Iriehuhb
        show Iriesad at right with dissolve

        e "Su rostro se oscureció de repente."

        e "Para cualquier integrante de la SSS, ser comparado con un NPC es mucho más ofensivo que cualquier otro insulto que te puedas imaginar."

        IR5 "¿Tú crees… que un NPC es mejor persona que yo...?"

        hide Sekineangry2
        show Sekinetalkangry2

        S7 "Sí. Y creo que deberías pensar sobre ello."

        hide Sekinetalkangry2
        show Sekineangry2

        IR5 "S- Sollozo… "

        e "Los hombros de Miyukichi comenzaron a temblar…"

        hide Iriesad with dissolve

        play sound "bosu36.wav" 

        IR "¡Guaaaaaah!" with vpunch

        show Sekineangry2 with fade

        e "Salió corriendo mientras cubría su rostro con sus manos."

        show Sekinetalkangry2

        S4 "Sheesh… "

        hide Sekinetalkangry2

        scene bg Concerthall
        with fade

        e "Más tarde, se lo expliqué todo a Kinoshita."

        e "Ocultando la parte de que era un NPC, obviamente."

        e "Incluso si lo hubiera hecho, se habría confundido tanto que olvidaría todo lo que le dije."

        show Sekine with dissolve

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        S7 "Lo siento."

        hide Sekine
        show Sekinetalk

        S1 "Hiciste absolutamente todo lo que te pidió, pero esto se te fue de las manos."

        hide Sekinetalk
        show Sekine

        K "Entonces, eso significa que… yo fui el único que sintió amor de verdad… "

        e "No apartó la mirada del suelo, completamente abatido. "

        hide Sekine
        show Sekinesad

        S3 "Sí… supongo que tienes razón… "

        K "Ya veo, pero no voy a llorar por esto. Porque, ¡encontré a mi nuevo amor!"

        e "Sus ojos brillaron cómo nunca antes y alzó a lo alto su puño cerrado."

        hide Sekinesad
        show Sekinesmile

        S1 "¿Eh? ¡Eso es genial! "

        K "¡Tú!"

        hide Sekinesmile
        show Sekinegeh

        stop music fadeout 1.0

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        S5 "¡¿Qué?! ¡¿Yo?! " with vpunch

        K "¡Sí, tú! ¡Tú siempre te preocupaste por un pobre sujeto como yo! "

        K "¡Estoy verdaderamente enamorado de ti! "

        hide Sekinegeh
        show Sekinegeh2

        S5 "¿D- De verdad?"

        K "¡Por favor, salga conmigo, señorita Sekine!"

        hide Sekinegeh2
        show Sekinesad

        S5 "Espera, no estoy segura de esto… "

        K "¡¿Te gustan los afros?! ¿O brochetas? ¡Quizás te vayan los chicos rebeldes!"

        hide Sekinesad
        show Sekinegeh

        S5 "No, uh… a mí no me van todas esas cosas raras… "

        K "¡¿Entonces te gusto tal y cómo soy?! " with vpunch

        hide Sekinegeh
        show Sekinegeh2

        stop music fadeout 1.0

        S5 "Uh… espera… eso no es lo que… ¡Adiós! "

        hide Sekinegeh2 with dissolve

        e "Escapé lo más rápido que pude." with vpunch

        scene bg black01
        with fade

        e "Al final, Miyukichi no era tan malvada como yo creía; tan solo disfrutaba demasiado jugando con los pobres NPCs. Aunque no se puede negar que es cruel."

        jump set4





    elif result == "Iwasawa":

        $ renpy.block_rollback()    

        scene bg black01 with fade

        play music "08 - Alchemy (Yui ver).mp3" fadeout 1.0 fadein 1.0

        e "La última que queda es la líder de Girls Dead Monster, nuestra superior, Iwasawa. "

        e "Si Hisako es el diablo en persona y Miyukichi es su versión en miniatura, entonces no hay mejor manera de describir a Iwasawa como una fanática de la música."

        e "Quiero decir, no le interesa absolutamente nada que no sea la música."

        scene bg Emptyclassroom with fade

        e "El otro día, estábamos practicando en un aula vacía."

        e "Terminamos la intro y comenzamos con los primeros versos, pero Iwasawa no estaba cantando."

        stop music fadeout 1.0

        e "Por lo que todas nos detuvimos, y entonces Hisako preguntó:"

        show Hisakohuh at right with dissolve 

        H2 "¿Qué te pasa, Iwasawa?"

        I5 "¡Doo-loo, doo-dwa! "

        e "Iwasawa habló."

        show Sekinesad at left with dissolve
        show Irie at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        e "Todas nos quedamos en blanco y dijimos: ''¿Qué?'' ''¿Eh?'' a esas extrañas palabras."

        scene bg Iwasawa with fade

        I3 "Sekine."

        play sound "bosu36.wav" 

        S2 "¡Ah, sí! " with vpunch

        I5 "Es un par lo que viene luego de la intro. Así que antes de cantar, mueve la cabeza y di: ¡doo-loo, doo-dwa! "

        S5 "Ah, aah... 'Doo-loo, doo-dwa', ¿así? ¡Bien, lo tengo!"

        stop music fadeout 1.0

        scene bg Emptyclassroom with fade

        show Hisakosmile2 at right with dissolve
        show Irie at center with dissolve

        H10 "¡Muy bien, una vez más!"

        hide Irie
        show Irietalk

        IR6 "¡Esperen! ¡Uno, dos!"

        scene bg window1 with fade

        play music "08 - Alchemy (Yui ver).mp3" fadeout 1.0 fadein 1.0

        e "Irie comenzó a contar cuando Hisako le dio la señal."

        e "La intro comenzó y en muy poco tiempo llegamos al verso A."

        stop music fadeout 1.0

        scene bg black01

        I5 "… Naw."

        scene bg Iwasawa with fade

        e "Iwasawa tenía el micrófono cerca de su boca."

        e "Y en vez de cantar, empezó a murmurar. "

        I5 "Naw."

        scene bg class1 with fade

        show Sekine at left with dissolve
        show Iriehuh at center with dissolve
        show Hisakooh at right with dissolve

        e "Todas nos detuvimos otra vez. "

        I3 "Sekine."

        hide Sekine
        show Sekinesad2 at left with dissolve

        e "Dijo mi nombre, otra vez."

        play music "04 - girl's hop.mp3" fadeout 1.0 fadein 1.0

        I3 "No es... 'doo-loo, doo-doo'."

        e "Siguió hablando a través de los parlantes."

        hide Sekinesad2
        show Sekinegeh2 at left

        S5 "Um, pero si me dijiste que hiciera un 'doo-loo, doo-doo'."

        scene bg window1 with dissolve

        play sound "bosu36.wav" 

        I5 "¡Oye, no es así! ¡Escucha bien, es 'doo-loo, doo-dwa'! " with vpunch

        S2 "¿No son lo mismo? "

        play sound "bosu36.wav" 

        I5 "¡Yo dije, 'dwa'! ¡No, 'doo'! ¡'Dwa'! " with vpunch

        S7 "¿Eso último?"

        play sound "bosu36.wav" 

        I4 " ¡Síp!" with vpunch

        scene bg Iwasawa with fade

        e "Iwasawa solo habló por el micrófono todo el tiempo."

        e "No me miró a la cara ni por un segundo."

        e "Me daba mucho más miedo cuando no podía ver la expresión de su rostro."

        stop music fadeout 1.0

        scene bg Emptyclassroom with fade

        H9 "¡Bien, intentémoslo otra vez!"

        e "Hisako intentó animarme con su voz."

        IR6 "¡Bien! ¡Uno, dos!"

        scene bg black01

        play sound "bosu36.wav" 

        I5 "¡Noooooouuuuwww! " with vpunch

        e "Otra vez, ella gritó."

        e "Y todas nos detuvimos."

        I3 "Sekine."

        e "Mi nombre, por tercera vez."

        scene bg Iwasawa with fade

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S5 "S-Sí…"

        I4 "¡T-Te dije 'doo-loo, doo-dwa'! ¡Hazlo otra vez!"

        play sound "bosu36.wav"

        I5 "Oye, solo haz lo yo hago. ¡¡'Doo-loo, doo-dwa'!! " with vpunch

        S5 "Pero suena muy parecido a lo que yo hago…"

        play sound "bosu36.wav"

        I5 "¡'Doo' y 'dwa' zon doz coshas muy diferentes'! " with vpunch

        S7 "Casi no veo la diferencia…"

        S7 "Con mi habilidad, o mejor dicho, en mi bajo directamente no se nota la diferencia…"

        I4 "Entonzes, grítalo."

        S5 "¿Qué? "

        I4 "Zolo grita 'dwa' al final. ¿Para qué tienes el micrófono? "

        S5 "Para los coros, supongo… "

        I4 "Para esto también. ¡Azí que grita! ¡Te ashudará a zeguir el ritmo! "

        S7 "Podría… pero no creo que decir 'dwa' en el micrófono me vaya a ayudar a controlar mi ritmo…"

        scene bg Emptyclassroom with fade

        show Sekinesad2 at left with dissolve
        show Irie at center with dissolve
        show Hisakooh at right with dissolve

        I3 "¡E Irie! " with vpunch

        e "Empezó a gritarle a Miyukichi."

        hide Irie
        show Iriesad2

        play sound "bosu36.wav" 

        IR6 "¿S-Sí, senpai…? " with vpunch

        I5 "¡Aliviana todo' lo' golpes y bada bum que pueda'! "

        hide Sekinesad2
        show Sekinegeh2 at left

        e "Prácticamente se burló de la existencia de la batería..."

        hide Iriesad2
        show Iriehuhb2

        IR5 "Pero eso es todo lo que hace la batería… "

        hide Iriehuhb2
        show Iriehuh2

        I4 "Más despacio. Por cierto, deberías ver cómo queda tu cabello después de usar un aclarador."

        hide Iriehuh2
        show Iriehuhb2

        IR1 "Uh, nunca usé algo como eso. Pero, ¿qué tiene que ver eso con mi batería? "

        hide Iriehuhb2
        show Iriehuh2

        play sound "bosu36.wav"

        I5 "¡Oye, haz una voltereta con los palillos! " with vpunch

        I4 "¡Erez lizta, piénzalo! "

        I4 "Erez una adulta, ¡¿o no?! "

        hide Iriehuh2
        show Irietalk2

        IR6 "Oh, una voltereta… Entiendo, lo haré."

        hide Irietalk2
        show Iriesad2

        hide Sekinegeh2
        show Sekinesad2 at left

        hide Hisakooh
        show Hisakotalk at right

        H6 "Esto probablemente vaya a ser una pérdida de tiempo…"

        hide Hisakotalk
        show Hisakooh at right

        e "Un sentimiento de preocupación invadió la cara de Hisako."

        I4 "Sí, Hisako, no te pongaz pezada conmigo. "

        hide Hisakooh
        show Hisakotalk at right

        H9 "Ni siquiera te estoy molestando… "

        hide Hisakotalk
        show Hisakooh at right

        I5 "¡Entonce' para ya de tocar todo el twang al inicio! "

        play sound "bosu36.wav"

        I5 "¡Y buzca un aclarante de cabello! " with vpunch

        I3 "Y buzca algo que te ashude a penza' para toca' mejor. ¿Shí, mi niña?"

        hide Hisakooh
        show Hisakotalk at right

        H5 "Entonces, ¿cómo debería tocar?"

        hide Hisakotalk
        show Hisakooh at right

        I4 "Toca conmigo, amia."

        hide Hisakooh
        show Hisakotalk at right

        H2 "¿Dónde?"

        hide Hisakotalk
        show Hisakooh at right

        I5 "¡Aquí, entre el parlante y tu guitarra! Zino zuena raro, ¿entiende'? "

        play sound "bosu36.wav" 

        I4 "¡Haz ezo y todoz te amarán!" with vpunch

        I3 "Lez robaráz los corazonez, ¿entiende’? "

        hide Hisakooh
        show Hisakosmile at right

        H15 "¿Hablas en serio…? Bien, de acuerdo… ¡Empecemos de nuevo desde el inicio! "

        stop music fadeout 1.0

        hide Iriesad2
        show Iriesmile2

        IR2 "¡Bien! ¡Uno, dos! "

        scene bg black01

        play sound "bosu36.wav" 

        I5 "¡¿Canzadas ya?! ¿Cuánto llevamo' tocando? " with vpunch

        play sound "bosu36.wav" 

        I4 "Zolo tomen un rezpiro, ¡y hagan lo que digo! " with vpunch

        play sound "bosu36.wav" 

        I5 "No cuenten, ¡esto va por Pete!" with vpunch

        IR6 "Bien, um… ¡Ya! "

        e "... ...... ........... "

        e "Tsssssssssssst.~"

        e "¡Boing!"

        e "Doo-loo, doo…"

        S2 "Dwa.~"

        scene bg outside with fade

        play sound "bosu36.wav" 

        I5 "¡¿Quéééééé demonioz fue ezo?! ¡¿Qué eztan haciendo?!" with vpunch

        play sound "bosu36.wav" 

        everyone "¡Tú nos dijiste que lo hiciéramos!" with vpunch

        e "Ahí la tienen. Es nuestra Iwasawa, la maníaca de la música."

        scene bg black01 with fade

        e "Y con eso terminaron las actividades del día para las Girls Dead Monster! O Girldemo, para hacerlo más corto. "

        e "¡Y las presentaciones fueron tan solo el principio!"

        jump end

    window hide





label end:

    $ renpy.block_rollback()    

    scene bg black01
    with fade

    play music "26 - evening breeze.mp3" fadeout 1.0 fadein 1.0

    S2 "Fiu..."

    e "Suelto mi bolígrafo."

    H "¡Buen trabajo! "

    e "Mis hombros se sienten pesados de repente."

    H "Oh... eso se ve muy interesante."

    e "Esa voz… ¿Hisako?"

    scene bg dorm with fade

    e "Me doy la vuelta para encontrar a las tres en mi habitación."

    e "Miyukichi es mi compañera de cuarto, así que no hay nada de raro con que ella esté aquí."

    e "Mi cara se vuelve pálida de repente."

    show Hisakosmile with dissolve

    H15 "¿Trampas? ¿Cuándo hice algo tan vergonzoso? "

    e "Nunca la vi con una sonrisa tan enorme. Da miedo… "

    show Iriehappytalk2 at right with dissolve

    IR6 "Shiorin, ¡¿a quién estás llamando pequeña diablilla que trata a los NPCs como si fuesen juguetes?!"

    hide Iriehappytalk2 with dissolve
    show Iriesmile at right with dissolve

    e "Hasta la siempre cariñosa y tranquila Miyukichi tiene una vena exaltada en su cuello... "

    H10 "Te obligamos a hacer un diario de nuestras actividades solo porque arruinaste nuestro concierto con esa estúpida broma que hiciste. "

    H15 "¡Es solo el primer día y ya escribiste toda esta basura! ¿Acaso estás buscando una pelea?"

    e "Hunde fuertemente sus uñas en mis hombros."

    play sound "bosu36.wav" 

    S5 "¡Ay! ¡Eso duele, Hisako! " with vpunch

    hide Iriesmile with dissolve
    show Iriehappytalk2 at right with dissolve

    IR2 "Bien. Puedes seguir lastimándola, entonces."

    hide Iriehappytalk2
    show Iriesmile2 at right

    S5 "¡¿Qué?! ¡¿Tú también estás en mi contra, Miyukichi?!"

    hide Iriesmile2
    show Iriehappytalk2 at right

    IR2 "No puedo creer que hayas escrito esto de mí…"

    hide Iriehappytalk2
    show Iriehuhb at right with dissolve

    IR3 "Pero, estoy segura de que Iwasawa se llevó la peor parte…"

    IR1 "Dios, fuiste demasiado lejos."

    hide Iriehuhb
    show Iriehuh at right

    S5 "Oh, vamos… "

    hide Hisakosmile with dissolve
    hide Iriehuh with dissolve

    show Sekinegeh at right with dissolve

    e "Temblando de miedo, miro con Hisako hacia la entrada. Allí se encuentra Iwasawa de pie y en silencio. "

    show Iwasawasmile at left with dissolve

    I1 "¿Eh? ¿Qué?"

    e "Responde fríamente."

    hide Sekinegeh
    show Sekinesad at right

    S4 "Erm, ¿no lo leíste…?"

    I2 "Sí, lo hice."

    hide Sekinesad
    show Sekinetalk at right

    S5 "¿No estás enojada?"

    hide Iwasawasmile
    show Iwasawahappy at left

    I1 "¿Por qué?"

    show Sekinegeh at right

    hide Iwasawahappy
    show Iwasawacool at left

    H10 "Uh, Iwasawa… te hizo ver como una tonta."

    H15 "Con un tonto acento irlandés, también."

    H15 "Está arruinando tu imagen, ¿sabes?"

    hide Iwasawacool
    show Iwasawatalk at left

    I6 "Es su diario, puede escribir en él lo que sea que le venga en gana."

    hide Iwasawatalk
    show Iwasawahappy at left

    I1 "No me importa… Por cierto, ya terminé esa nueva canción que quería que escuchen."

    scene bg gang with fade

    I2 "Ya es muy tarde, así que directamente vine a tu habitación. Dame un segundo para prepararme y entonces te la mostraré."

    e "Coloca en el suelo el estuche que lleva a sus espaldas, toma la guitarra y comienza a tocar."

    stop music fadeout 1.0

    e "Sí, realmente es una maníaca de la música."

label finalend:
    $ renpy.block_rollback()    

    scene bg black01
    with fade

    e "Capítulo Extra 01: Fin."

    window hide dissolve
    $ show_button_game_menu = False
    with dissolve

    scene bg black01
    with fade

    $ renpy.movie_cutscene("amv 2.avi")

    scene bg black01
    with fade

    window show dissolve
    $ show_button_game_menu = True
    with dissolve
