label alt_day0_prologue:
    $ renpy.pause(2)
    $ prolog_time()
    scene black
    play music music_list["drown"] fadein 3
    $ plthr = u"Выбор"
    $ alt_chapter0()
    with fade
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    if persistent.mi_7dl_good_human or persistent.mi_7dl_good_star:
        show acm_m
    if persistent.dv_7dl_good_ussr:
        show acm_a
    if persistent.sl_7dl_loki_good or persistent.sl_7dl_herc_good or persistent.sl_7dl_dr_good2:
        show acm_s
    if persistent.un_7dl_good_ussr:
        show acm_l
    if persistent.mt_7dl_good:
        show acm_o
    if persistent.us_7dl_good:
        show acm_u
    with dissolve2
    pause(3)
    if persistent.alt_binder:
        scene cg d7_trio_7dl with flash
        $ renpy.pause(.4)
        scene black with fade2
        show alt_credits timeskip_come with dissolve2:
            pos (200,540)
    else:
        scene black with fade2
        show alt_credits timeskip0 with dissolve2:
            pos (200,540)
    with dissolve2
    window hide

label alt_day0_charsel:
    $ renpy.block_rollback()
    if persistent.alt_binder:
        call screen alt_day0_charsel_septim
    else:
        call screen alt_day0_charsel

label alt_day0_approve_herc:
    play sound sfx_7dl["mpbt"] fadein 0
    scene intro_herc with dissolve
    pause(1)
    $ renpy.block_rollback()
    menu:
        "Так всё и начиналось":
            jump alt_day0_role_h
        "Но я не уверен точно…":
            with fade2
            jump alt_day0_charsel

label alt_day0_approve_loki:
    play sound sfx_punch_medium
    scene intro_loki with dissolve
    pause(1)
    $ renpy.block_rollback()
    menu:
        "Так всё и начиналось":
            jump alt_day0_role_l
        "Но я не уверен точно…":
            with fade2
            jump alt_day0_charsel

label alt_day0_approve_dr:
    play sound sfx_wind_gust
    scene intro_dr with dissolve
    pause(1)
    $ renpy.block_rollback()
    menu:
        "Так всё и начиналось":
            jump alt_day0_role_d
        "Но я не уверен точно…":
            with fade2
            jump alt_day0_charsel

label alt_day0_approve_herc_septim:
    play sound sfx_7dl["mpbt"] fadein 0
    scene intro_herc_septim with dissolve
    pause(1)
    $ renpy.block_rollback()
    menu:
        "Так всё и начиналось":
            jump alt_day0_role_h
        "Но я не уверен точно…":
            with fade2
            jump alt_day0_charsel

label alt_day0_approve_loki_septim:
    play sound sfx_punch_medium
    scene intro_loki_septim with dissolve
    pause(1)
    $ renpy.block_rollback()
    menu:
        "Так всё и начиналось":
            jump alt_day0_role_l
        "Но я не уверен точно…":
            with fade2
            jump alt_day0_charsel

label alt_day0_approve_dr_septim:
    play sound sfx_wind_gust
    scene intro_dr_septim with dissolve
    pause(1)
    $ renpy.block_rollback()
    menu:
        "Так всё и начиналось":
            jump alt_day0_role_d
        "Но я не уверен точно…":
            with fade2
            jump alt_day0_charsel

label alt_day0_approve_septim:
    play sound sfx_wind_gust
    scene intro_septim with dissolve
    pause(1)
    $ renpy.block_rollback()
    menu:
        "Так всё и начиналось":
            jump alt_day0_role_s
        "Но я не уверен точно…":
            with fade2
            jump alt_day0_charsel

label alt_day0_role_h:
    $ renpy.block_rollback()
    $ herc = True
    $ plthr = u"Герк"
    $ alt_chapter0()
    play sound sfx_7dl["role_herc"]
    $ renpy.pause(4, hard=True)
    with fade2
    $ routetag = 'prologue'
    scene black with fade
    show alt_credits timeskip6 with dissolve2:
        pos (200,540)
    $ renpy.pause(4, hard=True)
    $ prolog_time()
    call alt_day0_start_h
    jump alt_day0_start

label alt_day0_role_l:
    $ renpy.block_rollback()
    $ loki = True
    $ plthr = u"Локи"
    $ alt_chapter0()
    play sound sfx_7dl["role_loki"]
    $ renpy.pause(4, hard=True)
    with dissolve2
    $ routetag = 'prologue'
    scene black with fade
    show alt_credits timeskip6 with dissolve2:
        pos (200,540)
    $ renpy.pause(4, hard=True)
    $ prolog_time()
    call alt_day0_start_l
    jump alt_day0_start

label alt_day0_role_d:
    $ renpy.block_rollback()
    $ dr = True
    $ plthr = u"Дрищ"
    $ alt_chapter0()
    play sound sfx_7dl["role_drisch"]
    $ renpy.pause(4, hard=True)
    with fade2
    $ routetag = 'prologue'
    scene black with fade
    show alt_credits timeskip6 with dissolve2:
        pos (200,540)
    $ renpy.pause(4, hard=True)
    $ prolog_time()
    call alt_day0_start_d
    jump alt_day0_start

label alt_day0_role_s:
    $ renpy.block_rollback()
    $ d3 = True
    $ plthr = u"Септим"
    $ alt_chapter0()
    $ renpy.pause(4, hard=True)
    with fade2
    $ routetag = 'prologue'
    $ prolog_time()
    call alt_day0_d3_prologue
    jump alt_day0_start

label alt_day0_start:
    if alt_day_catapult == 1:
        call alt_day0_epic_fail
        return
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        play music _7DL.music("seven_summer_days") fadein 5
    else:
        play music _7DL.music("intro2") fadein 5
    scene black
    $ renpy.pause(3, hard=True)
    scene op_back
    with dissolve2
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        show expression Notch("op_mi")
    else:
        show op_mi
    with dissolve2
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        show expression Notch("op_dv") zorder 2
    else:
        show op_dv zorder 2
    with dissolve2
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        show expression Notch("sl_bus")
    else:
        show sl_bus
    with dissolve2
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        show expression Notch("op_un")
    else:
        show op_un
    with dissolve2
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        show expression Notch("mt_bus")
    else:
        show mt_bus
    with dissolve2
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        show expression Notch("op_us")
    else:
        show op_us
    show uv_bus zorder 1
    with dissolve2
    $ renpy.pause(2, hard=True)
    if persistent.alt_binder:
        show expression Desat1("logo_day"):
            pos (400,150)
    else:
        show logo_day:
            pos (400,150)
    with dissolve2
    show acm_logo with zoomin:
        pos (1200,350)
    with vpunch
    $ renpy.pause(2, hard=True)
    scene black
    with dissolve2
    stop music fadeout 5
    $ renpy.pause(5, hard=True)
    pause(1)
    if d3:
        jump alt_day1_me_d3_start
    else:
        jump alt_day1_start