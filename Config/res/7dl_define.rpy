screen intro_loki:
    add "intro_loki" xalign 0.0 yalign 0.0

screen intro_herc:
    add "intro_herc" xalign 0.0 yalign 0.0

screen intro_dr:
    add "intro_dr" xalign 0.0 yalign 0.0

screen intro_loki_septim:
    add "intro_loki_septim" xalign 0.0 yalign 0.0

screen intro_herc_septim:
    add "intro_herc_septim" xalign 0.0 yalign 0.0

screen intro_dr_septim:
    add "intro_dr_septim" xalign 0.0 yalign 0.0

screen intro_septim:
    add "intro_septim" xalign 0.0 yalign 0.0

screen alt_day0_charsel:
    tag menu
    modal False
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 635, 1080)):
            hovered [Show("intro_loki", transition=Dissolve(0.5))]
            unhovered [Hide("intro_loki", transition=Dissolve(1.0))]
            action [Hide("intro_loki", transition=Dissolve(0.5)), Jump("alt_day0_approve_loki")]
        hotspot ((635, 0, 652, 1080)):
            hovered [Show("intro_herc", transition=Dissolve(0.5))]
            unhovered [Hide("intro_herc", transition=Dissolve(1.0))]
            action [Hide("intro_herc", transition=Dissolve(0.5)), Jump("alt_day0_approve_herc")]
        hotspot ((1287, 0, 634, 1080)):
            hovered [Show("intro_dr", transition=Dissolve(0.5))]
            unhovered [Hide("intro_dr", transition=Dissolve(1.0))]
            action [Hide("intro_dr", transition=Dissolve(0.5)), Jump("alt_day0_approve_dr")]

screen alt_day0_charsel_septim:
    tag menu
    modal False
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 498, 1080)):
            hovered [Show("intro_loki_septim", transition=Dissolve(0.5))]
            unhovered [Hide("intro_loki_septim", transition=Dissolve(1.0))]
            action [Hide("intro_loki_septim", transition=Dissolve(0.5)), Jump("alt_day0_approve_loki_septim")]
        hotspot ((498, 0, 498, 1080)):
            hovered [Show("intro_herc_septim", transition=Dissolve(0.5))]
            unhovered [Hide("intro_herc_septim", transition=Dissolve(1.0))]
            action [Hide("intro_herc_septim", transition=Dissolve(0.5)), Jump("alt_day0_approve_herc_septim")]
        hotspot ((996, 0, 464, 1080)):
            hovered [Show("intro_dr_septim", transition=Dissolve(0.5))]
            unhovered [Hide("intro_dr_septim", transition=Dissolve(1.0))]
            action [Hide("intro_dr_septim", transition=Dissolve(0.5)), Jump("alt_day0_approve_dr_septim")]
        hotspot ((1458, 0, 462, 1080)):
            hovered [Show("intro_septim", transition=Dissolve(0.5))]
            unhovered [Hide("intro_septim", transition=Dissolve(1.0))]
            action [Hide("intro_septim", transition=Dissolve(0.5)), Jump("alt_day0_approve_septim")]

screen alt_timer:
    add "timer_anim" xalign 0.5 yalign 0.5
    key "7" action [Hide("alt_timer"), Jump("alt_day3_dv_stayhere")]
    text "ВЕРНУТЬСЯ В ЛАГЕРЬ! (--->7<---)" align (0.5, 0.8) color "#FF0000"
    timer 2.0 action Jump("alt_day3_leave")

