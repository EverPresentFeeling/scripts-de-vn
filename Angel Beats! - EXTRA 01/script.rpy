



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
    show text "DisfrĂștala..."
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

    e "CapĂ­tulo Extra 01: Girl's Dead Monster."

    e "DisfrĂștenlo."

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

        S7 "ÂżPor dĂłnde deberĂ­a empezar?"

        S1 "ÂżQuĂ© de que hablĂł? "

        S1 "De mis compaĂ±eras de Girls Dead Monster. A veces nos hacemos llamar Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabĂ­as, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mĂ­a y de nadie mĂĄs."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compaĂ±eras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un dĂ­a le dije en broma a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''ÂĄEsas dos son unas monstruos! ÂĄHuye, Miyukichi! Escapa cĂłmo puedas, ÂĄno te preocupes por mĂ­!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzĂł a formar parte de nuestra banda."

        S7 "Supongo que tambiĂ©n puedo hablar un poco mĂĄs de las otras miembros..."

        S1 "Honestamente, espero que disfrutes lo que estoy por contarte."

        S3 "..."

        S2 "ÂżEmpezamos?"

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

        S7 "ÂżPor dĂłnde deberĂ­a empezar?"

        S1 "ÂżQuĂ© de que hablĂł? "

        S1 "De mis compaĂ±eras de Girls Dead Monster. A veces nos hacemos llamar Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabĂ­as, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mĂ­a y de nadie mĂĄs."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compaĂ±eras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un dĂ­a le dije en broma a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''ÂĄEsas dos son unas monstruos! ÂĄHuye, Miyukichi! Escapa cĂłmo puedas, ÂĄno te preocupes por mĂ­!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzĂł a formar parte de nuestra banda."

        S7 "Supongo que tambiĂ©n puedo hablar un poco mĂĄs de las otras miembros..."

        S1 "Honestamente, espero que disfrutes lo que estoy por contarte."

        S3 "..."

        jump set2





    elif result == "Hisako":

        $ renpy.block_rollback()    

        play music "04 - girl's hop.mp3" fadeout 1.0 fadein 1.0

        S1 "Primero se las presentarĂ©."

        S1 "EstĂĄ es Hisako-senpai."

        S1 "Y cĂłmo puedes intuir, es mi superior."

        S1 "Hisako es la guitarrista principal de nuestra banda."

        S1 "Puede parecer extraĂ±o, pero tiene un pequeĂ±o problema:"

        S1 "Ella es una jugadora compulsiva."

        S7 "Para ser mĂĄs especĂ­fica: es una jugadora compulsiva... que hace trampas."

        S7 "Un dĂ­a tuve mucha suerte y pude ver con mis propios ojos lo habilidosos que eran sus trucos."

        scene bg sunset02
        with fade

        S "Ese dĂ­a estaba jugando a las escondidas con Miyukichi. Me habĂ­a encerrado en un casillero."

        S "El sol estaba comenzando a ocultarse, asĂ­ que comencĂ© a preguntarme si debĂ­a salir."

        scene bg black01

        stop music fadeout 1.0

        play sound "bosu36.wav" 

        e "*GOLPE*" with vpunch

        scene bg sunset01
        with dissolve

        S "Las luces se encendieron. Y, una voz muy familiar entrĂł al salĂłn y dijo:"

        play sound "bosu36.wav" 

        e2 "ÂĄHagĂĄmoslo!" with vpunch

        S "Y se sentĂł cerca de una mesa."

        S "Yo pude verlo todo desde las ventilas del casillero."

        S "Me quedĂ© encerrada, no querĂ­a salir del casillero delante de tanta gente como si fuese lo mĂĄs normal del mundo."

        S "No lo sabĂ­a en ese momento, pero esa iba a ser la primera vez que verĂ­a el lado mĂĄs divertido de Hisako."

        S "Los cuatro que estaban sentados alrededor de la mesa eran Fujimaki, TK, Ooyama, y Hisako. "

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S "Ellos comenzaron mezclando y repartiendo las tablas de Mahjong."

        S "Las reglas del Mahjong son simples, tienen que formar una mano en la que tengan un par de tablas que sean iguales, y cuatro grupos de tres tablas iguales."

        S "El primero en formar una mano completa, gana. El ganador puede juntar los puntos de todos los demĂĄs."

        S "Siendo honesta, no sĂ© mucho de Mahjong. AĂșn hay muchas reglas que se me escapan."

        show Hisakotalk at right with dissolve

        H13 "ÂĄEmpecemos!"

        hide Hisakotalk
        show Hisako at right

        S "Hisako formĂł una jugada de mil puntos en la mesa, mostrando que estaba a una tabla de formar una mano completa."

        show Fujimaki2 at left with dissolve

        F2 "BienâŠ ÂĄVamos! "

        hide Hisako with dissolve
        show Hisako2 at right with dissolve

        H14 "Gano por pura suerte, tan simple que solo necesitĂ© un tiro."

        H14 "Oh, con esta Dora, todos los puntos van para mĂ­. "

        hide Hisako2
        show Hisakohng2 at right

        S "Fue como una pequeĂ±a guerra."

        S "Pero era obvio que la mano de Hisako no tenĂ­a suficientes tablas."

        S "DeberĂ­a de haber trece, pero ella solo tenĂ­a diez."

        S "Escondiendo las otras tres en su mano, ganĂł formando tres filas en vez de cuatro."

        hide Fujimaki2
        show Fujimakihah2 at left 

        F3 "TskâŠ Mierda."

        hide Fujimakihah2 with fade

        hide Hisakohng2
        show Hisako2 at right

        S "Fujimaki fue tan idiota que no se dio cuenta."

        stop music fadeout 1.0

        S "Solo le quedĂł juntar sus pequeĂ±as tablas con obediencia."

        S "La estrategia de Hisako era imbatible."

        S "Haciendo eso, siempre formarĂ­a una mano mucho mĂĄs rĂĄpido que cualquiera."

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        show TK2 at left with dissolve

        hide Hisako2 with dissolve
        show Hisakosmile at right with dissolve

        H13 "TerminĂ©. Bien, ganĂ© descartando. Ni un solo puntero, mĂĄs la Dora que estĂĄ en el medio."

        H14 "Ah, saquĂ© el mĂĄximo otra vez."

        hide TK2
        show TKyell2 at left

        play sound "bosu36.wav"

        TK1 "ÂĄAh! ÂĄFuck me! " with vpunch

        S "TK fue un poco idiota tambiĂ©n, asĂ­ que tampoco se percatĂł de ello."

        S "No sĂ© mucho de inglĂ©s, pero... para que TK diga eso, estoy segura que se enojĂł muchĂ­simo."

        stop music fadeout 1.0

        hide TKyell2 with fade

        show oyama at left with dissolve

        O2 "TerminĂ©. "

        hide Hisakosmile
        show Hisakohuh2 at right

        play music "25 - let's operation.mp3" fadeout 1.0 fadein 1.0

        S "Aunque esa vez, Ooyama casi vence a Hisako."

        S "Tan solo llegaron al tercer turno, pero..."

        S "No podĂ­a ganar incluso teniendo solo diez fichas en la mesa."

        S "Entonces, Hisako decidiĂł hacer algo aĂșn mĂĄs descarado."

        S "EscondiĂł otras tres fichas en su mano."

        S "Ahora solo quedan siete, de las cuales solo dos son puentes."

        hide Hisakohuh2 with dissolve
        show Hisakosmile at right with dissolve

        H14 "ÂĄYo tambiĂ©n terminĂ©!"

        S "Dijo sin miedo."

        S "Pero eso fue demasiado obvio. Solo tenĂ­a la mitad de las fichas a diferencia de Ooyama."

        S "Aparentemente Ooyama no lo aguantĂł mĂĄs y se quejĂł de ello."

        S "Bueno, se quejĂł lo mĂĄs fuerte que pudo hacerlo."

        hide oyama
        show Oyamatalk at left

        O1 "ÂżEstĂĄs segura que tienes trece fichas?"

        hide Hisakosmile
        show Hisakotalk at right

        H13 "SĂ­p."

        hide Hisakotalk
        show Hisakosmile at right

        hide Oyamatalk
        show Oyamageh at left

        play sound "bosu36.wav"

        stop music fadeout 1.0

        O4 "âŠ ÂĄÂżQuĂ©Ă©Ă©Ă©Ă©Ă©Ă©?!" with vpunch

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        S "Incluso desde el casillero pude oĂ­r su grito ahogado."

        S "PensĂĄndolo bien, el casillero era el escondite perfecto."

        S "Con una vista perfecta de toda la mesa.~"

        S "Pero como nadie mĂĄs dijo nada, el pobre Ooyama se quedĂł quieto y tomĂł otra ficha."

        hide Oyamageh
        show Oyamatalk at left

        play sound "bosu36.wav" 

        O3 "ÂĄQuiero ganarâŠ! ÂĄMierda! ÂĄEsta ficha no sirve! " with vpunch

        S "Pero Ă©l ya dijo que habĂ­a terminado, asĂ­ que no podĂ­a hacer nada."

        O3 "ÂĄMuĂ©vete! "

        hide Oyamatalk
        show Oyamahm at left

        hide Hisakosmile with dissolve
        show Hisakosmile2 at right with dissolve

        H11 "Oh, no servirĂĄ."

        H11 "Gano por descarte."

        hide Hisakosmile2 with dissolve
        show Hisakosmile at right with dissolve

        H11 "GanĂ© el mano a mano; todas parejas y ningĂșn puntero. Todo en una misma cadena y con dos Doras. Ah, tambiĂ©n hay que contar la Dora del medioâŠ "

        H14 "ÂżCuĂĄnto es esoâŠ? "

        H13 "Un mĂșltiplo de trece, Âżeh? Un nuevo mĂĄximo, ja. "

        stop music fadeout 1.0

        hide Oyamahm with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamahm at center with dissolve

        F2 "Oh, por DiosâŠ Eso fue genial, HisakoâŠ "

        S "Fujimaki quedĂł absolutamente asombrado. "

        hide Fujimakihah2 with dissolve
        hide Oyamahm with dissolve

        show Oyamatalk at left with dissolve

        O1 "ÂĄEspera, espera un poco! ÂĄÂżDices que eso es genial?!"

        play sound "bosu36.wav" 

        O1 "ÂĄCualquiera puede hacerlo solo con siete tablas! " with vpunch

        hide Oyamatalk
        show oyama at left

        hide Hisakosmile with dissolve
        show Hisakohng2 at right with dissolve

        H12 "Te dije que son trece. En fin, juguemos otra... ÂĄEmpecemos!"

        S "MezclĂł todas las fichas en el centro para ocultar la evidencia."

        hide oyama
        show Oyamatalk at left

        O4 "ÂĄEres una tramposa! ÂĄMuy bien, yo tambiĂ©n lo harĂ©! ÂĄTerminĂ©! "

        hide Oyamatalk
        show oyama at left

        hide Hisakohng2
        show Hisakosmile2 at right

        S "Ooyama escondiĂł tres fichas en su mano y la atacĂł con nueve tablas, teniendo una fila menos que una mano completa."

        hide oyama with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamageh at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        F3 "Espera, Ooyama, maldito estĂșpido, ÂżcuĂĄntas fichas tienes? "

        hide Oyamageh
        show oyama at center

        hide Fujimakihah2
        show Fujimakisad2 at left

        S "Fujimaki las mirĂł y empezĂł a contar."

        hide Fujimakisad2
        show Fujimakihah2 at left

        F1 "ÂżVes? ÂĄTe faltan tres! TĂș no juegas mĂĄs, idiota. "

        hide oyama
        hide Fujimakihah2
        show Oyamatalk at center
        show Fujimakisad2 at left

        play sound "bosu36.wav" 

        O4 "ÂĄÂżQuĂ© demo-?! ÂĄÂżPor quĂ© soy el Ășnico al que le sale mal?!" with vpunch

        hide Fujimakisad2 with dissolve
        hide Oyamatalk

        show oyama at left with dissolve

        S "Fue obligado a devolver la ficha que tomĂł de la pila."

        hide Hisakosmile2 with dissolve
        show Hisakolargemouth at right with dissolve

        stop music fadeout 1.0

        H13 "GanĂ© por descarte. "

        hide Hisakolargemouth
        show Hisakosmile at right

        S "Dijo Hisako. "

        O1 "ÂżEh? ÂżQuiĂ©n ganĂł por descarte? "

        hide oyama
        show Oyamageh at left

        hide Hisakosmile
        show Hisakohng at right with dissolve

        H14 "Yo ganĂ© gracias a ti. "

        play sound "bosu34.wav" 

        e "*FLOP*" with vpunch

        scene oyamaowned
        with fade

        S "Ella mostrĂł sus fichas. "

        S "Los cuatro vientos mĂĄs los tres dragones. "

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        O3 "ÂżQuĂ© demonios es esoâŠ? "

        H13 "Trece deseos, el puntaje mĂĄximo pero multiplicado por dos."

        play sound "bosu36.wav" 

        O1 "ÂĄÂżTrece deseos con solo siete tablas?! ÂĄÂżNo ven que hay algo raro?!" with vpunch

        H14 "Ah, y todo en la primera mano. Entonces serĂĄ por tres."

        play sound "bosu36.wav" 

        O4 "ÂĄÂżQuĂ©Ă©Ă©Ă©Ă©Ă©?! " with vpunch

        F1 "GuauâŠ nunca vi a alguien reunir los trece deseos en la primera manoâŠ"

        play sound "bosu36.wav" 

        O3 "ÂĄPorque es literalmente imposible!" with vpunch

        scene bg sunset01
        with fade

        S "Y con eso, Ooyama entrĂł en cĂłleraâŠ "

        show oyama at left with dissolve
        show Hisakosmile at right with dissolve

        H12 "Muy bien, entrĂ©guenme todos los boletos de comida que me deben."

        hide oyama
        show Oyamahm at left

        O4 "Oh, vamosâŠ "

        S6 "Alguien sin misericordia, con una arrogancia en su estado mĂĄs puro."

        S6 "Esa es nuestra Hisako; una embustera. La encarnaciĂłn perfecta del Diablo en persona."

        stop music fadeout 1.0

        scene bg black01
        with fade

        e "ÂĄSigamos con Irie!"

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

        S7 "ÂżPor dĂłnde empiezo?"

        S1 "ÂżQuĂ© de que hablĂł?"

        S1 "De mis compaĂ±eras de Girls Dead Monster. A veces nos llamamos Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabĂ­as, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mĂ­a y de nadie mĂĄs."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compaĂ±eras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un dĂ­a le dije bromeando a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''ÂĄEsas dos son unas monstruos! ÂĄHuye, Miyukichi! Escapa cĂłmo puedas, ÂĄno te preocupes por mĂ­!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzĂł a formar parte de nuestra banda."

        S3 "..."

        jump set2





    elif result == "Hisako":

        $ renpy.block_rollback()    

        play music "04 - girl's hop.mp3" fadeout 1.0 fadein 1.0

        S1 "Primero se las presentarĂ©."

        S1 "EstĂĄ es Hisako-senpai."

        S1 "Y cĂłmo puedes intuir, es mi superior."

        S1 "Hisako es la guitarrista principal de nuestra banda."

        S1 "Puede parecer extraĂ±o, pero tiene un pequeĂ±o problema: "

        S1 "Ella es una jugadora compulsiva."

        S7 "Para ser mĂĄs especĂ­fica: es una jugadora compulsiva... que hace trampas."

        S7 "Un dĂ­a tuve mucha suerte y pude ver con mis propios ojos lo habilidosos que eran sus trucos."

        scene bg sunset02
        with fade

        S "Ese dĂ­a estaba jugando a las escondidas con Miyukichi. Me habĂ­a encerrado en un casillero."

        S "El sol estaba comenzando a ocultarse, asĂ­ que comencĂ© a preguntarme si debĂ­a salir."

        scene bg black01

        stop music fadeout 1.0

        play sound "bosu36.wav" 

        e "*GOLPE*" with vpunch

        scene bg sunset01
        with dissolve

        S "Las luces se encendieron. Y, una voz muy familiar entrĂł al salĂłn y dijo:"

        play sound "bosu36.wav" 

        e2 "ÂĄHagĂĄmoslo!" with vpunch

        S "Y se sentĂł cerca de una mesa."

        S "Yo pude verlo todo desde las ventilas del casillero."

        S "Me quedĂ© encerrada, no querĂ­a salir del casillero delante de tanta gente como si fuese lo mĂĄs normal del mundo."

        S "No lo sabĂ­a en ese momento, pero esa iba a ser la primera vez que verĂ­a el lado mĂĄs divertido de Hisako."

        S "Los cuatro que estaban sentados alrededor de la mesa eran Fujimaki, TK, Ooyama, y Hisako. "

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S "Ellos comenzaron mezclando y repartiendo las tablas de Mahjong."

        S "Las reglas del Mahjong son simples, tienen que formar una mano en la que tengan un par de tablas que sean iguales, y cuatro grupos de tres tablas iguales."

        S "El primero en formar una mano completa, gana. El ganador puede juntar los puntos de todos los demĂĄs."

        S "Siendo honesta, no sĂ© mucho de Mahjong. AĂșn hay muchas reglas que se me escapan."

        show Hisakotalk at right with dissolve

        H13 "ÂĄEmpecemos!"

        hide Hisakotalk
        show Hisako at right

        S "Hisako formĂł una jugada de mil puntos en la mesa, mostrando que estaba a una tabla de formar una mano completa."

        show Fujimaki2 at left with dissolve

        F2 "BienâŠ ÂĄVamos! "

        hide Hisako with dissolve
        show Hisako2 at right with dissolve

        H14 "Gano por pura suerte, tan simple que solo necesitĂ© un tiro."

        H14 "Oh, con esta Dora, todos los puntos van para mĂ­. "

        hide Hisako2
        show Hisakohng2 at right

        S "Fue como una pequeĂ±a guerra."

        S "Pero era obvio que la mano de Hisako no tenĂ­a suficientes tablas."

        S "DeberĂ­a de haber trece, pero ella solo tenĂ­a diez."

        S "Escondiendo las otras tres en su mano, ganĂł formando tres filas en vez de cuatro."

        hide Fujimaki2
        show Fujimakihah2 at left 

        F3 "TskâŠ Mierda."

        hide Fujimakihah2 with fade

        hide Hisakohng2
        show Hisako2 at right

        S "Fujimaki fue tan idiota que no se dio cuenta."

        stop music fadeout 1.0

        S "Solo le quedĂł juntar sus pequeĂ±as tablas con obediencia."

        S "La estrategia de Hisako era imbatible."

        S "Haciendo eso, siempre formarĂ­a una mano mucho mĂĄs rĂĄpido que cualquiera."

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        show TK2 at left with dissolve

        hide Hisako2 with dissolve
        show Hisakosmile at right with dissolve

        H13 "TerminĂ©. Bien, ganĂ© descartando. Ni un solo puntero, mĂĄs la Dora que estĂĄ en el medio."

        H14 "Ah, saquĂ© el mĂĄximo otra vez."

        hide TK2
        show TKyell2 at left

        play sound "bosu36.wav"

        TK1 "ÂĄAh! ÂĄFuck me! " with vpunch

        S "TK fue un poco idiota tambiĂ©n, asĂ­ que tampoco se percatĂł de ello."

        S "No sĂ© mucho de inglĂ©s, pero... para que TK diga eso, estoy segura que se enojĂł muchĂ­simo."

        stop music fadeout 1.0

        hide TKyell2 with fade

        show oyama at left with dissolve

        O2 "TerminĂ©. "

        hide Hisakosmile
        show Hisakohuh2 at right

        play music "25 - let's operation.mp3" fadeout 1.0 fadein 1.0

        S "Aunque esa vez, Ooyama casi vence a Hisako."

        S "Tan solo llegaron al tercer turno, pero..."

        S "No podĂ­a ganar incluso teniendo solo diez fichas en la mesa."

        S "Entonces, Hisako decidiĂł hacer algo aĂșn mĂĄs descarado."

        S "EscondiĂł otras tres fichas en su mano."

        S "Ahora solo quedan siete, de las cuales solo dos son puentes."

        hide Hisakohuh2 with dissolve
        show Hisakosmile at right with dissolve

        H14 "ÂĄYo tambiĂ©n terminĂ©!"

        S "Dijo sin miedo."

        S "Pero eso fue demasiado obvio. Solo tenĂ­a la mitad de las fichas a diferencia de Ooyama."

        S "Aparentemente Ooyama no lo aguantĂł mĂĄs y se quejĂł de ello."

        S "Bueno, se quejĂł lo mĂĄs fuerte que pudo hacerlo."

        hide oyama
        show Oyamatalk at left

        O1 "ÂżEstĂĄs segura que tienes trece fichas?"

        hide Hisakosmile
        show Hisakotalk at right

        H13 "SĂ­p."

        hide Hisakotalk
        show Hisakosmile at right

        hide Oyamatalk
        show Oyamageh at left

        play sound "bosu36.wav"

        stop music fadeout 1.0

        O4 "âŠ ÂĄÂżQuĂ©Ă©Ă©Ă©Ă©Ă©Ă©?!" with vpunch

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        S "Incluso desde el casillero pude oĂ­r su grito ahogado."

        S "PensĂĄndolo bien, el casillero era el escondite perfecto."

        S "Con una vista perfecta de toda la mesa.~"

        S "Pero como nadie mĂĄs dijo nada, el pobre Ooyama se quedĂł quieto y tomĂł otra ficha."

        hide Oyamageh
        show Oyamatalk at left

        play sound "bosu36.wav" 

        O3 "ÂĄQuiero ganarâŠ! ÂĄMierda! ÂĄEsta ficha no sirve! " with vpunch

        S "Pero Ă©l ya dijo que habĂ­a terminado, asĂ­ que no podĂ­a hacer nada."

        O3 "ÂĄMuĂ©vete! "

        hide Oyamatalk
        show Oyamahm at left

        hide Hisakosmile with dissolve
        show Hisakosmile2 at right with dissolve

        H11 "Oh, no servirĂĄ."

        H11 "Gano por descarte."

        hide Hisakosmile2 with dissolve
        show Hisakosmile at right with dissolve

        H11 "GanĂ© el mano a mano; todas parejas y ningĂșn puntero. Todo en una misma cadena y con dos Doras. Ah, tambiĂ©n hay que contar la Dora del medioâŠ "

        H14 "ÂżCuĂĄnto es esoâŠ? "

        H13 "Un mĂșltiplo de trece, Âżeh? Un nuevo mĂĄximo, ja. "

        stop music fadeout 1.0

        hide Oyamahm with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamahm at center with dissolve

        F2 "Oh, por DiosâŠ Eso fue genial, HisakoâŠ "

        S "Fujimaki quedĂł absolutamente asombrado. "

        hide Fujimakihah2 with dissolve
        hide Oyamahm with dissolve

        show Oyamatalk at left with dissolve

        O1 "ÂĄEspera, espera un poco! ÂĄÂżDices que eso es genial?!"

        play sound "bosu36.wav" 

        O1 "ÂĄCualquiera puede hacerlo solo con siete tablas! " with vpunch

        hide Oyamatalk
        show oyama at left

        hide Hisakosmile with dissolve
        show Hisakohng2 at right with dissolve

        H12 "Te dije que son trece. En fin, juguemos otra... ÂĄEmpecemos!"

        S "MezclĂł todas las fichas en el centro para ocultar la evidencia."

        hide oyama
        show Oyamatalk at left

        O4 "ÂĄEres una tramposa! ÂĄMuy bien, yo tambiĂ©n lo harĂ©! ÂĄTerminĂ©! "

        hide Oyamatalk
        show oyama at left

        hide Hisakohng2
        show Hisakosmile2 at right

        S "Ooyama escondiĂł tres fichas en su mano y la atacĂł con nueve tablas, teniendo una fila menos que una mano completa."

        hide oyama with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamageh at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        F3 "Espera, Ooyama, maldito estĂșpido, ÂżcuĂĄntas fichas tienes? "

        hide Oyamageh
        show oyama at center

        hide Fujimakihah2
        show Fujimakisad2 at left

        S "Fujimaki las mirĂł y empezĂł a contar."

        hide Fujimakisad2
        show Fujimakihah2 at left

        F1 "ÂżVes? ÂĄTe faltan tres! TĂș no juegas mĂĄs, idiota. "

        hide oyama
        hide Fujimakihah2
        show Oyamatalk at center
        show Fujimakisad2 at left

        play sound "bosu36.wav" 

        O4 "ÂĄÂżQuĂ© demo-?! ÂĄÂżPor quĂ© soy el Ășnico al que le sale mal?!" with vpunch

        hide Fujimakisad2 with dissolve
        hide Oyamatalk

        show oyama at left with dissolve

        S "Fue obligado a devolver la ficha que tomĂł de la pila."

        hide Hisakosmile2 with dissolve
        show Hisakolargemouth at right with dissolve

        stop music fadeout 1.0

        H13 "GanĂ© por descarte. "

        hide Hisakolargemouth
        show Hisakosmile at right

        S "Dijo Hisako. "

        O1 "ÂżEh? ÂżQuiĂ©n ganĂł por descarte? "

        hide oyama
        show Oyamageh at left

        hide Hisakosmile
        show Hisakohng at right with dissolve

        H14 "Yo ganĂ© gracias a ti. "

        play sound "bosu34.wav" 

        e "*FLOP*" with vpunch

        scene oyamaowned
        with fade

        S "Ella mostrĂł sus fichas. "

        S "Los cuatro vientos mĂĄs los tres dragones. "

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        O3 "ÂżQuĂ© demonios es esoâŠ? "

        H13 "Trece deseos, el puntaje mĂĄximo pero multiplicado por dos."

        play sound "bosu36.wav" 

        O1 "ÂĄÂżTrece deseos con solo siete tablas?! ÂĄÂżNo ven que hay algo raro?!" with vpunch

        H14 "Ah, y todo en la primera mano. Entonces serĂĄ por tres."

        play sound "bosu36.wav" 

        O4 "ÂĄÂżQuĂ©Ă©Ă©Ă©Ă©Ă©?! " with vpunch

        F1 "GuauâŠ nunca vi a alguien reunir los trece deseos en la primera manoâŠ"

        play sound "bosu36.wav" 

        O3 "ÂĄPorque es literalmente imposible!" with vpunch

        scene bg sunset01
        with fade

        S "Y con eso, Ooyama entrĂł en cĂłleraâŠ "

        show oyama at left with dissolve
        show Hisakosmile at right with dissolve

        H12 "Muy bien, entrĂ©guenme todos los boletos de comida que me deben."

        hide oyama
        show Oyamahm at left

        O4 "Oh, vamosâŠ "

        S6 "Alguien sin misericordia, con una arrogancia en su estado mĂĄs puro."

        S6 "Esa es nuestra Hisako; una embustera. La encarnaciĂłn perfecta del Diablo en persona."

        stop music fadeout 1.0

        scene bg black01
        with fade

        jump set3





    elif result == "Irie":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        e "La siguiente es nuestra baterista, Irie; aunque nosotras la llamamos Miyukichi. Se uniĂł a la banda al mismo tiempo que yo."

        e "Si Hisako era el Diablo, entonces Miyukichi es su versiĂłn en miniatura."

        e "Es muy dĂ©bil fĂ­sicamente, pero realmente es una demonio. Suele tentar a los demĂĄs estudiantes, los NPCs, a hacer cosas muy peligrosas solo para ver hasta dĂłnde puede influenciarlos. Verdaderamente es una demonio."

        scene bg corridoor2
        with fade

        show Sekinesad at center with dissolve
        show Iriesmile at left with dissolve

        play music "15 - study time.mp3" fadeout 1.0 fadein 1.0

        IR6 "Oye, oye, Âżconoces a ese chico, uhâŠ Kinoshita, el NPC? ÂĄPues Ă©l... estĂĄ enamorado de mĂ­!"

        IR6 "Cuando estĂĄbamos en clase, ÂĄcruzamos miradas y su cara se volviĂł completamente roja!"

        show Iriesmileb at left

        IR3 "ÂĄOh, por Dios, es muy obvio! "

        e "Un dĂ­a se jacto de ello."

        hide Iriesmileb
        show Iriesmile at left

        IR6 "AsĂ­ que ayer, le dije que a mĂ­ me gustaban mĂĄs los chicos, eh... 'rebeldes'; como los de esas series de los 90s. Cuando lo vi hoy por la maĂ±ana, ÂĄestaba usando unos pantalones holgados!"

        IR1 "ÂĄNo estoy mintiendo! "

        hide Iriesmile
        show Iriehappytalk at left

        IR6 "ÂĄEstaba usando su chaqueta del uniforme con esos pantalones holgados! ÂĄOh, por Dios, no podĂ­a parar de reĂ­rme!"

        IR2 "Estos NPCs son demasiado geniales."

        IR2 "ÂĄÂżCĂłmo se las arreglĂł para conseguirlos?!"

        IR2 "ÂżSe desvelĂł haciĂ©ndolos?"

        IR6 "Cuando me vio empezĂł a actuar salvajemente. 'ÂżQuĂ© miran, idiotas?' , fue lo que dijo a todos sus compaĂ±eros. ÂĄPero era obvio que con eso solo lo mirarĂ­an mĂĄs! "

        play sound "bosu36.wav" 

        IR "ÂĄJa, ja, ja, ja!" with vpunch

        hide Iriehappytalk
        show Irie at left

        IR2 "ÂĄLo mĂĄs gracioso de todo es que lo hizo para tratar de conquistarme!"

        scene bg corridoor1
        with dissolve

        show Irie at center with dissolve

        e "PodrĂ­amos ser amigas de Ă©l, pero tenĂ­amos que decĂ­rselo apropiadamente."

        e "Incluso si eran NPCs, me sentĂ­a mal por ellos."

        hide Irie
        show Irie2 with dissolve

        IR4 "Entonces, Shiorin, ÂżquĂ© deberĂ­amos pedirle ahora? HarĂĄ cualquier cosa, ÂĄestoy segura de ello!"

        show Sekinetalkangry at right with dissolve

        S6 "Dios, Miyukichi, Âżno sabes cuĂĄndo parar?"

        S6 "Ya lo molestaste demasiado."

        hide Sekinetalkangry
        show Sekineangry at right

        e "IntentĂ© provocar alguna pizca de piedad en ella."

        e "Era tan humana como todos nosotros, asĂ­ que supuse que debĂ­a tenerla en alguna parte."

        hide Irie2 with dissolve
        show Irietalk at left with dissolve

        IR6 "ÂżPero no te da curiosidad quĂ© tan lejos pueden llegar? DespuĂ©s de todo, ÂĄsomos espĂ­as del escuadrĂłn del mĂĄs allĂĄ!"

        hide Irietalk
        show Iriesmile at left

        e "ÂżDesde cuĂĄndo te volviste una espĂ­a?"

        e "ÂżY quĂ© es eso del escuadrĂłn del mĂĄs allĂĄ?"

        e "QuĂ© nombre mĂĄs raro... "

        e "ÂżAcaso intentaste darle tu propia versiĂłn a la SSS?"

        e "Aunque, la SSS siempre la integraron un montĂłn de idiotas."

        e "Es imposible que lleguen a tener miembros tan inteligentes como yo o Miyukichi."

        hide Iriesmile
        show Iriehappytalk at left 

        IR4 "ÂĄÂżQuĂ© te parece un afro?! Si le digo que a mĂ­ me gustan los chicos que tienen un afro, ÂĄestoy segura que maĂ±ana vendrĂĄ con uno! ÂĄOh, por Dios, no puedo parar de reĂ­r! "

        hide Iriehappytalk
        show Iriesmileb at left 

        hide Sekineangry
        show Sekinetalk at right

        S7 "DeberĂ­as dejarlo. Los pantalones holgados ya fueron mĂĄs que suficiente."

        S7 "Un poco mĂĄs y creo que enfadarĂĄs al pobre NPC."

        hide Sekinetalk
        show Sekine at right

        hide Iriesmileb
        show Iriehuh2 at left with dissolve

        stop music fadeout 1.0

        IR4 "ÂĄPero ese es el punto!"

        IR4 "ÂĄQuiero saber hasta dĂłnde pueden llegar!"

        IR4 "EstĂĄ bien, me decidĂ­. ÂĄMaĂ±ana, Kinoshita tendrĂĄ un afro! "

        scene bg black01
        with fade

        e "Al dĂ­a siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekine at left with dissolve

        play sound "bosu36.wav" 

        IR "ÂĄOh, por Dios, ese es Kinoshita!" with vpunch

        hide Sekine with dissolve
        show Sekine2 at left with dissolve

        e "QuerĂ­a practicar mi bajo en paz, asĂ­ que me fui a un aula vacĂ­a. Cuando, Miyukichi entrĂł corriendo al salĂłn."

        e "Luego de que finalmente parara de reĂ­r, ella dijo:"

        show Iriehappytalk at right with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        IR2 "ÂĄLo hizo, vino con un maldito afro! ÂĄNo te estoy mintiendo! ÂĄDios, no tenĂ­a idea de que nuestra escuela tuviese a un peluquero con tanto talento! ÂĄQuĂ© desperdicio! " with vpunch

        e "De hecho, estoy segura de que eso es imposible. No importa lo que hagas, no puedes hacerte crecer un afro en solo una noche."

        hide Iriehappytalk
        show Iriesmile at right 

        hide Sekine2
        show Sekinetalk2 at left

        S3 "Yo tambiĂ©n lo vi, era muy fĂĄcil de identificar. Pude adivinar quiĂ©n era apenas me lo crucĂ© por el pasillo; pobre chico."

        hide Sekinetalk2
        show Sekine2 at left

        hide Iriesmile with dissolve
        show Iriesmile2 at right with dissolve

        IR6 "Entonces, ÂżquĂ© sigue? ÂĄĂl verdaderamente harĂĄ cualquier cosa que le pida!"

        IR6 "ÂĄOh, por Dios, es demasiado gracioso!"

        hide Iriesmile2 with dissolve
        show Iriesmileb2 at center with dissolve

        show Sekinetalkangry2 at left 

        stop music fadeout 1.0

        S4 "SĂ­âŠ ÂżQuĂ© pasĂł con tu meta principal? Ahora lo Ășnico que quieres es reĂ­rte."

        show Sekineangry2 at left

        scene bg corridoor3
        with fade

        show Iriehappytalk at center with dissolve

        play music "27 - moment of rest.mp3" fadeout 1.0 fadein 1.0

        IR6 "ÂĄNo, no es asĂ­! Esto es algo verdaderamente serioâŠ Je, je, je.~"

        hide Iriehappytalk
        show Iriesmile

        e "Es muy difĂ­cil de creer cuando lo dices tĂș, Âżsabes?"

        scene bg corridoor1
        with dissolve

        show Iriesmileb at center with dissolve

        IR3 "Oye, la prĂłxima vez... ÂĄÂżQuĂ© te parece si le pido que se ponga brochetas en su afro?!"

        hide Iriesmileb with dissolve
        show Iriesmileb2 at center with dissolve

        IR3 "El cafĂ© harĂĄ brochetas esta noche."

        IR6 "ÂĄAsĂ­ que haremos que Ă©l aparezca con un montĂłn de ellas en su afro!"

        IR2 "Je, je, je.~"

        scene bg corridoor2
        with dissolve

        show Sekinesad at right with dissolve
        show Irie at center with dissolve

        S4 "Al menos el afro es un estilo de verdad, Âżpero brochetas?"

        show Sekinetalk at right

        S4 "ÂżCĂłmo piensas pedĂ­rselo?"

        show Sekine at right

        hide Irie with dissolve
        show Iriehappytalk2 at left with dissolve

        IR2 "FĂĄcil. Cuando me lo encuentre le dirĂ© algo como... "

        IR2 "Oh, si tan solo tuvieras algunas brochetas en tu afro, Kinoshita.~ Se que caerĂ­a rendida a los pies de cualquiera que lo tuviese asĂ­.~ Ah, llevo fijĂĄndome en ti desde hace mucho tiempo.~ Je, je, je.~"

        hide Iriehappytalk2
        show Iriesmile2 at left 

        show Sekinesad

        stop music fadeout 1.0

        e "QuĂ© mujerâŠ "

        scene bg black01
        with fade

        e "Y luego de que se fuera, seguĂ­ practicando en el aula."

        e "Al dĂ­a siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekinesad with dissolve

        play sound "bosu36.wav" 

        IR "ÂĄOh, por Dios! ÂĄOh, por Dios! ÂĄDe verdad se clavĂł brochetas en su afro!" with vpunch

        scene bg irie
        with fade

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        e "Estaba a punto de estallar en lĂĄgrimas de risa. No tengo dudas de que se rio en todo el camino hasta aquĂ­."

        S7 "SĂ­, lo vi. Te creo."

        IR3 "Es genial, ÂĄÂżverdad?! Y uno de sus amigos le dijo: 'ÂĄDame una!' Pero el respondiĂł enojado: 'ÂĄNo me toques!' ÂĄJA, JA, JA, JA, JA! ÂĄSantos cielos!"

        S3 "Entonces, Âżte comiste una? "

        IR2 "ÂĄIugh, claro que no! ÂĄEran de ayer y estaban muy frĂ­as!"

        IR2 "ÂĄY estoy segura que fue al baĂ±o con ellas! ÂĄAsqueroso!"

        scene bg Emptyclassroom
        with fade

        show Sekinesad2 with dissolve
        show Iriesmileb at right with dissolve

        stop music fadeout 1.0

        e "Oh, hombre. Miyukichi fue demasiado lejosâŠ "

        e "Este mundo transforma a las personasâŠ "

        e "Y, a pesar de todo, aĂșn hay gente que se toma la vida en serio y hacen lo imposible para pelear contra Dios."

        scene bg class1
        with fade

        IR4 "ÂĄOooh, hagamos que maĂ±ana camine con uno de esos aros de nataciĂłn!"

        IR6 "No los usarĂĄ para nadar, ÂĄpero estoy segura que andarĂĄ por todos lados con eso!"

        IR2 "ÂĄPantalones holgados, un afro con brochetas clavadas en Ă©l y un aro de nataciĂłn!"

        IR2 "ÂĄJA, JA! ÂĄEse NPC tendrĂĄ mucha mĂĄs personalidad que todos nosotros!"

        scene bg black01

        play sound "hit_p07.wav" 

        e "*GOLPE* " with vpunch

        scene bg Emptyclassroom
        with fade

        show Iriehuhb2 at right with dissolve

        IR "ÂĄ...!"

        e "Le di una bofetada con todas mis fuerzas."

        e "Miyukichi mantuvo su mirada fija, mirando a la nada."

        e "Se quedĂł completamente paralizada."

        show Sekinetalkangry2 at center with dissolve

        play sound "bosu36.wav" 

        S6 "QuizĂĄs los NPCs no tengan un alma como sĂ­ tenemos nosotros, ÂĄpero siguen siendo personas! " with vpunch

        S6 "ÂĄEllos tienen sentimientos! Y por encima de todo, ÂĄKinoshita es demasiado dulce e inocente!"

        S6 "A menos que le pidas que se suicide, ÂĄestoy segura que harĂĄ cualquier cosa que le pidas!"

        S3 "ÂĄPero todo lo que haces es aprovecharte de eso y sigues burlĂĄndote de Ă©l! ÂĄÂżNo tienes vergĂŒenza?!"

        hide Sekinetalkangry2 with dissolve
        show Sekineangry with dissolve

        hide Iriehuhb2
        show Iriehuh2 at right

        IR5 "P- PeroâŠ pensĂ© que tĂș tambiĂ©n estabas divirtiĂ©ndoteâŠ "

        hide Iriehuh2
        show Iriehuhb at right

        hide Sekinetalkangry2
        hide Sekineangry
        show Sekineyellangry2

        play sound "bosu36.wav" 

        S6 "ÂĄÂżCĂłmo podrĂ­a divertirme con algo asĂ­?! " with vpunch

        S6 "ÂĄKinoshita es mucho mĂĄs humano que tĂș! "

        show Sekineangry2

        hide Iriehuhb
        show Iriesad at right with dissolve

        e "Su rostro se oscureciĂł de repente."

        e "Para cualquier integrante de la SSS, ser comparado con un NPC es mucho mĂĄs ofensivo que cualquier otro insulto que te puedas imaginar."

        IR5 "ÂżTĂș creesâŠ que un NPC es mejor persona que yo...?"

        hide Sekineangry2
        show Sekinetalkangry2

        S7 "SĂ­. Y creo que deberĂ­as pensar sobre ello."

        hide Sekinetalkangry2
        show Sekineangry2

        IR5 "S- SollozoâŠ "

        e "Los hombros de Miyukichi comenzaron a temblarâŠ"

        hide Iriesad with dissolve

        play sound "bosu36.wav" 

        IR "ÂĄGuaaaaaah!" with vpunch

        show Sekineangry2 with fade

        e "SaliĂł corriendo mientras cubrĂ­a su rostro con sus manos."

        show Sekinetalkangry2

        S4 "SheeshâŠ "

        hide Sekinetalkangry2

        scene bg Concerthall
        with fade

        e "MĂĄs tarde, se lo expliquĂ© todo a Kinoshita."

        e "Ocultando la parte de que era un NPC, obviamente."

        e "Incluso si lo hubiera hecho, se habrĂ­a confundido tanto que olvidarĂ­a todo lo que le dije."

        show Sekine with dissolve

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        S7 "Lo siento."

        hide Sekine
        show Sekinetalk

        S1 "Hiciste absolutamente todo lo que te pidiĂł, pero esto se te fue de las manos."

        hide Sekinetalk
        show Sekine

        K "Entonces, eso significa queâŠ yo fui el Ășnico que sintiĂł amor de verdadâŠ "

        e "No apartĂł la mirada del suelo, completamente abatido. "

        hide Sekine
        show Sekinesad

        S3 "SĂ­âŠ supongo que tienes razĂłnâŠ "

        K "Ya veo, pero no voy a llorar por esto. Porque, ÂĄencontrĂ© a mi nuevo amor!"

        e "Sus ojos brillaron cĂłmo nunca antes y alzĂł a lo alto su puĂ±o cerrado."

        hide Sekinesad
        show Sekinesmile

        S1 "ÂżEh? ÂĄEso es genial!"

        K "ÂĄTĂș!"

        hide Sekinesmile
        show Sekinegeh

        stop music fadeout 1.0

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        S5 "ÂĄÂżQuĂ©?! ÂĄÂżYo?! " with vpunch

        K "ÂĄSĂ­, tĂș! ÂĄTĂș siempre te preocupaste por un pobre sujeto como yo! "

        K "ÂĄEstoy verdaderamente enamorado de ti! "

        hide Sekinegeh
        show Sekinegeh2

        S5 "ÂżD- De verdad?"

        K "ÂĄPor favor, salga conmigo, seĂ±orita Sekine!"

        hide Sekinegeh2
        show Sekinesad

        S5 "Espera, no estoy segura de estoâŠ"

        K "ÂĄÂżTe gustan los afros?! ÂżO brochetas? ÂĄQuizĂĄs te vayan los chicos rebeldes!"

        hide Sekinesad
        show Sekinegeh

        S5 "No, uhâŠ a mĂ­ no me van todas esas cosas rarasâŠ "

        K "ÂĄÂżEntonces te gusto tal y cĂłmo soy?! " with vpunch

        hide Sekinegeh
        show Sekinegeh2

        stop music fadeout 1.0

        S5 "UhâŠ esperaâŠ eso no es lo queâŠ ÂĄAdiĂłs! "

        hide Sekinegeh2 with dissolve

        e "EscapĂ© lo mĂĄs rĂĄpido que pude." with vpunch

        scene bg black01
        with fade

        e "Al final, Miyukichi no era tan malvada como yo creĂ­a; tan solo disfrutaba demasiado jugando con los pobres NPCs. Aunque no se puede negar que es cruel."

        e "Y por Ășltimo, nos queda Iwasawa."

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

        S7 "ÂżPor dĂłnde empiezo?"

        S1 "ÂżQuĂ© de que hablo? "

        S1 "De mis compaĂ±eras de Girls Dead Monster. A veces lo llamamos Girl-De-Mo."

        scene bg sekine
        with fade

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        show Sekinetalk with dissolve

        S2 "Si no lo sabĂ­as, Girls Dead Monster es el nombre de la banda de rock en la que yo, Sekine, toco el bajo."

        S2 "Si tampoco sabes lo que es eso..."

        S2 "Digamos que es la segunda guitarra que apoya al guitarrista principal."

        S1 "Y esa es, Hisako-senpai."

        hide Sekinetalk with dissolve
        show Sekinesmile at right with dissolve

        S1 "En fin, el nombre de la banda 'Girls Dead Monster' fue idea mĂ­a y de nadie mĂĄs."

        scene bg sekine2
        with fade

        show Sekinetalkangry at right with dissolve

        show Iwasawa at center with dissolve
        show Hisako at left with dissolve

        S7 "Cuando empezamos a tocar, mis compaĂ±eras, Iwasawa y Hisako, daban miedo con lo estrictas que eran."

        hide Sekinetalkangry with dissolve

        scene bg sekine3
        with fade

        show Irie at right with dissolve
        show Sekine2 at left with dissolve

        S1 "Entonces un dĂ­a le dije bromeando a Irie, nuestra baterista, algo muy tonto: "

        hide Sekine2
        show Sekinetalkangry2 at left

        S6 "''ÂĄEsas dos son unas monstruos! ÂĄHuye, Miyukichi! Escapa cĂłmo puedas, ÂĄno te preocupes por mĂ­!'''"

        stop music fadeout 1.0

        scene bg black01
        with fade

        S1 "Y por esa broma la palabra 'Monsters' comenzĂł a formar parte de nuestra banda."

        S3 "..."

        jump set2





    elif result == "Hisako":

        $ renpy.block_rollback()    

        play music "04 - girl's hop.mp3" fadeout 1.0 fadein 1.0

        S1 "Primero se las presentarĂ©. "

        S1 "EstĂĄ es Hisako-senpai."

        S1 "Y cĂłmo puedes intuir, es mi superior."

        S1 "Hisako es la guitarrista principal de nuestra banda."

        S1 "Puede parecer extraĂ±o, pero tiene un pequeĂ±o problema: "

        S1 "Ella es una jugadora compulsiva."

        S7 "Para ser mĂĄs especĂ­fica: es una jugadora compulsiva... que hace trampas."

        S7 "Un dĂ­a tuve mucha suerte y pude ver con mis propios ojos lo habilidosos que eran sus trucos."

        scene bg sunset02
        with fade

        S "Ese dĂ­a estaba jugando a las escondidas con Miyukichi. Me habĂ­a encerrado en un casillero."

        S "El sol estaba comenzando a ocultarse, asĂ­ que comencĂ© a preguntarme si debĂ­a salir."

        scene bg black01

        stop music fadeout 1.0

        play sound "bosu36.wav" 

        e "*GOLPE*" with vpunch

        scene bg sunset01
        with dissolve

        S "Las luces se encendieron. Y, una voz muy familiar entrĂł al salĂłn y dijo:"

        play sound "bosu36.wav" 

        e2 "ÂĄHagĂĄmoslo!" with vpunch

        S "Y se sentĂł cerca de una mesa."

        S "Yo pude verlo todo desde las ventilas del casillero."

        S "Me quedĂ© encerrada, no querĂ­a salir del casillero delante de tanta gente como si fuese lo mĂĄs normal del mundo."

        S "No lo sabĂ­a en ese momento, pero esa iba a ser la primera vez que verĂ­a el lado mĂĄs divertido de Hisako."

        S "Los cuatro que estaban sentados alrededor de la mesa eran Fujimaki, TK, Ooyama, y Hisako. "

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S "Ellos comenzaron mezclando y repartiendo las tablas de Mahjong."

        S "Las reglas del Mahjong son simples, tienen que formar una mano en la que tengan un par de tablas que sean iguales, y cuatro grupos de tres tablas iguales."

        S "El primero en formar una mano completa, gana. El ganador puede juntar los puntos de todos los demĂĄs."

        S "Siendo honesta, no sĂ© mucho de Mahjong. AĂșn hay muchas reglas que se me escapan."

        show Hisakotalk at right with dissolve

        H13 "ÂĄEmpecemos!"

        hide Hisakotalk
        show Hisako at right

        S "Hisako formĂł una jugada de mil puntos en la mesa, mostrando que estaba a una tabla de formar una mano completa."

        show Fujimaki2 at left with dissolve

        F2 "BienâŠ ÂĄVamos! "

        hide Hisako with dissolve
        show Hisako2 at right with dissolve

        H14 "Gano por pura suerte, tan simple que solo necesitĂ© un tiro."

        H14 "Oh, con esta Dora, todos los puntos van para mĂ­. "

        hide Hisako2
        show Hisakohng2 at right

        S "Fue como una pequeĂ±a guerra."

        S "Pero era obvio que la mano de Hisako no tenĂ­a suficientes tablas."

        S "DeberĂ­a de haber trece, pero ella solo tenĂ­a diez."

        S "Escondiendo las otras tres en su mano, ganĂł formando tres filas en vez de cuatro."

        hide Fujimaki2
        show Fujimakihah2 at left 

        F3 "TskâŠ Mierda."

        hide Fujimakihah2 with fade

        hide Hisakohng2
        show Hisako2 at right

        S "Fujimaki fue tan idiota que no se dio cuenta."

        stop music fadeout 1.0

        S "Solo le quedĂł juntar sus pequeĂ±as tablas con obediencia."

        S "La estrategia de Hisako era imbatible."

        S "Haciendo eso, siempre formarĂ­a una mano mucho mĂĄs rĂĄpido que cualquiera."

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        show TK2 at left with dissolve

        hide Hisako2 with dissolve
        show Hisakosmile at right with dissolve

        H13 "TerminĂ©. Bien, ganĂ© descartando. Ni un solo puntero, mĂĄs la Dora que estĂĄ en el medio."

        H14 "Ah, saquĂ© el mĂĄximo otra vez."

        hide TK2
        show TKyell2 at left

        play sound "bosu36.wav"

        TK1 "ÂĄAh! ÂĄFuck me! " with vpunch

        S "TK fue un poco idiota tambiĂ©n, asĂ­ que tampoco se percatĂł de ello."

        S "No sĂ© mucho de inglĂ©s, pero... para que TK diga eso, estoy segura que se enojĂł muchĂ­simo."

        stop music fadeout 1.0

        hide TKyell2 with fade

        show oyama at left with dissolve

        O2 "TerminĂ©. "

        hide Hisakosmile
        show Hisakohuh2 at right

        play music "25 - let's operation.mp3" fadeout 1.0 fadein 1.0

        S "Aunque esa vez, Ooyama casi vence a Hisako."

        S "Tan solo llegaron al tercer turno, pero..."

        S "No podĂ­a ganar incluso teniendo solo diez fichas en la mesa."

        S "Entonces, Hisako decidiĂł hacer algo aĂșn mĂĄs descarado."

        S "EscondiĂł otras tres fichas en su mano."

        S "Ahora solo quedan siete, de las cuales solo dos son puentes."

        hide Hisakohuh2 with dissolve
        show Hisakosmile at right with dissolve

        H14 "ÂĄYo tambiĂ©n terminĂ©!"

        S "Dijo sin miedo."

        S "Pero eso fue demasiado obvio. Solo tenĂ­a la mitad de las fichas a diferencia de Ooyama."

        S "Aparentemente Ooyama no lo aguantĂł mĂĄs y se quejĂł de ello."

        S "Bueno, se quejĂł lo mĂĄs fuerte que pudo hacerlo."

        hide oyama
        show Oyamatalk at left

        O1 "ÂżEstĂĄs segura que tienes trece fichas?"

        hide Hisakosmile
        show Hisakotalk at right

        H13 "SĂ­p."

        hide Hisakotalk
        show Hisakosmile at right

        hide Oyamatalk
        show Oyamageh at left

        play sound "bosu36.wav"

        stop music fadeout 1.0

        O4 "âŠ ÂĄÂżQuĂ©Ă©Ă©Ă©Ă©Ă©Ă©?!" with vpunch

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        S "Incluso desde el casillero pude oĂ­r su grito ahogado."

        S "PensĂĄndolo bien, el casillero era el escondite perfecto."

        S "Con una vista perfecta de toda la mesa.~"

        S "Pero como nadie mĂĄs dijo nada, el pobre Ooyama se quedĂł quieto y tomĂł otra ficha."

        hide Oyamageh
        show Oyamatalk at left

        play sound "bosu36.wav" 

        O3 "ÂĄQuiero ganarâŠ! ÂĄMierda! ÂĄEsta ficha no sirve! " with vpunch

        S "Pero Ă©l ya dijo que habĂ­a terminado, asĂ­ que no podĂ­a hacer nada."

        O3 "ÂĄMuĂ©vete! "

        hide Oyamatalk
        show Oyamahm at left

        hide Hisakosmile with dissolve
        show Hisakosmile2 at right with dissolve

        H11 "Oh, no servirĂĄ."

        H11 "Gano por descarte."

        hide Hisakosmile2 with dissolve
        show Hisakosmile at right with dissolve

        H11 "GanĂ© el mano a mano; todas parejas y ningĂșn puntero. Todo en una misma cadena y con dos Doras. Ah, tambiĂ©n hay que contar la Dora del medioâŠ "

        H14 "ÂżCuĂĄnto es esoâŠ? "

        H13 "Un mĂșltiplo de trece, Âżeh? Un nuevo mĂĄximo, ja. "

        stop music fadeout 1.0

        hide Oyamahm with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamahm at center with dissolve

        F2 "Oh, por DiosâŠ Eso fue genial, HisakoâŠ "

        S "Fujimaki quedĂł absolutamente asombrado. "

        hide Fujimakihah2 with dissolve
        hide Oyamahm with dissolve

        show Oyamatalk at left with dissolve

        O1 "ÂĄEspera, espera un poco! ÂĄÂżDices que eso es genial?!"

        play sound "bosu36.wav" 

        O1 "ÂĄCualquiera puede hacerlo solo con siete tablas! " with vpunch

        hide Oyamatalk
        show oyama at left

        hide Hisakosmile with dissolve
        show Hisakohng2 at right with dissolve

        H12 "Te dije que son trece. En fin, juguemos otra... ÂĄEmpecemos!"

        S "MezclĂł todas las fichas en el centro para ocultar la evidencia."

        hide oyama
        show Oyamatalk at left

        O4 "ÂĄEres una tramposa! ÂĄMuy bien, yo tambiĂ©n lo harĂ©! ÂĄTerminĂ©! "

        hide Oyamatalk
        show oyama at left

        hide Hisakohng2
        show Hisakosmile2 at right

        S "Ooyama escondiĂł tres fichas en su mano y la atacĂł con nueve tablas, teniendo una fila menos que una mano completa."

        hide oyama with dissolve

        show Fujimakihah2 at left with dissolve
        show Oyamageh at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        F3 "Espera, Ooyama, maldito estĂșpido, ÂżcuĂĄntas fichas tienes? "

        hide Oyamageh
        show oyama at center

        hide Fujimakihah2
        show Fujimakisad2 at left

        S "Fujimaki las mirĂł y empezĂł a contar."

        hide Fujimakisad2
        show Fujimakihah2 at left

        F1 "ÂżVes? ÂĄTe faltan tres! TĂș no juegas mĂĄs, idiota. "

        hide oyama
        hide Fujimakihah2
        show Oyamatalk at center
        show Fujimakisad2 at left

        play sound "bosu36.wav" 

        O4 "ÂĄÂżQuĂ© demo-?! ÂĄÂżPor quĂ© soy el Ășnico al que le sale mal?!" with vpunch

        hide Fujimakisad2 with dissolve
        hide Oyamatalk

        show oyama at left with dissolve

        S "Fue obligado a devolver la ficha que tomĂł de la pila."

        hide Hisakosmile2 with dissolve
        show Hisakolargemouth at right with dissolve

        stop music fadeout 1.0

        H13 "GanĂ© por descarte. "

        hide Hisakolargemouth
        show Hisakosmile at right

        S "Dijo Hisako. "

        O1 "ÂżEh? ÂżQuiĂ©n ganĂł por descarte? "

        hide oyama
        show Oyamageh at left

        hide Hisakosmile
        show Hisakohng at right with dissolve

        H14 "Yo ganĂ© gracias a ti. "

        play sound "bosu34.wav" 

        e "*FLOP*" with vpunch

        scene oyamaowned
        with fade

        S "Ella mostrĂł sus fichas. "

        S "Los cuatro vientos mĂĄs los tres dragones. "

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        O3 "ÂżQuĂ© demonios es esoâŠ? "

        H13 "Trece deseos, el puntaje mĂĄximo pero multiplicado por dos."

        play sound "bosu36.wav" 

        O1 "ÂĄÂżTrece deseos con solo siete tablas?! ÂĄÂżNo ven que hay algo raro?!" with vpunch

        H14 "Ah, y todo en la primera mano. Entonces serĂĄ por tres."

        play sound "bosu36.wav" 

        O4 "ÂĄÂżQuĂ©Ă©Ă©Ă©Ă©Ă©?! " with vpunch

        F1 "GuauâŠ nunca vi a alguien reunir los trece deseos en la primera manoâŠ"

        play sound "bosu36.wav" 

        O3 "ÂĄPorque es literalmente imposible!" with vpunch

        scene bg sunset01
        with fade

        S "Y con eso, Ooyama entrĂł en cĂłleraâŠ "

        show oyama at left with dissolve
        show Hisakosmile at right with dissolve

        H12 "Muy bien, entrĂ©guenme todos los boletos de comida que me deben."

        hide oyama
        show Oyamahm at left

        O4 "Oh, vamosâŠ "

        S6 "Alguien sin misericordia, con una arrogancia en su estado mĂĄs puro."

        S6 "Esa es nuestra Hisako; una embustera. La encarnaciĂłn perfecta del Diablo en persona."

        stop music fadeout 1.0

        scene bg black01
        with fade

        jump set3





    elif result == "Irie":

        $ renpy.block_rollback()    

        scene bg black01
        with fade

        e "La siguiente es nuestra baterista, Irie; aunque nosotras la llamamos Miyukichi. Se uniĂł a la banda al mismo tiempo que yo."

        e "Si Hisako era el Diablo, entonces Miyukichi es su versiĂłn en miniatura."

        e "Es muy dĂ©bil fĂ­sicamente, pero realmente es una demonio. Suele tentar a los demĂĄs estudiantes, los NPCs, a hacer cosas muy peligrosas solo para ver hasta dĂłnde puede influenciarlos. Verdaderamente es una demonio."

        scene bg corridoor2
        with fade

        show Sekinesad at center with dissolve
        show Iriesmile at left with dissolve

        play music "15 - study time.mp3" fadeout 1.0 fadein 1.0

        IR6 "Oye, oye, Âżconoces a ese chico, uhâŠ Kinoshita, el NPC? ÂĄPues Ă©l... estĂĄ enamorado de mĂ­!"

        IR6 "Cuando estĂĄbamos en clase, ÂĄcruzamos miradas y su cara se volviĂł completamente roja!"

        show Iriesmileb at left

        IR3 "ÂĄOh, por Dios, es muy obvio! "

        e "Un dĂ­a se jacto de ello."

        hide Iriesmileb
        show Iriesmile at left

        IR6 "AsĂ­ que ayer, le dije que a mĂ­ me gustaban mĂĄs los chicos, eh... 'rebeldes'; como los de esas series de los 90s. Cuando lo vi hoy por la maĂ±ana, ÂĄestaba usando unos pantalones holgados!"

        IR1 "ÂĄNo estoy mintiendo! "

        hide Iriesmile
        show Iriehappytalk at left

        IR6 "ÂĄEstaba usando su chaqueta del uniforme con esos pantalones holgados! ÂĄOh, por Dios, no podĂ­a parar de reĂ­rme!"

        IR2 "Estos NPCs son demasiado geniales."

        IR2 "ÂĄÂżCĂłmo se las arreglĂł para conseguirlos?!"

        IR2 "ÂżSe desvelĂł haciĂ©ndolos?"

        IR6 "Cuando me vio empezĂł a actuar salvajemente. 'ÂżQuĂ© miran, idiotas?' , fue lo que dijo a todos sus compaĂ±eros. ÂĄPero era obvio que con eso solo lo mirarĂ­an mĂĄs! "

        play sound "bosu36.wav" 

        IR "ÂĄJa, ja, ja, ja!" with vpunch

        hide Iriehappytalk
        show Irie at left

        IR2 "ÂĄLo mĂĄs gracioso de todo es que lo hizo para tratar de conquistarme!"

        scene bg corridoor1
        with dissolve

        show Irie at center with dissolve

        e "PodrĂ­amos ser amigas de Ă©l, pero tenĂ­amos que decĂ­rselo apropiadamente."

        e "Incluso si eran NPCs, me sentĂ­a mal por ellos."

        hide Irie
        show Irie2 with dissolve

        IR4 "Entonces, Shiorin, ÂżquĂ© deberĂ­amos pedirle ahora? HarĂĄ cualquier cosa, ÂĄestoy segura de ello!"

        show Sekinetalkangry at right with dissolve

        S6 "Dios, Miyukichi, Âżno sabes cuĂĄndo parar?"

        S6 "Ya lo molestaste demasiado."

        hide Sekinetalkangry
        show Sekineangry at right

        e "IntentĂ© provocar alguna pizca de piedad en ella."

        e "Era tan humana como todos nosotros, asĂ­ que supuse que debĂ­a tenerla en alguna parte."

        hide Irie2 with dissolve
        show Irietalk at left with dissolve

        IR6 "ÂżPero no te da curiosidad quĂ© tan lejos pueden llegar? DespuĂ©s de todo, ÂĄsomos espĂ­as del escuadrĂłn del mĂĄs allĂĄ!"

        hide Irietalk
        show Iriesmile at left

        e "ÂżDesde cuĂĄndo te volviste una espĂ­a?"

        e "ÂżY quĂ© es eso del escuadrĂłn del mĂĄs allĂĄ?"

        e "QuĂ© nombre mĂĄs raro... "

        e "ÂżAcaso intentaste darle tu propia versiĂłn a la SSS?"

        e "Aunque, la SSS siempre la integraron un montĂłn de idiotas."

        e "Es imposible que lleguen a tener miembros tan inteligentes como yo o Miyukichi."

        hide Iriesmile
        show Iriehappytalk at left 

        IR4 "ÂĄÂżQuĂ© te parece un afro?! Si le digo que a mĂ­ me gustan los chicos que tienen un afro, ÂĄestoy segura que maĂ±ana vendrĂĄ con uno! ÂĄOh, por Dios, no puedo parar de reĂ­r! "

        hide Iriehappytalk
        show Iriesmileb at left 

        hide Sekineangry
        show Sekinetalk at right

        S7 "DeberĂ­as dejarlo. Los pantalones holgados ya fueron mĂĄs que suficiente."

        S7 "Un poco mĂĄs y creo que enfadarĂĄs al pobre NPC."

        hide Sekinetalk
        show Sekine at right

        hide Iriesmileb
        show Iriehuh2 at left with dissolve

        stop music fadeout 1.0

        IR4 "ÂĄPero ese es el punto!"

        IR4 "ÂĄQuiero saber hasta dĂłnde pueden llegar!"

        IR4 "EstĂĄ bien, me decidĂ­. ÂĄMaĂ±ana, Kinoshita tendrĂĄ un afro! "

        scene bg black01
        with fade

        e "Al dĂ­a siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekine at left with dissolve

        play sound "bosu36.wav" 

        IR "ÂĄOh, por Dios, ese es Kinoshita!" with vpunch

        hide Sekine with dissolve
        show Sekine2 at left with dissolve

        e "QuerĂ­a practicar mi bajo en paz, asĂ­ que me fui a un aula vacĂ­a. Cuando, Miyukichi entrĂł corriendo al salĂłn."

        e "Luego de que finalmente parara de reĂ­r, ella dijo:"

        show Iriehappytalk at right with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        IR2 "ÂĄLo hizo, vino con un maldito afro! ÂĄNo te estoy mintiendo! ÂĄDios, no tenĂ­a idea de que nuestra escuela tuviese a un peluquero con tanto talento! ÂĄQuĂ© desperdicio! " with vpunch

        e "De hecho, estoy segura de que eso es imposible. No importa lo que hagas, no puedes hacerte crecer un afro en solo una noche."

        hide Iriehappytalk
        show Iriesmile at right 

        hide Sekine2
        show Sekinetalk2 at left

        S3 "Yo tambiĂ©n lo vi, era muy fĂĄcil de identificar. Pude adivinar quiĂ©n era apenas me lo crucĂ© por el pasillo; pobre chico."

        hide Sekinetalk2
        show Sekine2 at left

        hide Iriesmile with dissolve
        show Iriesmile2 at right with dissolve

        IR6 "Entonces, ÂżquĂ© sigue? ÂĄĂl verdaderamente harĂĄ cualquier cosa que le pida!"

        IR6 "ÂĄOh, por Dios, es demasiado gracioso!"

        hide Iriesmile2 with dissolve
        show Iriesmileb2 at center with dissolve

        show Sekinetalkangry2 at left 

        stop music fadeout 1.0

        S4 "SĂ­âŠ ÂżQuĂ© pasĂł con tu meta principal? Ahora lo Ășnico que quieres es reĂ­rte."

        show Sekineangry2 at left

        scene bg corridoor3
        with fade

        show Iriehappytalk at center with dissolve

        play music "27 - moment of rest.mp3" fadeout 1.0 fadein 1.0

        IR6 "ÂĄNo, no es asĂ­! Esto es algo verdaderamente serioâŠ Je, je, je.~"

        hide Iriehappytalk
        show Iriesmile

        e "Es muy difĂ­cil de creer cuando lo dices tĂș, Âżsabes?"

        scene bg corridoor1
        with dissolve

        show Iriesmileb at center with dissolve

        IR3 "Oye, la prĂłxima vez... ÂĄÂżQuĂ© te parece si le pido que se ponga brochetas en su afro?!"

        hide Iriesmileb with dissolve
        show Iriesmileb2 at center with dissolve

        IR3 "El cafĂ© harĂĄ brochetas esta noche."

        IR6 "ÂĄAsĂ­ que haremos que Ă©l aparezca con un montĂłn de ellas en su afro!"

        IR2 "Je, je, je.~"

        scene bg corridoor2
        with dissolve

        show Sekinesad at right with dissolve
        show Irie at center with dissolve

        S4 "Al menos el afro es un estilo de verdad, Âżpero brochetas?"

        show Sekinetalk at right

        S4 "ÂżCĂłmo piensas pedĂ­rselo?"

        show Sekine at right

        hide Irie with dissolve
        show Iriehappytalk2 at left with dissolve

        IR2 "FĂĄcil. Cuando me lo encuentre le dirĂ© algo como... "

        IR2 "Oh, si tan solo tuvieras algunas brochetas en tu afro, Kinoshita.~ Se que caerĂ­a rendida a los pies de cualquiera que lo tuviese asĂ­.~ Ah, llevo fijĂĄndome en ti desde hace mucho tiempo.~ Je, je, je.~"

        hide Iriehappytalk2
        show Iriesmile2 at left 

        show Sekinesad

        stop music fadeout 1.0

        e "QuĂ© mujerâŠ "

        scene bg black01
        with fade

        e "Y luego de que se fuera, seguĂ­ practicando en el aula."

        e "Al dĂ­a siguiente."

        scene bg Emptyclassroom
        with fade

        show Sekinesad with dissolve

        play sound "bosu36.wav" 

        IR "ÂĄOh, por Dios! ÂĄOh, por Dios! ÂĄDe verdad se clavĂł brochetas en su afro!" with vpunch

        scene bg irie
        with fade

        play music "23 - play ball.mp3" fadeout 1.0 fadein 1.0

        e "Estaba a punto de estallar en lĂĄgrimas de risa. No tengo dudas de que se rio en todo el camino hasta aquĂ­."

        S7 "SĂ­, lo vi. Te creo."

        IR3 "Es genial, ÂĄÂżverdad?! Y uno de sus amigos le dijo: 'ÂĄDame una!' Pero el respondiĂł enojado: 'ÂĄNo me toques!' ÂĄJA, JA, JA, JA, JA! ÂĄSantos cielos!"

        S3 "Entonces, Âżte comiste una? "

        IR2 "ÂĄIugh, claro que no! ÂĄEran de ayer y estaban muy frĂ­as!"

        IR2 "ÂĄY estoy segura que fue al baĂ±o con ellas! ÂĄAsqueroso!"

        scene bg Emptyclassroom
        with fade

        show Sekinesad2 with dissolve
        show Iriesmileb at right with dissolve

        stop music fadeout 1.0

        e "Oh, hombre. Miyukichi fue demasiado lejosâŠ "

        e "Este mundo transforma a las personasâŠ "

        e "Y, a pesar de todo, aĂșn hay gente que se toma la vida en serio y hacen lo imposible para pelear contra Dios."

        scene bg class1
        with fade

        IR4 "ÂĄOooh, hagamos que maĂ±ana camine con uno de esos aros de nataciĂłn!"

        IR6 "No los usarĂĄ para nadar, ÂĄpero estoy segura que andarĂĄ por todos lados con eso!"

        IR2 "ÂĄPantalones holgados, un afro con brochetas clavadas en Ă©l y un aro de nataciĂłn!"

        IR2 "ÂĄJA, JA! ÂĄEse NPC tendrĂĄ mucha mĂĄs personalidad que todos nosotros!"

        scene bg black01

        play sound "hit_p07.wav" 

        e "*GOLPE* " with vpunch

        scene bg Emptyclassroom
        with fade

        show Iriehuhb2 at right with dissolve

        IR "ÂĄ...!"

        e "Le di una bofetada con todas mis fuerzas."

        e "Miyukichi mantuvo su mirada fija, mirando a la nada."

        e "Se quedĂł completamente paralizada."

        show Sekinetalkangry2 at center with dissolve

        play sound "bosu36.wav" 

        S6 "QuizĂĄs los NPCs no tengan un alma como sĂ­ tenemos nosotros, ÂĄpero siguen siendo personas!" with vpunch

        S6 "ÂĄEllos tienen sentimientos! Y por encima de todo, ÂĄKinoshita es demasiado dulce e inocente!"

        S6 "A menos que le pidas que se suicide, ÂĄestoy segura que harĂĄ cualquier cosa que le pidas!"

        S3 "ÂĄPero todo lo que haces es aprovecharte de eso y sigues burlĂĄndote de Ă©l! ÂĄÂżNo tienes vergĂŒenza?!"

        hide Sekinetalkangry2 with dissolve
        show Sekineangry with dissolve

        hide Iriehuhb2
        show Iriehuh2 at right

        IR5 "P- PeroâŠ pensĂ© que tĂș tambiĂ©n estabas divirtiĂ©ndoteâŠ "

        hide Iriehuh2
        show Iriehuhb at right

        hide Sekinetalkangry2
        hide Sekineangry
        show Sekineyellangry2

        play sound "bosu36.wav" 

        S6 "ÂĄÂżCĂłmo podrĂ­a divertirme con algo asĂ­?! " with vpunch

        S6 "ÂĄKinoshita es mucho mĂĄs humano que tĂș! "

        show Sekineangry2

        hide Iriehuhb
        show Iriesad at right with dissolve

        e "Su rostro se oscureciĂł de repente."

        e "Para cualquier integrante de la SSS, ser comparado con un NPC es mucho mĂĄs ofensivo que cualquier otro insulto que te puedas imaginar."

        IR5 "ÂżTĂș creesâŠ que un NPC es mejor persona que yo...?"

        hide Sekineangry2
        show Sekinetalkangry2

        S7 "SĂ­. Y creo que deberĂ­as pensar sobre ello."

        hide Sekinetalkangry2
        show Sekineangry2

        IR5 "S- SollozoâŠ "

        e "Los hombros de Miyukichi comenzaron a temblarâŠ"

        hide Iriesad with dissolve

        play sound "bosu36.wav" 

        IR "ÂĄGuaaaaaah!" with vpunch

        show Sekineangry2 with fade

        e "SaliĂł corriendo mientras cubrĂ­a su rostro con sus manos."

        show Sekinetalkangry2

        S4 "SheeshâŠ "

        hide Sekinetalkangry2

        scene bg Concerthall
        with fade

        e "MĂĄs tarde, se lo expliquĂ© todo a Kinoshita."

        e "Ocultando la parte de que era un NPC, obviamente."

        e "Incluso si lo hubiera hecho, se habrĂ­a confundido tanto que olvidarĂ­a todo lo que le dije."

        show Sekine with dissolve

        play music "03 - school days.mp3" fadeout 1.0 fadein 1.0

        S7 "Lo siento."

        hide Sekine
        show Sekinetalk

        S1 "Hiciste absolutamente todo lo que te pidiĂł, pero esto se te fue de las manos."

        hide Sekinetalk
        show Sekine

        K "Entonces, eso significa queâŠ yo fui el Ășnico que sintiĂł amor de verdadâŠ "

        e "No apartĂł la mirada del suelo, completamente abatido. "

        hide Sekine
        show Sekinesad

        S3 "SĂ­âŠ supongo que tienes razĂłnâŠ "

        K "Ya veo, pero no voy a llorar por esto. Porque, ÂĄencontrĂ© a mi nuevo amor!"

        e "Sus ojos brillaron cĂłmo nunca antes y alzĂł a lo alto su puĂ±o cerrado."

        hide Sekinesad
        show Sekinesmile

        S1 "ÂżEh? ÂĄEso es genial! "

        K "ÂĄTĂș!"

        hide Sekinesmile
        show Sekinegeh

        stop music fadeout 1.0

        play music "16 - niku udon.mp3" fadeout 1.0 fadein 1.0

        play sound "bosu36.wav" 

        S5 "ÂĄÂżQuĂ©?! ÂĄÂżYo?! " with vpunch

        K "ÂĄSĂ­, tĂș! ÂĄTĂș siempre te preocupaste por un pobre sujeto como yo! "

        K "ÂĄEstoy verdaderamente enamorado de ti! "

        hide Sekinegeh
        show Sekinegeh2

        S5 "ÂżD- De verdad?"

        K "ÂĄPor favor, salga conmigo, seĂ±orita Sekine!"

        hide Sekinegeh2
        show Sekinesad

        S5 "Espera, no estoy segura de estoâŠ "

        K "ÂĄÂżTe gustan los afros?! ÂżO brochetas? ÂĄQuizĂĄs te vayan los chicos rebeldes!"

        hide Sekinesad
        show Sekinegeh

        S5 "No, uhâŠ a mĂ­ no me van todas esas cosas rarasâŠ "

        K "ÂĄÂżEntonces te gusto tal y cĂłmo soy?! " with vpunch

        hide Sekinegeh
        show Sekinegeh2

        stop music fadeout 1.0

        S5 "UhâŠ esperaâŠ eso no es lo queâŠ ÂĄAdiĂłs! "

        hide Sekinegeh2 with dissolve

        e "EscapĂ© lo mĂĄs rĂĄpido que pude." with vpunch

        scene bg black01
        with fade

        e "Al final, Miyukichi no era tan malvada como yo creĂ­a; tan solo disfrutaba demasiado jugando con los pobres NPCs. Aunque no se puede negar que es cruel."

        jump set4





    elif result == "Iwasawa":

        $ renpy.block_rollback()    

        scene bg black01 with fade

        play music "08 - Alchemy (Yui ver).mp3" fadeout 1.0 fadein 1.0

        e "La Ășltima que queda es la lĂ­der de Girls Dead Monster, nuestra superior, Iwasawa. "

        e "Si Hisako es el diablo en persona y Miyukichi es su versiĂłn en miniatura, entonces no hay mejor manera de describir a Iwasawa como una fanĂĄtica de la mĂșsica."

        e "Quiero decir, no le interesa absolutamente nada que no sea la mĂșsica."

        scene bg Emptyclassroom with fade

        e "El otro dĂ­a, estĂĄbamos practicando en un aula vacĂ­a."

        e "Terminamos la intro y comenzamos con los primeros versos, pero Iwasawa no estaba cantando."

        stop music fadeout 1.0

        e "Por lo que todas nos detuvimos, y entonces Hisako preguntĂł:"

        show Hisakohuh at right with dissolve 

        H2 "ÂżQuĂ© te pasa, Iwasawa?"

        I5 "ÂĄDoo-loo, doo-dwa! "

        e "Iwasawa hablĂł."

        show Sekinesad at left with dissolve
        show Irie at center with dissolve

        play music "18 - toy of spring.mp3" fadeout 1.0 fadein 1.0

        e "Todas nos quedamos en blanco y dijimos: ''ÂżQuĂ©?'' ''ÂżEh?'' a esas extraĂ±as palabras."

        scene bg Iwasawa with fade

        I3 "Sekine."

        play sound "bosu36.wav" 

        S2 "ÂĄAh, sĂ­! " with vpunch

        I5 "Es un par lo que viene luego de la intro. AsĂ­ que antes de cantar, mueve la cabeza y di: ÂĄdoo-loo, doo-dwa! "

        S5 "Ah, aah... 'Doo-loo, doo-dwa', ÂżasĂ­? ÂĄBien, lo tengo!"

        stop music fadeout 1.0

        scene bg Emptyclassroom with fade

        show Hisakosmile2 at right with dissolve
        show Irie at center with dissolve

        H10 "ÂĄMuy bien, una vez mĂĄs!"

        hide Irie
        show Irietalk

        IR6 "ÂĄEsperen! ÂĄUno, dos!"

        scene bg window1 with fade

        play music "08 - Alchemy (Yui ver).mp3" fadeout 1.0 fadein 1.0

        e "Irie comenzĂł a contar cuando Hisako le dio la seĂ±al."

        e "La intro comenzĂł y en muy poco tiempo llegamos al verso A."

        stop music fadeout 1.0

        scene bg black01

        I5 "âŠ Naw."

        scene bg Iwasawa with fade

        e "Iwasawa tenĂ­a el micrĂłfono cerca de su boca."

        e "Y en vez de cantar, empezĂł a murmurar. "

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

        e "SiguiĂł hablando a travĂ©s de los parlantes."

        hide Sekinesad2
        show Sekinegeh2 at left

        S5 "Um, pero si me dijiste que hiciera un 'doo-loo, doo-doo'."

        scene bg window1 with dissolve

        play sound "bosu36.wav" 

        I5 "ÂĄOye, no es asĂ­! ÂĄEscucha bien, es 'doo-loo, doo-dwa'! " with vpunch

        S2 "ÂżNo son lo mismo? "

        play sound "bosu36.wav" 

        I5 "ÂĄYo dije, 'dwa'! ÂĄNo, 'doo'! ÂĄ'Dwa'! " with vpunch

        S7 "ÂżEso Ășltimo?"

        play sound "bosu36.wav" 

        I4 " ÂĄSĂ­p!" with vpunch

        scene bg Iwasawa with fade

        e "Iwasawa solo hablĂł por el micrĂłfono todo el tiempo."

        e "No me mirĂł a la cara ni por un segundo."

        e "Me daba mucho mĂĄs miedo cuando no podĂ­a ver la expresiĂłn de su rostro."

        stop music fadeout 1.0

        scene bg Emptyclassroom with fade

        H9 "ÂĄBien, intentĂ©moslo otra vez!"

        e "Hisako intentĂł animarme con su voz."

        IR6 "ÂĄBien! ÂĄUno, dos!"

        scene bg black01

        play sound "bosu36.wav" 

        I5 "ÂĄNoooooouuuuwww! " with vpunch

        e "Otra vez, ella gritĂł."

        e "Y todas nos detuvimos."

        I3 "Sekine."

        e "Mi nombre, por tercera vez."

        scene bg Iwasawa with fade

        play music "06 - today is ok.mp3" fadeout 1.0 fadein 1.0

        S5 "S-SĂ­âŠ"

        I4 "ÂĄT-Te dije 'doo-loo, doo-dwa'! ÂĄHazlo otra vez!"

        play sound "bosu36.wav"

        I5 "Oye, solo haz lo yo hago. ÂĄÂĄ'Doo-loo, doo-dwa'!! " with vpunch

        S5 "Pero suena muy parecido a lo que yo hagoâŠ"

        play sound "bosu36.wav"

        I5 "ÂĄ'Doo' y 'dwa' zon doz coshas muy diferentes'! " with vpunch

        S7 "Casi no veo la diferenciaâŠ"

        S7 "Con mi habilidad, o mejor dicho, en mi bajo directamente no se nota la diferenciaâŠ"

        I4 "Entonzes, grĂ­talo."

        S5 "ÂżQuĂ©? "

        I4 "Zolo grita 'dwa' al final. ÂżPara quĂ© tienes el micrĂłfono? "

        S5 "Para los coros, supongoâŠ "

        I4 "Para esto tambiĂ©n. ÂĄAzĂ­ que grita! ÂĄTe ashudarĂĄ a zeguir el ritmo! "

        S7 "PodrĂ­aâŠ pero no creo que decir 'dwa' en el micrĂłfono me vaya a ayudar a controlar mi ritmoâŠ"

        scene bg Emptyclassroom with fade

        show Sekinesad2 at left with dissolve
        show Irie at center with dissolve
        show Hisakooh at right with dissolve

        I3 "ÂĄE Irie! " with vpunch

        e "EmpezĂł a gritarle a Miyukichi."

        hide Irie
        show Iriesad2

        play sound "bosu36.wav" 

        IR6 "ÂżS-SĂ­, senpaiâŠ? " with vpunch

        I5 "ÂĄAliviana todo' lo' golpes y bada bum que pueda'! "

        hide Sekinesad2
        show Sekinegeh2 at left

        e "PrĂĄcticamente se burlĂł de la existencia de la baterĂ­a..."

        hide Iriesad2
        show Iriehuhb2

        IR5 "Pero eso es todo lo que hace la baterĂ­aâŠ "

        hide Iriehuhb2
        show Iriehuh2

        I4 "MĂĄs despacio. Por cierto, deberĂ­as ver cĂłmo queda tu cabello despuĂ©s de usar un aclarador."

        hide Iriehuh2
        show Iriehuhb2

        IR1 "Uh, nunca usĂ© algo como eso. Pero, ÂżquĂ© tiene que ver eso con mi baterĂ­a? "

        hide Iriehuhb2
        show Iriehuh2

        play sound "bosu36.wav"

        I5 "ÂĄOye, haz una voltereta con los palillos! " with vpunch

        I4 "ÂĄErez lizta, piĂ©nzalo! "

        I4 "Erez una adulta, ÂĄÂżo no?! "

        hide Iriehuh2
        show Irietalk2

        IR6 "Oh, una volteretaâŠ Entiendo, lo harĂ©."

        hide Irietalk2
        show Iriesad2

        hide Sekinegeh2
        show Sekinesad2 at left

        hide Hisakooh
        show Hisakotalk at right

        H6 "Esto probablemente vaya a ser una pĂ©rdida de tiempoâŠ"

        hide Hisakotalk
        show Hisakooh at right

        e "Un sentimiento de preocupaciĂłn invadiĂł la cara de Hisako."

        I4 "SĂ­, Hisako, no te pongaz pezada conmigo. "

        hide Hisakooh
        show Hisakotalk at right

        H9 "Ni siquiera te estoy molestandoâŠ "

        hide Hisakotalk
        show Hisakooh at right

        I5 "ÂĄEntonce' para ya de tocar todo el twang al inicio! "

        play sound "bosu36.wav"

        I5 "ÂĄY buzca un aclarante de cabello! " with vpunch

        I3 "Y buzca algo que te ashude a penza' para toca' mejor. ÂżShĂ­, mi niĂ±a?"

        hide Hisakooh
        show Hisakotalk at right

        H5 "Entonces, ÂżcĂłmo deberĂ­a tocar?"

        hide Hisakotalk
        show Hisakooh at right

        I4 "Toca conmigo, amia."

        hide Hisakooh
        show Hisakotalk at right

        H2 "ÂżDĂłnde?"

        hide Hisakotalk
        show Hisakooh at right

        I5 "ÂĄAquĂ­, entre el parlante y tu guitarra! Zino zuena raro, Âżentiende'? "

        play sound "bosu36.wav" 

        I4 "ÂĄHaz ezo y todoz te amarĂĄn!" with vpunch

        I3 "Lez robarĂĄz los corazonez, Âżentiendeâ? "

        hide Hisakooh
        show Hisakosmile at right

        H15 "ÂżHablas en serioâŠ? Bien, de acuerdoâŠ ÂĄEmpecemos de nuevo desde el inicio! "

        stop music fadeout 1.0

        hide Iriesad2
        show Iriesmile2

        IR2 "ÂĄBien! ÂĄUno, dos! "

        scene bg black01

        play sound "bosu36.wav" 

        I5 "ÂĄÂżCanzadas ya?! ÂżCuĂĄnto llevamo' tocando? " with vpunch

        play sound "bosu36.wav" 

        I4 "Zolo tomen un rezpiro, ÂĄy hagan lo que digo! " with vpunch

        play sound "bosu36.wav" 

        I5 "No cuenten, ÂĄesto va por Pete!" with vpunch

        IR6 "Bien, umâŠ ÂĄYa! "

        e "... ...... ........... "

        e "Tsssssssssssst.~"

        e "ÂĄBoing!"

        e "Doo-loo, dooâŠ"

        S2 "Dwa.~"

        scene bg outside with fade

        play sound "bosu36.wav" 

        I5 "ÂĄÂżQuĂ©Ă©Ă©Ă©Ă©Ă© demonioz fue ezo?! ÂĄÂżQuĂ© eztan haciendo?!" with vpunch

        play sound "bosu36.wav" 

        everyone "ÂĄTĂș nos dijiste que lo hiciĂ©ramos!" with vpunch

        e "AhĂ­ la tienen. Es nuestra Iwasawa, la manĂ­aca de la mĂșsica."

        scene bg black01 with fade

        e "Y con eso terminaron las actividades del dĂ­a para las Girls Dead Monster! O Girldemo, para hacerlo mĂĄs corto. "

        e "ÂĄY las presentaciones fueron tan solo el principio!"

        jump end

    window hide





