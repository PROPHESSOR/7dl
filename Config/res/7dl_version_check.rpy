init:
    # Номер релиза сохранения, пустой по инициализации, в начале игры - присваивается номер релиза мода,
    # при загрузке:
    #  - если было сохранение с присвоением номера, при загрузке переменная будет взята из сохранения;
    #  - если загружается "старое" сохранение (до ввода процедуры контроля загрузок) - останется None 
    $ alt_save_release_no = None 

    $ alt_aicr_string = " "

screen alt_incompatible_release:
    tag menu
    modal True
    python: # почти цельностянуто из "menu:" в игре, цвета меняются со временем дня игры

        aicr_colors_hover = {'day': '#9dcd55', 'night': '#3ccfa2', 'sunset': '#dcd168', 'prologue': '#98d8da'}
        aicr_colors = {'day': '#466123', 'night': '#145644', 'sunset': '#69652f', 'prologue': '#496463'}
         
    window:
        text alt_aicr_string align (0.5, 0.05) color "#FF2500" font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"РАБОТОСПОСОБНОСТЬ НЕ ГАРАНТИРУЕТСЯ. ВЫЛЕТ ИГРЫ ВОЗМОЖЕН В ЛЮБОЙ МОМЕНТ" align(0.5, 0.25) color "#FF2500" font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"РЕКОМЕНДУЕТСЯ НАЧАТЬ ИГРУ ЗАНОВО"  align(0.5, 0.45) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"Ваши действия:"  align(0.5, 0.55) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 55 bold True text_align 0.5 line_spacing 20

        right_padding 75
        bottom_padding 50
        yalign 0.5
        top_padding 50
        xfill True
        background (Frame(get_image((('gui/choice/' + persistent.timeofday) + '/choice_box.png')), 50, 50))
        left_padding 75
# кнопки выборов
        button: # начинаем заново
            xalign 0.5
            yalign 0.65
            action Jump("start_7dl")
            background None
            text u"Начать игру заново":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
        button: # выходим в меню загрузки, ищем что-то другое
            xalign 0.5
            yalign 0.75
            action ShowMenu('load')
            background None
            text u"Загрузить другое сохранение":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
# Для особо упёртых\упорных\…. Пробуем продолжить, авось получится.
# Продолжение игры номер сохранения не перепишет; так что окно проверки будет вываливаться каждый раз
        button:  
            xalign 0.5
            yalign 0.85
            action Jump("alt_continue_game")
            background None
            text u"Загрузить это сохранение. На свой страх и риск, о возможных последствиях предупрежден.":
                hover_size 40
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 40

# После загрузки файла переходим именно в это место. Определено механикой Ренпая - 
# если есть метка 'after_load' - переходить на нее. В классике и других модах такая метка не обнаружена
# Не путать со служебной меткой '_after_load'

label after_load:

    # читаем 'save_name' и ищем в строке "7ДЛ" - думаю, этого для идентификации мода достаточно
    if save_name.find(u'7ДЛ') != -1: #Если нашли вхождение '7ДЛ' в имени сохранения игры

        # загружаем имена персонажей
        $ save_names_known()
        
        # если до этого не было кастомных менюшек
        if not persistent.alt_interface:
            $ alt_interface_on()
        
        # если Нуар - включаем интерфейс; если Нуар был, но больше не нужен - отключаем
        if noir_interface:
            $ noir_interface_on()
        elif persistent.noir_interface:
            $ noir_interface_off()
        
        # Проверяем, совпадают ли версии сохранения и мода и есть ли версия сохранения в списке совместимых
        if (alt_save_release_no not in alt_compatible_release_no): # и если сохранение несовместимо
            python: # генерируем строку с номерами версий
                alt_aicr_string = (u"ЗАГРУЖАЕМАЯ ВЕРСИЯ СОХРАНЕНИЯ (%s) НЕСОВМЕСТИМА С ЭТОЙ ВЕРСИЕЙ МОДА (%s)") % (alt_save_release_no, alt_release_no)
            call screen alt_incompatible_release # и показываем экран предупреждения с выбором вариантов
        elif (alt_save_release_no in ["0.34.a", "0.34.b", "0.35.a", "0.36.a", "0.37.a", "0.38.a", "0.39.a", "0.40", "0.40.1"]):
            # Спасаем сейвы Дрища
            if not (loki or herc or d3):
                $ dr = True
            # Спасаем данные в списках
            if (len(list_joined_clubs_7dl) == 0) and (len(list_clubs_7dl) > 0):
                $ list_joined_clubs_7dl = list_clubs_7dl
            if not alt_day2_convoy:
                python:
                    try:
                        alt_day2_convoy = list_d2_convoy_7dl[0]
                    except IndexError:
                        pass
            if not alt_day2_date:
                python:
                    try:
                        alt_day2_date = list_d2_date_7dl[0]
                    except IndexError:
                        pass
            # Новая переменная
            if (alt_day2_convoy == 'un_rej'):
                $ alt_day2_un_rej_convoy = True
        else:
            pass # версии совпали, играем дальше
    else:
        # если до этого был запущен 7дл (и кастомные менюшки в т.ч.)
        if persistent.alt_interface:
            $ alt_interface_off()
            # сбрасываем имена персонажей на дефолтные
            $ reset_names_to_default()
            $ reload_names()
        
        # если был запущен Нуар, а сейв не с 7дл - выключаем интерфейс
        if persistent.noir_interface:
            $ noir_interface_off()

label alt_continue_game:
    return # .. и если все нормально - возвращаемся в игру