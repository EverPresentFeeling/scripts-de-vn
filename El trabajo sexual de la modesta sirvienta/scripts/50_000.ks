;※時間帯：夜
;※------------------------------------------------------------

;※背景：和室　夜

;※判定

[if exp="f.root_flg == 0"]
[jump target="*50_000b"]
[endif]



;※フラグ１

;=============================================================================;
*50_000a|
;=============================================================================;

No puedo negar que siento algo por Kochi.
[tp]

Pero no debo olvidar que soy el prometido de Yuuki.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

[name text="Asato"]
Debería pensar en Yuuki antes que nada. Eso es obvio...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Vuelvo a intentarlo por enésima vez hoy.
[tp]

;※合流へ

[jump target="*50_000c"]

;※フラグ０

;=============================================================================;
*50_000b|
;=============================================================================;

No me arrepiento de haberme convertido en el prometido de[r]Yuuki.
[tp]

Yuuki es atractiva, y es cierto que es mi primer amor. O mejor[r]dicho, la he admirado desde que era un niño. Estoy[r]honestamente feliz de que me haya elegido para ser su[r]prometido.
[tp]

Y por otro lado, solo después de que Kochi y yo tuviéramos una[r]relación física me interesé por ella.
[tp]

Por eso estoy seguro de que mis sentimientos por Kochi se[r]basan en el deseo sexual, porque este comienza con el cuerpo.
[tp]

Para decirlo sin rodeos, creo que solo me interesa porque está[r]disponible para el sexo.
[tp]

Es una falta de respeto tanto a Yuuki como a Kochi dejar que[r]esos sentimientos impuros influyan en mi corazón.
[tp]

Creo que es hora de que me lo piense con detenimiento.
[tp]

;※合流へ

[jump target="*50_000c"]

;※合流

;=============================================================================;
*50_000c|
;=============================================================================;

Quizá he pedido demasiado últimamente, sobre todo cuando hago[r]cosas con Kochi.
[tp]

A partir de ahora, intentaré mantener esas cosas al mínimo, para[r]no olvidar mi posición en todo esto.
[tp]

Trataré a Kochi como a la hermana mayor de una amiga de la[r]infancia.
[tp]

Hoy, gracias a mi decisión, siento que me he quitado parte del[r]peso de encima.
[tp]

Por eso he intentado pasar todo el tiempo posible con Yuuki[r]mientras estudio para mi examen de grado.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="bg" fade="cross" time="1000"]

;※効果：場面転換＋時間経過（夜　→数週間後へ

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※50_010へ