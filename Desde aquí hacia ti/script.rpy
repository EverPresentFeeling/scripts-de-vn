#From me to you
#Music from Jukedeck - create your own at http://jukedeck.com.

define m = Character(_("Melón"), color="#FAA8D0")
define k = Character(_("Kiwi"), color="#C3FFC6")

# The game starts here.

label start:
    #Variables
    $ happy = 0
    $ dango = False

    play music "<loop 0>music/friends.ogg" fadein 2.0

    scene bg dedicatoria
    show bg bedroom
    with fade

    show kiwi sleep at left
    show melon sleep at right

    k "Zzz..."
    m "Zzz..."
    k "Zzz..."
    m "Zzz..."
    k "..."
    k "Bmmfgh."
    k "Uggh... Bien, es hora de levantarse."
    show kiwi grumpy at left
    k "Aaaamgh."
    k "Tengo que ir a la escuela..."
    show kiwi normal at left
    k "Ya... puedo hacerlo. Solo unos días más y estaré de vacaciones."
    k "¡Tú puedes, Kiwi!"
    k "Falta muy poco para que la veas de nuevo..."
    show kiwi blush at left
    k "Aaah..."
    k "Ya. Ya, me voy."

    scene bg fewhours
    $ renpy.pause(4.0, hard=True)

    scene bg schoolbedroom
    show kiwi normal at left
    show melon sleep at right
    m "Zzz... zzz..."
    m "Zzz..."
    show melon normal at right with vpunch
    m "¡Estoy despierta!"
    show melon grump at right
    m "Oh, dormí demasiado. Demonios."
    show melon normal at right
    m "Pero, quizás aún tenga tiempo de saludarlo."
    show melon silly at right
    m "Aaaah, ya no puedo esperar más."
    show melon normal at right
    m "Me pregunto cuándo volverá Kiwi a casa..."
    show melon grump at right
    m "Sus estudios están durando muchos meses..."
    m "Umgh... las vacaciones de verano no serán divertidas sin él."
    show melon normal at right
    m "Espero que él esté teniendo un buen día."
    m "Le escribiré un lindo mensaje mientras tanto."
    show melon silly at right
    m "Je, je, seré un poco pervertida. Umm.~"
    m "Pff..."
    show melon pnormal at right
    m "En fin, ¡hora de trabajar!"
    m "Ejem..."
    #play music "typing.sumn"
    m "¡Bienvenido a casa, mi cielo! Espero que hayas dormido muy bien y..."
    m "Tuviste un gran día en la escuela, ¿no? ¡Cuéntamelo todo!"
    show melon pblush at right
    m "Sabes que adoro que me cuentes todo lo que haces..."
    m "Me pone muy, muy feliz."
    m "¡Nunca olvides que tú eres el mejor novio del mundo mundial!"
    show melon pnormal at right
    m "Estoy muy ansiosa de poder hablar contigo."
    m "Con cariño, Melón."
    show melon normal at right
    m "¡Y enviado!"

    scene bg bedroom

    show kiwi pblush at left
    show melon normal at right

    k "Amor, ¡estoy en casa!"

    show melon pnormal at right
    m "¡¡Eh, Kiwi!! ¡Acabo de enviarte un mensaje!"
    show kiwi pblush at left
    k "¡Sí, lo sé! Recién lo leí y es muy bonito. Me sacó una sonrisa muy tonta."
    m "Ay... bebé..."
    show melon pblush at right
    m "Vas a hacer que me sonroje."
    show kiwi psmirk at left
    k "Je, je. Qué tierna."
    show melon pnormal at right
    show kiwi pnormal left
    m "¿Qué tal te fue en la escuela, Kiki?"
    menu:

        k "Oh, ya sabes, fue.."

        "Lo mismo de siempre.":
            jump same

        "¡Bastante bien!":
            $ happy+=1
            jump good

label same:
    k "Ya sabes, lo mismo de siempre."
    show kiwi psleep at left
    k "Me esforcé para mantenerme despierto la mayor parte del tiempo, ugh."
    show kiwi pnormal at left
    k "¡Pero eso ya no importa! Porque, ¡ya casi entramos de vacaciones!"
    m "Umm, supongo que no. Pero, me hubiera gustado que te divirtieras un poco más."
    m "Después de todo, eres muy bueno haciéndolo."
    show melon psilly at right
    m "Bueno, me emociona mucho más pensar en todo lo que compartiré contigo, aah.~"
    m "Nos divertiremos mucho."
    k "¡Sí, no puedo esperar!"
    jump continue1

