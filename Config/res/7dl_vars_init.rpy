#Мод пилится на базе нетленки от АБЦБ - его сюжет и подача мне куда симпатичнее оригинальной стори.
#За что ему огромный респектище и, по возможности, оставлены отсылки на оригинальные правки.
init -1:
    $ alt_release_no = "0.40.2"
    $ alt_compatible_release_no = ["0.34.a", "0.34.b", "0.35.a", "0.36.a", "0.37.a", "0.38.a", "0.39.a", "0.40", "0.40.1", "0.40.2"]
    $ alt_hotfix_no = "hf0"
    $ plthr = u"None"

init 2:
    $ mods["scenario__alt_sevendl"] = u"7 Дней Лета: Lost Alpha"
    $ mod_tags["scenario__alt_sevendl"] = ["length:days","gameplay:vn","protagonist:male"]
    
    $ timeskip0 = "Я с трудом вспоминаю, \n с чего всё началось…"
    $ timeskip_come = "Ты пойдёшь со мной?"
    $ timeskip_dev = "Рут находится в разработке…\nВ активной разработке: новый карточный турнир."
    $ timeskip33 = "ВЕЛИКОЕ ОГРАБЛЕНИЕ!"
    $ timeskip3 = "Я скучаю…"
    $ timeskip4 = "Я хочу к тебе…"
    $ timeskip5 = "ПОШЛА ВОООООН!"
    $ timeskip6 = "ПРЕДУПРЕЖДЕНИЕ\nВсе совпадения персонажей и характеров\nс реально существующими людьми\nсчитать злой волей автора"
    $ timeskip7 = "Твоя Мику"
    $ timeskip8 = "ПРОСНИСЬ"
    $ timeskip9 = "Я буду ждать."
    $ timeskip10 = "Спасибо…"
    $ timeskip11 = "Прощай."
    $ timeskip12 = "Ты потерялся, малыш?"
    $ timeskip13 = "ПРИДИ В СЕБЯ!"
    
    $ alt_credits_text = "{image=acm_logo}\n\n\n{b}Сценарий{/b}\n\n7дл-кун aka Inakrin\n\nabcb\n\n\n{b}Графика{/b}\n\n{b}Спрайты{/b} — GoodbyeNona, Mannych\n\n{b}Фоны и CG{/b} — GoodbyeNona, Макс Смолев, Narwhal Iv, Kef34, FairyApple, nyamaznya, SkieyWayfarer, MarkTailor, nenkoket, Trojan, NikHaker, rina.jess, childofburningtime27, Касандра\n\n\n{b}Музыка{/b}\n\nApril Rain, Tym Nyman, DeadPunk, ППВК, Kevin MacLeod, SinkWay, DeepCosmo и др.\n\n\n{b}Логика повествования, вычитка сценария{/b}\n\nSitzileon, Dantiras, faddeev\n\n\n{b}Код и адаптация{/b}\n\nEldhenn, Kibconj - порт сценария в Steam\n\nSalotor - галерея, порт сценария в Steam и на Андроид\n\nBlackMazeGOD - главное меню\n\nSitzileon - рефаб рутов\n\nKaiserd3 - ачивлист\n\nNuttyprof, openplace - новая карта лагеря и новый карточный турнир\n\nЛенофаг Простой, Ravsii - стартовые меню\n\nDantiras - старый ачивлист\n\nКоманда мода БЛ:ПИ - алгоритм сборки спрайтов\n\n\n{b}Товарищи, помогавшие с вычиткой, кодом и всем остальным{/b}\n\nМакс Ветров, Drago23, Arlien, Peregarrett, Demiurge-kun, Дельта, KirillZ89, Ленофаг Простой, Ленивый Бегун, Занудный, Serge Domingo, Ravsii, Gr0m, shers, polandkyn, i___s___v, tngeyzer, alexzen84, Alex New, traven42, dllhz, nikolaystorm, mcoder, Eternal_Star, Varaboy, SuperStyle, avakson, hirrommant, redr4iders, ArchiVolt, NNUS3R, ginger_tigra, Дмитрий Мерзляков\n\n\n{b}Команда «7 Дней Лета: Lost Alpha»{/b}\n\nSalotor, Sitzileon, Ismir, still13free\n\n\nВыражаем благодарность команде «Soviet Games» за предоставление ресурсов и платформы для творчества\n\n\nПерсональная благодарнось 7дл-куну за проделанную работу над модификацией \"7 дней лета\"\n\n\nСпасибо всем, кто не был упомянут, но внёс свой вклад, - за то, что помогали и поддерживали!\n\n\n\nКОНЕЦ"
    
    #Day - базис
    #Sunset - 94%, 82%, 100%
    #Night - 58%, 67%, 67%
    #Prologue - 84%, 72%, 100% 

    $ colors['ai'] = {
    'night': (41, 164, 1, 255),
    'sunset': (67, 201, 2, 255),
    'day': (72, 246, 2, 255),
    'prolog': (60, 177, 2, 255)}
    $ store.names_list.append('ai')
    $ names['ai'] = u'Собеседник'

    $ colors['al'] = {
    'night': (122, 121, 102, 255),
    'sunset': (198, 148, 153, 255),
    'day': (211, 181, 153, 255),
    'prolog': (177, 130, 153, 255)}
    $ store.names_list.append('al')
    $ names['al'] = u'Алька'

    $ colors['am'] = {
    'night': (94, 143, 100, 255),
    'sunset': (152, 175, 149, 255),
    'day': (162, 214, 149, 255),
    'prolog': (136, 154, 149, 255)}
    $ store.names_list.append('am')
    $ names['am'] = u'Я'

    $ colors['ase'] = {
    'night': (137, 44, 44, 255),
    'sunset': (222, 54, 56, 255),
    'day': (236, 66, 66, 255),
    'prolog': (198, 48, 66, 255)}
    $ store.names_list.append('ase')
    $ names['ase'] = u'Алиса'

    $ colors['ba'] = {
    'night': (137, 153, 135, 255),
    'sunset': (223, 188, 201, 255),
    'day': (237, 229, 201, 255),
    'prolog': (199, 165, 201, 255)}
    $ store.names_list.append('ba')
    $ names['ba'] = u'Саныч'

    $ colors['bb'] = {
    'night': (133, 116, 90, 255),
    'sunset': (215, 142, 135, 255),
    'day': (229, 173, 135, 255),
    'prolog': (192, 125, 135, 255)}
    $ store.names_list.append('bb')
    $ names['bb'] = u'Алексей Максимыч'

    $ colors['dn'] = {
    'night': (119, 68, 45, 255),
    'sunset': (193, 84, 67, 255),
    'day': (205, 102, 67, 255),
    'prolog': (172, 73, 67, 255)}
    $ store.names_list.append('dn')
    $ names['dn'] = u'Даня'

    $ colors['dy'] = {
    'night': (192, 192, 192, 255),
    'sunset': (192, 192, 192, 255),
    'day': (56, 90, 107, 255),
    'prolog': (192, 192, 192, 255)}
    $ store.names_list.append('dy')
    $ names['dy'] = u'Динамики'
    
    $ colors['ka'] = {
    'night': (137, 82, 85, 255),
    'sunset': (222, 101, 127, 255),
    'day': (236, 123, 127, 255),
    'prolog': (198, 89, 127, 255)}
    $ store.names_list.append('ka')
    $ names['ka'] = u'Катюшка'

    $ colors['kids'] = {
    'night': (235, 120, 131, 255),
    'sunset': (235, 120, 131, 255),
    'day': (235, 120, 131, 255),
    'prolog': (235, 120, 131, 255)}
    $ store.names_list.append('kids')
    $ names['kids'] = u'Дети'
    
    $ colors['ln'] = {
    'night': (137, 82, 85, 255),
    'sunset': (222, 101, 127, 255),
    'day': (236, 123, 127, 255),
    'prolog': (198, 89, 127, 255)}
    $ store.names_list.append('ln')
    $ names['ln'] = u'Алёна'

    $ colors['ml'] = {
    'night': (43, 134, 98, 255),
    'sunset': (70, 164, 147, 255),
    'day': (74, 200, 147, 255),
    'prolog': (62, 144, 147, 255)}
    $ store.names_list.append('ml')
    $ names['ml'] = u'Мальчик'
    
    $ colors['ml2'] = {
    'night': (43, 53, 134, 255),
    'sunset': (70, 65, 200, 255),
    'day': (74, 79, 200, 255),
    'prolog': (62, 57, 200, 255)}
    $ store.names_list.append('ml2')
    $ names['ml2'] = u'Мальчик'
    
    $ colors['ml3'] = {
    'night': (62, 114, 98, 255),
    'sunset': (101, 139, 147, 255),
    'day': (107, 170, 147, 255),
    'prolog': (90, 122, 147, 255)}
    $ store.names_list.append('ml3')
    $ names['ml3'] = u'Мальчик'
    
    $ colors['sak'] = {
    'night': (89, 115, 146, 255),
    'sunset': (144, 140, 218, 255),
    'day': (153, 171, 218, 255),
    'prolog': (129, 123, 218, 255)}
    $ store.names_list.append('sak')
    $ names['sak'] = u'Сакишита Чихиро'

    $ colors['tn'] = {
    'night': (125, 111, 62, 255),
    'sunset': (203, 136, 93, 255),
    'day': (216, 166, 93, 255),
    'prolog': (181, 120, 93, 255)}
    $ store.names_list.append('tn')
    $ names['tn'] = u'Тоник'
    
    $ colors['voice1'] = {
    'night': (159, 8, 73, 255),
    'sunset': (196, 7, 92, 255),
    'day': (255, 136, 192, 255),
    'prolog': (196, 7, 124, 255)}
    $ store.names_list.append('voice1')
    $ names['voice1'] = u'Продавщица'
    
    $ colors['voices'] = {
    'night': (192, 192, 192, 255),
    'sunset': (192, 192, 192, 255),
    'day': (192, 192, 192, 255),
    'prolog': (192, 192, 192, 255)}
    $ store.names_list.append('voices')
    $ names['voices'] = u'Голоса'

    $ colors['we'] = {
    'night': (67, 23, 111, 255),
    'sunset': (132, 27, 100, 255),
    'day': (252, 15, 192, 255),
    'prolog': (150, 50, 100, 255)}
    $ store.names_list.append('we')
    $ names['we'] = u'Хором'
    
    $ reload_names()
    
