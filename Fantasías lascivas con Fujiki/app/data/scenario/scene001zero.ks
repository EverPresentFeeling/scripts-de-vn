[_tb_system_call storage=system/_scene001zero.ks]

[wait  time="2000"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg025.jpg"  ]
[wait  time="2000"  ]
[tb_show_message_window  ]
[playbgm  volume=""  time="1000"  loop="true"  storage="fugikibg/15_EDEN.ogg"  fadein="true"  ]
[tb_show_message_window  ]
[tb_start_text mode=1 ]
(ここに会話)[p]
[_tb_end_text]

[tb_hide_message_window  ]
[wait  time="2000"  ]
[stopbgm  time="1000"  ]
[bg  time="1000"  method="fadeInUp"  storage="fugikibg/fjkbg017.jpg"  ]
[jump  storage="scene002.ks"  target=""  ]
