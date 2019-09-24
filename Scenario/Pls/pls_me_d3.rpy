label alt_day1_me_d3_start:
    call alt_day1_me_d3_vars
    $ alt_d3_bad_0 = True
    $ reput = 100 # Базовый показатель репутации
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(1, u"ОТКАТ")
    call alt_day1_me_d3_M
    pause(1)
    call alt_day1_me_d3_A
    pause(1)
    call alt_day1_me_d3_S
    pause(1)
    call alt_day1_me_d3_L
    pause(1)
    call alt_day1_me_d3_O
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day1_me_d3_supper
    pause(1)
    call alt_day1_me_d3_U
    if not alt_day1_me_d3_us_robbed:
        call alt_day1_me_d3_U_reject
        pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day1_me_d3_ev_A_S
    pause(1)
    call alt_day1_me_d3_ev_mt
    pause(1)
    jump alt_day2_me_d3_start

label alt_day2_me_d3_start:
    $ persistent.sprite_time = "day"
    $ routetag = "slcas"
    $ day_time()
    pause(1)
    call alt_day2_me_d3_pre
    if not persistent.me_neu_true:
        $ sdl_cheat_disable()
        $ sdl_cheat_persistent_res("alt_cheater")
        pause(1)
        $ renpy.block_rollback()
        jump start_7dl # Прыг в начало
    window hide
    scene black
    with fade
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    return
    
    $ alt_chapter(2, u"Славя")
    call alt_day2_me_d3_begin
    pause(1)
    jump alt_day3_me_d3_start

label alt_day3_me_d3_start:
    $ persistent.sprite_time = "day"
    $ routetag = "mt7dluni"
    $ day_time()
    pause(1)
    $ alt_chapter(3, u"Ольга")
    call alt_day3_me_d3_begin
    pause(1)
    #перебивка
    jump alt_day3_me_d3_start
    #Завершение демо

label alt_day4_me_d3_start:
    $ persistent.sprite_time = "day"
    $ routetag = "us7dlbear"
    $ day_time()
    pause(1)
    $ alt_chapter(4, u"Ульянка")
    call alt_day4_me_d3_begin
    pause(1)
    jump alt_day5_me_d3_start

label alt_day5_me_d3_start:
    $ persistent.sprite_time = "day"
    $ routetag = "dv7dldress"
    $ day_time()
    pause(1)
    $ alt_chapter(5, u"Алиса")
    call alt_day5_me_d3_begin
    pause(1)
    jump alt_day6_me_d3_start

label alt_day6_me_d3_start:
    $ persistent.sprite_time = "day"
    $ routetag = "mi7dldress"
    $ day_time()
    pause(1)
    $ alt_chapter(6, u"Намики/Мику")
    call alt_day6_me_d3_begin
    pause(1)
    jump alt_day7_me_d3_start

label alt_day7_me_d3_start:
    $ persistent.sprite_time = "day"
    $ routetag = "un7dlwinter"
    $ day_time()
    pause(1)
    $ alt_chapter(7, u"Лена")
    call alt_day7_me_d3_begin
    pause(1)
    if persistent.me_d3_bad < 1:
        if (persistent.alt_cheater > 1) or config.developer:
            call alt_day7_me_d3_falsch
        elif persistent.chapter_counter > 2:
            call alt_day7_me_d3_fag
        else:
            call alt_day7_me_d3_bad
    else:
        call alt_day7_me_d3_true
    return
