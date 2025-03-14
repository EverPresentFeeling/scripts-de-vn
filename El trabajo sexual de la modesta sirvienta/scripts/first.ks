
[iscript]
/*	cfファイルチェック	*/
var	file	= ( Storages.chopStorageExt( System.exeName ) + ".cf" );

if( Storages.isExistentStorage( file ) != true )
{
	System.inform( 'cfファイルがありません。終了します。' );
	System.exit();
}

[endscript]

[eval exp="sf.scenario_complete = [] if sf.scenario_complete === void"]

[title name="El trabajo sexual de la modesta sirvienta ~Seré su pareja en lugar de la joven ama~　EPF"]

;レイヤー構成は script/layer.txt 参照
[laycount layers="21" messages="5"]

[loadplugin module="wuvorbis.dll"]

[call storage="autoInsertLabel.ks"]
[call storage="customDialog.ks"]
[call storage="extraForms.ks"]
[call storage="extraKeybind.ks"]

[call storage="function.ks"]
[call storage="coschange.ks"]
[call storage="oppaicom.ks"]
[call storage="command.ks"]

[call storage="CtrlSkip.ks"]

[call storage="message.ks"]
[call storage="trans.ks"]
[call storage="effect.ks"]
[call storage="private.ks"]
[call storage="util.ks"]
[call storage="emotion.ks"]

;//メニューバーの切り替え
[if exp="kag.menu.visible == true"]
	[call storage="customMenu.ks"]
[endif]

;//plugin_load
[call storage="snow.ks"]
[call storage="fubuki.ks"]
[call storage="soundsync.ks"]
[call storage="zoom.ks"]
[call storage="QuakeSpPlugin.ks"]
[call storage="HeartBeatPlugin.ks"]
[call storage="exzoom.ks"]
[call storage="negaposi.ks"]
[call storage="clickcable.ks"]
[call storage="cgzoom.ks"]

;//メッセージのフェードプラグイン追加処理
[iscript]
Scripts.execStorage("MessageLayerADV.tjs");
[endscript]

[call storage="mode_config.ks" target="*init_config"]
[call storage="system_cfg.ks"]

[call storage="_first.ks"]



[call storage="mode_title.ks"]


[eval exp="kag.shutdown()"]
