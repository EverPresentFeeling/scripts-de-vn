;=============================================================================;
;The Modest Handmaid's Sex Work ~I will be your partner in place of the young mistress~
;=============================================================================;

;各種フラグ初期化
[eval exp="f.root_flg = 0"]

[eval exp="f.ed01 = false"]
[eval exp="f.ed02 = false"]

;=============================================================================;
*00|
;=============================================================================;

[call storage="00_000.ks"]
[call storage="00_010.ks"]
[call storage="00_020.ks"]
[call storage="00_030.ks"]

[call storage="10_000.ks"]
[call storage="10_010.ks"]
[call storage="10_020.ks"]
[call storage="10_030.ks"]

;10_030内
;*************
;*	選択肢01 *
;*************

[call storage="10_040.ks"]

[call storage="20_000.ks"]
[call storage="20_010.ks"]
[call storage="20_020.ks"]

;*************
;*	  判定   *
;*************

[if exp="f.root_flg == 0"]
	[jump target="*20_021"]
[endif]

[jump target="*20_022"]


;=============================================================================;
*20_021|
;=============================================================================;

[call storage="20_021.ks"]

[jump target="*20_030"]


;=============================================================================;
*20_022|
;=============================================================================;

[call storage="20_022.ks"]

[jump target="*20_030"]


;=============================================================================;
*20_030|
;=============================================================================;

[call storage="20_030.ks"]

;*************
;*	  判定   *
;*************

[if exp="f.root_flg == 0"]
	[jump target="*20_031"]
[endif]

[jump target="*20_032"]


;=============================================================================;
*20_031|
;=============================================================================;

[call storage="20_031.ks"]

[jump target="*20_040"]


;=============================================================================;
*20_032|
;=============================================================================;

[call storage="20_032.ks"]

[jump target="*20_040"]


;=============================================================================;
*20_040|
;=============================================================================;

[call storage="20_040.ks"]
[call storage="20_050.ks"]

[call storage="30_000.ks"]

;フラグ０時は選択肢発生せず30_001直行
[if exp="f.root_flg == 0"]
	[jump target="*30_001"]
[endif]

;*************
;*	選択肢02 *
;*************
;選択肢１：俺は悠姫の婚約者だ
;選択肢２：話がしたい　フラグ＋１

[stopquake]
[hide_textwindow]
[exbuttonopt forevisible="false" backvisible="true"]
[begin_link]
[exbutton name="choice01" x="50"  y="133" file="choice02a" onclick="ChJump('', '*30_001')"]
[exbutton name="choice02" x="50"  y="323" file="choice02b" onclick="ChJump('', '*30_002')"]
[crossfade time="500"]
[end_link]

[wait_button]


;=============================================================================;
*30_001|
;=============================================================================;
[cm]
[exformopt delete="all" forevisible="false" backvisible="true"]
[hide_textwindow]

[call storage="30_001.ks"]

[jump target="*30_010"]


;=============================================================================;
*30_002|
;=============================================================================;
[cm]
[exformopt delete="all" forevisible="false" backvisible="true"]
[hide_textwindow]

[call storage="30_002.ks"]

[eval exp="f.root_flg++"]

[jump target="*30_010"]


;=============================================================================;
*30_010|
;=============================================================================;

[call storage="30_010.ks"]

;*************
;*	  判定   *
;*************

[if exp="f.root_flg == 2"]
	[jump target="*40_000"]
[endif]

[jump target="*50_000"]


;=============================================================================;
*40_000|
;=============================================================================;

[call storage="40_000.ks"]
[call storage="40_010.ks"]
[call storage="40_020.ks"]

[call storage="ed.ks"]

[call storage="40_999.ks"]


[jump target="*GameEnd"]


;=============================================================================;
*50_000|
;=============================================================================;

[call storage="50_000.ks"]
[call storage="50_010.ks"]
[call storage="50_020.ks"]
[call storage="50_030.ks"]

[call storage="ed.ks"]

;*************
;*	  判定   *
;*************

[if exp="f.root_flg == 1"]
	[jump target="*50_999"]
[endif]

[jump target="*60_999"]


;=============================================================================;
*50_999|
;=============================================================================;

[call storage="50_999.ks"]

[jump target="*GameEnd"]


;=============================================================================;
*60_999|
;=============================================================================;

[call storage="60_999.ks"]

[jump target="*GameEnd"]


;[eval exp="f.ed01 = true"]
;[eval exp="f.ed02 = true"]

;=============================================================================;
;終了処理
;=============================================================================;
*GameEnd|
[cm]


*Gamebad|

[stopquake]

;終了処理
[exmenuopt delete="all"]
[exsmenuopt delete="all"]
[exformopt delete="all"]
[exbuttonopt delete="all"]

[layopt layer="message0" page="back" visible="false"]
[layopt layer="message1" page="back" visible="false"]
[layopt layer="message2" page="back" visible="false"]
[layopt layer="message3" page="back" visible="false"]
[layopt layer="message4" page="back" visible="false"]

[layopt layer="00_" page="back" visible="false"]
[layopt layer="1" page="back" visible="false"]
[layopt layer="2" page="back" visible="false"]
[layopt layer="3" page="back" visible="false"]
[layopt layer="4" page="back" visible="false"]
[layopt layer="5" page="back" visible="false"]
[layopt layer="13" page="back" visible="false"]
[layopt layer="14" page="back" visible="false"]
[layopt layer="15" page="back" visible="false"]

[eval exp="sf.end = true"]

[return]
