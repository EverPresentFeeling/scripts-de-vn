;※時間帯：昼
;※------------------------------------------------------------

;※背景：模試会場　昼

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="500"]

[name text="Asato"]
Bueno, es hora de comer.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

Comienza la pausa para comer y todos sacan simultáneamente[r]sus almuerzos.
[tp]

Después de sacar la fiambrera, recuerdo lo que ha pasado esta[r]mañana.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="bg" fade="cross" time="1000"]

;※効果：暗転

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="36" time="1200"]

[sepia_mode]

;※回想
;※背景：屋敷外観　朝


;※立ち絵〜悠姫（私服）：イン

;背景　屋敷外観　朝
[hide_char]
[haikei file="cmnbg1510" st="ev" fade="36" time="1200"]

[bgm file="bgm20"]

;琴羽/私服/P1/Ｍ/微笑
[char_c file="ta202"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_021kth0000"]
Toma, ten esta bola de arroz; puedes desayunar en el coche. No[r]podrás concentrarte en el examen si no comes nada.
[tp]

;琴羽/私服/P2/Ｍ/微笑
[char_c file="ta212"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf20_021kth0001"]
Y aquí está tu almuerzo. Son solo algunas sobras del desayuno, así[r]que disculpame.
[tp]

[name text="Asato"]
¡Oh, gracias! ¡Esto es una gran ayuda! Bueno, me voy.
[tp]

;琴羽/私服/P1/Ｍ/笑顔
[char_c file="ta203"]
[char_action time="200"]

[name text="Kotoha"]
[voice id="kth" file="vf20_021kth0002"]
Buena suerte, Fujimiya.
[tp]

[reset_color_mode]

;※効果：暗転
;※回想終了

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="36" time="1200"]

;※背景：模試会場　昼

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="bg" fade="36" time="1200"]

[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

[bgm file="bgm26"]

Y así, Yuuki me despidió, y llegué a un coche de lujo que[r]tenía un chófer.
[tp]

El almuerzo que me dio tiene dos cajas apiladas una encima de la[r]otra, llenas de un equilibrio perfecto de arroz y guarniciones.
[tp]

La coordinación de colores es estupenda, pero la forma en que[r]está empaquetado parece un poco tosca. Me pregunto si Yuuki[r]se asustó y empaquetó esto ella misma. Imaginarlo casi me hace[r]reír.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="500"]

[name text="Asato"]
Debió de estar nerviosa y me preparó esto esta mañana...
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

Me siento agradecido mientras murmuro esto. No importa su[r]aspecto; me alegro de que haya sido muy considerada.[r]Probablemente tampoco sabe mal.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="500"]

[name text="Asato"]
Hora de comer...
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

Pero al mover la mano para comer, me doy cuenta de que no hay[r]palillos.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="ev" fade="cross" time="500"]

[name text="Asato"]
Ja, ja, ja... Bueno, eso no se podía evitar. Ella tenía prisa.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250b" st="nv" fade="cross" time="500"]

Por supuesto, no tengo ninguna queja sobre algo tan pequeño.[r]Comeré con las manos si es necesario.
[tp]

Así que me como el bento; utilizando un palillo para comer[r]primero el pollo frito y luego paso a los otros platos de[r]acompañamiento.
[tp]

;背景　模試会場　昼
[hide_char]
[haikei file="cmnbg0250" st="bg" fade="cross" time="1000"]

;※効果：場面転換＋時間経過（昼　→夕

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※20_030へ