init 2:
    $ sdl_cheat_string = ""
    
    image sdl_cheat_terminal_icon = get_image_7dl("gui/menu_elem/cheat/cheat_terminal_icon.png")

init python:
    # Обрабатываем символ
    def sdl_cheat_read_char(char):
        # Добавляем новый символ
        global sdl_cheat_string
        sdl_cheat_string += char
        
        # Проверяем, корректна ли введённая последовательность
        cheat_string_correct = False
        for code in sdl_cheat_code_to_handler:
            if code.startswith(sdl_cheat_string):
                cheat_string_correct = True
                break
        # Если нет - прерываем ввод чит-кода
        if not cheat_string_correct:
            sdl_cheat_string = ""
            renpy.hide_screen("sdl_cheat_reader")
            return
        
        # Если код полностью введён - вызываем обработчик
        if sdl_cheat_string in sdl_cheat_code_to_handler:
            sdl_cheat_code_to_handler[sdl_cheat_string]()
            sdl_cheat_string = ""
            renpy.hide_screen("sdl_cheat_reader")
            return
    
    def sdl_cheat_persistent_inc(p):
        if getattr(persistent, p):
            setattr(persistent, p, getattr(persistent, p) + 1)
        else:
            setattr(persistent, p, 1)
    
    def sdl_cheat_persistent_res(p):
        setattr(persistent, p, 0)
    
    # Обработчики чит-кодов
    def sdl_cheat_all_enable():
        sdl_cheat_persistent_inc("mi_7dl_sept")
        sdl_cheat_persistent_inc("mi_7dl_true")
        sdl_cheat_persistent_inc("mi_7dl_good_human")
        sdl_cheat_persistent_inc("mi_7dl_good_star")
        sdl_cheat_persistent_inc("mi_7dl_neu_human")
        sdl_cheat_persistent_inc("mi_7dl_neu_star")
        sdl_cheat_persistent_inc("mi_7dl_loki_exc")
        sdl_cheat_persistent_inc("mi_7dl_herc_exc")
        sdl_cheat_persistent_inc("mi_7dl_dr_exc")
        sdl_cheat_persistent_inc("mi_7dl_bad_human")
        sdl_cheat_persistent_inc("mi_7dl_bad_star")
        sdl_cheat_persistent_inc("mi_dj_true")
        sdl_cheat_persistent_inc("mi_dj_good_jap")
        sdl_cheat_persistent_inc("mi_dj_good_rf")
        sdl_cheat_persistent_inc("mi_dj_bad")
        sdl_cheat_persistent_inc("dv_7dl_sept")
        sdl_cheat_persistent_inc("dv_7dl_good_ussr")
        sdl_cheat_persistent_inc("dv_7dl_good_rf")
        sdl_cheat_persistent_inc("dv_7dl_rej_ussr")
        sdl_cheat_persistent_inc("dv_7dl_rej_rf")
        sdl_cheat_persistent_inc("dv_7dl_tran_mt")
        sdl_cheat_persistent_inc("dv_7dl_tran_un")
        sdl_cheat_persistent_inc("dv_7dl_loki_exc")
        sdl_cheat_persistent_inc("dv_7dl_bad")
        sdl_cheat_persistent_inc("sl_7dl_sept")
        sdl_cheat_persistent_inc("sl_7dl_good_rf")
        sdl_cheat_persistent_inc("sl_7dl_loki_good")
        sdl_cheat_persistent_inc("sl_7dl_loki_neu")
        sdl_cheat_persistent_inc("sl_7dl_loki_rej")
        sdl_cheat_persistent_inc("sl_7dl_herc_good")
        sdl_cheat_persistent_inc("sl_7dl_herc_neu")
        sdl_cheat_persistent_inc("sl_7dl_dr_good")
        sdl_cheat_persistent_inc("sl_7dl_dr_good2")
        sdl_cheat_persistent_inc("sl_7dl_bad")
        sdl_cheat_persistent_inc("sl_cl_int_true")
        sdl_cheat_persistent_inc("sl_cl_int_good")
        sdl_cheat_persistent_inc("sl_cl_int_bad")
        sdl_cheat_persistent_inc("sl_cl_good_ussr")
        sdl_cheat_persistent_inc("sl_cl_good_rf")
        sdl_cheat_persistent_inc("sl_cl_good_rf2")
        sdl_cheat_persistent_inc("sl_cl_rej_rf")
        sdl_cheat_persistent_inc("sl_cl_rej")
        sdl_cheat_persistent_inc("sl_cl_loki_exc")
        sdl_cheat_persistent_inc("sl_cl_bad")
        sdl_cheat_persistent_inc("un_7dl_sept")
        sdl_cheat_persistent_inc("un_7dl_true_tran")
        sdl_cheat_persistent_inc("un_7dl_good_ussr")
        sdl_cheat_persistent_inc("un_7dl_good_rf")
        sdl_cheat_persistent_inc("un_7dl_rej")
        sdl_cheat_persistent_inc("un_7dl_bad")
        sdl_cheat_persistent_inc("mt_7dl_sept")
        sdl_cheat_persistent_inc("mt_7dl_true")
        sdl_cheat_persistent_inc("mt_7dl_good")
        sdl_cheat_persistent_inc("mt_7dl_neu")
        sdl_cheat_persistent_inc("mt_7dl_bad")
        sdl_cheat_persistent_inc("us_7dl_true")
        sdl_cheat_persistent_inc("us_7dl_good")
        sdl_cheat_persistent_inc("us_7dl_tran_un")
        sdl_cheat_persistent_inc("us_7dl_tran_mi")
        sdl_cheat_persistent_inc("us_7dl_bad")
        sdl_cheat_persistent_inc("us_px_sept")
        sdl_cheat_persistent_inc("us_px_good")
        sdl_cheat_persistent_inc("me_neu_true")
        sdl_cheat_persistent_inc("me_neu_loki_neu")
        sdl_cheat_persistent_inc("me_neu_dr_neu")
        sdl_cheat_persistent_inc("me_neu_bad")
        sdl_cheat_persistent_inc("alt_lamp")
        sdl_cheat_persistent_inc("alt_deep")
        sdl_cheat_persistent_inc("alt_qte")
        sdl_cheat_persistent_inc("alt_victim")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_mi_enable():
        sdl_cheat_persistent_inc("mi_7dl_sept")
        sdl_cheat_persistent_inc("mi_7dl_true")
        sdl_cheat_persistent_inc("mi_7dl_good_human")
        sdl_cheat_persistent_inc("mi_7dl_good_star")
        sdl_cheat_persistent_inc("mi_7dl_neu_human")
        sdl_cheat_persistent_inc("mi_7dl_neu_star")
        sdl_cheat_persistent_inc("mi_7dl_loki_exc")
        sdl_cheat_persistent_inc("mi_7dl_herc_exc")
        sdl_cheat_persistent_inc("mi_7dl_dr_exc")
        sdl_cheat_persistent_inc("mi_7dl_bad_human")
        sdl_cheat_persistent_inc("mi_7dl_bad_star")
        sdl_cheat_persistent_inc("mi_dj_true")
        sdl_cheat_persistent_inc("mi_dj_good_jap")
        sdl_cheat_persistent_inc("mi_dj_good_rf")
        sdl_cheat_persistent_inc("mi_dj_bad")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_dv_enable():
        sdl_cheat_persistent_inc("dv_7dl_sept")
        sdl_cheat_persistent_inc("dv_7dl_good_ussr")
        sdl_cheat_persistent_inc("dv_7dl_good_rf")
        sdl_cheat_persistent_inc("dv_7dl_rej_ussr")
        sdl_cheat_persistent_inc("dv_7dl_rej_rf")
        sdl_cheat_persistent_inc("dv_7dl_tran_mt")
        sdl_cheat_persistent_inc("dv_7dl_tran_un")
        sdl_cheat_persistent_inc("dv_7dl_loki_exc")
        sdl_cheat_persistent_inc("dv_7dl_bad")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_sl_enable():
        sdl_cheat_persistent_inc("sl_7dl_sept")
        sdl_cheat_persistent_inc("sl_7dl_good_rf")
        sdl_cheat_persistent_inc("sl_7dl_loki_good")
        sdl_cheat_persistent_inc("sl_7dl_loki_neu")
        sdl_cheat_persistent_inc("sl_7dl_loki_rej")
        sdl_cheat_persistent_inc("sl_7dl_herc_good")
        sdl_cheat_persistent_inc("sl_7dl_herc_neu")
        sdl_cheat_persistent_inc("sl_7dl_dr_good")
        sdl_cheat_persistent_inc("sl_7dl_dr_good2")
        sdl_cheat_persistent_inc("sl_7dl_bad")
        sdl_cheat_persistent_inc("sl_cl_int_true")
        sdl_cheat_persistent_inc("sl_cl_int_good")
        sdl_cheat_persistent_inc("sl_cl_int_bad")
        sdl_cheat_persistent_inc("sl_cl_good_ussr")
        sdl_cheat_persistent_inc("sl_cl_good_rf")
        sdl_cheat_persistent_inc("sl_cl_good_rf2")
        sdl_cheat_persistent_inc("sl_cl_rej_rf")
        sdl_cheat_persistent_inc("sl_cl_rej")
        sdl_cheat_persistent_inc("sl_cl_loki_exc")
        sdl_cheat_persistent_inc("sl_cl_bad")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_un_enable():
        sdl_cheat_persistent_inc("un_7dl_sept")
        sdl_cheat_persistent_inc("un_7dl_true_tran")
        sdl_cheat_persistent_inc("un_7dl_good_ussr")
        sdl_cheat_persistent_inc("un_7dl_good_rf")
        sdl_cheat_persistent_inc("un_7dl_rej")
        sdl_cheat_persistent_inc("un_7dl_bad")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_mt_enable():
        sdl_cheat_persistent_inc("mt_7dl_sept")
        sdl_cheat_persistent_inc("mt_7dl_true")
        sdl_cheat_persistent_inc("mt_7dl_good")
        sdl_cheat_persistent_inc("mt_7dl_neu")
        sdl_cheat_persistent_inc("mt_7dl_bad")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_us_enable():
        sdl_cheat_persistent_inc("us_7dl_true")
        sdl_cheat_persistent_inc("us_7dl_good")
        sdl_cheat_persistent_inc("us_7dl_tran_un")
        sdl_cheat_persistent_inc("us_7dl_tran_mi")
        sdl_cheat_persistent_inc("us_7dl_bad")
        sdl_cheat_persistent_inc("us_px_sept")
        sdl_cheat_persistent_inc("us_px_good")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_me_enable():
        sdl_cheat_persistent_inc("me_neu_true")
        sdl_cheat_persistent_inc("me_neu_loki_neu")
        sdl_cheat_persistent_inc("me_neu_dr_neu")
        sdl_cheat_persistent_inc("me_neu_bad")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_va_enable():
        sdl_cheat_persistent_inc("alt_lamp")
        sdl_cheat_persistent_inc("alt_deep")
        sdl_cheat_persistent_inc("alt_qte")
        sdl_cheat_persistent_inc("alt_victim")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_on, channel='sound')
    
    def sdl_cheat_disable():
        sdl_cheat_persistent_res("mi_7dl_sept")
        sdl_cheat_persistent_res("mi_7dl_true")
        sdl_cheat_persistent_res("mi_7dl_good_human")
        sdl_cheat_persistent_res("mi_7dl_good_star")
        sdl_cheat_persistent_res("mi_7dl_neu_human")
        sdl_cheat_persistent_res("mi_7dl_neu_star")
        sdl_cheat_persistent_res("mi_7dl_loki_exc")
        sdl_cheat_persistent_res("mi_7dl_herc_exc")
        sdl_cheat_persistent_res("mi_7dl_dr_exc")
        sdl_cheat_persistent_res("mi_7dl_bad_human")
        sdl_cheat_persistent_res("mi_7dl_bad_star")
        sdl_cheat_persistent_res("mi_dj_true")
        sdl_cheat_persistent_res("mi_dj_good_jap")
        sdl_cheat_persistent_res("mi_dj_good_rf")
        sdl_cheat_persistent_res("mi_dj_bad")
        sdl_cheat_persistent_res("dv_7dl_sept")
        sdl_cheat_persistent_res("dv_7dl_good_ussr")
        sdl_cheat_persistent_res("dv_7dl_good_rf")
        sdl_cheat_persistent_res("dv_7dl_rej_ussr")
        sdl_cheat_persistent_res("dv_7dl_rej_rf")
        sdl_cheat_persistent_res("dv_7dl_tran_mt")
        sdl_cheat_persistent_res("dv_7dl_tran_un")
        sdl_cheat_persistent_res("dv_7dl_loki_exc")
        sdl_cheat_persistent_res("dv_7dl_bad")
        sdl_cheat_persistent_res("sl_7dl_sept")
        sdl_cheat_persistent_res("sl_7dl_good_rf")
        sdl_cheat_persistent_res("sl_7dl_loki_good")
        sdl_cheat_persistent_res("sl_7dl_loki_neu")
        sdl_cheat_persistent_res("sl_7dl_loki_rej")
        sdl_cheat_persistent_res("sl_7dl_herc_good")
        sdl_cheat_persistent_res("sl_7dl_herc_neu")
        sdl_cheat_persistent_res("sl_7dl_dr_good")
        sdl_cheat_persistent_res("sl_7dl_dr_good2")
        sdl_cheat_persistent_res("sl_7dl_bad")
        sdl_cheat_persistent_res("sl_cl_int_true")
        sdl_cheat_persistent_res("sl_cl_int_good")
        sdl_cheat_persistent_res("sl_cl_int_bad")
        sdl_cheat_persistent_res("sl_cl_good_ussr")
        sdl_cheat_persistent_res("sl_cl_good_rf")
        sdl_cheat_persistent_res("sl_cl_good_rf2")
        sdl_cheat_persistent_res("sl_cl_rej_rf")
        sdl_cheat_persistent_res("sl_cl_rej")
        sdl_cheat_persistent_res("sl_cl_loki_exc")
        sdl_cheat_persistent_res("sl_cl_bad")
        sdl_cheat_persistent_res("un_7dl_sept")
        sdl_cheat_persistent_res("un_7dl_true_tran")
        sdl_cheat_persistent_res("un_7dl_good_ussr")
        sdl_cheat_persistent_res("un_7dl_good_rf")
        sdl_cheat_persistent_res("un_7dl_rej")
        sdl_cheat_persistent_res("un_7dl_bad")
        sdl_cheat_persistent_res("mt_7dl_sept")
        sdl_cheat_persistent_res("mt_7dl_true")
        sdl_cheat_persistent_res("mt_7dl_good")
        sdl_cheat_persistent_res("mt_7dl_neu")
        sdl_cheat_persistent_res("mt_7dl_bad")
        sdl_cheat_persistent_res("us_7dl_true")
        sdl_cheat_persistent_res("us_7dl_good")
        sdl_cheat_persistent_res("us_7dl_tran_un")
        sdl_cheat_persistent_res("us_7dl_tran_mi")
        sdl_cheat_persistent_res("us_7dl_bad")
        sdl_cheat_persistent_res("us_px_sept")
        sdl_cheat_persistent_res("us_px_good")
        sdl_cheat_persistent_res("me_neu_true")
        sdl_cheat_persistent_res("me_neu_loki_neu")
        sdl_cheat_persistent_res("me_neu_dr_neu")
        sdl_cheat_persistent_res("me_neu_bad")
        sdl_cheat_persistent_res("alt_lamp")
        sdl_cheat_persistent_res("alt_deep")
        sdl_cheat_persistent_res("alt_qte")
        sdl_cheat_persistent_res("alt_victim")
        
        sdl_cheat_persistent_inc("alt_cheater")
        
        renpy.play(sfx_konami_off, channel='sound')
    
    # Словарь чит-кодов
    sdl_cheat_code_to_handler = {
        "7dl4people"  : sdl_cheat_all_enable,
        "justnamiki"  : sdl_cheat_mi_enable,
        "justalice"   : sdl_cheat_dv_enable,
        "justslavya"  : sdl_cheat_sl_enable,
        "justlena"    : sdl_cheat_un_enable,
        "justolga"    : sdl_cheat_mt_enable,
        "justulyana"  : sdl_cheat_us_enable,
        "foreveralone": sdl_cheat_me_enable,
        "getmisc"     : sdl_cheat_va_enable,
        "fullreset"   : sdl_cheat_disable
    }