label scenario__alt_sevendl:
# только если игру начали заново - принимаем номер релиза сохранения по номеру релиза мода
    $ alt_save_release_no = alt_release_no
# инициализация карт. Должна выполняться ТОЛЬКО один раз - иначе не работают сохранения
    $ init_map_zones_alt1()
    $ init_map_zones_alt2()
# включаем кастомные менюшки
    $ alt_interface_on()
# переходим к главному меню мода
    jump main_menu_7dl

init 4:
# вызываем все переменные в init
    call alt_vars

label alt_vars:
    call alt_day0_vars
    call alt_day1_vars
    call alt_day2_vars
    call alt_day3_vars
    call alt_day4_mi_7dl_vars
    call alt_day5_mi_7dl_vars
    call alt_day6_mi_7dl_vars
    call alt_day4_mi_cl_vars
    call alt_day4_mi_dj_vars
    call alt_day5_mi_dj_vars
    call alt_day6_mi_dj_vars
    call alt_day4_dv_7dl_vars
    call alt_day6_dv_7dl_vars
    call alt_day4_sl_7dl_vars
    call alt_day5_sl_7dl_vars
    call alt_day6_sl_7dl_vars
    call alt_day7_sl_7dl_vars
    call alt_day4_sl_cl_vars
    call alt_day5_sl_cl_vars
    call alt_day6_sl_cl_vars
    call alt_day7_sl_cl_vars
    call alt_day5_sl_wh_vars
    call alt_day4_un_7dl_vars
    call alt_day5_un_7dl_vars
    call alt_day6_un_7dl_vars
    call alt_day7_un_7dl_vars
    call alt_day4_un_fz_vars
    call alt_day5_mt_7dl_vars
    call alt_day6_mt_7dl_vars
    call alt_day5_us_7dl_vars
    call alt_day6_us_7dl_vars
    call alt_day6_us_px_vars
    call alt_day7_us_px_vars
    call alt_day4_neu_us_vars
    call alt_day5_neu_us_vars
    call alt_day4_me_no_vars
    call alt_day1_me_d3_vars
    return

