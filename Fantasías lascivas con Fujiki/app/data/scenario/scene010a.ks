[_tb_system_call storage=system/_scene010a.ks]

[wait  time="2000"  ]
[live2d_new  model_id="01fujikitatid"  breath="true"  lip_time="100"  ]
[live2d_fadeout  time="1000"  wait="false"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg002.jpg"  ]
[tb_show_message_window  ]
[tb_start_text mode=1 ]
Tarde por la noche, y no puedes dormir.[p]
Tomas tu tableta y empiezas a escribir.[p]
El título es: Placer.[p]
[_tb_end_text]

[tb_hide_message_window  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg017.jpg"  ]
[wait  time="2000"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg025.jpg"  ]
[wait  time="2000"  ]
[tb_show_message_window  ]
[playbgm  volume=""  time="1000"  loop="true"  storage="fugikibg/15_EDEN.ogg"  fadein="true"  ]
[tb_show_message_window  ]
[tb_start_text mode=1 ]
...[p]
Llevas toda la tarde trabajando, pero Fujiki aún no ha aparecido.[p]
Es el mayor tiempo que has pasado solo en esta cajita vacía desde que la conociste.[p]
No es que te moleste, ya que te ha dado tiempo para concentrarte en tu trabajo.[p]
Dices trabajo, pero no es nada del otro mundo. Algunos deberes, algo de lectura, navegar por sitios de vídeos y noticias, y ahora la entrada diaria en el diario.[p]
Nadie te habla, nadie te interrumpe. Por fin has alcanzado la verdadera paz.[p]
A pesar de lo cerca que está este edificio de la universidad, no has visto a nadie más que conozcas aquí. Y, mucho menos has hablado con ellos.[p]
Solo has tardado unos días en enamorarte de este lugar.[p]
Incluso le has tomado cariño al cuadro de un mono con una pistola en la mano, que siempre te mira desde arriba.[p]
Se respira paz.[p]
...[p]
La paz es lo único que hay.[p]
[_tb_end_text]

[tb_hide_message_window  ]
[wait  time="2000"  ]
[live2d_show  name="01fujikitatid"  x="0.03"  y="-0.38"  scale="1.7"  ]
[live2d_fadein  time="1000"  wait="false"  ]
[live2d_motion  name="01fujikitatid"  mtn="Idles2"  no="1"  ]
[wait  time="2000"  ]
[tb_show_message_window  ]
[playse  volume=""  time="1000"  buf="1"  storage="fsi/fct01.ogg"  ]
[tb_start_text mode=1 ]
"Oye".[p]
...[p]
"¿Pensaste que llegaría antes? No es que tenga la obligación de estar aquí".[p]
[_tb_end_text]

[live2d_motion  name="01fujikitatid"  mtn="Idles6"  no="6"  ]
[playse  volume=""  time="1000"  buf="1"  storage="fsi/fct32.ogg"  ]
[tb_start_text mode=1 ]
"Es solo que, ya sabes, tuve problemas para decidir qué ponerme".[p]
...[p]
[_tb_end_text]

[live2d_motion  name="01fujikitatid"  mtn="Idles"  no="0"  ]
[playse  volume=""  time="1000"  buf="1"  storage="fsi/fct21.ogg"  ]
[tb_start_text mode=1 ]
"De cualquier manera...".[p]
Escuchas una vez más las historias de la chica.[p]
Su cara se ilumina un poco cada vez que asientes a sus palabras.[p]
[_tb_end_text]

[tb_hide_message_window  ]
[live2d_fadeout  time="1000"  wait="false"  ]
[stopbgm  time="3000"  fadeout="true"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg017.jpg"  ]
[wait  time="4000"  ]
[jump  storage="scene011ed.ks"  target=""  cond="sf.adult==0"  ]
[jump  storage="h01wapaizuri.ks"  target=""  ]
