;※時間帯：朝
;※------------------------------------------------------------

;ＳＥ/小鳥の囀り
[se file="se070"]

;背景　空　昼
[hide_char]
[haikei file="cmnbg9900" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]

;※背景：和室　朝

;※ＳＥ＜ピピピ、チュンチュンなど＞小鳥のさえずり

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="1500"]

[bgm file="bgm20"]

[name text="Asato"]
Ugh, uups, aaah...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Esta mañana también me he levantado con ganas. Me despierto[r]todos los días incluso sin alarma.
[tp]

Todas las noches, gracias a Kochi, me siento moderadamente[r]cansado, fresco y duermo como un tronco.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Uy, hoy tengo exámenes de prueba para la escuela de posgrado.[r]Será mejor que me asegure de no llegar tarde.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

[stop_bgm fadeout="1500"]

Después de estirarme y levantarme, miro la hora en mi[r]teléfono...
[tp]

Dice '8:45' en la pantalla.
[tp]

¿No '7:45'?
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[bgm file="bgm07"]

[name text="Asato"]
De ninguna manera, a las 8 en punto... ¡Voy a llegar tarde!
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

No me he dado cuenta en absoluto, pero la alarma probablemente[r]ha sonado hace una hora. Seguro tenía demasiado sueño para[r]detenerla. Típico, ¿no?
[tp]

De todos modos, aunque me dé prisa, seguro que llegaré tarde.[r]Aun así, tengo que ir. Tengo que hacer los exámenes de prueba[r]para las clases que puedo...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
De todas formas, si corro y cojo un taxi desde algún sitio... ¡¡Guah,[r]date prisa, date prisa!!
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

De todos modos tengo que cambiarme, meter el material de[r]escritura y el teléfono en el bolso y salir corriendo de la[r]habitación.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="bg" fade="cross" time="1000"]

;※効果：暗転

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[haikei file="black" st="bg" fade="22" time="1200"]

;※背景：屋敷玄関　朝

;※効果：画面を小さく揺らす

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="22" time="1200"]

[quake time="700" hmax="10" vmax="5"]

;※声だけ
[name text="Sayuri"]
[voice id="syr" file="vf20_010syr0000"]
¡¿Kyah?!
[tp]

[name text="Asato"]
¡¿Guah?!
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Cuando salgo corriendo de la habitación, casi me tropiezo con[r]Kochi.
[tp]

;※立ち絵〜小百合（メイド服）：イン

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

;小百合/メイド服/P2/Ｍ/きょとん
[char_c file="ta115"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_010syr0001"]
¿Qué pasa? Lleva mucha prisa.
[tp]

[name text="Asato"]
¡Lo siento, Kochi! Me quedé dormido, ¡así que voy a llegar tarde a[r]mis exámenes de prueba!
[tp]

[name text="Asato"]
Quiero decir que estoy cien por cien seguro de que voy a llegar[r]tarde, pero al menos tengo que tomar los que pueda.
[tp]

;小百合/メイド服/P2/Ｍ/真剣
[char_c file="ta111"]
[char_action time="200"]

[name text="Sayuri"]
[voice id="syr" file="vf20_010syr0002"]
Pues...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Le explico rápidamente la situación y estoy a punto de correr[r]hacia la entrada, pero Kochi me detiene.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

;小百合/メイド服/P1/Ｍ/真剣
[char_c file="ta101"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_010syr0003"]
¡Fujimiya-sama! ¿Por qué no hablas con la joven ama y le dices que[r]te lleve si es el caso?
[tp]

[name text="Asato"]
Err, ¡¿que me lleve?!
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

No puedo evitar repetirle la inesperada sugerencia.
[tp]

Así es. No lo había pensado porque iba a la escuela en tren, pero[r]seguro que en casa de Yuuki hay coches.
[tp]

Depende de las condiciones de la carretera, pero sin duda será[r]más rápido que correr hasta la calle principal y esperar un taxi.[r]Quizá pueda llegar a tiempo...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Asato"]
¡Gracias, Kochi! ¡¡Iré a hablar con Yuuki!!
[tp]

;小百合/メイド服/P2/Ｍ/きょとん
[char_c file="ta115"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_010syr0004"]
¡Oh! ¡Por favor, espere! La joven ama todavía está...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Kochi sigue diciendo algo. Pero lo siento, no tengo tiempo para[r]escucharla.
[tp]

;※効果：暗転

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[haikei file="black" st="bg" fade="22" time="1200"]

;※背景：黒

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="22" time="1200"]

[name text="Asato"]
Muy bien...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Me apresuro y llego a la habitación de Yuuki, a la que he visitado[r]varias veces para que me ayude con mis estudios.
[tp]

;※ＳＥ＜コンコンコンなど＞効果音　ドアノック早い

;ＳＥ/ドアノック３回トントントン
[se file="se085"]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Asato"]
¡Yuuki! Sé que es temprano, ¡pero quiero pedirte un favor! ¡Voy a[r]entrar!
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Giro el pomo de la puerta antes de oír una respuesta.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="bg" fade="cross" time="1000"]

;※効果：暗転

[hide_char]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="03" time="1200"]

