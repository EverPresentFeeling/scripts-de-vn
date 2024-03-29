;※50_030

;アイキャッチ

[haikei file="ec04a" st="bg" fade="cross" time="1500"]

[se file="ec02"]

[haikei file="ec04b" st="bg" fade="20" time="1500"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]



;※背景：屋敷の外観や玄関など　朝

;※ＳＥ＜ピピピ、チュンチュンなど＞小鳥のさえずり


;ＳＥ/小鳥の囀り
[se file="se070"]

;背景　屋敷外観　朝
[hide_char]
[haikei file="cmnbg1510" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

[bgm file="bgm11"]

A la mañana siguiente.
[tp]

Aparte de que Yuuki vuelve a su habitación después de pasar la[r]noche, todo está como suele estar cuando me despierto. Pero...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Asato"]
Buenos días.
[tp]

[name text="Sirvienta"]
Buenos días, Fujimiya-sama.
[tp]

[name text="Mayordomo"]
Buenos días. Parece que hoy será otro buen día.
[tp]

[name text="Asato"]
Uh, sí, el tiempo de hoy es... sí... Ja, ja, ja...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

¿Qué ocurre? Siento que la gente de la mansión me mira de[r]forma diferente a cómo lo hacían antes.
[tp]

Es como si fueran más amistosos y relajados... Básicamente, más[r]familiares...
[tp]

Es como si me trataran no como un invitado o un inquilino, sino[r]como un miembro de la familia. Parece que me ven como uno de[r]los suyos de alguna manera.
[tp]

Me pregunto si es porque anoche me comprometí firmemente a[r]ser el prometido de Yuuki; tanto de nombre como de espíritu.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf50_030kth0000"]
¿Te sientes un poco más cómodo? Les dije que fueran más[r]amistosos contigo de ahora en adelante.
[tp]

[name text="Asato"]
¿Eeh? Oh... Yuuki...
[tp]

;※立ち絵〜悠姫（私服）：イン

;琴羽/私服/P1/Ｍ/微笑
[char_c file="ta202"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf50_030kth0001"]
Je, je. Buenos días, Fujimiya. No, quizás debería llamarte 'Asato'.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Al oír una voz, me doy la vuelta y veo a mi prometida Yuuki de[r]pie... No, ahora debería llamarla 'Kotoha'.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Asato"]
Buenos días. Um... ¿te preocupa mi comodidad?
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Intento que mis emociones no se reflejen en mi cara, pero[r]supongo que se habrá dado cuenta.
[tp]

Las cosas se estaban poniendo muy incómodas.[r]Independientemente de si soy su prometido o no, todo sucedió[r]tan repentinamente cuando vine a vivir a la mansión.
[tp]

Habría sido imposible relajarse y seguir viviendo aquí así.
[tp]

Imagino que la gente de la mansión no sabía cómo tratarme;[r]aunque no fuera su prometido, tampoco soy un miembro del[r]personal.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

;琴羽/私服/P2/Ｍ/笑顔
[char_c file="ta213"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf50_030kth0002"]
Sí, bueno, eres tú; así que puedo decir lo que estás pensando. Al fin[r]y al cabo somos novios. Je, je, je.
[tp]

[name text="Asato"]
Ja, ja... Se nota lo que estoy pensando, ¿eh?
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

También me río de las palabras de Yuuki... No, de Kotoha.
[tp]

Ya lo sabía, pero me da la sensación de que va a ser ella la que[r]lleve la voz cantante en esta relación.
[tp]

Dicho esto, se podría decir que ya lo es.
[tp]


;※フラグ０の場合※お嬢様一人です。※

[if exp="f.root_flg == 0"]
[jump target="*50_030end"]
[endif]

;※50_030後フラグ分岐へ


;※フラグ１の場合※お嬢様の側に侍女もいる。※

;=============================================================================;
*50_030a|
;=============================================================================;

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

;※声だけ
[name text="Sayuri"]
[voice id="syr" file="vf50_030syr0000"]
Je, je...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

Oigo otra voz desde las sombras.
[tp]

Kochi está escuchando nuestras idas y venidas; parece reírse[r]de nosotros mientras limpia.
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="ev" fade="cross" time="500"]

[name text="Asato"]
Ugh...
[tp]

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520b" st="nv" fade="cross" time="500"]

¿Qué demonios? Todos pueden ver a través de mí.
[tp]

Que se rían de mí dos mujeres que pueden saber exactamente lo[r]que estoy pensando, es vergonzoso se mire por donde se mire.[r]Sin embargo, no creo que sea algo malo.
[tp]


*50_030end|

;背景　屋敷玄関　朝
[hide_char]
[haikei file="cmnbg1520" st="bg" fade="cross" time="1000"]

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※50_030後フラグ分岐へ

;※;=================;
;※50_030後フラグ分岐
;※;=================;

;※フラグ１→50_999へ
;※フラグ０→60_999へ