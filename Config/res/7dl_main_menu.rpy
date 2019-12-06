init 1 python:
    presentscript_font = default_7dl_path + "Pics/fonts/presentscript.ttf"
    control_freak_upset_font = default_7dl_path + "Pics/fonts/ContFU.ttf"
    
    style.alt_settings_textbutton = Style(style.base_font)
    style.alt_settings_textbutton.font  = presentscript_font
    style.alt_settings_textbutton.size = 37
    style.alt_settings_textbutton.kerning = -2
    style.alt_settings_textbutton.color = "#2f059a"
    style.alt_settings_textbutton.hover_color = "#9a0505"
    style.alt_settings_textbutton.selected_color = "#2f059a"
    style.alt_settings_textbutton.selected_idle_color = "#2f059a"
    style.alt_settings_textbutton.selected_hover_color = "#9a0505"
    style.alt_settings_textbutton.insensitive_color = "#2f059a"

    style.alt_settings_text = Style(style.base_font)
    style.alt_settings_text.font  = presentscript_font
    style.alt_settings_text.size = 37
    style.alt_settings_text.kerning = -2
    style.alt_settings_text.color = "#2f059a"
    
    style.alt_version_text = Style(style.base_font)
    style.alt_version_text.font  = control_freak_upset_font
    style.alt_version_text.size = 20
    
    #def check_time_7dl(time_7dl):
        #from time import localtime, strftime
        #t = strftime("%H:%M:%S", localtime())
        #hour, min, sec = t.split(":")
        #hour = int(hour)
        #if hour in (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18):
            #time_7dl = "day"
            #return time_7dl
        #elif hour in (19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5):
            #time_7dl = "night"
            #return time_7dl
            
    if not persistent.not_first_start3_7dl:
        persistent.not_first_start3_7dl = True
        if persistent.filters:
            for i in persistent.filters:
                if (i['id'] == "widget__7dl_widget") or (i['id'] == "music_widget_7dl"):
                    persistent.filters.remove(i)

init 1:
    $ list_waifu_7dl = []
    $ persistent.waifu_7dl = 0
    $ dlc_is_here = False # по умолчанию кошочка не в директории БЛ
    #$ time_7dl = ""
    image bg un_bg_7dl = get_image_7dl("gui/menu_main/un_bg.png")
    image bg sl_bg_7dl = get_image_7dl("gui/menu_main/sl_bg.png")
    image bg dv_bg_7dl = get_image_7dl("gui/menu_main/dv_bg.png")
    image bg mi_bg_7dl = get_image_7dl("gui/menu_main/mi_bg.png")
    image bg us_bg_7dl = get_image_7dl("gui/menu_main/us_bg.png")
    image bg mt_bg_7dl = get_image_7dl("gui/menu_main/mt_bg.png")
    image bg uv_bg_7dl = get_image_7dl("gui/menu_main/uv_bg.png")

init 3:
    if not dlc_is_here:
        $ persistent.uv_dlc_on_7dl = False

transform left_menu_7dl(xal, yal):
    xalign -0.1
    alpha 0.0
    easein 1 xalign xal alpha 1.0

screen alt_wip:
    modal True
    add get_image("gui/o_rly/base.png")
    text "РАЗДЕЛ НАХОДИТСЯ В РАЗРАБОТКЕ":
        text_align 0.5
        yalign 0.46
        xalign 0.5
        color "#64483c"
        font header_font
        size 40
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.6
        xalign 0.5
        action Hide("alt_wip")

screen settings_widget_lp_on_7dl():
    text "Включить виджет для" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "отображения прогресса и" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "информации по моду (в" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "т.ч. очков отношений)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_widget_lp_off_7dl():
    text "Выключить виджет для" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "отображения прогресса и" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "информации по моду (в" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "т.ч. очков отношений)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_widget_music_on_7dl():
    text "Включить виджет для" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "отображения музыки, иг-" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "рающей в данный момент." xpos 0.653 ypos 0.692:
        style "alt_settings_text"

screen settings_widget_music_off_7dl():
    text "Выключить виджет для" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "отображения музыки, иг-" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "рающей в данный момент." xpos 0.653 ypos 0.692:
        style "alt_settings_text"

