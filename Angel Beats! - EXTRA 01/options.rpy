








init -1 python hide:





    config.developer = False



    config.screen_width = 900
    config.screen_height = 600




    config.window_title = u"Angel Beats! Track Zero Extra 01"







    layout.button_menu()











    theme.roundrect(
        
                                    
        
        widget = "#003c78",

        
        widget_hover = "#0050a0",

        
        widget_text = "#c8ffff",

        
        
        widget_selected = "#ffffc8",

        
        disabled = "#404040",

        
        disabled_text = "#c8c8c8",

        
        label = "#ffffff",

        
        frame = "#6496c8",

        
        
        
        mm_root = "menu.jpg",

        
        
        
        gm_root = "menu2.jpg",

        
        
        rounded_window = False,

        
        
        
        )










    style.window.background = Frame("frame.png", 12, 12)












    style.window.left_padding = 15



































    style.default.font = "CALIFR.TTF"



    style.default.size = 24











    config.has_sound = True



    config.has_music = True



    config.has_voice = True



    style.button.activate_sound = "click.wav"
    style.imagemap.activate_sound = "click.wav"



    config.enter_sound = "click.wav"
    config.exit_sound = "click.wav"

    config.hard_rollback_limit = 100    









init python:


    style.window.right_padding = 100

    def toggle_skipping():
        config.skipping = not config.skipping

    show_button_game_menu = True

    def button_game_menu():
        
        if show_button_game_menu:
            
            
            ccinc = renpy.curried_call_in_new_context
            
            ui.vbox(xpos=0.99, ypos=0.98, xanchor='right', yanchor='bottom')
            ui.textbutton("Guardar", clicked=ccinc("_game_menu_save"), xminimum=100)
            ui.textbutton("Cargar", clicked=ccinc("_game_menu_load"), xminimum=100)
            ui.textbutton("Menú", clicked=ccinc("_game_menu_load"), xminimum=100)
            ui.close()


    config.overlay_functions.append(button_game_menu)    

    config.main_menu_music = "op.mp3"












    config.help = "README.html"






    config.enter_transition = dissolve


    config.exit_transition = dissolve


    config.intra_transition = None


    config.main_game_transition = dissolve


    config.game_main_transition = fade


    config.end_splash_transition = None


    config.end_game_transition = fade


    config.after_load_transition = fade


    config.window_show_transition = None


    config.window_hide_transition = None






python early:
    config.save_directory = "Angel Beats! Extra Chapter 01-1277151191"

init -1 python hide:









    config.default_fullscreen = False



    config.default_text_cps = 0




init:
    $ style.default.drop_shadow = (1, 1)
    $ style.default.drop_shadow_color = "#000"        
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