label alt_day0_vars: # Переменные нулевого дня
    $ lp_mi = 0
    $ lp_sl = 0
    $ lp_un = 0
    $ lp_us = 0
    $ lp_dv = 0
    $ karma = 0
    $ reput = 0
    $ alt_sp = 0
    $ alt_spt = 0
    $ alt_hpt = 0
    $ mt_pt = 0
    $ d3_pt = 0
    $ us_pt = 0
    $ alt_day_catapult = 0
    $ alt_replay_on = False
    $ alt_dlc_active = False
    $ dr = False
    $ herc = False
    $ loki = False
    $ d3 = False
    $ routetag = "prologue"
    $ role_bg = "intro_ground"
    $ alt_day_binder = 0
    if (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star) and persistent.dv_7dl_good_ussr and (persistent.sl_7dl_loki_good or persistent.sl_7dl_herc_good or persistent.sl_7dl_dr_good2) and persistent.un_7dl_good_ussr and persistent.mt_7dl_good and persistent.us_7dl_good:
        $ persistent.alt_binder = True
    else:
        $ persistent.alt_binder = False
    if persistent.uv_dlc_on_7dl:
        $ alt_dlc_active = True
    return

label alt_day1_vars: # Переменные первого дня
    $ alt_route_flag = 1
    $ counter_sl_cl = 0 # Счётчик рута (Славя-классик)
    $ counter_sl_7dl = 0 # Счётчик рута (Славя-7дл)
    $ list_slavya_7dl = []
    $ alt_day1_chase = False
    $ alt_day1_chase_uvao = False
    $ alt_day1_cofront_sl_dv = 0
    $ alt_day1_el_followed = False
    $ alt_day1_genda_investigation = False
    $ alt_day1_me_d3_dv_feed = False    # XXX: хвост от возможности выхода для троицы на альт день
    $ alt_day1_sam_paniqued = False
    $ alt_day1_sl_ignored = False
    $ alt_day1_sl_keys_took = 0
    $ alt_day1_sl_met = False
    $ alt_day1_un_camp = False
    $ alt_day1_un_dated = False
    $ alt_day1_un_ignored = False
    $ alt_day1_un_stopped = False
    $ alt_day1_us_shotted = False
    return

