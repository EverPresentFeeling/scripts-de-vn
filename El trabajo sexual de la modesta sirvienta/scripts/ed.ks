;背景変化なし版

[eval exp="tf.ending = true"]
[cancelskip]
[cancelautomode]
;[clickskip enable="true"] 

[exmenuopt delete="all"]
[exsmenuopt delete="all"]
[exformopt delete="all"]

;エンドロールで流すBGMをここで指定
[bgm file="bgmed01" loop="false"]
;[stop_bgm fadeout="200000"]

;エンドロール背景をここで指定

;[eval exp="f.ramdom=intrandom(1,2)"]

;[if exp="f.ramdom == 1"]
;	[bg file="ed01"]
;[endif]

;[if exp="f.ramdom == 2"]
;	[bg file="ed02"]
;[endif]


;[if exp="f.ed01"]
;	[bg file="ed01"]
;[endif]

;[if exp="f.ed02"]
;	[bg file="ed02"]
;[endif]

;[if exp="f.ed03"]
;	[bg file="ed03"]
;[endif]

;[if exp="f.ed04"]
;	[bg file="ed04"]
;[endif]

[freeimage layer="0" page="back"]
[freeimage layer="1" page="back"]
[freeimage layer="2" page="back"]
[freeimage layer="3" page="back"]
[freeimage layer="4" page="back"]

[trans time="500" method="crossfade"]
[wt canskip="true"]

[wait time="500"]

[image layer="0" storage="staff2" page="back" left="0" top="0" visible="true"]
[trans time="500" method="crossfade"]
[wt]

;[layopt layer="0" page="fore" visible="true"]

[image layer="1" storage="staff" left="0" top="750"]
[layopt layer="1" page="fore" visible="true"]

;スクロールの指定、素材に合わせて毎回変更。
;layer="0"、staff2：背景、現在はＭＶの透過画像。pathは縦サイズ-600（画面サイズ）
;layer="1"、staff ：スタッフロール素材。pathは縦サイズ
;time：BGMの再生時間。曲の長さにあわせて変更。両方に共通。
[move layer="0" page="fore" time="90000" path="(0,-498,255)"]
[move layer="1" page="fore" time="90000" path="(0,-6600,255)"]

[wm canskip="true"]

*exit
[stop_bgm fadeout="1000"]

[eval exp="tf.ending = false"]
[clickskip enable="true"] 

;背景　ブラック
[haikei file="black" st="bg" fade="cross" time="1000"]

[call storage="mode_scenario.ks" target="*set_scenario_mode"]

[return]