init:
    transform fleft:
        xalign 0.16
        xanchor 0.5

    transform left:
        xalign 0.28
        xanchor 0.5

    transform cleft:
        xalign 0.355
        xanchor 0.5

    transform center:
        xalign 0.5

    transform cright:
        xalign 0.645
        xanchor 0.5

    transform right:
        xalign 0.72
        xanchor 0.5

    transform fright:
        xalign 0.84
        xanchor 0.5

    transform voy_left:
        xalign 0.0
        xanchor 0.5

    transform voy_right:
        xalign 1.0
        xanchor 0.5
        
    transform zenterright:
        xalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.7
        
    transform enterright:
        xalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.9
        
    transform zenterleft:
        xalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.3
        
    transform enterleft: #по левую
        xalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.1
        
    transform zentercenter: #для открывающихся дверей
        xalign 0.5 zoom 1.0
        linear 0.8 zoom 1.05 xalign 0.5
        
    transform zentercenter2: #для открывающихся дверей
        xalign 0.5 zoom 1.0 subpixel True
        linear 20.0 zoom 1.5 xalign 0.5
        
    transform zexitcenter: #отдаляющий эффект от центра
        xalign 0.5 zoom 1.05 subpixel True
        linear 0.8 zoom 1.0 xalign 0.5
        
    transform zexitcenter2: #отдаляющий эффект от центра
        xalign 0.5 zoom 1.5
        linear 20 zoom 1.0 xalign 0.5
        
    transform zexitright: #отдалаюящий эффект от левого края к центру
        xalign 0.7 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5
        
    transform zexitleft: #отдаляющий эффект от правого края к центру 
        xalign 0.3 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5
        
    transform bottotop:
        pos (0,-1261)
        linear 10.0 pos (0,0)
        linear 2.0 pos (0, -200)
    
    transform salute_main_black(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            "sal_splash" with dspq
            0.2
            salute with dspr
            "sal_black" with dsps
            6.0
        repeat
        
    transform salute_main(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            "sal_splash" with dspq
            0.2
            choice:
                salute with dspr
                "sal_black" with dsps
                6.0
            choice:
                salute with dspr
                "sal_black" with dissolve
                6.0
        repeat
        
    transform running:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset 25 yoffset 50
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset -25 yoffset 50
        repeat

    transform fast_running:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat

    transform fast_running2:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.1 xoffset 0 yoffset 0
            ease 0.1 xoffset 12 yoffset 25
            ease 0.1 xoffset 0 yoffset 0
            ease 0.1 xoffset -12 yoffset 25
        repeat

# Наши транзиты, с блекджеком и разными цветами.
    $ flash_cyan = Fade(1, 0, 1, color="#1fa")
    $ fade_red = Fade(2, 2, 2, color="#f11")
    $ flash2_red = Fade(0.5, 0, 0.5, color="#f11")
    $ flash_pink = Fade(1, 0, 1, color="#e25")
    # Кристал
    $ diam = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern.jpg")), 1.1, 1)
    $ fdiam = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern.jpg")), 0.4, 1)
    $ fulldiam = MultipleTransition([False,fdiam,get_image_7dl("screens/digi1.jpg"),fdiam,True])
    # Поворотный переключатель
    $ gopr = ImageDissolve(im.Tile(get_image_7dl("gui/transit/blackout_go.png")), 0.95, 1)
    $ clock_l = ImageDissolve(im.Tile(get_image_7dl("gui/transit/clock_l.jpg")), 0.95, 1)
    $ joff_l = MultipleTransition([False, clock_l, Solid("#000"), clock_l, True])
    $ clock_r = ImageDissolve(get_image_7dl("gui/transit/clock_r.png"), 2.5, 50, reverse=False)
    $ joff_r = MultipleTransition([False, clock_r, Solid("#000"), clock_r, True])
    # Жалюзи а ля KS
    $ blind_d = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks.jpg")), 1.3)
    $ blinds_l = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks2.jpg")), 0.6)
    $ blinds_r = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks3.jpg")), 0.7)
    $ blinds_ud = ImageDissolve(get_image_7dl("gui/transit/blackout_ud.png"), 0.3)
    $ blind_l = MultipleTransition([False,blinds_l,Solid("#011"),blinds_r,True])
    $ blind_r = MultipleTransition([False,blinds_r,Solid("#011"),blinds_l,True])
    # Разное
    $ touch = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern2.jpg")), 0.9, 1)
    $ dspq = Dissolve(0.04, alpha=True)
    $ dsps = Dissolve(3.0, alpha=True)
    $ guess_on = ImageDissolve(get_image_7dl("screens/blackpalm.png"), 0.25, ramplen=256, reverse=True)
    $ guess_off = ImageDissolve(get_image_7dl("screens/blackpalm.png"), 0.3, ramplen=256)

# Анимы
    image anim_digi:
        get_image_7dl("screens/digi1.jpg")  with Dissolve(1.5) 
        pause 1.5
        get_image_7dl("screens/digi2.jpg")  with Dissolve(1.5) 
        pause 1.5
        repeat
    
    image anim_grain: #Смэртельный номер: тянем картинку, делаем прозрачной и запускаем в секвенцию - и всё в коде!
        filmetile(get_image_7dl("screens/alt_noise1.png"))
        pause 0.1
        filmetile(get_image_7dl("screens/alt_noise2.png"))
        pause 0.1
        filmetile(get_image_7dl("screens/alt_noise3.png"))
        pause 0.1
        repeat
    
    image anim_noir: # белый шум с заставкой
        get_image_7dl("bg/ext_noir1_7dl.png")
        pause 0.14
        get_image_7dl("bg/ext_noir2_7dl.png")
        pause 0.14
        get_image_7dl("bg/ext_noir3_7dl.png")
        pause 0.14
        repeat
    
    image anim_intro_recall:
        get_image("bg/semen_room.jpg")
        pause 0.1
        get_image("bg/semen_room_window.jpg")
        pause 0.1
        get_image("anim/intro_1.jpg")
        pause 0.1
        get_image("anim/intro_2.jpg")
        pause 0.1
        get_image("anim/intro_3.jpg")
        pause 0.1
        get_image("anim/intro_4.jpg")
        pause 0.1
        get_image("anim/intro_5.jpg")
        pause 0.1
        get_image("anim/intro_6.jpg")
        pause 0.1
        get_image("anim/intro_8.jpg")
        pause 0.1
        get_image("anim/prolog_2.jpg")
        pause 0.1
        get_image("anim/prolog_1.jpg")
        pause 0.1
        get_image("anim/intro_9.jpg")
        pause 0.1
        get_image("anim/intro_10.jpg")
        pause 0.1
        get_image("anim/intro_11.jpg")
        pause 0.1
        get_image("anim/intro_13.jpg")
        pause 0.1
        get_image("bg/intro_xx.jpg")
        pause 0.1
        repeat
    
    image anim_square_party:
        get_image("bg/ext_square_night_party.jpg") with Dissolve(.5) 
        pause 0.6
        get_image("bg/ext_square_night_party2.jpg") with Dissolve(.5) 
        pause 0.6
        repeat
    
    image anim_square_preparty:
        get_image_7dl("bg/ext_square_sunset3_7dl.jpg") with Dissolve(1.5) 
        pause 1.6
        get_image_7dl("bg/ext_square_sunset2_7dl.jpg") with Dissolve(1.5) 
        pause 1.4
        repeat
    
    image uv_bus:
        get_sprite_7dl("custom/uv_alt1_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt2_7dl.png") 
        pause 0.5
        get_sprite_7dl("custom/uv_alt3_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt2_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt1_7dl.png")
        pause 0.5
    
    image anim_underwater:
        get_image_7dl("bg/ext_underwater_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater2_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater3_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater2_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        repeat
    
    image salute = LiveComposite((1920,1080),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh1.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh11.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh2.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh21.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh3.png")),

                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh4.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh41.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh5.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh51.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh6.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh61.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh7.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh71.png")),

                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh91.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh9.png")))

    
    image timer_anim: 
        get_sprite_7dl("custom/win_7dl.png") 
        0.1 # Задержка
        get_sprite_7dl("custom/win2_7dl.png")
        0.1
        get_sprite_7dl("custom/win3_7dl.png")
        0.1
        repeat # Не убирать
        
    image ftl_anim: 
        get_image_7dl("screens/ftl1.png") 
        0.1 # Задержка
        get_image_7dl("screens/ftl2.png")
        0.1
        get_image_7dl("screens/ftl3.png")
        0.1
        repeat # Не убирать
        
    image un serious dress anim: 
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png") 
        8.0 # Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.1
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png") 
        4.0 # Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.15
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png") 
        7.0 # Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.1
        repeat # Не убирать
        
    image scenery:
        get_image("anim/prolog_2.jpg") with Dissolve(.5) 
        pause 2.6
        get_image("anim/prolog_1.jpg") with Dissolve(.5) 
        pause 0.6
        repeat
        
    image scenery2:
        get_image("anim/prolog_2.jpg") with Dissolve(.4) 
        pause 2.0
        get_image("anim/prolog_1.jpg") with Dissolve(.4) 
        pause 0.4
        repeat    
        
    image scenery3:
        get_image("anim/prolog_2.jpg") with Dissolve(.25) 
        pause 1.4
        get_image("anim/prolog_1.jpg") with Dissolve(.25) 
        pause 0.25
        repeat

#Заставки
    image bg ext_stand3_night_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.63, 0.78, 0.82))
    image bg ext_stand3_sunset_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.94, 0.82, 1.0))
    image bg ext_stand3_prolog_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand_pr_7dl.png"), im.matrix.tint(0.82, 0.84, 1.0))
    image bg ext_noir_7dl = get_image_7dl("bg/ext_noir_7dl.png")

