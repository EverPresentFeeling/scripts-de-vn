

[iscript]

/*	システム	*/
kag.systemMenu.add( kag.configMenuItem = new KAGMenuItem( kag, "Ajustes(&C)", 0, config, false ) );
kag.systemMenu.add( kag.saveMenuItem = new KAGMenuItem( kag, "Guardar(&S)", 0, save, false ) );
kag.systemMenu.add( kag.loadMenuItem = new KAGMenuItem( kag, "Cargar(&L)", 0, load, false ) );
kag.systemMenu.add( kag.goToStartMenuItem = new KAGMenuItem( kag, "Ir al inicio(&R)", 0, goToStart, false ) );
kag.systemMenu.add( kag.exitMenuItem = new KAGMenuItem( kag, "Salir(&X)", 0, exit, false ) );

/*	クイックセーブ	*/
kag.menu.add( kag.quickSaveMenu = new KAGMenuItem( kag, "Guardar rápido(&Q)", 0, quickSave, false ) );

/*	クイックロード	*/
kag.menu.add( kag.quickLoadMenu = new KAGMenuItem( this, "Carga rápida(&W)", 0, quickLoad, false ) );

/*	選択肢に戻る	*/
kag.menu.add( kag.backHistoryMenu = new KAGMenuItem( this, "Opciones(&B)", 0, backHistory, false ) );

/*	ボイスリピート	*/
kag.menu.add( kag.voiceRepeatMenu = new KAGMenuItem( this, "Repetir voz(&V)", 0, voiceRepeat, false ) );

/*	バックログ	*/
kag.menu.add( kag.showHistoryMenu = new KAGMenuItem( this, "Atrás(&O)", 0, showHistory, false ) );

/*	オート	*/
kag.menu.add( kag.autoMenu = new KAGMenuItem( this, "Automático(&A)", 0, auto, false ) );

/*	スキップ	*/
kag.menu.add( kag.skipMenu = new KAGMenuItem( this, "Saltar(&F)", 0, skip, false ) );

kag.setMenuAccessibleAll();

[endscript]

[return]