screen settings_dlc_on_7dl():
    text "Включить возможность" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "выхода на Кошкорут, пи-" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "шущийся командой добро-" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "вольцев (рут недописан)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_dlc_off_7dl():
    text "Выключить возможность" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "выхода на Кошкорут, пи-" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "шущийся командой добро-" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "вольцев (рут недописан)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_hentai_un_new_7dl():
    text "Переключить на новую" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "версию 18+ сцен в руте" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "Лены-7дл (изменяется" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "только текст)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_hentai_un_old_7dl():
    text "Переключить на старую" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "версию 18+ сцен в руте" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "Лены-7дл (изменяется" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "только текст)." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_hentai_graphics_on_7dl():
    text "Включить 18+ арты и" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "убрать цензуру со спрай-" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "тов. Доступно не для" xpos 0.653 ypos 0.692:
        style "alt_settings_text"
    text "всех сцен." xpos 0.653 ypos 0.738:
        style "alt_settings_text"

screen settings_hentai_graphics_off_7dl():
    text "Выключить 18+ арты и" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "добавить цензуру на" xpos 0.653 ypos 0.646:
        style "alt_settings_text"
    text "спрайты." xpos 0.653 ypos 0.692:
        style "alt_settings_text"

screen settings_chapter_on_7dl():
    text "Включить заставки в" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "начале глав." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_chapter_off_7dl():
    text "Выключить заставки в" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "начале глав." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_achv_sprite_emo_on_7dl():
    text "Включить смену эмоций" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "персонажей в ачивлисте." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen settings_achv_sprite_emo_off_7dl():
    text "Выключить смену эмоций" xpos 0.653 ypos 0.6:
        style "alt_settings_text"
    text "персонажей в ачивлисте." xpos 0.653 ypos 0.646:
        style "alt_settings_text"

screen menu_7dl():
    imagemap at left_menu_7dl(0.1, 0.7):
        if persistent.waifu_7dl == 1:
            auto get_image_7dl("gui/menu_main/un_menu_%s.png")
        elif persistent.waifu_7dl == 2:
            auto get_image_7dl("gui/menu_main/sl_menu_%s.png")
        elif persistent.waifu_7dl == 3:
            auto get_image_7dl("gui/menu_main/dv_menu_%s.png")
        elif persistent.waifu_7dl == 4:
            auto get_image_7dl("gui/menu_main/mi_menu_%s.png")
        elif persistent.waifu_7dl == 5:
            auto get_image_7dl("gui/menu_main/us_menu_%s.png")
        elif persistent.waifu_7dl == 6:
            auto get_image_7dl("gui/menu_main/mt_menu_%s.png")
        elif persistent.waifu_7dl == 7:
            auto get_image_7dl("gui/menu_main/uv_menu_%s.png")
        hotspot (170, 511, 299, 33):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("start_7dl")]
        hotspot (170, 558, 243, 39):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Show("settings_7dl", transition=Dissolve(0.2))]
        hotspot (170, 617, 293, 38):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("sdl_achvlist_main")]
        hotspot (170, 670, 221, 33):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Show("contacts_7dl", transition=Dissolve(0.2))]
        hotspot (170, 723, 143, 33):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Show("media_7dl", transition=Dissolve(0.2))]
        hotspot (170, 770, 137, 39):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Function(alt_exit), MainMenu(confirm=False)]   
    
    # Открываем экран для ввода чит-кодов
    key "~" action Show("sdl_cheat_reader")
    
    # Указываем номер версии
    if persistent.waifu_7dl == 1:
        text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#D456FF", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 2:
        text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#AA8700", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 3:
        text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#FF7F00", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 4:
        text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#1A9183", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 5:
        text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#FF0000", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 6:
        text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#00EA00", absolute(0), absolute(0)) ]
    elif persistent.waifu_7dl == 7:
        text "v.[alt_release_no].[alt_hotfix_no]"    style "alt_version_text" xcenter 1810 ycenter 1055 color "#FFFFFF" outlines [ (absolute(1), "#00EA00", absolute(0), absolute(0)) ]

