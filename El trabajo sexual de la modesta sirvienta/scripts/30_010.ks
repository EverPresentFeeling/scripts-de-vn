;※時間帯：夜
;※------------------------------------------------------------

;ＳＥ/犬の遠吠え
[se file="se187"]

;背景　屋敷外観　夜（消灯）
[hide_char]
[haikei file="cmnbg1513" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]

;※背景：和室　夜

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

[bgm file="bgm26"]

Esta noche.
[tp]

Me encuentro pensando en mi situación actual y en lo que[r]debería hacer en el futuro.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

[name text="Asato"]
...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

...
[tp]

...
[tp]

Llevo mucho tiempo pensando en ello, pero no se me ocurre una[r]respuesta...
[tp]

[return]

;※判定
;※フラグ２→40_000へ
;※それ以外→50_000へ