label alt_day2_vars: # Переменные второго дня
    $ alt_route_flag = 2
    $ list_clubs_7dl = [] # список клубов, которые не вычеркнули из бегунка
    $ list_joined_clubs_7dl = [] # список клубов, в которые записались
    $ list_voyage_7dl = [] # список посещённых при обходе мест
    $ alt_day2_bf_dv_us = False
    $ alt_day2_bf_un = False
    $ alt_day2_cake = False
    $ alt_day2_cardgame_block_rollback = False
    $ alt_day2_convoy = False
    $ alt_day2_date = False
    $ alt_day2_dv_bet_approve = False
    $ alt_day2_dv_bet_won = 0
    $ alt_day2_dv_chased = False
    $ alt_day2_dv_dinner = False
    $ alt_day2_dv_harass = False
    $ alt_day2_dv_tears = False
    $ alt_day2_dv_us_house_visited = False
    $ alt_day2_fail = 0
    $ alt_day2_loki_minijack = False
    $ alt_day2_mi_dinner = False
    $ alt_day2_mi_hyst = False
    $ alt_day2_mi_kumuhimo = 0
    $ alt_day2_mi_met = False
    $ alt_day2_mi_rejected = False
    $ alt_day2_mi_snap = False
    $ alt_day2_mt_help = False
    $ alt_day2_olga_help = False
    $ alt_day2_sl_bf = False
    $ alt_day2_slot_us_cake = False
    $ alt_day2_sup = 0
    $ alt_day2_un_secret_spot = 0
    $ alt_day2_un_rej_convoy = False
    $ alt_day2_us_dubstep = False
    $ alt_day2_us_escape = False
    $ alt_day2_walk = 0
    # Переменные для турнира
    $ alt_day2_round1 = 0 # 0 не участвовал, 1 проиграл, если победил то -V-
    $ alt_day2_round2 = 0 # 0 не участвовал, 1 проиграл, если победил, то -V-
    $ alt_day2_round3 = 0 # 0 не участвовал 1 для проигрыша 2 для победы
    $ alt_day2_desk1 = 0
    $ alt_day2_hf1 = 0
    $ alt_day2_desk2 = 0
    $ alt_day2_hf2 = 0
    $ alt_day2_f1 = 0
    $ alt_day2_desk3 = 0
    $ alt_day2_hf3 = 0
    $ alt_day2_desk4 = 0
    $ alt_day2_hf4 = 0
    $ alt_day2_f2 = 0
    $ alt_day2_revanche = False
    $ alt_day3_us_shenan = False
    $ alt_day3_duty = False
    $ alt_day2_sl_chased = False
    return

