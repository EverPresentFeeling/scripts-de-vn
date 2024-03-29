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

;※背景：和室

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

[bgm file="bgm02"]

Tras la cena y el baño, esta noche vuelvo a entrar en silencio en[r]la habitación de Kochi.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;小百合/下着/P1/Ｍ/伏せ目＋口開き（返答用）
[char_c file="ta123"]
[char_action time="800"]

;※声だけ
[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0000"]
Gracias por venir de nuevo esta noche, Fujimiya-sama.
[tp]

[name text="Asato"]
No, gracias a ti. Ja, ja...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Me acerco lentamente al lado del futón y empiezo a quitarme la[r]ropa.
[tp]

Ya he visto esta escena innumerables veces, pero mi corazón[r]sigue acelerándose y me excita.
[tp]

Tal vez sea porque me apetece mucho, pero ya estoy listo para[r]ir a por ello; solo tengo que esperar a que Kochi se quite la ropa.
[tp]

;※立ち絵〜小百合（下着）：イン

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;小百合/下着/P2/Ｍ/真剣
[char_c file="ta131"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0001"]
Bueno...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Después de que Kochi se desnuda y empieza a dar un paso[r]adelante. Pero, entonces la puerta se abre sin hacer ruido.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;小百合/下着/P2/Ｍ/きょとん
[char_c file="ta135"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0002"]
¿Eh? Oh... señora...
[tp]

[name text="Asato"]
¿Eh? ¿Yuuki?
[tp]

;※立ち絵〜琴羽（私服）：イン

[hide_char]
;琴羽/私服/P2/Ｍ/ため息
[char_l file="ta215"]
;小百合/下着/P2/Ｍ/きょとん
[char_r file="ta135"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0000"]
Disculpen.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Yuuki entra.
[tp]

Kochi está aquí. Yuuki parece saber lo que estamos haciendo,[r]pero no le molesta vernos.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

[name text="Asato"]
¿Qué pasa?
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Teniendo en cuenta que entró en la sala en un momento como[r]este, mi tono resulta duro.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/ジト目
[char_c file="ta206"]
[char_action time="800"]

[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0001"]
¿Qué pasa? He venido a ver lo que estaban haciendo. ¿Estaban[r]haciendo esto desde el principio?
[tp]

[name text="Asato"]
Uh, um... sí.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Al principio, solo estábamos Kochi y yo; así que por supuesto.
[tp]

Esperaba que fuéramos solo nosotros dos.
[tp]

Así que, honestamente, me preocupa que Yuuki esté aquí[r]ahora...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

[name text="Asato"]
Kochi, ¿qué te parece?
[tp]

;小百合/下着/P1/Ｍ/伏せ目＋口開き（返答用）
[char_c file="ta123"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0003"]
No hay problema, esto es lo que la joven ama desea.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Pero si Kochi dice que está bien, entonces no puedo decir nada.
[tp]

Vuelvo a centrar mi atención en Kochi y la abrazo. Lo único que[r]puedo hacer es concentrarme en esto.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="bg" fade="cross" time="1000"]

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]

*begin_scene

;※cg080

[flash layer="6" count="0" interval="80"]

[se file="seha06"]

[haikei file="AP3U_080" st="ev" fade="cross" time="1500"]

[bgm file="bgm04"]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0004"]
Mm, aah, mm... aah...
[tp]

;//我慢小
[playse buf="2"  storage="bgv025" loop="true"]

[name text="Asato"]
Ugh...
[tp]

Después de besarla y abrazarla, Kochi se sienta sobre mí y guía mi[r]pene dentro de ella.
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0005"]
Me moveré...
[tp]

;//打ち付け　早め
[playse buf="3" storage="seha08" loop="true"]

;//あえぎ声小
[playse buf="2"  storage="bgv021" loop="true"]

[name text="Asato"]
Claro, aaah...
[tp]

Un ruido de aplastamiento resuena por la unión de nuestros[r]genitales. Disfruto de este placer mientras aprieto los pechos de[r]Kochi.
[tp]

[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0002"]
Te has acostumbrado a esto mientras yo no he estado mirando.
[tp]

;//我慢小
[playse buf="2"  storage="bgv025" loop="true"]

[name text="Asato"]
Ugh...
[tp]

La voz de Yuuki enfría mi fuego.
[tp]

Antes miraba con interés, pero ahora parece un poco molesta.
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0006"]
Señora...
[tp]

[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0003"]
Oh, no te preocupes por mí. Por favor, continúa. Umm...
[tp]

;//我慢小
[playse buf="2"  storage="bgv025" loop="true"]

[name text="Asato"]
Ugh...
[tp]

Me enfrento a Kochi directamente. Pero como Yuuki dijo que[r]continuáramos, decidimos seguir avanzando.
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0007"]
Aah, ah, ah...
[tp]

;//あえぎ声小
[playse buf="2"  storage="bgv021" loop="true"]

[name text="Asato"]
Kgh...
[tp]

Me dejo arrastrar por el placer que surge. Me siento mal, pero me[r]olvido de la presencia de Yuuki y decido hundir más mi pene dentro[r]de Kochi...
[tp]

;※cg081

[haikei file="AP3U_081" st="ev" fade="cross" time="1000"]

[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0004"]
...
[tp]

;//あえぎ声小（併せ）
[playse buf="2"  storage="bgv221" loop="true"]

[name text="Asato"]
Ugh...
[tp]

Cuando cambio de posición para intentar profundizar, algo entra en[r]mi campo de visión.
[tp]

[name text="Asato"]
¿Eh?
[tp]

No importa cómo lo mire, ella se está masturbando. Yuuki se está[r]masturbando.
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0008"]
Aah...
[tp]

;//あえぎ声小（併せ）
[playse buf="2"  storage="bgv221" loop="true"]

Al notar mi reacción, Kochi también levanta la vista y se da cuenta[r]de lo que está pasando.
[tp]

[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0005"]
¡Aah, mm, aah, aaah...!
[tp]

;//我慢小（琴羽）
[playse buf="2"  storage="bgv125" loop="true"]

Yuuki está tan absorta en lo que está haciendo que tiene los ojos[r]cerrados, así que no se da cuenta de que nos hemos dado cuenta.
[tp]

[name text="Asato"]
(¿Por qué está... masturbándose tan fuerte...? Antes no era así, ¿por[r]qué ahora...?)
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0009"]
¿Continuamos, Fujimiya-sama? Si la joven ama se entera de que nos[r]fijamos en ella, se sentirá herida.
[tp]

;//我慢小（琴羽）
[playse buf="2"  storage="bgv125" loop="true"]

[name text="Asato"]
Es cierto. Eso no sería bueno, aah...
[tp]

Si eso sucede, Yuuki recibirá un gran shock mental. Sería mejor[r]fingir que no vemos nada.
[tp]

;※cg082

[haikei file="AP3U_082" st="ev" fade="cross" time="1000"]

;//打ち付け　通常
[playse buf="3" storage="seha07" loop="true"]

;//あえぎ声中（併せ）
[playse buf="2"  storage="bgv222" loop="true"]

Squelch, squelch, squelch...
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0010"]
¡Ah, ah, aah, mm! ¡Me estoy corriendo, estoy a punto de correrme...!
[tp]

;//あえぎ声中（併せ）
[playse buf="2"  storage="bgv222" loop="true"]

[name text="Asato"]
Ugh, aah...
[tp]

De repente, empieza a meter y sacar los dedos con más fuerza.[r]Aunque estoy desconcertado, ver a Yuuki metiéndose los dedos tan[r]agresivamente me excita aún más.
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0011"]
Para que la joven ama no empiece a sospechar, aah, mm, tenemos[r]que concentrarnos en lo que estamos haciendo, o se dará cuenta.
[tp]

;//あえぎ声中（併せ）
[playse buf="2"  storage="bgv222" loop="true"]

[name text="Asato"]
¡Uh, ugh, eso es, aah! ¡Concentrémonos... kgh...!
[tp]

El placer que se dispara en la parte inferior de mi cuerpo, combinado[r]con la obscena visión de la masturbación de Yuuki, me pone al[r]borde del clímax.
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0012"]
Solo te centras en la joven ama... Mm, aah...
[tp]

;//あえぎ声中（併せ）
[playse buf="2"  storage="bgv222" loop="true"]

[name text="Asato"]
Lo siento, kgh... Estoy a punto de correrme, aah...
[tp]

Para distraerla, empiezo a empujar mis caderas con más fuerza.
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0013"]
¡Ah, aah! ¡Por favor, córrete! Yo también me estoy corriendo... ¡Voy a[r]tener un orgasmo, umm...!
[tp]

;※効果：白フラッシュ

;※cg083

[flash layer="6" count="3" interval="80"]

[stopse buf="2"]
[stopse buf="3"]
[hide_textwindow]
[haikei file="white" st="bg" fade="cross" time="500"]

[se file="seha11"]

[haikei file="AP3U_083" st="ev" fade="cross" time="1000"]

[se file="seha10"]

¡¡Spurt, spurt, glug, spurt!!
[tp]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0014"]
¡Ah, mm, ah, aah, aaah...!
[tp]

[name text="Asato"]
¡Uf, kgh, aaah!
[tp]

[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0006"]
Aah, aah, uh, ugh...
[tp]

Parece que los tres llegamos al orgasmo simultáneamente.
[tp]

Gracias al espectáculo de Yuuki, estoy más excitado que de[r]costumbre y me corro enseguida.
[tp]

;※効果：暗転

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]

[end_scene]

;※背景：和室

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="bg" fade="cross" time="1500"]

[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

[bgm file="bgm26"]

Cuando terminamos, Kochi se desploma sobre mí;[r]aparentemente sin energía.
[tp]

La atrapo, mientras mi respiración se encuentra agitada.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

[name text="Asato"]
Aah, aah, Kochi... Eso se sintió muy bien...
[tp]

;※立ち絵〜小百合（全裸）：イン

;小百合/裸/P1/Ｍ/微笑
[char_c file="ta142"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0015"]
Sí... a mí también me sentó muy bien...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Nuestros cuerpos calientes y sudorosos están pegados el uno al[r]otro.
[tp]

El suave cuerpo de Kochi es agradable al tacto, y me encuentro[r]acariciando su espalda.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/ため息
[char_c file="ta205"]
[char_action time="800"]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0007"]
Ugh...
[tp]

[name text="Asato"]
Oh...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Puedo sentir la presencia de Yuuki allí. Cuando me vuelvo para[r]mirarla, se está acomodando la ropa desaliñada; me mira como si[r]nada.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;琴羽/私服/P1/Ｍ/ジト目
[char_c file="ta206"]
[char_action time="800"]

;※声だけ
[name text="Kotoha"]
[voice id="kth" file="vf20_050kth0008"]
Voy a volver a mi habitación...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Dice eso con una voz un poco áspera y se va.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;小百合/裸/P1/Ｍ/伏せ目＋口開き（ため息用）
[char_c file="ta144"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0016"]
Gracias... Ah, umm...
[tp]

[name text="Asato"]
Ugh...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Tras verla marchar, dejo escapar un largo suspiro.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="ev" fade="cross" time="500"]

;小百合/裸/P1/Ｍ/伏せ目＋口開き（返答用）
[char_c file="ta143"]
[char_action time="800"]

[name text="Sayuri"]
[voice id="syr" file="vf20_050syr0017"]
Fujimiya-sama. Por favor, no digas ni una palabra de lo que has visto[r]aquí a nadie.
[tp]

[name text="Asato"]
Sí, está bien... No se lo diré a nadie...
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702b" st="nv" fade="cross" time="500"]

Tengo muchos sentimientos al respecto, pero al menos puedo[r]prometer eso. Ni una palabra a nadie.
[tp]

;背景　和室　夜
[hide_char]
[haikei file="cmnbg0702" st="bg" fade="cross" time="1000"]

;※効果：場面転換＋時間経過（夜　→昼

[stopse buf="2"]
[stopse buf="3"]

[hide_char]
[hide_balloon_window]
[hide_textwindow]
[stop_bgm fadeout="1500"]
[stop_se]
[haikei file="black" st="bg" fade="cross" time="1500"]
[return]

;※30_000へ