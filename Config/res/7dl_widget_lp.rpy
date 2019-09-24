python early:
    def widget_lp_7dl():
        if (not persistent.lp_widget_7dl) or (plthr == u"None" or plthr == u"Выбор" or plthr == u"Достижения" or plthr == u"Меню"):
            return
        elif plthr == u"Нуар":
            # Нуар
            ui.button(clicked=None, xpos=0.0, xanchor=0.0, ypos=2, xpadding=6, xminimum=220)
            ui.text("%s: %s" % ("Рут", plthr), style="button_text", size=13)
            ui.button(clicked=None, xpos=0.16, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            ui.text("%s" % (save_name), style="button_text", size=13)
            
            ui.button(clicked=None, xpos=0.79, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            ui.text("%s: %d" % ("Патроны", alt_no_ammo), style="button_text", size=13, color="#ffffff")
            ui.button(clicked=None, xpos=0.86, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            ui.text("%s: %d" % ("Оружие", alt_no_weapon), style="button_text", size=13, color="#ffffff")
            ui.button(clicked=None, xpos=0.93, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            ui.text("%s: %d" % ("Зацепки", alt_no_clue), style="button_text", size=13, color="#ffffff")
            ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
            ui.text("%s: %d" % ("Лена", alt_no_un), style="button_text", size=13, color="#ffffff")
        else:
            # Роль
            ui.button(clicked=None, xpos=0.0, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            ui.text("%s: %s" % ("Роль", plthr), style="button_text", size=13)
            
            ui.button(clicked=None, xpos=0.16, xanchor=0.0, ypos=2, xpadding=6, xminimum=200)
            ui.text("%s" % (save_name), style="button_text", size=13)
            
            # Особые поинты
            ui.button(clicked=None, xpos=0.07, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
            if alt_sp > 0:
                ## Карма | Воля (Славя-Классик)
                if karma >= 75:
                    ui.text("%s: %d | %s: %d" % ("Карма", karma, "Воля", alt_sp), style="button_text", size=14, color="#7bacff")
                else:
                    ui.text("%s: %d | %s: %d" % ("Карма", karma, "Воля", alt_sp), style="button_text", size=13)
            elif alt_spt > 0 or alt_hpt > 0:
                ## Princess | Human (Мику-7дл)
                if alt_spt >= 7:
                    ui.text("%s: %d | %s: %d" % ("Princess", alt_spt, "Human", alt_hpt), style="button_text", size=14, color="#ff7bac")
                elif alt_hpt >= 7:
                    ui.text("%s: %d | %s: %d" % ("Human", alt_hpt, "Princess", alt_spt), style="button_text", size=14, color="#ac7bff")
                else:
                    ui.text("%s: %d | %s: %d" % ("Human", alt_hpt, "Princess", alt_spt), style="button_text", size=13)
            elif d3:
                if reput >= 100:
                    ui.text("%s: %d" % ("Репутация", reput), style="button_text", size=14, color="#4BE123")
                elif 75 >= reput >= 50:
                    ui.text("%s: %d" % ("Репутация", reput), style="button_text", size=14, color="#E1D323")
                elif 50 > reput >= 25:
                    ui.text("%s: %d" % ("Репутация", reput), style="button_text", size=13, color="#E17F23")
                else:
                    ui.text("%s: %d" % ("Репутация", reput), style="button_text", size=12, color="#E12334")
            else:
                ## Карма
                if karma >= 75:
                    ui.text("%s: %d" % ("Карма", karma), style="button_text", size=14, color="#7bacff")
                else:
                    ui.text("%s: %d" % ("Карма", karma), style="button_text", size=13)
            
            # ЛП поинты
            if (us_pt > 0) or (mt_pt > 0) or (d3_pt > 0):
                ## Одиночка | Ольга | Ульяна (Одиночка)
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if us_pt < 8:
                    ui.text("%s: %d" % ("Ульяна", us_pt), style="button_text", size=13, color="#f65252")
                else:
                    ui.text("%s: %d" % ("Ульяна", us_pt), style="button_text", size=14, color="#ff3200")
                ui.button(clicked=None, xpos=0.93, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if us_pt < 8:
                    ui.text("%s: %d" % ("Ольга", mt_pt), style="button_text", size=13, color="#f65252")
                else:
                    ui.text("%s: %d" % ("Ольга", mt_pt), style="button_text", size=14, color="#00ea32")
                ui.button(clicked=None, xpos=0.86, xanchor=1.0, ypos=2, xpadding=6, xminimum=140)
                if us_pt < 8:
                    ui.text("%s: %d" % ("Одиночка", d3_pt), style="button_text", size=13, color="#f65252")
                else:
                    ui.text("%s: %d" % ("Одиночка", d3_pt), style="button_text", size=14, color="#e1dd7d")
            else:
                ## Лена | Славя | Алиса | Мику | Ульяна
                ### Ульяна
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                ui.text("%s: %d" % ("Ульяна", lp_us), style="button_text", size=13)
                
                ### Мику
                ui.button(clicked=None, xpos=0.93, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if lp_mi < 13:
                    ui.text("%s: %d" % ("Мику", lp_mi), style="button_text", size=13)
                else:
                    if alt_day3_mi_date and (alt_day2_date == 'mi') and ((alt_day3_dancing == 41) or (alt_day3_dancing == 40)):
                        if (alt_spt >= 8) or ((alt_hpt >= 9) and (lp_mi > 16)):
                            ui.text("%s: %d" % ("Мику-7ДЛ", lp_mi), style="button_text", size=15, color="#00ffff")
                        else:
                            ui.text("%s: %d" % ("Мику-7ДЛ", lp_mi), style="button_text", size=14, color="#00bbbb")
                    elif (lp_mi >= 13) and alt_day3_mi_dj:
                        if (lp_mi >= 13) and alt_day3_mi_dj and (alt_day6_mi_dj_hentai2 or alt_day6_mi_dj_no_hentai):
                            ui.text("%s: %d" % ("Мику-DJ", lp_mi), style="button_text", size=15, color="#00ffff")
                        else:
                            ui.text("%s: %d" % ("Мику-DJ", lp_mi), style="button_text", size=14, color="#00bbbb")
                    else:
                        ui.text("%s: %d" % ("Мику", lp_mi), style="button_text", size=14)
                
                ### Алиса
                ui.button(clicked=None, xpos=0.86, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if lp_dv >=11:
                    if lp_dv < 18:
                        ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text", size=14, color="#bb8800")
                    else:
                        ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text", size=15, color="#ffaa00")
                else:
                    ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text", size=13)
                
                ### Славя
                ui.button(clicked=None, xpos=0.79, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if (lp_sl < 13) and (counter_sl_cl < 7) and (counter_sl_7dl < 5):
                    ui.text("%s: %d" % ("Славя", lp_sl), style="button_text", size=13)
                else:
                    if counter_sl_cl == 7:
                        if ((lp_sl >= 20) or (alt_sp >= 6)) or ((lp_sl >=20) and (alt_day6_sl_arc == 1)):
                            ui.text("%s: %d" % ("Славя-КЛ", lp_sl), style="button_text", size=15, color="#ffaa00")
                        else:
                            ui.text("%s: %d" % ("Славя-КЛ", lp_sl), style="button_text", size=14, color="#bbb200")
                    elif counter_sl_7dl == 5:
                        if (lp_sl >= 20) and (karma > 120):
                            ui.text("%s: %d" % ("Славя-7ДЛ", lp_sl), style="button_text", size=15, color="#ffaa00")
                        elif (lp_sl >= 20):
                            ui.text("%s: %d" % ("Славя-7ДЛ", lp_sl), style="button_text", size=15, color="#bbb200")
                        else:
                            ui.text("%s: %d" % ("Славя-7ДЛ", lp_sl), style="button_text", size=14, color="#bbb200")
                    else:
                        ui.text("%s: %d" % ("Славя", lp_sl), style="button_text", size=14)
                
                ### Лена
                ui.button(clicked=None, xpos=0.72, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if lp_un >= 12:
                    if lp_un < 20:
                        ui.text("%s: %d" % ("Лена", lp_un), style="button_text", size=14, color="#9f72be")
                    else:
                        ui.text("%s: %d" % ("Лена", lp_un), style="button_text", size=15, color="#d599ff")
                else:
                    ui.text("%s: %d" % ("Лена", lp_un), style="button_text", size=13)
        
    config.overlay_functions.append(widget_lp_7dl)