label end:

    $ renpy.block_rollback()    

    scene bg black01
    with fade

    play music "26 - evening breeze.mp3" fadeout 1.0 fadein 1.0

    S2 "Fiu..."

    e "Suelto mi bolĂ­grafo."

    H "ÂĄBuen trabajo! "

    e "Mis hombros se sienten pesados de repente."

    H "Oh... eso se ve muy interesante."

    e "Esa vozâŠ ÂżHisako?"

    scene bg dorm with fade

    e "Me doy la vuelta para encontrar a las tres en mi habitaciĂłn."

    e "Miyukichi es mi compaĂ±era de cuarto, asĂ­ que no hay nada de raro con que ella estĂ© aquĂ­."

    e "Mi cara se vuelve pĂĄlida de repente."

    show Hisakosmile with dissolve

    H15 "ÂżTrampas? ÂżCuĂĄndo hice algo tan vergonzoso? "

    e "Nunca la vi con una sonrisa tan enorme. Da miedoâŠ "

    show Iriehappytalk2 at right with dissolve

    IR6 "Shiorin, ÂĄÂża quiĂ©n estĂĄs llamando pequeĂ±a diablilla que trata a los NPCs como si fuesen juguetes?!"

    hide Iriehappytalk2 with dissolve
    show Iriesmile at right with dissolve

    e "Hasta la siempre cariĂ±osa y tranquila Miyukichi tiene una vena exaltada en su cuello... "

    H10 "Te obligamos a hacer un diario de nuestras actividades solo porque arruinaste nuestro concierto con esa estĂșpida broma que hiciste. "

    H15 "ÂĄEs solo el primer dĂ­a y ya escribiste toda esta basura! ÂżAcaso estĂĄs buscando una pelea?"

    e "Hunde fuertemente sus uĂ±as en mis hombros."

    play sound "bosu36.wav" 

    S5 "ÂĄAy! ÂĄEso duele, Hisako! " with vpunch

    hide Iriesmile with dissolve
    show Iriehappytalk2 at right with dissolve

    IR2 "Bien. Puedes seguir lastimĂĄndola, entonces."

    hide Iriehappytalk2
    show Iriesmile2 at right

    S5 "ÂĄÂżQuĂ©?! ÂĄÂżTĂș tambiĂ©n estĂĄs en mi contra, Miyukichi?!"

    hide Iriesmile2
    show Iriehappytalk2 at right

    IR2 "No puedo creer que hayas escrito esto de mĂ­âŠ"

    hide Iriehappytalk2
    show Iriehuhb at right with dissolve

    IR3 "Pero, estoy segura de que Iwasawa se llevĂł la peor parteâŠ"

    IR1 "Dios, fuiste demasiado lejos."

    hide Iriehuhb
    show Iriehuh at right

    S5 "Oh, vamosâŠ "

    hide Hisakosmile with dissolve
    hide Iriehuh with dissolve

    show Sekinegeh at right with dissolve

    e "Temblando de miedo, miro con Hisako hacia la entrada. AllĂ­ se encuentra Iwasawa de pie y en silencio. "

    show Iwasawasmile at left with dissolve

    I1 "ÂżEh? ÂżQuĂ©?"

    e "Responde frĂ­amente."

    hide Sekinegeh
    show Sekinesad at right

    S4 "Erm, Âżno lo leĂ­steâŠ?"

    I2 "SĂ­, lo hice."

    hide Sekinesad
    show Sekinetalk at right

    S5 "ÂżNo estĂĄs enojada?"

    hide Iwasawasmile
    show Iwasawahappy at left

    I1 "ÂżPor quĂ©?"

    show Sekinegeh at right

    hide Iwasawahappy
    show Iwasawacool at left

    H10 "Uh, IwasawaâŠ te hizo ver como una tonta."

    H15 "Con un tonto acento irlandĂ©s, tambiĂ©n."

    H15 "EstĂĄ arruinando tu imagen, Âżsabes?"

    hide Iwasawacool
    show Iwasawatalk at left

    I6 "Es su diario, puede escribir en Ă©l lo que sea que le venga en gana."

    hide Iwasawatalk
    show Iwasawahappy at left

    I1 "No me importaâŠ Por cierto, ya terminĂ© esa nueva canciĂłn que querĂ­a que escuchen."

    scene bg gang with fade

    I2 "Ya es muy tarde, asĂ­ que directamente vine a tu habitaciĂłn. Dame un segundo para prepararme y entonces te la mostrarĂ©."

    e "Coloca en el suelo el estuche que lleva a sus espaldas, toma la guitarra y comienza a tocar."

    stop music fadeout 1.0

    e "SĂ­, realmente es una manĂ­aca de la mĂșsica."

label finalend:
    $ renpy.block_rollback()    

    scene bg black01
    with fade

    e "CapĂ­tulo Extra 01: Fin."

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