screen settings_7dl():
    tag menu
    add get_image_7dl("gui/menu_elem/settings/settings_bg.png")
    if not persistent.lp_widget_7dl:
        textbutton "Виджет (ЛП): выкл." xpos 0.65 ypos 0.255:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_lp_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'lp_widget_7dl', True), Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2)), Show("settings_widget_lp_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Виджет (ЛП): вкл." xpos 0.65 ypos 0.255:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_lp_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'lp_widget_7dl', False), Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2)), Show("settings_widget_lp_on_7dl", transition=Dissolve(0.2))]
    if not persistent.music_widget_7dl:
        textbutton "Виджет (музыка): выкл." xpos 0.65 ypos 0.3:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_music_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'music_widget_7dl', True), Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2)), Show("settings_widget_music_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Виджет (музыка): вкл." xpos 0.65 ypos 0.3:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_music_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'music_widget_7dl', False), Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2)), Show("settings_widget_music_on_7dl", transition=Dissolve(0.2))]
    if not persistent.hentai_un_old_7dl:
        textbutton "Х-сцены с Леной: новые" xpos 0.65 ypos 0.347:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_un_old_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_un_old_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_un_old_7dl',True), Hide("settings_hentai_un_old_7dl", transition=Dissolve(0.2)), Show("settings_hentai_un_new_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Х-сцены с Леной: старые" xpos 0.65 ypos 0.347:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_un_new_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_un_new_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_un_old_7dl',False), Hide("settings_hentai_un_new_7dl", transition=Dissolve(0.2)), Show("settings_hentai_un_old_7dl", transition=Dissolve(0.2))]
    if not persistent.hentai_graphics_7dl:
        textbutton "Х-графика: выкл." xpos 0.65 ypos 0.392:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_graphics_7dl',True), Hide("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2)), Show("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Х-графика: вкл." xpos 0.65 ypos 0.392:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'hentai_graphics_7dl',False), Hide("settings_hentai_graphics_off_7dl", transition=Dissolve(0.2)), Show("settings_hentai_graphics_on_7dl", transition=Dissolve(0.2))]
    if not persistent.chapter_off_7dl:
        textbutton "Заставки: вкл." xpos 0.65 ypos 0.438:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_chapter_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_chapter_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'chapter_off_7dl',True), Hide("settings_chapter_off_7dl", transition=Dissolve(0.2)), Show("settings_chapter_on_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Заставки: выкл." xpos 0.65 ypos 0.438:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_chapter_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_chapter_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'chapter_off_7dl',False), Hide("settings_chapter_on_7dl", transition=Dissolve(0.2)), Show("settings_chapter_off_7dl", transition=Dissolve(0.2))]
    if not persistent.achv_sprite_emo_7dl:
        textbutton "Эмоции (ачивлист): выкл." xpos 0.65 ypos 0.483:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'achv_sprite_emo_7dl',True), Hide("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2)), Show("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2))]
    else:
        textbutton "Эмоции (ачивлист): вкл." xpos 0.65 ypos 0.483:
            style "log_button"
            text_style "alt_settings_textbutton"
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2))]
            action [SetField(persistent,'achv_sprite_emo_7dl',False), Hide("settings_achv_sprite_emo_off_7dl", transition=Dissolve(0.2)), Show("settings_achv_sprite_emo_on_7dl", transition=Dissolve(0.2))]
    if dlc_is_here:
        if not persistent.uv_dlc_on_7dl:
            textbutton "Кошкорут: выкл." xpos 0.65 ypos 0.528:
                style "log_button"
                text_style "alt_settings_textbutton"
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                hovered Show("settings_dlc_on_7dl", transition=Dissolve(0.2))
                unhovered [Hide("settings_dlc_on_7dl", transition=Dissolve(0.2))]
                action [SetField(persistent,'uv_dlc_on_7dl',True), Hide("settings_dlc_on_7dl", transition=Dissolve(0.2)), Show("settings_dlc_off_7dl", transition=Dissolve(0.2))]
        else:
            textbutton "Кошкорут: вкл." xpos 0.65 ypos 0.528:
                style "log_button"
                text_style "alt_settings_textbutton"
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                hovered Show("settings_dlc_off_7dl", transition=Dissolve(0.2))
                unhovered [Hide("settings_dlc_off_7dl", transition=Dissolve(0.2))]
                action [SetField(persistent,'uv_dlc_on_7dl',False), Hide("settings_dlc_off_7dl", transition=Dissolve(0.2)), Show("settings_dlc_on_7dl", transition=Dissolve(0.2))]

