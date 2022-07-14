label start:
    $_game_menu_screen = None #El tiempo es efímero, las decisiónes no.
    stop music
    
    scene white with dissolve
    image intro = Text("   Hecho por Wending Yan en 2009 \n\n        yuumei.deviantart.com \n\n    Dedicado a alguien que hizo \n\n           la diferencia. \n\n         Gracias por leerlo.", size=45, font="fonts/Trixie.ttf")
    show intro at truecenter with dissolve
    ""
    #=====================================
    play sound "sound/forest.mp3"
    scene 03 with dissolve
    ""
    #====================================
    play music "<loop 11>sound/Lindsey Stirling - River Flows In You.mp3" fadein 1.0
    scene 04 with dissolve
    image 04he = Text("¿Qué quieres, niña?", size=35, font="fonts/Carefree.ttf")
    show 04he with dissolve:
        xpos 500 ypos 70
    ""
    image 04she = Text(" Señor,\n¿me podría enseñar a dibujar?", size=25, font="fonts/Scotch.ttf")
    show 04she with dissolve:
        xpos 600 ypos 160
    ""
    #===================================
    stop sound fadeout 4.0
    scene 05 with dissolve
    image 05she = Text("Es muy bueno dibujando...", size=25, font="fonts/Scotch.ttf")
    show 05she with dissolve:
        xpos 100 ypos 450
    ""
    #===================================
    scene 06 with dissolve
    transform slide06_1:
        xpos 0 ypos -200 alpha 0.0
        linear 1.0 ypos 0 alpha 1.0
    show 06-1 at slide06_1
    image 06she = Text(" Enséñeme, por favor.\n   Quiero dibujar algo...", size=25, font="fonts/Scotch.ttf")
    $ renpy.pause(1.0)
    show 06she with dissolve:
        xpos 360 ypos 275
    ""
    transform slide06_2:
        xpos 0 ypos 250 alpha 0.0
        linear 1.0 ypos 0 alpha 1.0
    show 06-2 at slide06_2
    image 06she2 = Text("especial.", size=25, font="fonts/Scotch.ttf")
    $ renpy.pause(1.0)
    show 06she2 with dissolve:
        xpos 690 ypos 330
    ""
    #===================================
    scene 07 with dissolve
    image 07she = Text(" Pero, esto es\n   lo mejor que\n     puedo hacer.", size=25, font="fonts/Scotch.ttf")
    show 07she with dissolve:
        xpos 300 ypos 50
    ""
    transform slide07:
        xpos 0 ypos -250 alpha 0.0
        linear 1.0 ypos 0 alpha 1.0
    show 07-1 at slide07
    image 07she1 = Text("Mire.", size=25, font="fonts/Scotch.ttf")
    $ renpy.pause(1.0)
    show 07she1 with dissolve:
        xpos 620 ypos 450
    ""
    #====================================
    scene 08 with dissolve
    image 08he = Text("Me parece que dibujas bonito.", size=33, font="fonts/Carefree.ttf")
    show 08he with dissolve:
        xpos 50 ypos 5
    ""
    transform slide08_1:
        xpos 200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 08-1 at slide08_1
    image 08she = Text("Pero quiero \n   ser tan buena\n\n\n\n\n\n        como usted...", size=25, font="fonts/Scotch.ttf")
    $ renpy.pause(1.0)
    show 08she with dissolve:
        xpos 350 ypos 30
    ""
    transform slide08_2:
        xpos 200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 08-2 at slide08_2
    image 08he2 = Text("Solo practica \n   cada día y serás\n       muy buena en \n          algunos años.", size=33, font="fonts/Carefree.ttf")
    $ renpy.pause(1.0)
    show 08he2 with dissolve:
        xpos 680 ypos 410
    ""
    #===================================
    scene 09 with dissolve
    transform slide09_1:
        xpos -200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 09-1 at slide09_1
    image 09she1 = Text("¡¿En unos años?!", size=25, font="fonts/Scotch.ttf")
    $ renpy.pause(1.0)
    show 09she1 with dissolve:
        xpos 10 ypos 70
    ""
    transform slide09_2:
        xpos 200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 09-2 at slide09_2
    image 09she2 = Text("Será muy tarde para entonces...", size=25, font="fonts/Scotch.ttf")
    $ renpy.pause(1.0)
    show 09she2 with dissolve:
        xpos 500 ypos 280
    ""
    #====================================
    scene white with dissolve
    transform slide10:
        xpos -200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 10 at slide10
    transform slide10_1:
        xpos 200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 10-1 at slide10_1
    image 10he = Text("¿A qué te refieres con tarde? ¿Qué sucede?", size=33, font="fonts/Carefree.ttf")
    $ renpy.pause(1.0)
    show 10he with dissolve:
        xpos 330 ypos 170
    ""
    #====================================
    scene 11 with dissolve
    image 11she = Text("Pues...", size=25, font="fonts/Scotch.ttf")
    show 11she with dissolve:
        xpos 670 ypos 170
    ""
    #====================================
    scene 12 with dissolve
    ""
    #====================================
    scene 13 with dissolve
    image 13she1 = Text("Мamá y papá", size=25, font="fonts/Scotch.ttf")
    show 13she1 with dissolve:
        xpos 50 ypos 250
    ""
    image 13she2 = Text("van a divorciarse...", size=25, font="fonts/Scotch.ttf")
    show 13she2 with dissolve:
        xpos 600 ypos 250
    ""
    #====================================
    scene 14 with dissolve
    image 14she1 = Text("Y si eso pasa,\n     mi familia nunca volverá a estar junta.\n           Una imagen es lo único que quedará.", size=25, font="fonts/Scotch.ttf")
    show 14she1 with dissolve:
        xpos 50 ypos 50
    ""
    image 14she2 = Text("Es por eso que...", size=25, font="fonts/Scotch.ttf")
    show 14she2 with dissolve:
        xpos 350 ypos 470
    ""
    #====================================
    scene 15 with dissolve
    image 15she = Text("quiero que me enseñe a dibujar.", size=25, font="fonts/Scotch.ttf")
    show 15she with dissolve:
        xpos 50 ypos 50
    ""
    #====================================
    scene 16 with dissolve
    image 16he = Text("No puedo, eso me llevaría más de un año y \n                    yo soy un viajero. Me iré mañana.", size=33, font="fonts/Carefree.ttf")
    show 16he with dissolve:
        xpos 330 ypos 30
    ""
    image 16he1 = Text("Además...", size=33, font="fonts/Carefree.ttf")
    show 16he1 with dissolve:
        xpos 660 ypos 220
    ""
    #====================================
    scene 17 with dissolve
    image 17he = Text("¿No es mejor salvar a tu familia", size=33, font="fonts/Carefree.ttf")
    show 17he with dissolve:
        xpos 430 ypos 30
    ""
    image 17he1 = Text("que solo dibujarla?", size=33, font="fonts/Carefree.ttf")
    show 17he1 with dissolve:
        xpos 660 ypos 220
    ""
    #====================================
    scene 18 with dissolve
    ""
    #====================================
    define flash = Fade(0.5, 0.0, 0.5, color="#fff") #te quiero vannessa
    scene 22 with flash
    image 22she = Text("Pero no puedo hacer ninguna de las dos.", size=25, font="fonts/Scotch.ttf")
    show 22she with dissolve:
        xpos 250 ypos 250
    ""
    #====================================
    scene 23 with dissolve
    image 23he = Text("No te desesperes.", size=33, font="fonts/Carefree.ttf")
    show 23he with dissolve:
        xpos 150 ypos 30
    ""
    #====================================
    scene 24 with dissolve
    image 24he = Text("Un hombre me dijo una vez \n      que lo principal en una imagen es \n            el mensaje, no la habilidad.", size=33, font="fonts/Carefree.ttf")
    show 24he with dissolve:
        xpos 550 ypos 50
    ""
    image 24he1 = Text("     Así es como una imagen \n           puede expresar más \n                  que mil palabras.", size=33, font="fonts/Carefree.ttf")
    show 24he1 with dissolve:
        xpos 550 ypos 350
    ""
    #====================================
    scene 25 with dissolve
    image 25he = Text("Se me ocurre algo.", size=33, font="fonts/Carefree.ttf")
    show 25he with dissolve:
        xpos 450 ypos 50
    ""
    image 25he1 = Text("¿Quieres hacer un trato?", size=33, font="fonts/Carefree.ttf")
    show 25he1 with dissolve:
        xpos 650 ypos 250
    ""
    #====================================
    scene 26 with dissolve
    image 26he = Text("Tu dibujo,", size=33, font="fonts/Carefree.ttf")
    show 26he with dissolve:
        xpos 50 ypos 200
    ""
    image 26he1 = Text("por mil palabras mías.", size=33, font="fonts/Carefree.ttf")
    show 26he1 with dissolve:
        xpos 690 ypos 200
    ""
    #====================================
    scene 27 with dissolve
    image 27she = Text("Pero... está roto.", size=25, font="fonts/Scotch.ttf")
    show 27she with dissolve:
        xpos 30 ypos 200
    ""
    image 27she1 = Text("¿Y qué puedo hacer...", size=25, font="fonts/Scotch.ttf")
    show 27she1 with dissolve:
        xpos 660 ypos 200
    ""
    #====================================
    scene 28 with dissolve
    image 28she = Text("con", size=25, font="fonts/Scotch.ttf")
    show 28she with dissolve:
        xpos 440 ypos 100
    ""
    image 28she1 = Text("mil palabras?", size=25, font="fonts/Scotch.ttf")
    show 28she1 with dissolve:
        xpos 400 ypos 400
    ""
    #====================================
    scene 29 with dissolve
    image 29he = Text("Creo que eso es suficiente \n     para que tus padres hagan las paces.", size=33, font="fonts/Carefree.ttf")
    show 29he with dissolve:
        xpos 450 ypos 50
    ""
    image 29he1 = Text("Pero es solo una suposición...", size=33, font="fonts/Carefree.ttf")
    show 29he1 with dissolve:
        xpos 330 ypos 350
    ""
    #====================================
    scene 30 with dissolve
    image 30he = Text("Ven aquí mañana", size=33, font="fonts/Carefree.ttf")
    show 30he with dissolve:
        xpos 50 ypos 50
    ""
    image 30he1 = Text("y comprueba \n    mi corazonada.", size=33, font="fonts/Carefree.ttf")
    show 30he1 with dissolve:
        xpos 520 ypos 250
    ""
    #====================================
    #------------------------------------
    #====================================
    #TODO Transición de días.
    scene 31 with dissolve
    ""
    #====================================
    scene 32 with dissolve
    image 32she = Text(" Señor, \n     ¡estás aquí!", size=25, font="fonts/Scotch.ttf")
    show 32she with dissolve:
        xpos 480 ypos 30
    ""
    #====================================
    scene 33 with dissolve
    image 33he = Text("¿Lo dudabas?", size=33, font="fonts/Carefree.ttf")
    show 33he with dissolve:
        xpos 350 ypos 50
    ""
    #====================================
    scene 34 with dissolve
    image 34he = Text("Y como lo prometí, \n         aquí tienes tus mil palabras.", size=33, font="fonts/Carefree.ttf")
    show 34he with dissolve:
        xpos 50 ypos 50
    ""
    #====================================
    scene 35 with dissolve
    image 35he = Text("Pero no abras el sobre,", size=33, font="fonts/Carefree.ttf")
    show 35he with dissolve:
        xpos 10 ypos 150
    ""
    image 35he1 = Text("dáselo primero...", size=33, font="fonts/Carefree.ttf")
    show 35he1 with dissolve:
        xpos 670 ypos 150
    ""
    #====================================
    scene 36 with dissolve
    image 36he = Text("... a tus padres.", size=33, color="#fff", font="fonts/Carefree.ttf")
    show 36he with dissolve:
        xpos 400 ypos 100
    ""
    #====================================
    scene 37 with dissolve
    ""
    #====================================
    scene 38 with dissolve
    ""
    #====================================
    scene black with dissolve
    image 39he = Text("       No importa lo que suceda,", size=30, color="#fff", font="fonts/Trixie.ttf")
    show 39he with dissolve:
        xpos 220 ypos 270
    ""
    #====================================
    scene 18
    transform bl_u:
        xpos 0 ypos 0
        linear 1.5 ypos 240
    transform bl_d:
        xpos 0 ypos 0
        linear 1.5 ypos -240
    show bl-1 at bl_u
    show bl-2 at bl_d

    image 40he = Text(" sobre las nubes siempre brilla el sol.", size=30, color="#fff", font="fonts/Trixie.ttf")
    show 40he with dissolve:
        xpos 30 ypos 20
    ""
    image 40he1 = Text("         Solo hay que esperar a que las nubes se dispersen.", size=30, color="#fff", font="fonts/Trixie.ttf") 
    show 40he1 with dissolve:
        xpos 120 ypos 550
    ""
    #====================================
    transform son:
        alpha 0.0
        linear 1.0 alpha 1.0
    show shine at son
    $ renpy.pause(0.7)
    scene white with dissolve
    image 41he = Text("  Y entonces...", size=33, color="#311500", font="fonts/Trixie.ttf")
    show 41he with dissolve:
        xpos 350 ypos 270
    ""
    #====================================
    #------------------------------------
    #====================================
    #TODO Transición de años.
    play sound "sound/forest.mp3"
    scene 42 with dissolve
    ""
    #====================================
    scene 43 with dissolve
    ""
    #====================================
    #play music "sound/Mono - Rainbow.mp3"
    scene 44 with dissolve
    image 44she = Text("¡Señor!", size=25, font="fonts/Scotch.ttf")
    show 44she with dissolve:
        xpos 640 ypos 320
    ""
    #====================================
    stop sound fadeout 1.0
    scene 45 with dissolve
    image 45he = Text("Veo que has crecido.", size=33, font="fonts/Carefree.ttf")
    show 45he with dissolve:
        xpos 280 ypos 70
    ""
    #====================================
    scene 46 with dissolve
    image 46she = Text("Quiero agradecerle", size=25, font="fonts/Scotch.ttf")
    show 46she with dissolve:
        xpos 120 ypos 70
    ""
    transform slide46_1:
        xpos 200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 46-1 at slide46_1
    image 46she1 = Text("por la ayuda que me brindo.", size=25, font="fonts/Scotch.ttf")
    $ renpy.pause(1.0)
    show 46she1 with dissolve:
        xpos 400 ypos 140
    ""
    transform slide46_2:
        xpos 200 ypos 0 alpha 0.0
        linear 1.0 xpos 0 alpha 1.0
    show 46-2 at slide46_2
    image 46he2 = Text("Entonces, ¿tus padres \n     se reconciliaron? \n        Me alegro mucho.", size=31, font="fonts/Carefree.ttf")
    $ renpy.pause(1.0)
    show 46he2 with dissolve:
        xpos 660 ypos 400
    ""
    #===================================
    scene 47 with dissolve
    image 47she = Text("En realidad, \n   se divorciaron", size=25, font="fonts/Scotch.ttf")
    show 47she with dissolve:
        xpos 20 ypos 200
    ""
    image 47she1 = Text("una semana después \n     de eso.", size=25, font="fonts/Scotch.ttf")
    show 47she1 with dissolve:
        xpos 670 ypos 200
    ""
    #====================================
    scene 48 with dissolve
    ""
    #====================================
    scene 49 with dissolve
    image 49he = Text("Perdóname... \n\n                    fallé en hacer la diferencia.", size=33, font="fonts/Carefree.ttf")
    show 49he with dissolve:
        xpos 400 ypos 50
    ""
    #====================================
    scene 50 with dissolve
    image 50she = Text("¡Eso no es verdad! \n        Todo a cambiado...", size=25, font="fonts/Scotch.ttf")
    show 50she with dissolve:
        xpos 50 ypos 50
    ""
    image 50she1 = Text("en mí.", size=25, font="fonts/Scotch.ttf")
    show 50she1 with dissolve:
        xpos 350 ypos 150
    ""
    #====================================
    scene 51 with dissolve
    image 51she = Text("Decidí ser una artista  \n                          como usted.", size=25, font="fonts/Scotch.ttf")
    show 51she with dissolve:
        xpos 280 ypos 50
    ""
    image 51she1 = Text("Yo haré la diferencia \n    y cambiaré el mundo para mejor; \n          con mil palabras a la vez.", size=25, font="fonts/Scotch.ttf")
    show 51she1 with dissolve:
        xpos 350 ypos 250
    ""
    #====================================
    scene 52 with dissolve
    image 52she = Text("Tome. \n   Son mil palabras \n            de mi gratitud.", size=25, font="fonts/Scotch.ttf")
    show 52she with dissolve:
        xpos 400 ypos 50
    ""
    #=====================================
    scene 53 with dissolve
    ""
    #=====================================
    scene 54 with dissolve
    image 54he = Text("Y realmente... \n            son mil palabras.", size=33, font="fonts/Carefree.ttf")
    show 54he with dissolve:
        xpos 600 ypos 50
    ""
    #=====================================
    scene 55 with dissolve
    ""
    #=====================================
    scene white with dissolve
    image 56she = Text("¡Gracias!", size=30, font="fonts/Scotch.ttf")
    show 56she with dissolve:
        xpos 400 ypos 270
    ""
    #=====================================
    scene 57 with dissolve
    image 57T = Text(" Autor original \n\n   Yuumei \n\n\n Programador y traductor \n\n   Dantalian \n\n\n Fondo \n\n   Lindsey Stirling - River Flows In You \n\n   Peder B. Helland - Always", size=25, color="#311500", font="fonts/Trixie.ttf")
    show 57T with dissolve:
        xalign 0.8 yalign 0.5
    ""
    #=====================================

    return
