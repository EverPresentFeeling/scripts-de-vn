;=====================================================================
;	起動した直後に呼ばれるファイルです
;	初期化処理やオープニングムービー等を記述してください
;	基本マクロや関数は既に読み込まれている状態です
;	[return]するとタイトル画面に移行します
;=====================================================================

[eval exp="tf.ver = '2017/07/21 01'"]

[eval exp="tf.debugsys = null"]

;TODO:デバッグ時のみこのファイルを読み込んでください
;[call storage="debug.ks"]

;TODO:ボイスデータが入る前はこのフラグを立ててください。
;     ボイスデータが入った後はこのコマンドをコメント化してください。
;[eval exp="sf.debug_mode=true"]

;TODO:リリース時のみこのファイルを読み込んでください
[call storage="release.ks"]

;ファイルチェックしない場合はこちらを使用（原則ノンプロ版を要求されたときのみ）
;[call storage="nop_release.ks"]

[iscript]
if( tf.debugsys == null )
{
	System.inform( 'debug.ksかrelease.ksが読み込まれていません' );
	System.exit();
}

[endscript]

[clickskip enabled=false]

;TODO:拡張トランジションを使用する場合は;コメントを解除してください
[call storage="extrans.ks"]
[call storage="zoom.ks"]

;ゲームごとの特殊機能がある場合はここで設定
;[call storage="25cmap.ks"]

[clickskip enabled=true]


;TODO:ムービーやタイトルロゴを表示する場合はここに記述してください



[return]