label good:
    k "¡Hoy fue un día muy interesante!"
    k "Mi profesor de historia es muy gracioso."
    show kiwi psilly at left
    k "Sus chistes son horribles."
    k "Todos fingimos odiarlo, pero en realidad él es muy simpático."
    show kiwi pnormal at left
    m "¡Aah, ya veo!"
    m "Estoy muy contenta de que te hayas divertido hoy."
    m "Desearía que pudieras estar así de animado todos los días; todo el rato."
    show melon psad at right
    m "Incluso cuando no podemos hablar o hacer algo juntos."
    show melon normal at right
    m "Pero, pronto podremos hacer todo lo que querramos."
    k "¡Ummm, no puedo esperar!"
    jump continue1

label continue1:
    m "¡Oh! Amor, tu avión aterriza a las 18:00, ¿no?"
    k "Déjame ver... ¡Sí, a las 18:00 de tu ciudad!"
    m "Je, je. Esa noche aún nos dará tiempo para hacer... algo."
    show kiwi psmirk at left
    k "Amor... ¿de qué hablas?"
    show melon pblush at right
    m "¡N-No hablo de {b}ESO{/b}!"
    m "Eeeh..."
    show melon psilly at right
    m "Quiero que nos pasemos algún videojuego o algo así."
    m "¡Quizás mirar una película!"
    show melon pnormal at right
    show kiwi pnormal at left
    k "Je, je. Claro que sí, Mel."
    k "Aunque recuerdo que me habías dicho que querías..."
    show melon pblush at right
    m "¡KIWI! Sé lo que dije, p-pero no hablaremos de eso ahora."
    show melon pgrump at right
    m "U-Umph."
    show kiwi psilly at left
    k "Je, je. Ya sé todo lo que quieres que hagamos."
    m "..."
    m "Bueno... sí."
    show melon pblush at right
    m "Desde hace mucho que quería estar contigo. Para mí, no hay nadie que sea más importante que tú, Kiwi."
    m "¿Por qué no querría tenerte solo para mí?"
    show kiwi pblush at left
    k "¡O-Oye!"
    show melon psilly at right
    m "Je, je."
    m "Ahora es tu turno de sonrojarte, casanova."
    show melon pnormal at right
    show kiwi pnormal at left
    k "Está bien, me atrapaste."
    k "Pero tienes razón, no puedo creer que voy a poder abrazarte en tan solo dos días."
    k "Esperamos mucho tiempo..."
    show melon psad at right
    m "Ah, lo sé. Estos cinco meses fueron una eternidad."
    m "La universidad no nos deja estar juntos..."
    show melon pnormal at right
    k "Es lo que hay."
    show melon psilly at right
    m "¡Pero no te cambiaría por nada en el mundo!"
    show kiwi pblush at left
    k "Ay..."
    show melon pnormal at right
    show kiwi pnormal at left
    menu:
        m "Oh... pero..."

        "¿Crees que ya fueron demasiados meses?":
            $ happy+=1
            jump toomany

        "Están siendo unos tiempos muy duros.":
            jump tough


label toomany:
    k "Umm..."
    k "Sí, fue demasiado tiempo. Per, no hubo ni un solo día en el que no me haya divertido contigo."
    k "Incluso cuando estamos muy lejos."
    show kiwi pblush at left
    show melon pblush at right
    k "Todo lo que quiero es poder pasar el tiempo contigo y que nunca dejemos de hablar."
    k "Y siempre valdrá la pena si puedo volverte a ver."
    k "Es por eso que no creo que haya sido demasiado tiempo."
    m "Ay... Kiwi..."
    show melon pnormal at right
    m "Me siento de la misma forma que tú."
    m "Incluso estando tú allá y yo aquí, sigues siendo mi mejor amigo."
    m "Y-Y el mejor novio que he tenido..."
    m "No quiero estar sin ti, ni perder el tiempo con otra persona."
    m "Tú eres simplemente... el mejor."
    show melon pblush at right
    m "> //// <"
    k "> //// <"
    show melon pnormal at right
    show kiwi pnormal at left
    k "Pero, eso no cambia el hecho de que estoy ansioso por verte otra vez."
    k "En la vida real."
    m "Lo sé, cariño. Yo también estoy muy impaciente."
    show melon psilly at right
    m "¡Voy a abrazarte y besarte mucho! ¡Lo estoy deseando muchísimo!"
    show kiwi psilly at left
    k "Oooh, nooo.~ No me soltarías jamás.~"
    k "Je, je."
    show kiwi pnormal at left
    jump continue2

