[_tb_system_call storage=system/_title_screen.ks]

[tb_eval  exp="sf.adult=1"  name="adult"  cmd="="  op="t"  val="0"  val_2="undefined"  ]
[hidemenubutton]

[tb_clear_images]

[chara_new name="fuj" storage=fujname01.png jname=""]

[tb_keyconfig  flag="0"  ]
[iscript]
if(sf.namesystem ==undefined){
sf.namesystem = `〇〇`;
}
[endscript]

[tb_hide_message_window  ]
[bg  storage="fugikibg/fjkbg001.jpg"  time="1000"  cross="false"  method="fadeInUp"  ]
[wait  time="1000"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/rogo002.png"  ]
[wait  time="1000"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg017.jpg"  ]
[bg  time="1000"  method="fadeIn"  storage="fugikibg/fjkbg049.jpg"  ]
*return01

[hidemenubutton]

[tb_clear_images]

[wait  time="2000"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg017.jpg"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg025.jpg"  ]
*title

[showmenubutton]

[tb_keyconfig  flag="1"  ]
[glink  color="btn_15_black"  storage="scene000.ks"  size="20"  text="Historia&nbsp;principal"  x="450"  y="260"  width="400"  height=""  _clickable_img=""  ]
[glink  color="btn_15_black"  storage="h08ntrstory.ks"  size="20"  x="450"  y="324"  width="400"  height=""  text="Historia&nbsp;adicional"  _clickable_img=""  ]
[glink  color="btn_15_black"  text="Cargar"  x="450"  y="391"  size="20"  target="*load"  width="400"  height=""  _clickable_img=""  ]
[jump  storage="title_screen.ks"  target="*noadult"  cond="sf.adult==0"  ]
[glink  color="btn_15_red"  storage="scenekaihou.ks"  size="20"  text="Escenas&nbsp;y&nbsp;escenas&nbsp;extra"  x="450"  y="459"  width="400"  height=""  _clickable_img=""  ]
[glink  color="btn_15_red"  storage="dougakaihou.ks"  size="20"  text="Colección&nbsp;de&nbsp;animaciones"  x="450"  y="528"  width="400"  height=""  _clickable_img=""  ]
[glink  color="btn_15_red"  storage="cgpage00.ks"  size="20"  text="Borradores&nbsp;y&nbsp;galería"  x="450"  y="599"  width="400"  height=""  _clickable_img=""  ]
*noadult

[glink  color="btn_15_blue"  storage="title_screen.ks"  size="20"  text="Créditos"  x="450"  y="670"  width="400"  height=""  _clickable_img=""  target="*credit"  ]
[glink  color="btn_07_black"  storage="title_screen.ks"  size="20"  text="Ajustes"  x="1070"  y="735"  width=""  height=""  _clickable_img=""  target="*config"  ]
[s  ]
*start

[cm  ]
[s  ]
*load

[cm  ]
[showload]

[jump  target="*title"  storage=""  ]
*credit

[tb_start_tyrano_code]
@layopt layer=message0 visible=true
[position layer=message0 width=1280 height=650 top=100 left=0 marginl=50]
[_tb_end_tyrano_code]

[tb_show_message_window  ]
[tb_start_text mode=3 ]
Versión del juego: 1.00 Development Build[r]
Creado por: Kurenai Book & Aki Masanari[r]
La voz de Fujiki es Kumoya Hachi[r]
Fondos: Haikei Senmonten Minikuru y Haikei Sozaiya[r]
Efectos de sonido: Matchmakers[r]
Sonidos de Woodpecker provistos por Tanuri no Otoya de Niconi Commons[r]
BGM:ayato sound create(東京詩篇～TOKYO　POETRY、純愛と背徳の為の音楽)[r]
Referencia de modelo 3D: Easy Poser[r]
[_tb_end_text]

[l  ]
[tb_start_text mode=3 ]
『Traducción al Español』[r]
Traducción:Dalians[r]

Edición:Dalians[r]

Control de calidad:Mougour[r]
[_tb_end_text]

[l  ]
[tb_start_tyrano_code]
@layopt layer=message0 visible=true
[position layer=message0 width=1280 height=250 top=530 left=0 margint=5 marginl=230 marginr=150 marginb=10]
[_tb_end_tyrano_code]

[tb_hide_message_window  ]
[jump  target="*title"  storage=""  ]
*config

[tb_show_message_window  ]
[tb_start_text mode=1 ]
Ajuste el volumen y otros parámetros desde AJUSTES en la barra lateral.[p]
(Actualmente no se pueden ver las escenas).[p]
[_tb_end_text]

[tb_hide_message_window  ]
[jump  target="*title"  storage=""  ]
[s  ]
