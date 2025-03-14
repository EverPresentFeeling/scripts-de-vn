;※時間帯：夕〜夜
;※------------------------------------------------------------

;ＳＥ/学校チャイムキンコンカンコン
[se file="se009"]

;背景　空　夕
[hide_char]
[haikei file="cmnbg9901" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]

;※背景：模試会場　夕

;背景　模試会場　夕
[hide_char]
[haikei file="cmnbg0251" st="ev" fade="cross" time="1500"]

[bgm file="bgm15"]

[name text="Examinador"]
¡Muy bien, se acabó el tiempo! Bolígrafos abajo.
[tp]

[name text="Asato"]
Ufff...
[tp]

;背景　模試会場　夕
[hide_char]
[haikei file="cmnbg0251b" st="nv" fade="cross" time="500"]

Por fin termino el simulacro de examen de mi última clase.
[tp]

Suelto un gran suspiro mientras entrego mi hoja de respuestas.
[tp]

Siento que lo he hecho aún mejor. Con esto, voy a...
[tp]

;背景　模試会場　夕
[hide_char]
[haikei file="cmnbg0251" st="bg" fade="cross" time="1000"]

;※効果：暗転

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]


;ＳＥ/夜の虫
[se file="se152"]

;※夜

;背景　空　夜
[hide_char]
[haikei file="cmnbg9902" st="bg" fade="cross" time="2000"]

[wait time="2000"]

[stop_se fadeout="1500"]
[haikei file="black" st="bg" fade="cross" time="1500"]

;※背景：駅前　夜

;背景　駅前　夜
[hide_char]
[haikei file="cmnbg0382" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg0382b" st="nv" fade="cross" time="500"]

[bgm file="bgm26"]

De camino a casa, me dirijo a la estación de tren más cercana.[r]Aprovecho el tiempo de espera en los múltiples cruces de las[r]carreteras principales para enviar un mensaje a mis padres.
[tp]

Envío un mensaje sencillo: “Creo que me fue muy bien en mis[r]exámenes de prueba para la escuela de posgrado; un cambio de[r]escenario me vino bien”.
[tp]

Mis padres responden diciendo que están aliviados.
[tp]

También me dicen que no lo sabré con certeza hasta que me den[r]los resultados, así que no debo confiarme.
[tp]

;背景　駅前　夜
[hide_char]
[haikei file="cmnbg0382" st="bg" fade="cross" time="1000"]

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※判定
;※フラグ０→20_031へ
;※フラグ１→20_032へ