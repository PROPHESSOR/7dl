label alt_day3_start:
    call alt_day3_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ prolog_time()
    $ alt_chapter(3, u"Утро")
    call alt_day3_begin
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(3, u"Завтрак")
    call alt_day3_bf
    pause(1)
    if alt_day3_un_event and not alt_day3_duty:
        $ persistent.sprite_time = "day"
        call alt_day3_event_library1
    elif alt_day3_dv_event and not alt_day3_duty:
        call alt_day3_event_estrade
    elif alt_day3_mi_event and not alt_day3_duty:
        call alt_day3_event_music_club
    elif alt_day3_duty:
        call alt_day3_bf_duty
        pause(1)
        if (alt_day2_date == 'un_fz'):
            call alt_day3_event_camp_entrance
        else:
            call alt_day3_map_prepare
    elif (alt_day2_date == 'un_fz'):
        call alt_day3_event_camp_entrance
    else:
        call alt_day3_map_prepare
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(3, u"Обед")
    call alt_day3_dinner
    pause(1)
    if alt_day3_duty:
        if (alt_day2_date == 'dv') and alt_day3_dv_event:
            pass
        else:
            call alt_day3_dinner_menu
    else:
        call alt_day3_dinner_menu
    pause(1)
    if (alt_day2_date == 'dv') and alt_day3_dv_event and alt_day3_duty:
        call alt_day3_eventAf_music_club1
    elif alt_day3_un_fz_dinner:
        pass
    elif alt_day3_un_invite == 1:
        call alt_day3_eventAf_library1
    else:
        call alt_day3_mapAf_prepare
    pause(1)
    if alt_day3_un_fz_dinner or alt_day3_dv_rep:
        call alt_day3_aftermath
        pause(1)
        call alt_day3_nightmare
        if alt_day_catapult == 1:
            return
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(3, u"Ужин")
        pause(1)
        call alt_day3_supper1
        pause(1)
        if not alt_day3_un_fz_dinner:
            $ sunset_time ()
            $ persistent.sprite_time = "sunset"
            call alt_day3_supper2
    else:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(3, u"Ужин")
        call alt_day3_supper
        pause(1)
        if alt_day3_mi_invite2:
            pass
        else:
            $ sunset_time ()
            $ persistent.sprite_time = "sunset"
            call alt_day3_supper2
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(3, u"Танцы")
    call alt_day3_dance_dance
    pause(1)
    if not alt_day3_dv_dj:
        call alt_day3_makeup
        pause(1)
        if (alt_day2_date == 'un_fz'):
            if alt_day3_un_fz_evening:
                jump alt_day3_disco
            else:
                call alt_day3_dv_lf
                pause(1)
                call alt_day3_rockstar
                pause(1)
                call alt_day3_sleeptime
                pause(1)
                jump alt_day3_slots
        elif alt_day3_dv_date or (alt_day3_dv2_event and (not alt_day3_dv_dj)):
            call alt_day3_dv_lf
            pause(1)
            call alt_day3_rockstar
            pause(1)
            if alt_day3_dv2_event:
                call alt_day3_sleeptime
                pause(1)
                jump alt_day3_slots
            else:
                call alt_day3_dv_reunion
                pause(1)
                scene black
                call screen alt_timer
        else:
            jump alt_day3_disco
    else:
        jump alt_day3_disco

label alt_day3_dv_stayhere:
    call alt_day3_dv_stayhere1
    pause(1)
    $ persistent.sprite_time = "night"
    call alt_day3_bath_voyeur
    pause(1)
    call alt_day3_sleeptime
    pause(1)
    jump alt_day3_slots

label alt_day3_leave:
    call alt_day3_leave1
    pause(1)
    return