label tough:
    m "Umm, pero últimamente ha sido un poco difícil..."
    m "Quiero decir, desde que te fuiste, tuve que estudiar muy duro y trabajar muchísimo."
    show melon psad at right
    m "Apenas hemos tenido tiempo para hablar..."
    k "Amor..."
    show melon pnormal at right
    k "Sabes que a mí tampoco me gusta que estemos así."
    k "Pero falta muy poco... ya casi estoy de vacaciones."
    m "Sí, tienes razón. Estoy siendo muy melodramática."
    show kiwi pgrumpy at left
    k "No... Oye, Mel, a mí también me molesta esto..."
    show kiwi pnormal at left
    k "Pero, no quiero que te sientas mal cuando sé que tú también te estás esforzando mucho."
    m "Umm, umm..."
    show melon psad at right
    m "Lo sé, pero te amo tdemasiado..."
    m "y además, eres mi mejor amigo..."
    m "Es normal que siempre tenga ganas de hablar contigo."
    k "Lo sé y te pido disculpas, cariño."
    k "Ya falta muy poco para que podamos volver a hablar todo el día; juntos."
    show melon pnormal at right
    m "Sí..."
    m "Bien, bien. No es momento para estar tristes."
    m "Todo será mucho mejor cuando pueda tenerte entre mis brazos."
    jump continue2

label continue2:
    show melon pgrump at right
    m "¡Aah, desearía que ya se acabasen estos días!"
    show melon pnormal at right
    k "Lo harán antes de que te des cuenta, cariño."
    m "¡Eso es verdad!"
    m "¡Oh, amor! Dame un momento que iré a echarme en el sofá."
    m "Aquí no llega muy bien el internet. ¡Dame un segundo!"
    k "¡Está bien!"
    scene bg bedliving
    show melon pnormal at right
    show kiwi pnormal at left
    m "¡Volví! Perdón por eso."
    k "Aw, no hay problema, amor. ¡Espero que la señal llegue mejor allí!"
    m "Creo que sí."
    m "¿Quieres mirar anime?"
    k "¡Me encantaría!"
    show melon psilly at right
    m "¡Genial! Déjame revisar si hay alguno bueno esta temporada."
    k "¡Yo también lo haré!"
    show melon pnormal at right
    m "Oye... Kiki.."
    k "¿Sí, Melmel?"
    show melon pblush at right
    stop music fadeout 2.0
    m "Te amo."
    show kiwi pblush at left
    k "Yo también te amo; más que a nada en el mundo."

    scene bg oneweek
    $ renpy.pause(4.0, hard=True)
    scene bg airportbedroom

    show kiwi normal at left
    show melon sleep at right

    play music "<loop 0>music/friends.ogg" fadein 2.0

    k "Uff, aún es temprano..."
    k "Supongo que Melón sigue durmiendo, je, je."
    k "Le escribiré un mensaje antes de subir al avión."
    show kiwi pnormal at left
    k "A mi querida novia;"
    k "solo quedan unas pocas horas antes de que estemos juntos en la misma habitación."
    k "Estoy muy nervioso y muy, pero que muy emocionado."
    k "No puedo esperar a hundir mi cara en tu hombro y..."
    k "... quedarnos así, en paz, por un buen tiempo."
    k "Me es imposible amarte más de lo que ya te amo, pero cada día en el que me hablas..."
    k "... me obligas a tragarme esas palabras."
    show kiwi pblush at left
    k "Con cariño, Kiwi."
    show kiwi normal at left
    k "Bien, es hora de que me vaya."
    k "Aah, estoy muy emocionado."
    k "Ojalá Melón no se ponga demasiado nerviosa por mi ausencia."
    k "Ah, tengo que irme."
    hide kiwi normal at left
    scene bg fewhours
    $ renpy.pause(4.0, hard=True)
    scene bg airportbedroom
    show melon sleep at right
    m "Zzz... zzz..."
    m "Zzz... Kiwi... tengo que..."
    m "Ah-"
    show melon normal at right
    m "Espera... ummm... ¿Qué hora es...?"
    m "¡¡¿¿QUÉ??!!"
    show melon grump at right
    m "Aah, no... No pude desearle un buen viaje a Kiwi..."
    m "Demonios, ¿por qué siempre me quedo dormida para las cosas más importantes?"
    m "*suspiro*"
    show melon blush at right
    m "Bueno, espero que haya llegado a tiempo."
    m "Ahh..."
    show melon normal at right
    m "¡Tengo que prepararme para cuando llegue!"
    m "¡Muy bien, hay que ordenar este desastre!"
    m "Tan solo tengo que tirar esta montaña de ropa sucia por aquí y..."
    m "¡Tengo que cambiar las sábanas!"
    show melon normal at right with vpunch
    m "¡Bien! Parece que ya está todo."

    menu:
        m "Umm, ¿no me estaré olvidado de algo...?"

        "¡Sí!":
            $ happy+=2
            $ dango=True
            jump yes

        "No":
            jump nope

