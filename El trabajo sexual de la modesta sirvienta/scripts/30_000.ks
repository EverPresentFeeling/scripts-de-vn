;※時間帯：朝
;※------------------------------------------------------------


;アイキャッチ

[haikei file="ec01a" st="bg" fade="cross" time="1500"]

[se file="ec01"]

[haikei file="ec01b" st="bg" fade="20" time="1500"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]



;ＳＥ/小鳥の囀り
[se file="se070"]

;背景　空　昼
[hide_char]
[haikei file="cmnbg9900" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]

;※背景：和室　朝

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

[bgm file="bgm15"]

Al día siguiente.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Um...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Esta mañana, estoy estudiando como siempre. Pero, no puedo[r]concentrarme en absoluto.
[tp]

La imagen de Yuuki masturbándose sigue apareciendo en mi[r]mente, y no puedo ignorarla.
[tp]

No he dejado de pensar en por qué hizo eso anoche.
[tp]

Además, estos últimos días, he notado cierta distancia entre[r]Yuuki y yo. Debo haberla hecho sentir mal.
[tp]

He admirado a Yuuki todo este tiempo, y debería estar feliz de[r]que me haya elegido para ser su prometido. Pero ahora, no lo sé.
[tp]

Mis sentimientos no están cambiando a Kochi porque ella es con[r]la que realmente me acosté, ¿verdad? En realidad no me importa[r]más Kochi, ¿verdad?
[tp]

La razón por la que Yuuki ha estado actuando de forma extraña[r]estos últimos días podría ser porque ha notado esos[r]sentimientos.
[tp]

Estoy aquí como el prometido de Yuuki. No como amante de[r]Kochi.
[tp]

Debería sentirme mal por haber hecho que Yuuki se preocupe de[r]que me esté enamorando de Kochi. Esto es culpa mía.
[tp]

[if exp="f.root_flg == 0"]
[jump target="*30_000end"]
[endif]

;※判定
;※フラグ１

Pero aunque sé que...
[tp]

Kochi también es muy importante para mí. No puedo olvidarla.
[tp]

No hay manera de que pueda entrelazar mi cuerpo con el suyo y[r]no sentir nada. Eso sería imposible.
[tp]

Pensando en eso, suspiro...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Ah...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

;※効果：暗転


;※背景：屋敷中庭　朝

Cuando miro el jardín, veo a Kochi rastrillando las hojas.
[tp]

Supongo que es su trabajo, así que no es algo tan inusual.[r]Pero...
[tp]


*30_000end

[return]


;※フラグ１の時のみ選択肢２発生
;※選択肢
;※こちねぇととにかく話がしたい？

;※俺は悠姫の婚約者だ　→　30_001へ
;※話がしたい　→　30_002へ


;※フラグ０

;※30_001へ