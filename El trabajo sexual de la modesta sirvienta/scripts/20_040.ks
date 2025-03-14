;※時間帯：昼
;※------------------------------------------------------------

;アイキャッチ

[haikei file="ec04a" st="bg" fade="cross" time="1500"]

[se file="ec02"]

[haikei file="ec04b" st="bg" fade="20" time="1500"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]


;ＳＥ/小鳥の囀り
[se file="se070"]

;背景　屋敷外観　朝
[hide_char]
[haikei file="cmnbg1510" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]


;※背景：和室　朝〜昼

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="1500"]

[bgm file="bgm01"]

[name text="Asato"]
¡Muy bien, aquí voy!
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Al día siguiente.
[tp]

Hoy también me estoy preparando para mi examen. Estos días,[r]mi vida es muy típica de un estudiante universitario que intenta[r]entrar en la escuela de posgrado.
[tp]

Pero gracias al simulacro de examen de ayer, tengo mucha[r]confianza e incluso puedo decir que mi motivación está por las[r]nubes.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
A este ritmo, ¡mejoraré aún más!
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Aprovechando esto, abro el cuaderno de preguntas de exámenes[r]anteriores y empiezo a trabajar en ellas; creo que puedo[r]pasarlas con rapidez.
[tp]

...
[tp]

...
[tp]

...
[tp]

Esta mañana he progresado mucho en mis estudios.
[tp]

Después de eso, hago un hueco para comer y, por la tarde, me[r]centro en las asignaturas más difíciles.
[tp]

Entonces, como era de esperar, empiezo a encontrarme con[r]problemas en los que me atasco.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
No puedo hacer esto a la ligera. No creo que pueda hacerlos solo.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Debo haberme relajado demasiado durante el almuerzo y haber[r]bajado la guardia. Además, es imposible que pueda superar las[r]asignaturas difíciles con facilidad.
[tp]

Quizá haga que Yuuki las revise conmigo. Si no sé algo, puedo[r]preguntar, y cuando me desconecte, se enfadará conmigo.[r]Podré sacudirme parte de la tensión que siento.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="bg" fade="cross" time="1000"]

;※効果：暗転

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]

;※背景：屋敷玄関　昼

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

[bgm file="bgm15"]

Voy a la habitación de Yuuki y llamo a la puerta.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Asato"]
Oye, Yuuki, ¿puedes ayudarme a estudiar?
[tp]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0000"]
Oh... Um, por favor, espera un momento.
[tp]

;※声だけ
[name text="Asato"]
¿Eh?
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Su voz está teñida de vacilación cuando contesta, y puedo oír un[r]poco de ruido procedente de su habitación.
[tp]

...
[tp]

...
[tp]

Me hace esperar un rato...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0001"]
Muy bien, puedes entrar.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Tras esperar la respuesta de Yuuki, entro en su habitación.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="bg" fade="cross" time="1000"]

;※効果：暗転

[haikei file="black" st="bg" fade="03" time="1200"]

;※背景：お嬢様部屋

;※立ち絵〜悠姫（私服）：イン

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="03" time="1200"]

