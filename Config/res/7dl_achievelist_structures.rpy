init 9999 python:
    ##### КАК ЭТО РАБОТАЕТ #####
    # Все концовки загоняются в массив концовок рута (в том порядке, в котором они и будут выводиться).
    # А руты - в массивы рутов персонажа.
    #
    # Объект sdl_achv_Achievement (ачивка):
    ## icon          - иконка концовки
    ## persistent    - название перзистента
    ## text          - надпись (объявляется в ресурсах), описывающая характер концовки
    ## prerequisites - массив объектов sdl_achv_Prerequisite, описывающих требования для выхода на концовку
    ## replay        - объект sdl_achv_Replay, использующийся для перехода к концовке
    #
    # Объект sdl_achv_Prerequisite (требование к концовке):
    ## text         - надпись (объявляется в ресурсах), описывающая тип требования
    ## achievements - список объектов sdl_achv_Achievement, удовлетворяющих условию (поля prerequisites и replay не обязательны)
    ###
    ### Пример: пусть для выхода на концовку стоит условие:
    ###     (persistent.us_7dl_tran_un or persistent.us_7dl_tran_mi) and persistent.us_px_good
    ### Тогда нужно создать 2 объекта-требования
    ###     sdl_achv_Prerequisite(
    ###         "sdl_achv_info_end",
    ###         {
    ###             sdl_achv_Achievement("acm_logo_us_px_good", "us_px_good", "sdl_achv_us_good", None, None)
    ###         }
    ###     ),
    ###     sdl_achv_Prerequisite(
    ###         "sdl_achv_info_end",
    ###         {
    ###             sdl_achv_Achievement("acm_logo_us_7dl_tran_un", "us_7dl_tran_un", "sdl_achv_us_tran_un", None, None),
    ###             sdl_achv_Achievement("acm_logo_us_7dl_tran_mi", "us_7dl_tran_mi", "sdl_achv_us_tran_mi", None, None)
    ###         }
    ###     )
    #
    # Объект sdl_achv_Replay (повтор):
    ## label - метка, к которой надо перейти для просмотра концовки
    ## scope - scope-параметр ренпаевского Replay. Здесь следует инициализировать необходимые переменные
    ############################
    
    # Массивы концовок всех рутов
    
    ## Мику-7дл
    sdl_achv_array_mi_7dl = [
        sdl_achv_Achievement(    # Септим
            "acm_logo_mi_7dl_sept",
            "mi_7dl_sept",
            "sdl_achv_mi_SE",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_mi_7dl_sept", {"alt_replay_on" : "True"}),
            "surprise"
        ),
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mi_7dl_true",
            "mi_7dl_true",
            "sdl_achv_mi_true",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_7dl_herc_exc", "mi_7dl_herc_exc", "sdl_achv_mi_HE_exc", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_loki_exc", "mi_7dl_loki_exc", "sdl_achv_mi_LO_exc", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_dr_exc", "mi_7dl_dr_exc", "sdl_achv_mi_DR_exc", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_mi_7dl_true", {"alt_replay_on" : "True"}),
            "serious"
        ),
        sdl_achv_Achievement(    # Гуд-M
            "acm_logo_mi_7dl_good_human",
            "mi_7dl_good_human",
            "sdl_achv_mi_good",
            [],
            sdl_achv_Replay("alt_day7_mi_7dl_good_human", {"alt_replay_on" : "True"}),
            "happy"
        ),
        sdl_achv_Achievement(    # Гуд-S
            "acm_logo_mi_7dl_good_star",
            "mi_7dl_good_star",
            "sdl_achv_mi_good_RF",
            [],
            sdl_achv_Replay("alt_day7_mi_7dl_good_star", {"alt_replay_on" : "True"}),
            "happy"
        ),
        sdl_achv_Achievement(    # Нейтрал-M
            "acm_logo_mi_7dl_neu_human",
            "mi_7dl_neu_human",
            "sdl_achv_mi_neu",
            [],
            sdl_achv_Replay("alt_day7_mi_7dl_neu_human", {"alt_replay_on" : "True"}),
            "cry_smile"
        ),
        sdl_achv_Achievement(    # Нейтрал-S
            "acm_logo_mi_7dl_neu_star",
            "mi_7dl_neu_star",
            "sdl_achv_mi_neu",
            [],
            sdl_achv_Replay("alt_day7_mi_7dl_neu_star", {"alt_replay_on" : "True"}),
            "cry"
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_mi_7dl_loki_exc",
            "mi_7dl_loki_exc",
            "sdl_achv_mi_LO_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_human", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_star", "mi_7dl_good_star", "sdl_achv_mi_good_RF", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_mi_7dl_loki_exc", {"alt_replay_on" : "True"}),
            "upset",
            char_mask=4
        ),
        sdl_achv_Achievement(    # Эксклюзив-Герк
            "acm_logo_mi_7dl_herc_exc",
            "mi_7dl_herc_exc",
            "sdl_achv_mi_HE_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_human", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_star", "mi_7dl_good_star", "sdl_achv_mi_good_RF", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_mi_7dl_herc_exc", {"alt_replay_on" : "True"}),
            "smile",
            char_mask=2
        ),
        sdl_achv_Achievement(    # Эксклюзив-Дрищ
            "acm_logo_mi_7dl_dr_exc",
            "mi_7dl_dr_exc",
            "sdl_achv_mi_DR_exc",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_human", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_7dl_good_star", "mi_7dl_good_star", "sdl_achv_mi_good_RF", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_mi_7dl_dr_exc", {"alt_replay_on" : "True"}),
            "smile2",
            char_mask=1
        ),
        sdl_achv_Achievement(    # Бэд-M
            "acm_logo_mi_7dl_bad_human",
            "mi_7dl_bad_human",
            "sdl_achv_mi_bad",
            [],
            sdl_achv_Replay("alt_day7_mi_7dl_bad_human", {"alt_replay_on" : "True"}),
            "sad"
        ),
        sdl_achv_Achievement(    # Бэд-S
            "acm_logo_mi_7dl_bad_star",
            "mi_7dl_bad_star",
            "sdl_achv_mi_bad",
            [],
            sdl_achv_Replay("alt_day7_mi_7dl_bad_star", {"alt_replay_on" : "True"}),
            "sad"
        )
    ]
    
    ## Мику-DJ
    sdl_achv_array_mi_djt = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mi_dj_true",
            "mi_dj_true",
            "sdl_achv_mi_true",
            [],
            sdl_achv_Replay("alt_day7_mi_dj_true", {"alt_replay_on" : "True"}),
            "cry_smile"
        ),
        sdl_achv_Achievement(    # Гуд-Япония
            "acm_logo_mi_dj_good",
            "mi_dj_good_jap",
            "sdl_achv_mi_good",
            [],
            sdl_achv_Replay("alt_day7_mi_dj_good_jap", {"alt_replay_on" : "True"}),
            "happy"
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_mi_dj_good_rf",
            "mi_dj_good_rf",
            "sdl_achv_mi_good_RF",
            [],
            sdl_achv_Replay("alt_day7_mi_dj_good_rf", {"alt_replay_on" : "True"}),
            "happy"
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_mi_dj_bad",
            "mi_dj_bad",
            "sdl_achv_mi_bad",
            [],
            sdl_achv_Replay("alt_day7_mi_dj_bad", {"alt_replay_on" : "True"}),
            "cry"
        )
    ]
    
    ## Алиса-7дл
    sdl_achv_array_dv_7dl = [
        sdl_achv_Achievement(    # Септим
            "acm_logo_dv_7dl_sept",
            "dv_7dl_sept",
            "sdl_achv_dv_SE",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_dv_7dl_sept", {"alt_replay_on" : "True"}),
            "soft_smile"
        ),
        sdl_achv_Achievement(    # Гуд-СССР
            "acm_logo_dv_7dl_good_ussr",
            "dv_7dl_good_ussr",
            "sdl_achv_dv_good_US",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_good_ussr", {"alt_replay_on" : "True"}),
            "laugh"
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_dv_7dl_good_rf",
            "dv_7dl_good_rf",
            "sdl_achv_dv_good_RF",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_good_rf", {"alt_replay_on" : "True"}),
            "laugh"
        ),
        sdl_achv_Achievement(    # Реджект-СССР
            "acm_logo_dv_7dl_rej_ussr",
            "dv_7dl_rej_ussr",
            "sdl_achv_dv_rej_US",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_rej_ussr", {"alt_replay_on" : "True"}),
            "sad"
        ),
        sdl_achv_Achievement(    # Реджект-РФ
            "acm_logo_dv_7dl_rej_rf",
            "dv_7dl_rej_rf",
            "sdl_achv_dv_rej_RF",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_rej_rf", {"alt_replay_on" : "True"}),
            "shy"
        ),
        sdl_achv_Achievement(    # Транзит-Ольга
            "acm_logo_dv_7dl_tran_mt",
            "dv_7dl_tran_mt",
            "sdl_achv_dv_HE_tran",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_bad", {"alt_replay_on" : "True", "herc" : "True", "alt_day7_dv_7dl_check" : 5}),
            "shocked",
            char_mask=2
        ),
        sdl_achv_Achievement(    # Транзит-Лена
            "acm_logo_dv_7dl_tran_un",
            "dv_7dl_tran_un",
            "sdl_achv_dv_tran",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_tran_un", {"alt_replay_on" : "True"}),
            "rage"
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_dv_7dl_loki_exc",
            "dv_7dl_loki_exc",
            "sdl_achv_dv_LO_exc",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_loki_exc", {"alt_replay_on" : "True"}),
            "guilty",
            char_mask=4
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_dv_7dl_bad",
            "dv_7dl_bad",
            "sdl_achv_dv_bad",
            [],
            sdl_achv_Replay("alt_day7_dv_7dl_bad", {"alt_replay_on" : "True"}),
            "cry"
        )
    ]
    
    ## Славя-7дл
    sdl_achv_array_sl_7dl = [
        sdl_achv_Achievement(    # Септим
            "acm_logo_sl_7dl_sept",
            "sl_7dl_sept",
            "sdl_achv_sl_SE",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_sl_7dl_sept", {"alt_replay_on" : "True"}),
            "sad"
        ),
        sdl_achv_Achievement(    # РФ-гуд
            "acm_logo_sl_7dl_good_rf",
            "sl_7dl_good_rf",
            "sdl_achv_sl_good_RF",
            [],
            sdl_achv_Replay("alt_day7_sl_7dl_good_rf", {"alt_replay_on" : "True"}),
            "shy"
        ),
        sdl_achv_Achievement(    # Локи-Гуд
            "acm_logo_sl_7dl_loki_good",
            "sl_7dl_loki_good",
            "sdl_achv_sl_LO_good",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_7dl_loki_neu", "sl_7dl_loki_neu", "sdl_achv_sl_LO_neu", None, None),
                        sdl_achv_Achievement("acm_logo_sl_7dl_loki_rej", "sl_7dl_loki_rej", "sdl_achv_sl_LO_rej", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_sl_7dl_loki_good", {"alt_replay_on" : "True"}),
            "happy",
            char_mask=4
        ),
        sdl_achv_Achievement(    # Локи-Нейтрал
            "acm_logo_sl_7dl_loki_neu",
            "sl_7dl_loki_neu",
            "sdl_achv_sl_LO_neu",
            [],
            sdl_achv_Replay("alt_day7_sl_7dl_loki_neu", {"alt_replay_on" : "True"}),
            "normal",
            char_mask=4
        ),
        sdl_achv_Achievement(    # Локи-Реджект
            "acm_logo_sl_7dl_loki_rej",
            "sl_7dl_loki_rej",
            "sdl_achv_sl_LO_rej",
            [],
            sdl_achv_Replay("alt_day7_sl_7dl_loki_rej", {"alt_replay_on" : "True"}),
            "dontlike",
            char_mask=4
        ),
        sdl_achv_Achievement(    # Герк-Гуд
            "acm_logo_sl_7dl_herc_good",
            "sl_7dl_herc_good",
            "sdl_achv_sl_HE_good",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_7dl_herc_neu", "sl_7dl_herc_neu", "sdl_achv_sl_HE_neu", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_sl_7dl_herc_good", {"alt_replay_on" : "True"}),
            "happy",
            char_mask=2
        ),
        sdl_achv_Achievement(    # Герк-Нейтрал
            "acm_logo_sl_7dl_herc_neu",
            "sl_7dl_herc_neu",
            "sdl_achv_sl_HE_neu",
            [],
            sdl_achv_Replay("alt_day7_sl_7dl_herc_neu", {"alt_replay_on" : "True"}),
            "normal",
            char_mask=2
        ),
        sdl_achv_Achievement(    # Дрищ-Гуд
            "acm_logo_sl_7dl_dr_good",
            "sl_7dl_dr_good",
            "sdl_achv_sl_DR_good",
            [],
            sdl_achv_Replay("alt_day7_sl_7dl_dr_good", {"alt_replay_on" : "True"}),
            "smile",
            1
        ),
        sdl_achv_Achievement(    # Дрищ-Гуд 2
            "acm_logo_sl_7dl_dr_good2",
            "sl_7dl_dr_good2",
            "sdl_achv_sl_DR_good",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_7dl_dr_good", "sl_7dl_dr_good", "sdl_achv_sl_DR_good", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_sl_7dl_dr_good2", {"alt_replay_on" : "True"}),
            "happy",
            1
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_sl_7dl_bad",
            "sl_7dl_bad",
            "sdl_achv_sl_bad",
            [],
            sdl_achv_Replay("alt_day7_sl_7dl_bad", {"alt_replay_on" : "True"}),
            "sad"
        )
    ]
    
    ## Славя-Классик
    sdl_achv_array_sl_clt = [
        sdl_achv_Achievement(    # Инт-ТруЪ
            "acm_logo_sl_cl_int_true",
            "sl_cl_int_true",
            "sdl_achv_sl_true_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_cl_int_good", "sl_cl_int_good", "sdl_achv_sl_good_IN", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_sl_cl_int_true", {"alt_replay_on" : "True"}),
            "sad"
        ),
        sdl_achv_Achievement(    # Инт-гуд
            "acm_logo_sl_cl_int_good",
            "sl_cl_int_good",
            "sdl_achv_sl_good_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_cl_good_ussr", "sl_cl_good_ussr", "sdl_achv_sl_good_US", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf", "sl_cl_good_rf", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf2", "sl_cl_good_rf2", "sdl_achv_sl_good_RF", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_sl_cl_int_good", {"alt_replay_on" : "True"}),
            "smile"
        ),
        sdl_achv_Achievement(    # Инт-бэд
            "acm_logo_sl_cl_int_bad",
            "sl_cl_int_bad",
            "sdl_achv_sl_bad_IN",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_cl_good_ussr", "sl_cl_good_ussr", "sdl_achv_sl_good_US", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf", "sl_cl_good_rf", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_cl_good_rf2", "sl_cl_good_rf2", "sdl_achv_sl_good_RF", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_sl_cl_int_bad", {"alt_replay_on" : "True"}),
            "upset"
        ),
        sdl_achv_Achievement(    # СССР-гуд
            "acm_logo_sl_cl_good_ussr",
            "sl_cl_good_ussr",
            "sdl_achv_sl_good_US",
            [],
            sdl_achv_Replay("alt_day7_sl_cl_good_ussr", {"alt_replay_on" : "True"}),
            "happy"
        ),
        sdl_achv_Achievement(    # РФ-гуд (Плюс-минус)
            "acm_logo_sl_cl_good_rf",
            "sl_cl_good_rf",
            "sdl_achv_sl_good_RF",
            [],
            sdl_achv_Replay("alt_day7_sl_cl_good_rf", {"alt_replay_on" : "True"}),
            "happy"
        ),
        sdl_achv_Achievement(    # РФ-гуд
            "acm_logo_sl_cl_good_rf2",
            "sl_cl_good_rf2",
            "sdl_achv_sl_good_RF",
            [],
            sdl_achv_Replay("alt_day7_sl_cl_good_rf2", {"alt_replay_on" : "True"}),
            "happy"
        ),
        sdl_achv_Achievement(    # Реджект-РФ
            "acm_logo_sl_cl_rej_rf",
            "sl_cl_rej_rf",
            "sdl_achv_sl_rej_RF",
            [],
            sdl_achv_Replay("alt_day7_sl_cl_rej_rf", {"alt_replay_on" : "True"}),
            "tender"
        ),
        sdl_achv_Achievement(    # Реджект-2
            "acm_logo_sl_cl_rej",
            "sl_cl_rej",
            "sdl_achv_sl_rej_RF",
            [],
            sdl_achv_Replay("alt_day7_sl_cl_rej", {"alt_replay_on" : "True"}),
            "surprise"
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_sl_cl_loki_exc",
            "sl_cl_loki_exc",
            "sdl_achv_sl_LO_exc",
            [],
            sdl_achv_Replay("alt_day6_sl_cl_loki_exc", {"alt_replay_on" : "True"}),
            "cry",
            char_mask=4
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_sl_cl_bad",
            "sl_cl_bad",
            "sdl_achv_sl_bad",
            [],
            sdl_achv_Replay("alt_day7_sl_cl_bad", {"alt_replay_on" : "True"}),
            "sad"
        )
    ]
    
    ## Лена-7дл
    sdl_achv_array_un_7dl = [
        sdl_achv_Achievement(    # Септим
            "acm_logo_un_7dl_sept",
            "un_7dl_sept",
            "sdl_achv_un_SE",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_un_7dl_sept", {"alt_replay_on" : "True"}),
            "smile"
        ),
        sdl_achv_Achievement(    # ТруЪ-транзит
            "acm_logo_un_7dl_true_tran",
            "un_7dl_true_tran",
            "sdl_achv_un_true_tran",
            [],
            sdl_achv_Replay("alt_day7_un_7dl_true_tran", {"alt_replay_on" : "True"}),
            "shy"
        ),
        sdl_achv_Achievement(    # Гуд-СССР
            "acm_logo_un_7dl_good_ussr",
            "un_7dl_good_ussr",
            "sdl_achv_un_good_US",
            [],
            sdl_achv_Replay("alt_day7_un_7dl_good_ussr", {"alt_replay_on" : "True"}),
            "smile2"
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_un_7dl_good_rf",
            "un_7dl_good_rf",
            "sdl_achv_un_good_RF",
            [],
            sdl_achv_Replay("alt_day7_un_7dl_good_rf", {"alt_replay_on" : "True"}),
            "smile2"
        ),
        sdl_achv_Achievement(    # Реджект
            "acm_logo_un_7dl_rej",
            "un_7dl_rej",
            "sdl_achv_un_rej",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_7dl_good", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_un_7dl_rej", {"alt_replay_on" : "True"}),
            "normal"
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_un_7dl_bad",
            "un_7dl_bad",
            "sdl_achv_un_bad",
            [],
            sdl_achv_Replay("alt_day7_un_7dl_bad", {"alt_replay_on" : "True"}),
            "sorrow"
        )
    ]
    
    ## Ольга-7дл
    sdl_achv_array_mt_7dl = [
        sdl_achv_Achievement(    # Септим
            "acm_logo_mt_7dl_sept",
            "mt_7dl_sept",
            "sdl_achv_mt_SE",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_mt_7dl_sept", {"alt_replay_on" : "True"}),
            "sad",
            char_mask=2
        ),
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mt_7dl_true",
            "mt_7dl_true",
            "sdl_achv_mt_true",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_7dl_good", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_mt_7dl_true", {"alt_replay_on" : "True"}),
            "smile",
            char_mask=5
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_mt_7dl_good",
            "mt_7dl_good",
            "sdl_achv_mt_good",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_7dl_bad", "mt_7dl_bad", "sdl_achv_mt_bad", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_mt_7dl_good", {"alt_replay_on" : "True"}),
            "grin",
            char_mask=5
        ),
        sdl_achv_Achievement(    # Нейтрал
            "acm_logo_mt_7dl_neu",
            "mt_7dl_neu",
            "sdl_achv_mt_neu",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_7dl_good", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_mt_7dl_neu", {"alt_replay_on" : "True"}),
            "normal"
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_mt_7dl_bad",
            "mt_7dl_bad",
            "sdl_achv_mt_bad",
            [],
            sdl_achv_Replay("alt_day7_mt_7dl_bad", {"alt_replay_on" : "True"}),
            "sad"
        )
    ]
    
    ## Ульяна-7дл
    sdl_achv_array_us_7dl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_us_7dl_true",
            "us_7dl_true",
            "sdl_achv_us_true",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_px_good", "us_px_good", "sdl_achv_us_good", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_7dl_tran_un", "us_7dl_tran_un", "sdl_achv_us_tran_un", None, None),
                        sdl_achv_Achievement("acm_logo_us_7dl_tran_mi", "us_7dl_tran_mi", "sdl_achv_us_tran_mi", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_us_7dl_true", {"alt_replay_on" : "True"}),
            "grin",
            char_mask=5
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_us_7dl_good",
            "us_7dl_good",
            "sdl_achv_us_good",
            [],
            sdl_achv_Replay("alt_day7_us_7dl_good", {"alt_replay_on" : "True"}),
            "laugh2",
            char_mask=5
        ),
        sdl_achv_Achievement(    # Лена-энд
            "acm_logo_us_7dl_tran_un",
            "us_7dl_tran_un",
            "sdl_achv_us_tran_un",
            [],
            sdl_achv_Replay("alt_day7_us_7dl_tran_un", {"alt_replay_on" : "True"}),
            "dontlike",
            char_mask=5
        ),
        sdl_achv_Achievement(    # Мику-энд
            "acm_logo_us_7dl_tran_mi",
            "us_7dl_tran_mi",
            "sdl_achv_us_tran_mi",
            [],
            sdl_achv_Replay("alt_day7_us_7dl_tran_mi", {"alt_replay_on" : "True"}),
            "dontlike",
            char_mask=5
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_us_7dl_bad",
            "us_7dl_bad",
            "sdl_achv_us_bad",
            [],
            sdl_achv_Replay("alt_day7_us_7dl_bad", {"alt_replay_on" : "True"}),
            "sad",
            char_mask=5
        )
    ]
    
    ## Ульяна-Огоньки
    sdl_achv_array_us_pxs = [
        sdl_achv_Achievement(    # Септим
            "acm_logo_us_px_sept",
            "us_px_sept",
            "sdl_achv_us_SE",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_us_px_sept", {"alt_replay_on" : "True"}),
            "normal",
            char_mask=5
        ),
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_us_px_true",
            "us_px_true",
            "sdl_achv_us_true",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_px_good", "us_px_good", "sdl_achv_us_good", None, None)
                    }
                )
            ],
            sdl_achv_Replay("alt_day7_us_px_true", {"alt_replay_on" : "True"}),
            "sad",
            char_mask=5
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_us_px_good",
            "us_px_good",
            "sdl_achv_us_good",
            [],
            sdl_achv_Replay("alt_day7_us_px_good", {"alt_replay_on" : "True"}),
            "laugh2",
            char_mask=5
        )
    ]
    
    ## Одиночка-Сыч
    sdl_achv_array_me_owl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_me_neu_true",
            "me_neu_true",
            "sdl_achv_me_true",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_me_neu_loki_neu", "me_neu_loki_neu", "sdl_achv_me_LO_neu", None, None),
                        sdl_achv_Achievement("acm_logo_me_neu_dr_neu", "me_neu_dr_neu", "sdl_achv_me_DR_neu", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_me_neu_bad", "me_neu_bad", "sdl_achv_me_bad", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_neu_true", {"alt_replay_on" : "True"}),
            char_mask=5
        ),
        sdl_achv_Achievement(    # Локи-Нейтрал
            "acm_logo_me_neu_loki_neu",
            "me_neu_loki_neu",
            "sdl_achv_me_LO_neu",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_me_neu_bad", "me_neu_bad", "sdl_achv_me_bad", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_neu_loki_neu", {"alt_replay_on" : "True"}),
            char_mask=4
        ),
        sdl_achv_Achievement(    # Дрищ-Нейтрал
            "acm_logo_me_neu_dr_neu",
            "me_neu_dr_neu",
            "sdl_achv_me_DR_neu",
            [
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_me_neu_bad", "me_neu_bad", "sdl_achv_me_bad", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_puz",
                    None
                )
            ],
            sdl_achv_Replay("alt_day7_neu_dr_neu", {"alt_replay_on" : "True"}),
            char_mask=1
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_me_neu_bad",
            "me_neu_bad",
            "sdl_achv_me_bad",
            [],
            sdl_achv_Replay("alt_day7_neu_bad", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Разное-Прочее
    sdl_achv_array_va_smt = [
        sdl_achv_Achievement(    # Ламповость
            "acm_logo_va_lamp",
            "alt_lamp",
            "sdl_achv_va_kat",
            [],
            sdl_achv_Replay("alt_day6_un_7dl_letmeout", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Глубина
            "acm_logo_va_deep",
            "alt_deep",
            "sdl_achv_va_kat",
            [],
            sdl_achv_Replay("alt_achv_deep_deep", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # QTE
            "acm_logo_va_qte",
            "alt_qte",
            "sdl_achv_va_qte",
            [],
            None
        ),
        sdl_achv_Achievement(    # QTE victim
            "acm_logo_va_victim",
            "alt_victim",
            "acm_achv_va_victim",
            [],
            None
        )
    ]
    
    
    
    
    
    # Нуарный интерфейс
    sdl_achv_interface_me_noi = sdl_achv_Interface(
        "sdl_achv_screen_noir",
        {
            "mi_active"  : "sdl_achv_mi_button_noir_active",
            "mi_inactive": "sdl_achv_mi_button_noir_inactive",
            "dv_active"  : "sdl_achv_dv_button_noir_active",
            "dv_inactive": "sdl_achv_dv_button_noir_inactive",
            "sl_active"  : "sdl_achv_sl_button_noir_active",
            "sl_inactive": "sdl_achv_sl_button_noir_inactive",
            "un_active"  : "sdl_achv_un_button_noir_active",
            "un_inactive": "sdl_achv_un_button_noir_inactive",
            "mt_active"  : "sdl_achv_mt_button_noir_active",
            "mt_inactive": "sdl_achv_mt_button_noir_inactive",
            "us_active"  : "sdl_achv_us_button_noir_active",
            "us_inactive": "sdl_achv_us_button_noir_inactive",
            "me_active"  : "sdl_achv_me_button_noir_active",
            "me_inactive": "sdl_achv_me_button_noir_inactive",
            "va_active"  : "sdl_achv_va_button_noir_active",
            "va_inactive": "sdl_achv_va_button_noir_inactive"
        },
        "sdl_achv_del_noir_active",
        "sdl_achv_ext_noir_active"
    )
    
    # Руты
    ## Мику
    sdl_achv_route_mi_7dl = sdl_achv_Route("sdl_achv_mi_7dl", "sdl_achv_7dl_route", "sdl_achv_mi_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_mi_7dl, "mi",  "casual")
    sdl_achv_route_mi_clt = sdl_achv_Route("sdl_achv_mi_clt", "sdl_achv_clt_route", "sdl_achv_mi_cl_active",  "sdl_achv_mi_cl_inactive", [],                    "mi",  "dress",      completed=False)
    sdl_achv_route_mi_djt = sdl_achv_Route("sdl_achv_mi_djt", "sdl_achv_xxx_route", "sdl_achv_mi_dj_active",  "sdl_achv_mi_dj_inactive", sdl_achv_array_mi_djt, "mi",  "voca")
    ## Алиса
    sdl_achv_route_dv_7dl = sdl_achv_Route("sdl_achv_dv_7dl", "sdl_achv_7dl_route", "sdl_achv_dv_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_dv_7dl, "dv",  "sport")
    sdl_achv_route_dv_clt = sdl_achv_Route("sdl_achv_dv_clt", "sdl_achv_clt_route", "sdl_achv_dv_cl_active",  "sdl_achv_dv_cl_inactive", [],                    "dv",  "winter",     completed=False)
    sdl_achv_route_dv_djt = sdl_achv_Route("sdl_achv_dv_djt", "sdl_achv_xxx_route", "sdl_achv_dv_dj_active",  "sdl_achv_dv_dj_inactive", [],                    "dv",  "dress",      completed=False)
    ## Славя
    sdl_achv_route_sl_7dl = sdl_achv_Route("sdl_achv_sl_7dl", "sdl_achv_7dl_route", "sdl_achv_sl_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_sl_7dl, "sl",  "casual")
    sdl_achv_route_sl_clt = sdl_achv_Route("sdl_achv_sl_clt", "sdl_achv_clt_route", "sdl_achv_sl_cl_active",  "sdl_achv_sl_cl_inactive", sdl_achv_array_sl_clt, "sl",  "pioneer2")
    sdl_achv_route_sl_wht = sdl_achv_Route("sdl_achv_sl_wht", "sdl_achv_xxx_route", "sdl_achv_sl_wh_active",  "sdl_achv_sl_wh_inactive", [],                    "sl2", "dress",      completed=False)
    ## Лена
    sdl_achv_route_un_7dl = sdl_achv_Route("sdl_achv_un_7dl", "sdl_achv_7dl_route", "sdl_achv_un_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_un_7dl, "un",  "modern")
    sdl_achv_route_un_clt = sdl_achv_Route("sdl_achv_un_clt", "sdl_achv_clt_route", "sdl_achv_un_cl_active",  "sdl_achv_un_cl_inactive", [],                    "un",  "winter",     completed=False)
    sdl_achv_route_un_fzd = sdl_achv_Route("sdl_achv_un_fzd", "sdl_achv_xxx_route", "sdl_achv_un_fz_active",  "sdl_achv_un_fz_inactive", [],                    "un",  "dress",      char_mask=2, completed=False)
    ## Ольга
    sdl_achv_route_mt_7dl = sdl_achv_Route("sdl_achv_mt_7dl", "sdl_achv_7dl_route", "sdl_achv_mt_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_mt_7dl, "mt",  "sport")
    sdl_achv_route_mt_clt = sdl_achv_Route("sdl_achv_mt_clt", "sdl_achv_clt_route", "sdl_achv_mt_cl_active",  "sdl_achv_mt_cl_inactive", [],                    "mt",  "dress",      completed=False)
    ## Ульяна
    sdl_achv_route_us_7dl = sdl_achv_Route("sdl_achv_us_7dl", "sdl_achv_7dl_route", "sdl_achv_us_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_us_7dl, "us",  "dress",      char_mask=5)
    sdl_achv_route_us_pxs = sdl_achv_Route("sdl_achv_us_pxs", "sdl_achv_xxx_route", "sdl_achv_us_px_active",  "sdl_achv_us_px_inactive", sdl_achv_array_us_pxs, "us",  "sport bear", char_mask=5)
    ## Одиночка
    sdl_achv_route_me_d3r = sdl_achv_Route("sdl_achv_me_d3r", "sdl_achv_d3r_route", "sdl_achv_me_d3_active",  "sdl_achv_me_d3_inactive", [],                    None,  None,         completed=False)
    sdl_achv_route_me_owl = sdl_achv_Route("sdl_achv_me_owl", "sdl_achv_7dl_route", "sdl_achv_me_ow_active",  "sdl_achv_me_ow_inactive", sdl_achv_array_me_owl, None,  None)
    sdl_achv_route_me_noi = sdl_achv_Route("sdl_achv_me_noi", "sdl_achv_xxx_route", "sdl_achv_me_no_active",  "sdl_achv_me_no_inactive", [],                    None,  None,         char_mask=2, interface=sdl_achv_interface_me_noi, func_in=noir_interface_on, func_out=noir_interface_off, completed=False)
    ## Разное
    sdl_achv_route_va_smt = sdl_achv_Route("sdl_achv_va_smt", "sdl_achv_smt_route", "sdl_achv_va_sm_active",  "sdl_achv_va_sm_inactive", sdl_achv_array_va_smt, None,  None)
    
    
    
    # Разделы
    sdl_achv_mi_routes = [
        sdl_achv_route_mi_7dl,
        sdl_achv_route_mi_clt,
        sdl_achv_route_mi_djt
    ]
    sdl_achv_dv_routes = [
        sdl_achv_route_dv_7dl,
        sdl_achv_route_dv_clt,
        sdl_achv_route_dv_djt
    ]
    sdl_achv_sl_routes = [
        sdl_achv_route_sl_7dl,
        sdl_achv_route_sl_clt,
        sdl_achv_route_sl_wht
    ]
    sdl_achv_un_routes = [
        sdl_achv_route_un_7dl,
        sdl_achv_route_un_clt,
        sdl_achv_route_un_fzd
    ]
    sdl_achv_mt_routes = [
        sdl_achv_route_mt_7dl,
        sdl_achv_route_mt_clt
    ]
    sdl_achv_us_routes = [
        sdl_achv_route_us_7dl,
        sdl_achv_route_us_pxs
    ]
    sdl_achv_me_routes = [
        sdl_achv_route_me_d3r,
        sdl_achv_route_me_owl,
        sdl_achv_route_me_noi
    ]
    sdl_achv_va_routes = [
        sdl_achv_route_va_smt
    ]
    
    sdl_achv_section_to_routes = {
        "mi": sdl_achv_mi_routes,
        "dv": sdl_achv_dv_routes,
        "sl": sdl_achv_sl_routes,
        "un": sdl_achv_un_routes,
        "mt": sdl_achv_mt_routes,
        "us": sdl_achv_us_routes,
        "me": sdl_achv_me_routes,
        "va": sdl_achv_va_routes
    }
    
    
    
    # Протагонисты
    sdl_achv_characters = [
        sdl_achv_Character("sdl_achv_char_none", 7, None, None),
        sdl_achv_Character("sdl_achv_char_loki", 4, "sdl_achv_char_label_loki", "loki"),
        sdl_achv_Character("sdl_achv_char_herc", 2, "sdl_achv_char_label_herc", "herc"),
        sdl_achv_Character("sdl_achv_char_dr",   1, "sdl_achv_char_label_dr",   "dr")
    ]