label alt_day3_vars: # Переменные третьего дня
    $ alt_route_flag = 3
    $ alt_day3_dancing = 0
    $ alt_day3_dv2_event = False
    $ alt_day3_dv_date = False
    $ alt_day3_dv_dj = False 
    $ alt_day3_dv_evening = False
    $ alt_day3_dv_event = False
    $ alt_day3_dv_guitar_lesson = False
    $ alt_day3_dv_invite = False
    $ alt_day3_dv_rejected = False
    $ alt_day3_dv_rep = False
    $ alt_day3_event1 = 0
    $ alt_day3_event2 = 0
    $ alt_day3_event3 = 0
    $ alt_day3_event4 = 0
    $ alt_day3_ladder_mt = 0
    $ alt_day3_ladder_phys = 0
    $ alt_day3_lp_route = 0
    $ alt_day3_mi_date = False
    $ alt_day3_mi_dj = False 
    $ alt_day3_mi_donor = False
    $ alt_day3_mi_event = False
    $ alt_day3_mi_invite = False
    $ alt_day3_mi_invite2 = False
    $ alt_day3_mi_rejected = False
    $ alt_day3_sl_bath_voy = False
    $ alt_day3_sl_invite = False
    $ alt_day3_technoquest_st0 = False
    $ alt_day3_technoquest_st1 = False
    $ alt_day3_technoquest_st2 = False
    $ alt_day3_technoquest_st3 = 0
    $ alt_day3_technoquest_st3_help = False
    $ alt_day3_timer_jump = 0
    $ alt_day3_timer_range = 0
    $ alt_day3_un_cheated = False
    $ alt_day3_un_date = False 
    $ alt_day3_un_event = False
    $ alt_day3_un_fz_dinner = False
    $ alt_day3_un_fz_evening = False
    $ alt_day3_un_invite = 0
    $ alt_day3_un_med_help = False
    $ alt_day3_un_strip_pool_sp = 5
    $ alt_day3_un_strip_pool_un = 5
    $ alt_day3_us_bugs = 0
    $ alt_day3_us_invite = False
    $ alt_day3_uvao_spotted = False
    $ alt_timer = 10
    return

label alt_day4_mi_7dl_vars:
    $ alt_day4_mi_7dl_bl_save = False
    $ alt_day4_mi_7dl_fireworks = False
    $ alt_day4_mi_7dl_donor = False
    $ alt_day4_mi_7dl_ev_savior = False
    return

