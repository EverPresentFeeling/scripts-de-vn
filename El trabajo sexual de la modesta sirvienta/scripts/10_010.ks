;※時間帯：朝
;※------------------------------------------------------------

;※背景：和室　朝

;※ＳＥ＜チッチッチッなど＞時計の秒針のSE

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

;[bgm file="bgm20"]

Después de desayunar, vuelvo a mi habitación y empiezo a[r]estudiar para mi examen de grado. Tengo que hacerlo lo mejor[r]posible; esta es mi principal tarea.
[tp]

;ＳＥ/秒針ゆっくり
[se file="se165" loop="true"]

...
[tp]

...
[tp]

...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Oh, lo entiendo.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

...
[tp]

...
[tp]

...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Umm...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

...
[tp]

...
[tp]

...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Oh, lo hice. Ya veo.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Estoy sorprendentemente concentrado. Estoy haciendo buenos[r]progresos.
[tp]

...
[tp]

...
[tp]

...
[tp]

O al menos, eso es lo que creo.
[tp]

[stop_se]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[bgm file="bgm20"]

[name text="Asato"]
Umm... Mierda, no lo entiendo.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Termino así muy rápidamente. Solo iba bien al principio.
[tp]

Al principio, podía avanzar con un libro de referencia en una[r]mano. Pero rápidamente acabé llegando a problemas que no[r]entendía, y ahora tanto mi cerebro como mi mano han dejado de[r]funcionar.
[tp]

Cuando miro el reloj, han pasado dos horas desde que empecé a[r]estudiar.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Oh... he hecho bastante...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Pensé que solo había pasado media hora. Incluso yo me[r]sorprendo de haber sido capaz de concentrarme durante tanto[r]tiempo.
[tp]

Este cambio de ambiente combinado con el cambio de mis[r]sentimientos debe haber funcionado bastante bien. Es mucho[r]más efectivo que todo lo que he intentado antes.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Umm...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Me gustaría tomarme un descanso ahora mismo, pero no estaré[r]contento si dejo sin resolver los problemas que no entiendo.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="ev" fade="cross" time="500"]

[name text="Asato"]
Yuuki dijo que me enseñaría...
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700b" st="nv" fade="cross" time="500"]

Cuando lo recuerdo, recojo mis herramientas de estudio y salgo[r]de la habitación.
[tp]

Si vivo bajo el mismo techo que una genio, sería una tontería no[r]preguntar.
[tp]

;背景　和室　昼
[hide_char]
[haikei file="cmnbg0700" st="bg" fade="cross" time="1000"]

;※効果：場面転換＋時間経過（短時間

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※10_020へ