label alt_day4_no_start:
    call alt_day4_me_no_vars
    $ noir_interface_on()
    $ noir_interface = True
    $ routetag = "Noir"
    $ plthr = "Нуар"
    $ alt_chapter(4, u"Долгий вечер")

    call alt_day4_no_begin
    pause(1)
    call alt_day4_no_trip
    pause(1)
    call alt_day4_no_passion
    pause(1)
    call alt_day4_no_corpse
    pause(1)
    call alt_day4_no_witch
    pause(1)
    call alt_day4_no_expo2
    pause(1)
    call alt_day4_no_rendezvous
    pause(1)
    call alt_day4_no_cop
    pause(1)

    $ noir_interface_off()
    $ noir_interface = False
    window hide
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    window hide
    return
    jump alt_day5_no_begin

label alt_day5_no_begin:
    $ persistent.sprite_time = "noir"
    $ day_time()
    $ alt_chapter(4, u"Чёртов дождь")
    call alt_day5_no_start
    pause(1)
    call alt_day5_no_sos
    pause(1)
    call alt_day5_no_knowledge_lab
    pause(1)
    call alt_day5_no_treat
    pause(1)
    call alt_day5_no_unknown
    jump alt_day6_no_begin

label alt_day6_no_begin:
    $ persistent.sprite_time = "noir"
    $ day_time()
    $ alt_chapter(4, u"Поиски")
    call alt_day6_no_start
    pause(1)
    call alt_day6_no_zugzwang
    pause(1)
    call alt_day6_no_witch
    pause(1)
    call alt_day6_no_stanger
    pause(1)
    call alt_day6_no_cop_failure
    jump alt_day7_no_begin

label alt_day7_no_begin:
    $ persistent.sprite_time = "noir"
    $ day_time()
    $ alt_chapter(4, u"Вера в себя")
    call alt_day7_no_start
    pause(1)
    call alt_day7_no_cop_end
    pause(1)
    call alt_day7_no_hitman
    pause(1)
    call alt_day7_no_knowledge_end
    pause(1)
    call alt_day7_no_final
    if (alt_no_clue < 4):
        if (alt_no_weapon == 4) and (alt_no_ammo == 3):
            call alt_day7_no_neu
        else:
            call alt_day7_no_bad
    else:
        if (alt_no_weapon == 4) and (alt_no_ammo == 3):
            call alt_day7_no_true
        else:
            call alt_day7_no_bad
    pause(1)
    return