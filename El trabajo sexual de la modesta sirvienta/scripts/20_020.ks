;※時間帯：昼
;※------------------------------------------------------------

;ＳＥ/学校チャイムキンコンカンコン
[se file="se009"]

;背景　模試会場廊下　昼
[hide_char]
[haikei file="cmnbg1110" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]

;※背景：模試会場　昼

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="1500"]

[bgm file="bgm26"]

[name text="Examinador"]
Muy bien, por favor, dejen sus bolígrafos.
[tp]

[name text="Asato"]
Ah...
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

A la señal del examinador, la prueba termina.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="500"]

[name text="Asato"]
Uff...
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="1000"]

Dejo el bolígrafo y suelto un enorme suspiro.
[tp]

Al principio no sabía cómo me iría, pero el simulacro de examen[r]de la mañana ha terminado.
[tp]

Me siento ligeramente satisfecho. También siento que me ha ido[r]muy bien después de estudiar en casa de Yuuki; estoy realmente[r]feliz.
[tp]

[return]


;※判定
;※フラグ０→20_021へ
;※フラグ１→20_022へ