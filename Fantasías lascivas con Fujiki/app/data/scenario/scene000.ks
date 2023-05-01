[_tb_system_call storage=system/_scene000.ks]

[wait  time="2000"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg017.jpg"  ]
[wait  time="2000"  ]
[tb_show_message_window  ]
[tb_start_text mode=1 ]
Introduce tu nombre, así te llamarán durante el juego. Si dejas este campo en blanco, te mencionarán como 〇〇.[p]
[_tb_end_text]

[tb_hide_message_window  ]
*name00

[edit  left="484"  top="360"  width="372"  height="45"  size="20"  maxchars="10"  reflect="false"  name="f.name"  ]
[button  storage="scene000.ks"  target="*name01"  graphic="config/arrow_next.png"  width="56"  height="52"  x="869"  y="360"  _clickable_img=""  name="img_8"  ]
[s  ]
*namemarumaru

[tb_eval  exp="f.name='〇〇'"  name="name"  cmd="="  op="t"  val="〇〇"  val_2="undefined"  ]
*name01

[commit  ]
[cm  ]
[jump  storage="scene000.ks"  target="*namemarumaru"  cond="f.name==''"  ]
[tb_eval  exp="sf.namesystem=f.name"  name="namesystem"  cmd="="  op="h"  val="name"  val_2="undefined"  ]
[tb_show_message_window  ]
[tb_start_text mode=1 ]
Tu nombre se ha determinado como [name].[p]
[_tb_end_text]

[tb_hide_message_window  ]
[playse  volume="100"  time="1000"  buf="0"  storage="bell00.ogg"  ]
[glink  color="white"  storage="scene000a.ks"  size="30"  text="Iniciar"  x="400"  y="322"  width="400"  height=""  _clickable_img=""  ]
[jump  storage="scene000.ks"  target="*noadult"  cond="sf.adult==0"  ]
[glink  color="white"  storage="h01wapaizuri.ks"  size="30"  text="Ir&nbsp;al&nbsp;contenido&nbsp;para&nbsp;adultos"  x="400"  y="430"  width="400"  height=""  _clickable_img=""  ]
*noadult

[wse  ]
[s  ]