label alt_day5_mi_7dl_vars:
    $ alt_day5_mi_7dl_voyeur = False
    $ alt_day5_mi_7dl_kiss = False
    return

label alt_day6_mi_7dl_vars:
    $ alt_day6_mi_7dl_left = False
    $ alt_day7_mi_7dl_trait = 0
    return

label alt_day4_mi_cl_vars:
    $ alt_day4_mi_mi2midj_transit = False
    $ alt_day4_mi_vodka = False
    $ alt_day4_mi_clothes = False
    $ alt_day4_mi_bake = False
    $ alt_day4_mi_coal = False
    $ alt_day4_mi_senio = 0
    $ alt_day4_mi_photo_slavya = False
    $ alt_day4_mi_photo = False
    $ alt_day4_mi_rival_won = False
    $ alt_day4_mi_dance = False
    $ alt_day4_mi_comfort = False
    $ alt_day4_mi_supper_sl = False
    return

label alt_day4_mi_dj_vars:
    $ alt_day4_mi_dj_hedg = False
    $ alt_day4_mi_dj_blackmailed = False
    $ alt_day4_mi_dj_sl_repet = False
    $ alt_day4_mi_dj_reasons = False
    $ alt_day4_mi_dj_sl_repet = False
    return

label alt_day5_mi_dj_vars:
    $ alt_day5_mi_dj_musclub_visited = False
    $ alt_day5_mi_dj_entrance_visited = False
    $ alt_day5_mi_dj_musclub_visited = False
    $ alt_day5_mi_dj_estrade_visited = False
    $ alt_day5_mi_dj_home_visited = False
    $ alt_day5_mi_dj_necessary_done = 0
    $ alt_day5_mi_dj_dv_blade = False
    $ alt_day5_mi_dj_voyeur = 0
    $ alt_day5_mi_dj_favorite_song = False
    $ alt_day5_mi_dj_hentai = False
    $ alt_day5_mi_dj_dv_kissing = False
    $ alt_day5_mi_dj_forgive = False
    $ alt_day5_mi_dj_cut = False
    return

label alt_day6_mi_dj_vars:
    $ alt_day6_mi_dj_sonic_agreed = False
    $ alt_day6_mi_dj_sl_evil = False
    $ alt_day6_mi_dj_dv_evil = False
    $ alt_day6_mi_dj_me_evil = False
    $ alt_day6_mi_dj_sl_feed = False
    $ alt_day6_mi_dj_un_evil = False
    $ alt_day6_mi_dj_key = False
    $ alt_day6_mi_dj_walkman = False
    $ alt_day6_mi_dj_hentai1 = False
    $ alt_day6_mi_dj_hentai2 = False
    $ alt_day6_mi_dj_hentai_catch = False
    $ alt_day6_mi_dj_letmeout = False
    $ alt_day6_mi_dj_letmestay = False
    $ alt_day6_mi_dj_no_hentai = False
    $ alt_day6_mi_dj_rejected = False
    return

label alt_day4_dv_7dl_vars:
    $ alt_day4_dv_7dl_extra_key = False
    $ alt_day4_dv_7dl_walkman_presented = False
    $ alt_day4_dv_7dl_roadtrip = 0
    $ alt_day4_dv_7dl_mt_drugs = 0
    $ alt_day4_dv_7dl_portwine = False
    $ alt_day4_dv_7dl_vodka = False
    $ alt_day4_dv_7dl_ba_conv = False
    $ alt_day4_dv_7dl_drank_vodka = False
    $ alt_day4_dv_7dl_hentai = False
    $ alt_day4_dv_7dl_help_cs = False
    $ alt_day4_dv_7dl_aidpost = False
    return