screen sdl_cheat_reader:
    tag cheat_reader
    
    key "0" action Function(sdl_cheat_read_char, '0')
    key "1" action Function(sdl_cheat_read_char, '1')
    key "2" action Function(sdl_cheat_read_char, '2')
    key "3" action Function(sdl_cheat_read_char, '3')
    key "4" action Function(sdl_cheat_read_char, '4')
    key "5" action Function(sdl_cheat_read_char, '5')
    key "6" action Function(sdl_cheat_read_char, '6')
    key "7" action Function(sdl_cheat_read_char, '7')
    key "8" action Function(sdl_cheat_read_char, '8')
    key "9" action Function(sdl_cheat_read_char, '9')
    key "a" action Function(sdl_cheat_read_char, 'a')
    key "b" action Function(sdl_cheat_read_char, 'b')
    key "c" action Function(sdl_cheat_read_char, 'c')
    key "d" action Function(sdl_cheat_read_char, 'd')
    key "e" action Function(sdl_cheat_read_char, 'e')
    key "f" action Function(sdl_cheat_read_char, 'f')
    key "g" action Function(sdl_cheat_read_char, 'g')
    key "h" action Function(sdl_cheat_read_char, 'h')
    key "i" action Function(sdl_cheat_read_char, 'i')
    key "j" action Function(sdl_cheat_read_char, 'j')
    key "k" action Function(sdl_cheat_read_char, 'k')
    key "l" action Function(sdl_cheat_read_char, 'l')
    key "m" action Function(sdl_cheat_read_char, 'm')
    key "n" action Function(sdl_cheat_read_char, 'n')
    key "o" action Function(sdl_cheat_read_char, 'o')
    key "p" action Function(sdl_cheat_read_char, 'p')
    key "q" action Function(sdl_cheat_read_char, 'q')
    key "r" action Function(sdl_cheat_read_char, 'r')
    key "s" action Function(sdl_cheat_read_char, 's')
    key "t" action Function(sdl_cheat_read_char, 't')
    key "u" action Function(sdl_cheat_read_char, 'u')
    key "v" action Function(sdl_cheat_read_char, 'v')
    key "w" action Function(sdl_cheat_read_char, 'w')
    key "z" action Function(sdl_cheat_read_char, 'z')
    key "y" action Function(sdl_cheat_read_char, 'y')
    key "z" action Function(sdl_cheat_read_char, 'z')
    
    add "sdl_cheat_terminal_icon" pos (1750, 910)