#Турнир
    image sal_black = Solid("#00000000")
    image sal_splash = Solid("#FFFFFF66")

#Элементы интерфейса
    image blackout = get_image_7dl("gui/transit/blackout.png")
    image blackout2 = get_image_7dl("gui/transit/blackout2.png")
    image blackout_exh = get_image_7dl("gui/transit/blackout_exh.png")
    image blackout_exh2 = get_image_7dl("gui/transit/blackout_exh2.png")
    image blackout_exh3 = get_image_7dl("gui/transit/blackout_exh3.png")
    image genda_portrait = get_image_7dl("sprites/custom/genda_portrait_7dl.png")
    image gfx bokeh = get_image_7dl("screens/splatter.png")
    
    image anim_exhausted:
        get_image_7dl("gui/blackout_exh2.png")
        0.03 # Задержка
        get_image_7dl("gui/blackout_exh3.png")
        0.03 # Задержка
        get_image_7dl("gui/blackout_exh2.png")
        0.03 # Задержка
        get_image_7dl("gui/blackout_exh3.png")
        0.03 # Задержка
        get_image_7dl("gui/blackout_exh2.png")
        0.03 # Задержка
        repeat # Не убирать

# Скачки по карте
    image bg map_explain = get_image_7dl("gui/maps/map_explain.jpg")
    image dvsem_el = get_image_7dl("gui/maps/dvsem_el.png")
    image eye_s = get_image_7dl("sprites/custom/eye_s_7dl.png")