label yes:
    m "¡Oh, claro!"
    show melon silly at right
    m "¡Casi olvido su regalo!"
    m "Dios, me habría puesto muy mal si lo olvidaba."
    scene bg grumpycat
    m "Conseguí esta foto..."
    m "Porque él ama a los gatos malhumorados."
    m "Je, je... Se ve muy tonto..."
    scene bg airportbedroom
    show melon normal at right
    m "¡Le encantará!"
    jump continue3

label nope:
    show melon normal at right
    m "Umm. ¡No, creo que eso es todo!"
    m "La verdad es que tampoco debe ser algo importante."
    show melon silly at right
    m "Tan solo quiero ver su cara y darle un gran abrazo."
    jump continue3

label continue3:
    show melon normal at right
    m "Ya es hora de ir al aeropuerto a recogerlo."
    show melon blush at right with vpunch
    m "¡Estoy tan emocionada que me cuesta manejarlo!"
    show melon normal at right
    if dango==True:
        m "Bien. Tengo la imagen del gato, mis llaves..."
        m "¡Umm, eso es todo!"
    m "Ya estoy lista para irme, creo."
    stop  music fadeout 2.0
    show melon silly at right
    m "Kiwi, ¡allá voy!"

    scene bg airport
    show melon normal at right

    play music "<loop 0>music/waiting.ogg" fadein 2.0

    m "Esperar en el aeropuerto es muy frustrante..."
    show melon sad at right
    m "Estoy muy nerviosa..."
    m "Ojalá no le haya pasado nada a su avión."
    show melon normal at right
    m "¡Nada de pensamientos negativos! Tengo que ser paciente, cálmate Mel."
    show melon sad at right
    m "Escuché que su vuelo aterrizó hace 10 minutos..."
    m "¿Dónde está...?"
    show melon normal at right
    m "¡¡No te preocupes!!"
    m "Él va a venir caminando a través de esa puerta en cualquier momento y..."
    m "Y..."
    show melon blush at right
    stop  music fadeout 2.0
    m "..."
    m "...."
    m "....."
    scene bg end with fade
    show melon blush at right with vpunch
    show kiwi blush at left with vpunch
    play music "<loop 0>music/desire.ogg" fadein 2.0
    m "¡¡Kiwi!!"
    k "¡¡Melón!!"
    scene bg together

    m "Estoy muy feliz de verte."
    m "No tienes idea."
    k "No. Lo sé, Melón. Lo sé."

    scene bg longhug
    $ renpy.pause(4.0, hard=True)

    scene bg end
    show kiwi normal at left
    show melon normal at right
    if dango==True:
        m "¡Oh, por cierto...! ¡Te tengo esto...!"
        m "¡Espero que te guste!"
        m "¡Es un gato muy enfadado!"
        show melon blush at right
        m "Bueno, ¡una imagen de uno!"
        k "Ay... Melón."
        k "Me encanta."
        show kiwi blush at left
        k "Muchísimo."
        k "Siempre sabes cómo sacarme una sonrisa."
    else:
        m "¡OH, DIABLOS!"
        k "¿Qué pasa?"
        show melon sad at right with vpunch
        m "Me olvidé de traer tu regalo..."
        k "¡Ay! Melón, ¡no te preocupes!"
        show kiwi blush at left
        k "Iremos a casa de todas formas."
        show kiwi normal at left
        show melon normal at right
        m "Tienes razón..."
        m "Tan solo espera, ¡vas a amarlo!"
        k "¡Claro que sí!"

    if happy == 4:
        k "Soy el chico más feliz del mundo."
        show kiwi blush at left
        show melon silly at right
        m "Ese es el plan."
    else:
        m "Oye, Kiwi..."
        m "Sé que las cosas pueden ponerse duras a veces, pero.."
        m "Daré lo mejor de mí para que seas la persona más feliz..."
        m "... del mundo entero."
        k "Estoy seguro que lo harás."
        show kiwi blush at left
        show melon silly at right
        k "Porque, ya me haces muy feliz."

    stop  music fadeout 3.0

    scene bg endend with fade
    $ renpy.pause(4.0, hard=True)
    scene bg credits with fade
    $ renpy.pause(4.0, hard=True)
    scene bg thanks with fade
    $ renpy.pause(4.0, hard=True)
# This ends the game.

    return