screen contacts_7dl():
    tag menu
    imagemap xalign 0.9 yalign 0.7:
        auto get_image_7dl("gui/menu_elem/contacts/contacts_%s.png")
        hotspot(1265, 330, 329, 59):
            action OpenURL("http://7dneyleta.ru") 
        hotspot(1265, 389, 329, 59):
            action OpenURL("https://vk.com/bl_7dl") 
        hotspot(1265, 449, 329, 59):
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=441054187") 
        hotspot(1265, 508, 329, 59):
            action OpenURL("https://vk.com/page-128046483_52530462") 

screen media_7dl():
    tag menu
    imagemap:
        auto get_image_7dl("gui/menu_elem/media/media_%s.png")
        hotspot(1333, 224, 540, 160):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            clicked [Show("alt_wip", transition=Dissolve(0.2))]
        hotspot(1218, 394, 700, 700):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            clicked [Hide("media_7dl", transition=Dissolve(0.2)), Hide("menu_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("alt_gallery_start")]

label main_menu_7dl:
    stop music
    stop ambience
    stop sound
    stop sound_loop
    window hide
    
    $ plthr = u"Меню"
    call alt_vars
    $ renpy.block_rollback()
    $ day_time()
    jump random_bg_7dl

label random_bg_7dl:
    if ((len(list_waifu_7dl) == 6) and ('uv' not in list_waifu_7dl)) or (len(list_waifu_7dl) == 7):
        $ list_waifu_7dl = []
    if persistent.waifu_7dl == 0:
        if renpy.random.randint(1, 65) == 1:
            $ persistent.waifu_7dl = 7
        else:
            $ persistent.waifu_7dl = renpy.random.choice([1, 2, 3, 4, 5, 6])
    elif persistent.waifu_7dl == 1:
        $ persistent.waifu_7dl = renpy.random.choice([2, 3, 4, 5, 6])
    elif persistent.waifu_7dl == 2:
        $ persistent.waifu_7dl = renpy.random.choice([1, 3, 4, 5, 6])
    elif persistent.waifu_7dl == 3:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 4, 5, 6])
    elif persistent.waifu_7dl == 4:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 3, 5, 6])
    elif persistent.waifu_7dl == 5:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 3, 4, 6])
    elif persistent.waifu_7dl == 6:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 3, 4, 5])
    elif persistent.waifu_7dl == 7:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 3, 4, 5, 6])
    if persistent.waifu_7dl == 1 and 'un' not in list_waifu_7dl:
        play music _7DL.music("take_my_hand") fadein 3
        $ list_waifu_7dl.append('un')
        scene bg un_bg_7dl with fade
        call screen menu_7dl
    elif persistent.waifu_7dl == 2 and 'sl' not in list_waifu_7dl:
        $ list_waifu_7dl.append('sl')
        scene bg sl_bg_7dl with fade
        play music _7DL.music("slavyas_fantazm") fadein 3
        call screen menu_7dl
    elif persistent.waifu_7dl == 3 and 'dv' not in list_waifu_7dl:
        $ list_waifu_7dl.append('dv')
        scene bg dv_bg_7dl with fade
        play music _7DL.music("sheiscool") fadein 3
        call screen menu_7dl
    elif persistent.waifu_7dl == 4 and 'mi' not in list_waifu_7dl:
        $ list_waifu_7dl.append('mi')
        scene bg mi_bg_7dl with fade
        play music _7DL.music("tellyourworld") fadein 3
        call screen menu_7dl
    elif persistent.waifu_7dl == 5 and 'us' not in list_waifu_7dl:
        $ list_waifu_7dl.append('us')
        scene bg us_bg_7dl with fade
        play music _7DL.music("thousand_of_pixies") fadein 3
        call screen menu_7dl
    elif persistent.waifu_7dl == 6 and 'mt' not in list_waifu_7dl:
        $ list_waifu_7dl.append('mt')
        scene bg mt_bg_7dl with fade
        play music _7DL.music("wheres_wonderland") fadein 3
        call screen menu_7dl
    elif persistent.waifu_7dl == 7 and 'uv' not in list_waifu_7dl:
        $ list_waifu_7dl.append('uv')
        scene bg uv_bg_7dl with fade
        play music _7DL.music("uvao2") fadein 3
        call screen menu_7dl
    else:
        jump random_bg_7dl

label start_7dl:
# переименовываем персонажей
    $ make_names_unknown_7dl()
    $ th_prefix = "«"
    $ th_suffix = "»"
# вызываем переменные
    call alt_vars
# вызываем сценарий
    call alt_day0_prologue
    jump main_menu_7dl