# Сотик
    image frame = get_image_7dl("gui/phone/frame.png")
    image frame_sl = get_image_7dl("gui/phone/frame_sl.png")
    image cam_ui = get_image_7dl("gui/phone/cam_ui.png")
# Пека
    image anim_laptop:
        get_image_7dl("gui/laptop/laptop_prologue.png") 
        0.3
        get_image_7dl("gui/laptop/laptop_prologue_weak.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_mid.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_strong.png")
        0.2
        get_image_7dl("gui/laptop/laptop_prologue_mid.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_weak.png")
        0.3
        repeat

# Камень-ножницы-бумага
    image miku_paper = get_image_7dl("gui/rps/miku_paper.png")
    image miku_rock = get_image_7dl("gui/rps/miku_rock.png")
    image miku_scissor = get_image_7dl("gui/rps/miku_scissor.png")
    image sam_paper = get_image_7dl("gui/rps/sam_paper.png")
    image sam_rock = get_image_7dl("gui/rps/sam_rock.png")
    image sam_scissor = get_image_7dl("gui/rps/sam_scissor.png")

# Ачивки
    image acm_logo_va_victim:
        get_image_7dl("gui/acm/acm_logo_va_victim_1.png")
        0.2
        get_image_7dl("gui/acm/acm_logo_va_victim_2.png")
        0.2
        get_image_7dl("gui/acm/acm_logo_va_victim_3.png")
        0.2
        repeat