label alt_day6_dv_7dl_vars:
    $ alt_day6_dv_7dl_mi_route = False
    $ alt_day6_dv_7dl_sl_route = False
    $ alt_day6_dv_7dl_transit = False
    $ alt_day6_dv_7dl_key = False
    $ alt_day6_dv_7dl_key_hentai = 0
    $ alt_day6_dv_7dl_alco_hentai = 0
    $ alt_day6_dv_7dl_ba_hentai = 0
    $ alt_day6_dv_7dl_hentai = 0
    $ alt_day6_dv_7dl_dance = 0
    $ alt_day7_dv_7dl_check = 0
    $ alt_day6_dv_7dl_escape_convince = False
    $ alt_day7_dv_7dl_brace = 0
    $ alt_day6_dv_7dl_sl_help_agree = False
    $ alt_day7_dv_7dl_loki_catapult = False
    return

label alt_day4_sl_7dl_vars:
    $ alt_day4_sl_7dl_workout = False
    $ alt_day4_sl_7dl_herc_appletree = False
    $ alt_day4_sl_7dl_help1 = False
    $ alt_day4_sl_7dl_phone = False
    $ alt_day4_sl_7dl_herc_rendezvous = False
    return

label alt_day5_sl_7dl_vars:
    $ alt_day5_sl_7dl_workout = False
    $ alt_day5_sl_7dl_defend = False
    $ alt_day5_sl_7dl_herc_sick = False
    $ alt_day5_random_val = 0
    $ alt_day5_sl_7dl_hentai_done = False
    $ alt_day5_sl_7dl_olroad = False
    $ alt_day5_sl_7dl_loki_true = False
    return

label alt_day6_sl_7dl_vars:
    $ alt_day6_sl_7dl_workout = False
    $ alt_day6_sl_7dl_hentai_done = False
    $ alt_day6_sl_7dl_forgive = False
    $ alt_day5_sl_7dl_loki_true = False
    return

label alt_day7_sl_7dl_vars:
    $ alt_day7_sl_7dl_workout = False
    $ alt_day7_sl_7dl_not_freewill = False
    $ alt_day7_sl_7dl_loki_park = False
    return

label alt_day4_sl_cl_vars:
    $ alt_day4_sl_un_rej = False
    $ alt_day4_sl_tut_iz = False
    $ alt_day4_sl_tut = False
    $ alt_day4_sl_tut_lf = False
    $ alt_day4_sl_lf_solo = 0
    $ alt_day4_sl_wh = False
    $ alt_day5_sl_wh_transit = False
    return

label alt_day5_sl_cl_vars:
    $ alt_day5_sl_extra_house = False
    $ alt_day5_sl_tan = False
    return

label alt_day6_sl_cl_vars:
    $ alt_day6_sl_arc = 0
    $ alt_day6_sl_repel = False
    $ alt_day6_sl_shirt = False
    $ alt_day6_sl_cl_rt = False
    $ alt_day6_sl_cl_int_pt = 0
    $ alt_day6_sl_cl_fin = 0
    $ alt_day6_sl_int = 0
    $ alt_day6_sl_good = 0
    return

label alt_day7_sl_cl_vars:
    $ alt_day7_d3_transit = False
    $ alt_day7_sl_map_progress = 0
    $ alt_day7_sl_code = False
    return

label alt_day5_sl_wh_vars:
    $ alt_day5_sl_wh_th_dead = False
    return

label alt_day4_un_7dl_vars:
    $ alt_un_old_hentai = False
    $ alt_day4_un_7dl_morning_searching = False
    $ alt_day4_un_7dl_ducks = False
    $ alt_day4_un_7dl_ba_alerted = False
    $ alt_day4_un_7dl_dv_calm = False
    $ alt_day4_un_7dl_un_calm = False
    $ alt_day4_un_7dl_dv_us_explosives = False
    $ alt_day4_un_7dl_hen1 = False
    return

label alt_day5_un_7dl_vars:
    $ alt_day5_un_7dl_cleanse = False
    $ alt_day5_un_7dl_square_duty = False
    $ alt_day5_un_7dl_club_day = False
    $ alt_day5_un_7dl_sl_un_washing = False
    $ alt_day5_un_7dl_solo_washing = False
    $ alt_day5_un_7dl_sl_fight = False
    return