;※背景：お嬢様部屋　朝

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="03" time="1200"]

[bgm file="bgm26"]

[name text="Asato"]
¡Yuuki! Yuu...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Me quedo sin palabras, a pesar de tener mucha prisa.
[tp]

Libros, tazas, artículos de maquillaje, ropa y ropa interior. La[r]habitación de Yuuki es un desastre, con todo tipo de cosas[r]abandonadas.
[tp]

Mientras me quedo helado ante la inesperada visión, el futón de[r]la cama de su habitación se mueve.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0000"]
Mmm... ¿Qué pasa? Eres muy ruidosa por la mañana...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Desde el interior del futón, una Yuuki con ojos de sueño y el[r]cabello revuelto, se asoma llevando solo su ropa interior.
[tp]

;※立ち絵〜悠姫（下着）：イン

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/下着/P1/Ｍ/ため息
[char_c file="ta225"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0001"]
Te dije que me dejaras dormir más de lo habitual ya que Fujimiya no[r]está aquí esta mañana...
[tp]

[name text="Asato"]
Bueno...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Me quedo congelado en el sitio. Cuando mis ojos se encuentran[r]con los suyos, Yuuki deja de moverse.
[tp]

Aturdido por la visión de esta habitación, y siendo esta la primera[r]vez que veo a Yuuki en ropa interior, no sé qué decir.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/下着/P1/Ｍ/きょとん
[char_c file="ta224"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0002"]
Fuji... ¿eh?
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

[stop_bgm fadeout="1500"]

Me mira, se mira a sí misma y luego me mira de nuevo...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

[bgm file="bgm07"]

;琴羽/下着/P2/Ｍ/きょとん
[char_c file="ta234"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0003"]
¡¡Kyaaaaaah!!
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

;※効果：画面を揺らす

;※ＳＥ＜ボフッなど＞クッションがぶつかる音

[quake time="700" hmax="10" vmax="5"]

Mientras grita, me lanza un cojín que me da directamente en la[r]cara.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

[name text="Asato"]
¡¡Aah!!
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Y es entonces cuando recobro el sentido común.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/下着/P2/Ｍ/ジト目
[char_c file="ta236"]
[char_action time="800"]

;※怒りではなく、恥ずかしさで取り乱している様子
[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0004"]
¡Sal de mi habitación! ¡Rápido!
[tp]

[name text="Asato"]
Lo siento...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="bg" fade="cross" time="1000"]

;※効果：暗転

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="22" time="1200"]

;※背景：屋敷玄関　朝

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="22" time="1200"]

[bgm file="bgm15"]

[name text="Asato"]
Aah, aah, ugh, aah, aaaah...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Me disculpo apresuradamente y salgo corriendo de la habitación[r]para alejarme de Yuuki, que sostiene un segundo cojín para[r]lanzármelo.
[tp]

Y desde el interior de la habitación, oigo un revuelo de actividad.
[tp]

Ahora que lo pienso, recuerdo haber esperado fuera de su[r]habitación cuando vine por primera vez para que me ayudara con mis[r]estudios.
[tp]

Me pregunto si su habitación estaba desordenada y ella también[r]la estaba limpiando esa vez.
[tp]

Había ropa interior y cosas en el suelo... ¿Es del tipo descuidada?
[tp]

;※立ち絵〜悠姫（私服）：イン

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/ため息
[char_c file="ta205"]
[char_action time="800"]

;※落ち着いているが、いつもより元気がない
[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0005"]
Gracias por esperar.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Mientras pienso en esto, Yuuki sale de la habitación; casi sin[r]aliento.
[tp]

Su cabello y su ropa están listos en su estilo habitual; rápida[r]como un rayo.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

[name text="Asato"]
Ah, lo siento, interrumpí tu sueño...
[tp]

;琴羽/私服/P2/Ｍ/ため息
[char_c file="ta215"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0006"]
Debes haberte sentido muy decepcionado conmigo... Siento haberte[r]mostrado algo desagradable...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Pero su brío y energía habituales han desaparecido y mira hacia[r]abajo.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

[name text="Asato"]
Me sorprendió porque nunca te había visto así, pero no me[r]decepcionó.
[tp]

;琴羽/私服/P2/Ｍ/真剣
[char_c file="ta211"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0007"]
Pero nunca habías tenido esa imagen de mí, ¿verdad? No quería que[r]me vieras así.
[tp]

[name text="Asato"]
Nadie es perfecto. Me alivia saber que tienes algunos defectos.
[tp]

;琴羽/私服/P1/Ｍ/微笑
[char_c file="ta202"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0008"]
Eres muy amable.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

No se me ocurren las palabras adecuadas para decirlo, pero[r]cuando veo que Yuuki me sonríe, yo también me siento aliviado.
[tp]

Pero al mismo tiempo, siento una punzada en el pecho al ver la[r]sonrisa de Yuuki.
[tp]

Pero antes de que pueda pensar en lo que está causando este[r]dolor...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/きょとん
[char_c file="ta204"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0009"]
Por cierto, ¿no se supone que hoy vas a hacer unos simulacros de[r]examen?
[tp]

[name text="Asato"]
¡Ah! ¡Oh, sí! ¡Los exámenes de prueba!
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Las palabras de Yuuki me recuerdan lo que debo hacer.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

[name text="Asato"]
¡Me he quedado dormido y voy a llegar tarde! ¡Por favor! ¡¡Dame un[r]aventón!!
[tp]

;琴羽/私服/P2/Ｍ/きょとん
[char_c file="ta214"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_010kth0010"]
¡¿Qué?! ¿No es un gran problema? Bien, tendrás que esperar fuera.
[tp]

;※効果：暗転


;※背景：黒

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="nv" fade="cross" time="1500"]

Al enterarse de lo sucedido, Yuuki me consigue inmediatamente[r]un coche.
[tp]

El coche empieza a moverse hacia el centro de pruebas mientras[r]Yuuki me despide.
[tp]

;※効果：暗転


;※背景：模試会場　朝

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg0250b" st="bg" fade="cross" time="500"]

[bgm file="bgm26"]

Entonces, con las prisas de última hora, soy capaz de llegar al[r]examen a tiempo.
[tp]

Como se esperaba de un conductor profesional, conducía[r]estupendamente y conocía bien las calles secundarias. Era[r] seguro y rápido.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="500"]

[name text="Asato"]
Aah... justo a tiempo...
[tp]

[name text="Examiner"]
Es hora de empezar. Por favor, tomen asiento.
[tp]

[name text="Asato"]
Lo siento...
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

Sin tomarme un momento para calmarme, tomo asiento; lo que[r]atrae la atención del examinador y de los demás alumnos. Casi[r]llego tarde, lo que me hace destacar.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="500"]

[name text="Asato"]
(Bien, tranquilízate... Llevas toda la mañana alterado, pero tienes[r]que bajar la cabeza de las nubes. No dejes que te distraigan...)
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

Hay un ambiente tenso en la sala. Si fuera el día de la prueba[r]real, sería aún más sofocante.
[tp]

Cuando le doy la vuelta a la hoja de respuestas a la señal del[r]examinador, para comenzar la prueba, me digo esto.
[tp]

A partir de aquí, solo tengo que mantener la calma y[r]concentrarme.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="bg" fade="cross" time="1000"]

;※効果：場面転換＋時間経過（朝　→昼

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※20_020へ