# Прочее
    image acm_logo = get_image_7dl("gui/acm/acm_logo1_7dl.png") # Логотип сюжета

    image dreamgirl_overlay = get_image_7dl("screens/dreamgirl_overlay.png")
    image wet1 = get_image_7dl("screens/wet1.png")
    image volley_fight = get_sprite_7dl("custom/volley_fight_7dl.png")
    image rain_overlay = get_image_7dl("screens/rain_overlay.png")

    image alt_KS_censor = get_image_7dl("screens/alt_KS_censor.png")
    image alt_KS_censor2 = get_image_7dl("screens/alt_KS_censor2.png")

# Картинки с использованием прозрачности и прочая спрайтовость
    image dv normal flipped = Transform("dv normal pioneer", xzoom=-1.0)
    image dv normal flipped far = Transform("dv normal pioneer far", xzoom=-1.0)
    image sl normal flipped = Transform("sl normal pioneer", xzoom=-1.0)
    image sl serious flipped = Transform("sl serious pioneer", xzoom=-1.0)
    #image d3_miku_dance_blush flipped = Transform("d3_miku_dance_blush", xzoom=-1.0)
    image uv shade3 sized = Transform("uv shade3", zoom=.4)
    image uv shade4 sized = Transform("uv shade4", zoom=.4)
    image digi_pad = get_sprite_7dl("custom/digi_pad_7dl.png")
    image sl_trench = get_sprite_7dl("custom/sl_trench_7dl.png")
    image sl_trench2 = get_sprite_7dl("custom/sl_trench2_7dl.png")
    image cotocomb_lighter = get_sprite_7dl("custom/cotocomb_lighter_7dl.png")
    image d4_cat_door_frame = get_sprite_7dl("custom/d4_cat_door_frame_7dl.png")
    image d6_miku_cries = get_sprite_7dl("custom/d6_miku_cries_7dl.png")
    image mouth_dull = get_sprite_7dl("custom/mouth_dull_7dl.png")
    image mi_ru = get_sprite_7dl("custom/mi_ru_7dl.png")
    image mt_bus = get_sprite_7dl("custom/mt_bus_7dl.png")
    image sl_bus = get_sprite_7dl("custom/sl_bus_7dl.png")
    image myst_mh = get_sprite_7dl("custom/myst_mh_7dl.png")
    image uvao_d1 = get_sprite_7dl("custom/uvao_d1_7dl.png")
    image dv_mt = get_sprite_7dl("custom/dv_mt_7dl.png")
    image backpack = get_sprite_7dl("custom/backpack_7dl.png")
    image backpack_tiny = get_sprite_7dl("custom/backpack_tiny_7dl.png")
    image dv_us_volley = get_sprite_7dl("custom/dv_us_volley_7dl.png")
    image ldb_blind = get_image_7dl("sprites/custom/ldb_blind.png")
    image PolaroidFrame_7dl = get_sprite_7dl("custom/PolaroidFrame_7dl.png")

# Dnd
    image alt_cat_map_wireframe = get_image_7dl("gui/dnd/alt_cat_map_wireframe.png")
    image alt_cat_map = get_image_7dl("gui/dnd/alt_cat_map.png")
    image alt_cat_map_pathfinding = get_image_7dl("gui/dnd/alt_cat_map_pathfinding.png")

# Звучок
    $ sfx_alisa_falls_novoice = "sound/sfx/alisa_falls_novoice.ogg"

init python:
    def bind_files_7dl():
        ''' Биндит .jpg и .png файлы в renpy.image,
            а .ogg - в xxx_7dl[] словари, соответственно
        '''

        for file in renpy.list_files():
            filename = file.split('/')[-1] # file.extension

            if filename.endswith((".jpg", ".png")):
                image_bind_prefix = ""

                if file.startswith((default_7dl_path + "Pics/bg/")):
                    image_bind_prefix = "bg "
                elif file.startswith((default_7dl_path + "Pics/cg/")):
                    image_bind_prefix = "cg "

                renpy.image((image_bind_prefix + filename[:-4]), file) # [:-4] - remove extension

    bind_files_7dl()