;琴羽/私服/P2/Ｍ/真剣
[char_c file="ta211"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0002"]
Perdón por la espera. Pasa.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Yuuki parece tranquila mientras se sienta frente a la mesa baja[r]de su habitación; ahora ordenada.
[tp]

Pero tengo una ligera sensación de antipatía. Algo parece fuera[r]de lugar...
[tp]


;※判定
;※フラグ０のとき

;*************
;*  判定   *
;*************

[if exp="f.root_flg == 0"]
[jump target="*20_040a"]
[endif]

[jump target="*20_040b"]


;=============================================================================;
*20_040a|
;=============================================================================;

Tal vez todavía está molesta por lo de ayer...
[tp]

;※合流へ

[jump target="*20_040c"]

;※フラグ１のとき

;=============================================================================;
*20_040b|
;=============================================================================;

Me pregunto qué pasa. ¿He hecho algo para que Yuuki se enfade?
[tp]

;※合流へ

[jump target="*20_040c"]

;※合流

;=============================================================================;
*20_040c|
;=============================================================================;

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/きょとん
[char_c file="ta204"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0003"]
¿No te vas a sentar?
[tp]

[name text="Asato"]
Ah, claro. Lo siento.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Sintiendo un poco de presión, me siento y extiendo mis[r]materiales de estudio. Lo primero es lo primero; tengo que[r]estudiar.
[tp]

...
[tp]

...
[tp]

Estudio diligentemente durante un tiempo.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/真剣
[char_c file="ta201"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0004"]
...
[tp]

[name text="Asato"]
...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Pero me molesta Yuuki, así que no puedo estudiar.
[tp]

Está tranquila como suele ser cuando estudiamos, y como[r]siempre, me explica las cuestiones que no entiendo si se lo pido.
[tp]

Pero hay algo pesado en el aire. No sé qué es...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;※判定

;*************
;*  判定   *
;*************

[if exp="f.root_flg == 0"]
[jump target="*20_040d"]
[endif]

[jump target="*20_040e"]

;※フラグ０のとき

;=============================================================================;
*20_040d|
;=============================================================================;

[name text="Asato"]
Oye, ¿todavía estás enfadada por lo de ayer?
[tp]

;琴羽/私服/P1/Ｍ/ため息
[char_c file="ta205"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0005"]
No estoy enfadada. Y no lo estaba, para empezar.
[tp]

[name text="Asato"]
Ya veo... Bien, claro, sí...
[tp]

;※合流へ

[jump target="*20_040f"]

;※フラグ１のとき

;=============================================================================;
*20_040e|
;=============================================================================;

[name text="Asato"]
Yuuki, ¿estás enfandada conmigo?
[tp]

;琴羽/私服/P1/Ｍ/きょとん
[char_c file="ta204"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0006"]
Para nada... ¿Hiciste algo que me debería enfadar?
[tp]

[name text="Asato"]
No, no tengo ni idea de lo que podría haber hecho... Umm...
[tp]

;※合流へ

[jump target="*20_040f"]

;※合流

;=============================================================================;
*20_040f|
;=============================================================================;

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Cuando dice eso, me pongo nervioso. Pero, no tengo más[r]remedio que tomarle la palabra.
[tp]

En realidad, no se me ocurre nada de lo que hice que haya hecho[r]enojar a Yuuki. Tal vez solo lo estoy pensando demasiado.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/ため息
[char_c file="ta205"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0007"]
...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Yuuki mira hacia otro lado, avergonzada.
[tp]

Parece que evita hablar de otra cosa que no sean mis estudios.
[tp]

No es la misma de siempre. Actúa avergonzada y mira hacia[r]abajo.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

[name text="Asato"]
(¡¿Tal vez ella está...?!)
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Se molesta con la gente sin razón y es difícil hablar con ella.[r]¡Ya sé lo que pasa!
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

[name text="Asato"]
Lo siento, Yuuki, no me di cuenta. Fui desconsiderado.
[tp]

;琴羽/私服/P2/Ｍ/きょとん
[char_c file="ta214"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0008"]
¿Eh? ¡¿Qué quieres decir?! No es nada...
[tp]

[name text="Asato"]
Estás con el período, ¿no? Por eso estás de mal humor. Siento no[r]haberme dado cuenta y seguir preguntándote...
[tp]

;琴羽/私服/P1/Ｍ/きょとん
[char_c file="ta204"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0009"]
¿Eh?
[tp]

[name text="Asato"]
Volveré a mi habitación, así que tómate una medicina y descansa.[r]Nos vemos.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Yuuki está asombrada. Recojo mis materiales de estudio y salgo[r]de la habitación; dejándola en paz.
[tp]

Oigo una voz enfadada detrás de mí.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/私服/P2/Ｍ/ふくれっ面
[char_c file="ta217"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0010"]
¡Lo has entendido todo mal! ¡No me malinterpretes y te vayas así!
[tp]

[name text="Asato"]
¿Qué? ¿Me equivoco?
[tp]

;琴羽/私服/P1/Ｍ/ふくれっ面
[char_c file="ta207"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0011"]
¡Estás completamente equivocado! Es decir, las mujeres se molestan[r]antes del período más a menudo que durante el mismo... ¡Ah, pero[r]no es eso!
[tp]

[name text="Asato"]
¿Qué? Pero entonces no sé qué pasa... ¿Por qué estás de mal[r]humor, Yuuki?
[tp]

;琴羽/私服/P1/Ｍ/ジト目
[char_c file="ta206"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0012"]
Ugh... bueno...
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Lo niega rotundamente, pero cuando la presiono, empieza a[r]murmurar. Cada vez entiendo menos. ¿Por qué está enfadada?
[tp]

Sé que no es bueno bombardearla con preguntas, pero ya que[r]me tiene así de confundido. No puedo dejar de preguntarme la[r]razón.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="ev" fade="cross" time="500"]

;琴羽/私服/P2/Ｍ/ふくれっ面
[char_c file="ta217"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0013"]
¡Esto no tiene nada que ver contigo! Si te estoy molestando,[r]¡entonces por favor vuelve a tu propia habitación y estudia!
[tp]

[name text="Asato"]
¡Guah! ¡¿Qué?!
[tp]

;※効果：画面を小さく揺らす

[quake time="700" hmax="10" vmax="5"]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870b" st="nv" fade="cross" time="500"]

Me quedo sin palabras y, al final, Yuuki utiliza la fuerza bruta para[r]empujarme fuera de su habitación.
[tp]

;背景　お嬢様部屋　昼
[hide_char]
[haikei file="cmnbg0870" st="bg" fade="cross" time="1000"]

;※効果：暗転

[haikei file="black" st="bg" fade="03" time="1200"]

;※背景：屋敷玄関　昼

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="03" time="1200"]

[name text="Asato"]
¡¿Espera un segundo, Yuuki?! ¡Lo siento, he hecho demasiadas[r]preguntas! ¡Um, y siento lo del período!
[tp]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0014"]
¡Dios, no tengo nada que decirte! ¡Vete!
[tp]

[name text="Asato"]
¡Yuuki!
[tp]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0015"]
¡Bleh! ¡Toma esto!
[tp]

;※ＳＥ＜バタンなど＞ドアを閉める音

;ＳＥ/ドア閉めるバタン
[se file="se006"]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Por un momento, Yuuki asoma la cabeza y me saca la lengua, y[r]luego cierra la puerta de su habitación.
[tp]

Estoy congelado y aturdido en la misma posición en la que[r]estaba cuando me empujó fuera de su habitación.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Asato"]
Bleh... ¿Qué? Buena suerte.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Nunca pensé que tuviera un lado infantil. Sin embargo, es algo[r]lindo.
[tp]

No, ¿qué acaba de pasar? ¿Por qué ha hecho eso?
[tp]

Al final, me echa y sigo sin saber nada. Estoy muy confundido.
[tp]

Sé que no puedo pedir más. Si voy más lejos, podría ser[r]golpeado.
[tp]

Espero frente a su puerta un rato, intentando obtener una[r]respuesta de ella, pero no da señales de salir. Así que, decido[r]volver a mi habitación con el rabo entre las piernas.
[tp]

Además, siento que la próxima vez que salga, me dará una[r]bofetada en la cara.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf20_040kth0016"]
¡Eres muy estúpido!
[tp]

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※効果：場面転換＋時間経過（昼　→夜

;※20_050へ