label alt_day6_un_7dl_vars:
    $ alt_day6_un_7dl_agreed = False
    return

label alt_day7_un_7dl_vars:
    $ alt_day7_un_7dl_rej_end = False
    return

label alt_day4_un_fz_vars:
    $ alt_day4_fz_play = 0
    $ alt_day4_fz_cards = False
    $ alt_day4_fz_sl_walk = False
    $ alt_day4_fz_sl_wish = False
    $ alt_day4_fz_girl_off_1 = False
    $ alt_day4_fz_girl_off_2 = False
    $ alt_day4_fz_girl_off_3 = False
    $ alt_day4_fz_girl_off_5 = False
    $ alt_day4_fz_sh = 0
    $ alt_day4_fz_un_letter = False
    $ alt_day4_fz_girl_off = 0
    return 

label alt_day5_mt_7dl_vars:
    $ alt_day5_neu_mt_diary = False
    $ alt_day5_mt_7dl_hentai = False
    return

label alt_day6_mt_7dl_vars:
    $ alt_day6_mt_7dl_pt = False
    $ alt_day6_mt_7dl_lms = False
    $ alt_day7_mt_7dl_pt = 0
    return

label alt_day5_us_7dl_vars:
    $ alt_day4_us_7dl_float = False
    $ alt_day5_us_7dl_carrier = False
    $ alt_day6_us_7dl_alice_convince = False
    $ alt_day6_us_7dl_lena_convince = False
    $ alt_day6_us_7dl_lost_road = False
    $ alt_day7_us_7dl_repair = False
    return

label alt_day6_us_7dl_vars:
    $ alt_day6_us_7dl_mi_friends = False
    $ alt_day6_us_7dl_sl_friends = False
    $ alt_day6_us_7dl_un_friends = False
    $ alt_day6_us_7dl_dance_mt = False
    $ alt_day6_us_7dl_tr = False
    return

label alt_day6_us_px_vars:
    $ alt_day6_us_px_sl_join = False
    $ alt_day6_us_px_dv_join = False
    return

label alt_day7_us_px_vars:
    $ alt_day7_us_px_escaped = False
    return

label alt_day4_neu_us_vars:
    $ alt_day4_neu_transit = 0
    $ alt_day4_neu_us_snake = False
    $ alt_day4_neu_back_pack = False
    $ alt_day4_neu_date = 0
    $ alt_day4_neu_mt_diary = False
    $ alt_day4_neu_mt_fire = False
    $ alt_day4_neu_mt_volley = False
    $ alt_day4_neu_mt_songs = False
    $ alt_day4_neu_mt_volonteer = False
    $ alt_day4_neu_sl_pup = False
    $ alt_day4_neu_siesta = False
    $ alt_day4_neu_bay = False
    $ alt_day4_neu_us_pixies = False
    return

label alt_day5_neu_us_vars:
    $ alt_day5_neu_candle = 0
    $ alt_day5_neu_mt_diary = False
    $ alt_day5_neu_potato = False
    $ alt_day5_neu_mt_voyeur = 0
    $ alt_day5_neu_sl_voyeur = False
    $ alt_day5_neu_us_stores = False
    $ alt_day5_neu_us_potato = False
    return

label alt_day4_me_no_vars:
    $ alt_no_un = 0
    $ alt_no_ammo = 0
    $ alt_no_weapon = 0
    $ alt_no_clue = 0
    return

label alt_day1_me_d3_vars:
    $ alt_d3_bad_0 = False
    $ alt_day1_me_d3_chase = False
    $ alt_day1_me_d3_robbery = False
    $ alt_day1_me_d3_dv_feed = False
    $ alt_day1_me_d3_sl_conv = False
    $ alt_day1_me_d3_sl_met = False
    $ alt_day1_me_d3_us_robbed = False
    return