label alt_day3_disco:
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day3_choose
    pause(1)
    if ((counter_sl_7dl >= 4) or (counter_sl_cl >= 6)) and (alt_day3_dancing == 2) and (lp_sl >= 12):
        if counter_sl_7dl == 5:
            pause(1)
            call alt_day3_bath_voyeur
            pause(1)
            call alt_day3_sleeptime
            pause(1)
            jump alt_day3_slots
        elif counter_sl_cl == 7:
            call alt_day3_technoquest3
            pause(1)
            jump alt_day3_slots
        else:
            jump alt_day3_disco2
    else:
        call alt_day3_dance_dance2
        pause(1)
        if alt_day3_un_med_help == 1:
            $ alt_chapter(3, u"Медпункт. Вечер.")
            call alt_day3_med_un
            pause(1)
            if persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf:
                call alt_day3_un_cards
                pause(1)
                call alt_day3_un_strip_play
                pause(1)
                if alt_day3_un_strip_pool_sp == 0:
                    call alt_day3_card_lose
                elif alt_day3_un_strip_pool_un == 0:
                    call alt_day3_card_won
                pause(1)
            call alt_day3_post_strip
            pause(1)
            call alt_day3_sleeptime
            pause(1)
            jump alt_day3_slots
        elif alt_day3_us_bugs == 1 and not (alt_day2_date == 'un_fz'):
            call alt_day3_mt_scare
            pause(1)
            call alt_day3_bath_voyeur
            pause(1)
            call alt_day3_sleeptime
            pause(1)
            jump alt_day3_slots
        elif alt_day3_technoquest_st3 == 1:
            if alt_day3_mi_dj or (lp_mi > 7):
                jump alt_day3_disco2
            else:
                call alt_day3_dance_dance2_menu
                pause(1)
                if alt_day3_technoquest_st3_help:
                    if alt_day3_dv_dj or alt_day3_mi_dj:
                        jump alt_day3_disco2
                    else:
                        call alt_day3_technoquest3
                        pause(1)
                        jump alt_day3_slots
                else:
                    if (alt_day2_date == 'un_fz'):
                        call alt_day3_technoquest3
                        pause(1)
                        jump alt_day3_slots
                    else:
                        $ girls_list = ('dv', 'un', 'mi', 'sl')
                        $ lp_max = max( [eval('lp_'+w) for w in girls_list] )
                        $ max_who = [w for w in girls_list if eval('lp_'+w) == lp_max]
                        $ max_who_id = max_who[0] if lp_max > 5 and len(max_who)==1 else 'nobody'
                        call expression 'alt_day3_max_lp_{}'.format(max_who_id)
                        if alt_day3_lp_route == 1 or alt_day3_lp_route == 2:
                            call alt_day3_technoquest3
                            pause(1)
                            jump alt_day3_slots
                        else:
                            jump alt_day3_disco2
        else:
            jump alt_day3_disco2

label alt_day3_disco2:
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day3_choose3
    pause(1)
    if alt_day3_mi_date and (alt_day2_date == 'mi') and ((alt_day3_dancing == 41) or (alt_day3_dancing == 40)):
        call alt_day3_mi_7dl_init
        pause(1)
        jump alt_day4_mi_7dl_start
    elif alt_day3_dancing != 5:
        call alt_day3_disco_past_d2
        pause(1)
        call alt_day3_bath_voyeur
        pause(1)
    call alt_day3_sleeptime
    pause(1)
    jump alt_day3_slots

label alt_day3_slots:
   scene scenery
   with dissolve
   $ alt_spt = 0
   $ alt_hpt = 0

label alt_day3_router_dv:
    if alt_day3_dv_evening:
        "Поворочавшись, я улыбнулся посетившей мои сны Алисе."
        if lp_dv >= 11:
            "Мне снилась Алиса…"
            window hide
            if alt_day3_dv_evening:
                $ routetag = "dv7dl"
                jump alt_day4_dv_7dl_start
            else:
                jump alt_day3_router_un

label alt_day3_router_un:
    if lp_un >= 12 or (lp_un >= 11 and (counter_sl_7dl >= 1)):
        "Мне снилась Лена…"
        window hide
    if (alt_day3_un_med_help == 1) and (lp_un >= 13):
        $ routetag = "un7dl"
        jump alt_day4_un_7dl_start
    elif (alt_day2_date == 'un_fz') and (alt_day3_dancing == 132):
        $ routetag = "un7dl"
        jump alt_day4_un_fz_start
    else:
        jump alt_day3_router_mi

label alt_day3_router_mi:
    if lp_mi >= 13:
        if alt_day3_mi_dj:
            "Мне снилась Мику…"
            "Правда, не очень долго."
            window hide
            $ routetag = "mi7dl"
            jump alt_day4_mi_dj_start
    else:
        jump alt_day3_router_sl

label alt_day3_router_sl:
    if lp_sl >= 13:
        "Мне снилась Славя…"
        window hide
        if counter_sl_7dl == 5:
            jump alt_day4_sl_7dl_start
        elif counter_sl_cl == 7:
            $ lp_us -= 3
            $ routetag = "sl"
            jump alt_day4_sl_start
    else:
        jump alt_day3_router_neutral

label alt_day3_router_neutral:
    if alt_dlc_active and alt_day3_uvao_spotted:
        $ routetag = "uv"
        "Сон был тревожным…"
        window hide
        jump alt_day4_start_uvao
    else:
         jump alt_day4_neu_begin
