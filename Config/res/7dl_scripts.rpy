init:
    $ style.alt_days = Style(style.default)
    $ style.alt_days.color = "#390874"
    $ style.alt_days.italic = False
    $ style.alt_days.bold = True
    $ style.alt_days.size = 64
    $ style.alt_days.text_align = 0.5

    $ style.alt_days_noir = Style(style.default)
    $ style.alt_days_noir.font = get_image_7dl("fonts/PT_Sans.ttf")
    $ style.alt_days_noir.color = "#efefef"
    $ style.alt_days_noir.italic = False
    $ style.alt_days_noir.bold = True
    $ style.alt_days_noir.size = 75
    $ style.alt_days_noir.text_align = 0.5
    
    $ style.alt_chapters = Style(style.default)
    $ style.alt_chapters.color = "#2572ff"
    $ style.alt_chapters.italic = False
    $ style.alt_chapters.bold = True
    $ style.alt_chapters.size = 48
    $ style.alt_chapters.text_align = 0.5
    
    $ style.alt_chapters_noir = Style(style.default)
    $ style.alt_chapters_noir.font = get_image_7dl("fonts/PT_Sans.ttf")
    $ style.alt_chapters_noir.color = "#121212"
    $ style.alt_chapters_noir.italic = False
    $ style.alt_chapters_noir.bold = True
    $ style.alt_chapters_noir.size = 90
    $ style.alt_chapters_noir.text_align = 0.5
    
    $ style.alt_credits = Style(style.default)
    $ style.alt_credits.color = "#EFF"
    $ style.alt_credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.alt_credits.drop_shadow_color = "#111"
    $ style.alt_credits.italic = False
    $ style.alt_credits.bold = False
    $ style.alt_credits.text_align = 0.5
    image alt_credits = ParameterizedText(style = "alt_credits", size = 50)
    
    $ style.alt_letter = Style(style.default)
    $ style.alt_letter.color = "#00ffff"
    $ style.alt_letter.drop_shadow = [ (-1, 0), (0, 0), (-1, 1), (0, 1) ]
    $ style.alt_letter.drop_shadow_color = "#0ff"
    $ style.alt_letter.italic = True
    $ style.alt_letter.bold = False
    
    image alt_letter = ParameterizedText(style = "alt_letter", size = 70)

    if renpy.mobile:
        $ style.base_font = Style(style.default)
        $ style.base_font.font  = get_image_7dl("fonts/calibri.ttf")
        $ style.base_font.size = 28
        $ style.base_font.line_spacing = 2
        
        $ style.chapter = Style(style.base_font)
        $ style.chapter.font  = get_image_7dl("fonts/corbel.ttf")
        $ style.chapter.size = 120
        $ style.chapter.color = "#fff"
        $ style.chapter.outlines = [ (1, "#ffdd7d", 0, 0) ]
        
        $ style.daynum = Style(style.chapter)
        $ style.daynum.font  = get_image_7dl("fonts/corbel.ttf")
        $ style.daynum.size = 45

init -66 python:
    import random
    
    class alt_CardGameRival:
        
        def __init__(self,avatar,name):
            self.name = name
            self.mood = 0
            self.avatar = avatar
        
        def pick_my_card_last(self):
            for i in range(0,n_cards):
                if  cards_my[i].interesting:
                    x = i
            return x
        
        def allow_to_take(self):
            for i in range(0,n_cards):
                cards_rival[i].allow = True
        
        def allow_to_defend(self):
            return True
        
        def want_to_defend(self):
            return True
        
        def what_to_xchange(self):
            i = random.randrange(0,n_cards)
            j = random.randrange(0,n_cards)
            while i==j:
                j = random.randrange(0,n_cards)
            return (i,j)
        
        def give_away_card(self):
            return random.randrange(0,n_cards)
    
    class CardGameRivalSl(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()
    
    class CardGameRivalSh(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()
    
    class CardGameRivalMz(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()
    
    class CardGameRivalMi(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()

init -10 python:
    p = get_image_7dl("gui/avaset/sh/sh-")
    sh_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo6.png",
            }
    
    p = get_image_7dl("gui/avaset/mi/mi-")
    mi_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo5.png",
            }
    
    p = get_image_7dl("gui/avaset/mz/mz-")
    mz_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo6.png",
            }

init 3 python:
    def meet(who, name):
        global store
        gl = globals()
        gl[who + "_name"] = name
        store.names[who] = name

    def save_names_known():
        gl = globals()
        global store
        for x in store.names_list:
            if not (x == 'narrator' or x == 'th'):
                store.names[x] = gl["%s_name"%x]

    def make_names_unknown_7dl():
        global store
        meet('al',u"Сердитый мальчик")
        meet('ase',u"Девочка")
        meet('ba',u"Физрук")
        meet('bb',u"Начальник лагеря")
        meet('cs',u"Медсестра")
        meet('dn',u"Кудрявый")
        meet('dreamgirl',u"…")
        meet('dv',u"Рыжая")
        meet('el',u"Кудрявый")
        meet('ka',u"Вожатая 2 отряда")
        meet('ln',u"Странная девочка")
        meet('me',u"Семён")
        meet('mi',u"Японка")
        meet('mt',u"Вожатая")
        meet('mz',u"Девушка в очках")
        meet('pi',u"Пионер")
        meet('sak',u"Пожилой японец")
        meet('sh',u"Очкарик")
        meet('sl',u"Блондинка")
        meet('tn',u"Странный мальчик")
        meet('un',u"Грустная девочка")
        meet('us',u"Мелкая")
        meet('uv',u"Кошкодевочка")
        meet('voice',u"Голос")

    def make_names_known_7dl():
        global store
        meet('al',u"Алька")
        meet('ase',u"Алиса")
        meet('ba',u"Саныч")
        meet('bb',u"Алексей Максимыч")
        meet('cs',u"Виола")
        meet('dn',u"Даня")
        meet('dv',u"Алиса")
        meet('el',u"Электроник")
        meet('ka',u"Катюшка")
        meet('ln',u"Алёна")
        meet('mi',u"Мику")
        meet('mt',u"Ольга Дмитриевна")
        meet('mz',u"Женя")
        meet('sak',u"Сакишита Чихиро")
        meet('sh',u"Шурик")
        meet('sl',u"Славя")
        meet('tn',u"Тоник")
        meet('un',u"Лена")
        meet('us',u"Ульяна")
        meet('uv',u"Юля")

    def reset_names_to_default():
        global store
        store.names['voice'] = translation_new["voice"]
        store.names['me'] = translation_new["Semyon"]
        store.names['el'] = translation_new["el"]
        store.names['un'] = translation_new["un"]
        store.names['dv'] = translation_new["dv"]
        store.names['sl'] = translation_new["sl"]
        store.names['us'] = translation_new["us"]
        store.names['mt'] = translation_new["mt"]
        store.names['cs'] = translation_new["cs"]
        store.names['mz'] = translation_new["mz"]
        store.names['mi'] = translation_new["mi"]
        store.names['uv'] = translation_new["uv"]
        store.names['sh'] = translation_new["sh"]
        store.names['pi'] = translation_new["pi"]
        store.names['dreamgirl'] = translation_new["dreamgirl"]

init -265 python: 
    #Пресеты с возможностью настройки
    def Noir(id, brightness = -0.4, tint_r = 0.2126, tint_g = 0.7152, tint_b = 0.0722, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) * im.matrix.tint(tint_r, tint_g, tint_b) * im.matrix.saturation(saturation))
    def D3_intro(id, brightness = -0.2, opacity = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.opacity(opacity))
    def Desat(id, brightness = -0.35, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.saturation(saturation))
    def Desat1(id, brightness = -0.4, saturation = 0.35):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.saturation(saturation))
        
    #Пресеты без возможности настройки
    #Мику-матрица
    def SS_com(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#0aa", "#000"))
    #Алиса-матрица
    def SS_com_o(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#eb4", "#000"))
    #Ульяна-матрица
    def SS_com_r(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#a00", "#000"))
    
    def Sepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))
    
    def Grayed(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.01))
    def Gjs(id):
        return im.MatrixColor(ImageReference(id), im.matrix.colorize("#007", "#000"))
    
    #Тинты для разного времени суток
    def Notch(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.saturation(0.6))
    def Dawn(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.94, 0.82, 1.0))
    def Noon(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(0.2) * im.matrix.tint(1.0, 0.94, 0.82))
    def HomeCity(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.82, 0.84, 1.0))
    def Rained(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.4) * im.matrix.tint(0.68, 0.90, 0.8) * im.matrix.saturation(0.6))

    def filmetile(bitmap, opacity=0.1):
        return im.Tile(im.Alpha(bitmap,opacity))

init -6 python:
    def alt_chapter0():
        global save_name
        save_name = (u"7ДЛ v.%s.%s: пролог. %s") % (alt_release_no, alt_hotfix_no, plthr)

init -5 python:
    def alt_chapter(alt_day_number, alt_chapter_name):
        global save_name
        renpy.block_rollback()
# ----------------------------------------------------------------------
# в имя сохраняемого файла добавим номер релиза игры
        sdn = (u"7ДЛ v.%s.%s: День %d") % (alt_release_no, alt_hotfix_no, alt_day_number)
        save_name = ((sdn) + (u" - ")) + (alt_chapter_name)
# -----------------------------------------------------------------------
        if not persistent.chapter_off_7dl:
            renpy.scene()
            if alt_d3_bad_0:
                if not persistent.d3_bad and not persistent.d3_fag and not persistent.d3_falsch:
                    renpy.show('bg ext_busstop_sun_7dl')
                elif persistent.d3_bad:
                    renpy.show('bg ext_busstop_dust_7dl')
                else:
                    renpy.show('noir_busstop_dust_7dl')
            elif persistent.sprite_time == "day":
                renpy.show('bg ext_stand3_7dl')
            elif persistent.sprite_time == "sunset":
                renpy.show('bg ext_stand3_sunset_7dl')
            elif persistent.sprite_time == "night":
                renpy.show('bg ext_stand3_night_7dl')
            elif persistent.sprite_time == "prolog":
                renpy.show('bg ext_stand3_prolog_7dl')
            #заготовка для Нуара
            elif persistent.sprite_time == "noir":
                renpy.show('anim_noir')
            renpy.pause(1.0)
            renpy.transition(dissolve)
            
            if routetag == "dv": #Классическая и диджей ветка гуд
                renpy.show("dv normal pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
            elif routetag == "dvbad": #Классическая ветка, бэд, диджей ветка дисмисс
                renpy.show("dv sad pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
               
            elif routetag == "dv7dl": #7дл-ветка, гуд
                renpy.show("dv normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "dv7dlbad": #7дл-ветка, реджект/дисмисс
                renpy.show("dv guilty pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "dv7dlgood": #7дл-ветка, гуд
                renpy.show("dv smile pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "dv7dldress": #7дл-ветка, гуд
                renpy.show("dv smile dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                

            elif routetag == "mi7dl": #7дл-ветка, диджей гуд
                renpy.show("mi normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7": #Мику-коммон
                renpy.show("mi sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlbad": #7дл-ветка, реджект, диджей нейтрал
                renpy.show("mi cry pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlgood": #7дл-ветка, реджект, диджей нейтрал
                renpy.show("mi happy pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dldress":
                renpy.show("mi normal dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7rej": #7дл-ветка, реджект, диджей бэд
                renpy.show("mi serious pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7true": #7дл-ветка, реджект, диджей бэд
                renpy.show("mi shy pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlvoca":
                renpy.show("mi shy voca", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas":
                renpy.show("mi happy casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas1":
                renpy.show("mi sad casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas2":
                renpy.show("mi cry casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlvoca1":
                renpy.show("mi sad voca", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "sl": #Классическая ветка, нормал
                renpy.show("sl normal pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sltrue": #Классик, тру
                renpy.show("sl shy sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "slcas": #Классическая ветка гуд
                renpy.show("sl smile casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "slbad": #Классическая ветка, бэд
                renpy.show("sl sad pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
            
            elif routetag == "sl7dl": #Ветка 7дл, базис
                renpy.show("sl normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_herc": #Ветка 7дл, Герк
                renpy.show("sl smile pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_loki": #Ветка 7дл, Локи
                renpy.show("sl smile2 pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "sl7dl_sport": #Ветка 7дл, спортивная
                renpy.show("sl smile sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_dress": #Ветка 7дл, платье
                renpy.show("sl smile2 dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            
            elif routetag == "sl7dltrue": #Ветка 7дл, тру
                renpy.show("sl_gr normal casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlneu": #Ветка 7дл, тру
                renpy.show("sl serious casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlgood": #Ветка 7дл, тру
                renpy.show("sl happy casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dluv": #Ветка 7дл, тру
                renpy.show("sl normal_uv dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlbad": #Ветка 7дл, тру
                renpy.show("sl cry pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            
            elif routetag == "un": #Классическая
                renpy.show("un normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
            elif routetag == "unbad": #Классическая ветка, бэд
                renpy.show("un sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
                
            elif routetag == "un7dl": #7дл-ветка, гуд
                renpy.show("un normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            #Флаг для плохого эпилога Лены
            elif routetag == "un7dlbad": #7дл-ветка, реджект/бэд
                renpy.show("un sorrow modern", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "un7dlwinter": #Леночка в пуховике
                renpy.show("un smile winter", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "un7dlgood": #7дл-ветка, реджект/бэд
                renpy.show("un smile modern", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
                
            elif routetag == "mt7dl": #Ольга - общая
                renpy.show("mt grin pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mt7dluni": #Ольга - общая
                renpy.show("mt smile uniform", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mt7dl_bad": #Ольга - плохая концовка
                renpy.show("mt sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_good":
                renpy.show("us smile sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_good_surp":
                renpy.show("us surp1 sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_bad":
                renpy.show("us normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "us7dlbear":
                renpy.show("show us laugh2 sport bear", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_bad_laugh":
                renpy.show("us laugh pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_bad_sad":
                renpy.show("us sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "uv_unknown": #Кошочку еще не знаем
                renpy.show("uv shade", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv": #Кошонка-распашонка
                renpy.show("uv normal", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv_true": #Кошочка поражена до самой глыбины своих глыбин
                renpy.show("uv surprise", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv_false": #Кошонка на позитиве
                renpy.show("uv grin", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv_bad": #Виноватая кошонка
                renpy.show("uv guilty", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "Noir":
                renpy.pause(0.3)
            elif alt_d3_bad_0:
                renpy.pause(0.3)
            else:
                renpy.show("owl")
                renpy.pause(0.3)
            if alt_d3_bad_0:
                dn = (u"7ДЛ. Септим:")
                if persistent.d3_bad:
                    dn2 = ("СПАСИТЕЛЬ")
                elif persistent.d3_fag:
                    dn2 = ("ПОМНЯЩИЙ")
                else:
                    dn2 = ("НАБЛЮДАТЕЛЬ")
                renpy.show('day_num', what=Text(dn, style=style.alt_days_noir,xcenter=0.5215,ycenter=0.35))
                renpy.show('day_text1', what=Text(dn2, style=style.alt_days_noir,xcenter=0.5215,ycenter=0.45))
                renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_days_noir,xcenter=0.5215,ycenter=0.65))
            else:
                dn = (u"7ДЛ: День %d") % (alt_day_number)
                if persistent.sprite_time == "prolog":
                    renpy.show('day_num', what=Text(dn, style=style.alt_days,xcenter=0.5215,ycenter=0.25))
                    renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters,xcenter=0.5215,ycenter=0.35))
                elif persistent.sprite_time == "noir":
                    renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters_noir,xcenter=0.5215,ycenter=0.35))
                else:
                    renpy.show('day_num', what=Text(dn, style=style.alt_days,xcenter=0.5215,ycenter=0.35))
                    renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters,xcenter=0.5215,ycenter=0.45))
        
            renpy.pause(3)
            renpy.scene()
            renpy.show('bg black')
            renpy.transition(blind_r)
            if noir_interface:
                noir_set_mode_adv()
            else:
                set_mode_adv()

    if persistent.altCardsDemo == None:
        persistent.altCardsDemo = False

    if persistent.altCardsFail == None:
        persistent.altCardsFail = False

    if persistent.altCardsWon1 == None:
        persistent.altCardsWon1 = False

    if persistent.altCardsWon2 == None:
        persistent.altCardsWon2 = False

    if persistent.altCardsWon3 == None:
        persistent.altCardsWon3 = False
        
    if persistent.altCardsWon4 == None:
        persistent.altCardsWon4 = False
    
    
    # Функция для дрожания огонька спички в котокомбах
    def random_zoom(trans, st, at):
        if st < 1.0: # 1 sec random zooming each 0.1 sec
            trans.zoom = 1.0 + renpy.random.random() * 0.5 
            return 0.1
        trans.zoom = 1.0
        return None

init 52 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["chibi"] = None

init -1001 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["map_chibi_7dl"] = None

init -1000 python:
    nonsteam_7dl = True
    default_7dl_path = 'mods/scenario_alt/' if nonsteam_7dl else 'scenario_alt/'

    # для совместимости с одной из ранних сборок на RenPy 7.0.0
    if not 'translation_new' in globals():
        translation_new = translation

init -999 python:
    def get_image_7dl(file):
        return default_7dl_path+"Pics/%s" % (file)

init -997 python:
    def get_sprite_7dl(file):
        return default_7dl_path+"Pics/sprites/%s" % (file)
    def get_sprite_ori(file):
        return get_image("sprites/%s") % (file)
    
    store.map_chibi_7dl = {
            "?" : get_image_7dl("gui/maps/map_icon_n00.png"),
            "me": get_image_7dl("gui/maps/map_icon_n01.png"),
            "mi": get_image_7dl("gui/maps/map_icon_n02.png"),
            "sh": get_image_7dl("gui/maps/map_icon_n03.png"),
            "el": get_image_7dl("gui/maps/map_icon_n04.png"),
            "mz": get_image_7dl("gui/maps/map_icon_n05.png"),
            "mt": get_image_7dl("gui/maps/map_icon_n06.png"),
            "uv": get_image_7dl("gui/maps/map_icon_n07.png"),
            "un": get_image_7dl("gui/maps/map_icon_n08.png"),
            "us": get_image_7dl("gui/maps/map_icon_n09.png"),
            "dv": get_image_7dl("gui/maps/map_icon_n10.png"),
            "sl": get_image_7dl("gui/maps/map_icon_n11.png"),
            "cs": get_image_7dl("gui/maps/map_icon_n12.png"),
        }

init python:

    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer… turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)

# Боремся с трейсбеками из-за ПЛ
init 9999 python:
    try:
        del(max)
    except NameError:
        pass
# Кастомные менюшки
init python:
    def alt_screens_save():
        renpy.display.screen.screens[("original_game_menu_selector", None)] =         renpy.display.screen.screens[("game_menu_selector", None)]

    alt_screens_save()
    
    def alt_screens_on():
        renpy.display.screen.screens[("game_menu_selector", None)] =                  renpy.display.screen.screens[("alt_game_menu_selector", None)]

    def alt_screens_load():
        renpy.display.screen.screens[("game_menu_selector", None)] =                  renpy.display.screen.screens[("original_game_menu_selector", None)]

    orig_config_version = config.version
        
    def alt_interface_on():
        # пишем версию 7дл в трейсбеках
        global alt_release_no
        global alt_hotfix_no
        if not "7DL" in config.version:
            config.version = config.version + " + 7DL v.%s.%s" % (alt_release_no, alt_hotfix_no)
        alt_screens_on()
        persistent.alt_interface = True

    def alt_interface_off():
        global orig_config_version
        config.version = orig_config_version
        alt_screens_load()
        plthr = u"None"
        persistent.alt_interface = False
        
    def alt_exit():
        global th_prefix
        global th_suffix
        alt_interface_off()
        reset_names_to_default()
        reload_names()
        th_prefix = "~ "
        th_suffix = " ~"

screen alt_game_menu_selector:
    tag menu
    modal True
    $ timeofday = persistent.timeofday
    button:
        style "blank_button"
        xpos 0
        ypos 0
        xfill True
        yfill True
        action Return()
    add get_image("gui/ingame_menu/"+timeofday+"/ingame_menu.png"):
        xalign 0.5
        yalign 0.5
    imagemap:
        if _preferences.language == "spanish":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_es_%s.png")
            xalign 0.5
            yalign 0.5
        elif _preferences.language == "italian":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_it_%s.png")
            xalign 0.5
            yalign 0.5
        elif _preferences.language == "english":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_en_%s.png")
            xalign 0.5
            yalign 0.5
        elif _preferences.language == "chinese":
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_ch_%s.png")
            xalign 0.5
            yalign 0.5
        else:
            auto get_image("gui/ingame_menu/"+timeofday+"/ingame_menu_%s.png")
            xalign 0.5
            yalign 0.5
        hotspot (0, 83, 660, 65):
            focus_mask None
            clicked [Function(alt_exit), MainMenu()]
        hotspot (0, 148, 660, 65):
            focus_mask None
            clicked ShowMenu('save')
        hotspot (0, 213, 660, 65):
            focus_mask None
            clicked ShowMenu('load')
        hotspot (0, 278, 660, 65):
            focus_mask None
            clicked (ShowMenu('alt_preferences'), Hide('alt_game_menu_selector'))
        hotspot (0, 343, 660, 65):
            focus_mask None
            clicked ShowMenu('quit')
    
screen alt_preferences:
    tag menu
    modal True
    $ translate()
    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),36,36)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),36,36)
    window:
        background get_image("gui/settings/preferences_bg.jpg")
        textbutton translation_new["SAVE"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.02
            yalign 0.08
            action ShowMenu('save')
        textbutton translation_new["LOAD"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.98
            yalign 0.08
            action ShowMenu('load')
        hbox:
            xalign 0.5
            yalign 0.08
            add get_image("gui/settings/star.png"):
                yalign 0.65
            text " "+translation_new["settings"]+" ":
                style "settings_link"
                yalign 0.5
                color "#ffffff"
            add get_image("gui/settings/star.png"):
                yalign 0.65
        textbutton translation_new["Back"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.015
            yalign 0.92
            action Return()
        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport:
                id "preferences"
                mousewheel True
                scrollbars None
                grid 1 20:
                    xfill True
                    spacing 15
                    text translation_new["Window_mode"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.fullscreen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Fullscreen"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("display", "fullscreen")
                        hbox:
                            xalign 0.5
                            if not _preferences.fullscreen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Window"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("display", "window")
                    text translation_new["Skip"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.skip_unseen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Skip_all"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("skip", "all")
                        hbox:
                            xalign 0.5
                            if not _preferences.skip_unseen:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Skip_seen"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("skip", "seen")
                    text translation_new["Volume"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Music_lower"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("music volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Sound"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("sound volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    grid 2 1:
                        xfill True
                        textbutton translation_new["Ambience"]:
                            style "log_button"
                            text_style "settings_text"
                            action Play("sound", "sound/test.ogg")
                            xpos 0.1
                        bar:
                            value Preference("voice volume")
                            left_bar bar_full
                            right_bar bar_null
                            thumb "images/gui/settings/htumb.png"
                            hover_thumb "images/gui/settings/htumb.png"
                            xmaximum 1.35
                            ymaximum 36
                            xpos -0.55
                    text translation_new["Text_speed"]:
                        style "settings_header"
                        xalign 0.5
                    bar:
                        value Preference("text speed")
                        left_bar bar_full
                        right_bar bar_null
                        thumb "images/gui/settings/htumb.png"
                        hover_thumb "images/gui/settings/htumb.png"
                        xalign 0.5
                        xmaximum 0.8
                        ymaximum 36
                    text translation_new["Autoforward"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if _preferences.afm_time != 0:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Adult_content_on"]:
                                style "log_button"
                                text_style "settings_text"
                                action Preference("auto-forward after click", "enable")
                        hbox:
                            xalign 0.5
                            if _preferences.afm_time == 0:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Adult_content_off"]:
                                style "log_button"
                                text_style "settings_text"
                                action (Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"))
                    text translation_new["Autoforward_time"]:
                        style "settings_header"
                        xalign 0.5
                    bar:
                        value Preference("auto-forward time")
                        left_bar bar_full
                        right_bar bar_null
                        thumb "images/gui/settings/htumb.png"
                        hover_thumb "images/gui/settings/htumb.png"
                        xalign 0.5
                        xmaximum 0.8
                        ymaximum 36
                    text translation_new["Font"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if persistent.font_size == "small":
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Normal_font"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "font_size", "small")
                        hbox:
                            xalign 0.5
                            if not persistent.font_size == "small":
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Big_font"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "font_size", "large")
                    textbutton translation_new["Language"]:
                        style "log_button"
                        text_style "settings_text"
                        text_size 50
                        xalign 0.5
                        action ShowMenu("language_menu")
                    text translation_new["show_achievments"]:
                        style "settings_header"
                        xalign 0.5
                    grid 2 1:
                        xfill True
                        hbox:
                            xalign 0.5
                            if persistent.show_achievements:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["Yes"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "show_achievements", True)
                        hbox:
                            xalign 0.5
                            if not persistent.show_achievements:
                                add get_image("gui/settings/leaf.png"):
                                    ypos 0.12
                            else:
                                null:
                                    width 22
                            textbutton translation_new["No"]:
                                style "log_button"
                                text_style "settings_text"
                                action SetField(persistent, "show_achievements", False)
                    null
            bar:
                value XScrollValue("preferences")
                left_bar "images/misc/none.png"
                right_bar "images/misc/none.png"
                thumb "images/misc/none.png"
                hover_thumb "images/misc/none.png"
            vbar:
                value YScrollValue("preferences")
                bottom_bar "images/misc/none.png"
                top_bar "images/misc/none.png"
                thumb "images/gui/settings/vthumb.png"
                thumb_offset -12

init 1: # массовые переименования персистентов
    if not persistent.not_first_start_7dl:
        $ persistent.not_first_start_7dl = True
        if persistent.dv_7dl_good_ussr_rf:
            $ persistent.dv_7dl_good_rf = True
        if persistent.un_7dl_true:
            $ persistent.un_7dl_rej = True
            $ persistent.un_7dl_true = False
    
    if not persistent.not_first_start2_7dl:
        $ persistent.not_first_start2_7dl = True
        if persistent.mi_7dl_ps:
            $ persistent.mi_7dl_sept = persistent.mi_7dl_ps
            $ persistent.mi_7dl_ps = False
        if persistent.mi_7dl_neutral_human:
            $ persistent.mi_7dl_neu_human = persistent.mi_7dl_neutral_human
            $ persistent.mi_7dl_neutral_human = False
        if persistent.mi_7dl_neutral_star:
            $ persistent.mi_7dl_neu_star = persistent.mi_7dl_neutral_star
            $ persistent.mi_7dl_neutral_star = False
        if persistent.dv_7dl_true:
            $ persistent.dv_7dl_sept = persistent.dv_7dl_true
            $ persistent.dv_7dl_true = False
        if persistent.dv_7dl_reject_ussr:
            $ persistent.dv_7dl_rej_ussr = persistent.dv_7dl_reject_ussr
            $ persistent.dv_7dl_reject_ussr = False
        if persistent.dv_7dl_reject_rf:
            $ persistent.dv_7dl_rej_rf = persistent.dv_7dl_reject_rf
            $ persistent.dv_7dl_reject_rf = False
        if persistent.dv_7dl_bad_mt:
            $ persistent.dv_7dl_tran_mt = persistent.dv_7dl_bad_mt
            $ persistent.dv_7dl_bad_mt = False
        if persistent.dv_7dl_un:
            $ persistent.dv_7dl_tran_un = persistent.dv_7dl_un
            $ persistent.dv_7dl_un = False
        if persistent.dv_7dl_tulpa:
            $ persistent.dv_7dl_loki_exc = persistent.dv_7dl_tulpa
            $ persistent.dv_7dl_tulpa = False
        if persistent.sl_7dl_true:
            $ persistent.sl_7dl_sept = persistent.sl_7dl_true
            $ persistent.sl_7dl_true = False
        if persistent.sl_7dl_herc_good:
            $ persistent.sl_7dl_herc_neu = persistent.sl_7dl_herc_good
            $ persistent.sl_7dl_herc_good = False
        if persistent.sl_7dl_herc_good2:
            $ persistent.sl_7dl_herc_good = persistent.sl_7dl_herc_good2
            $ persistent.sl_7dl_herc_good2 = False
        if persistent.sl_7dl_good:
            $ persistent.sl_7dl_dr_good = persistent.sl_7dl_good
            $ persistent.sl_7dl_good = False
        if persistent.sl_7dl_good2:
            $ persistent.sl_7dl_dr_good2 = persistent.sl_7dl_good2
            $ persistent.sl_7dl_good2 = False
        if persistent.sl_cl_int_ok:
            $ persistent.sl_cl_int_true = persistent.sl_cl_int_ok
            $ persistent.sl_cl_int_ok = False
        if persistent.sl_cl_reject_same:
            $ persistent.sl_cl_rej_rf = persistent.sl_cl_reject_same
            $ persistent.sl_cl_reject_same = False
        if persistent.sl_cl_reject_late:
            $ persistent.sl_cl_rej = persistent.sl_cl_reject_late
            $ persistent.sl_cl_reject_late = False
        if persistent.sl_cl_cata:
            $ persistent.sl_cl_loki_exc = persistent.sl_cl_cata
            $ persistent.sl_cl_cata = False
        if persistent.un_7dl_true:
            $ persistent.un_7dl_sept = persistent.un_7dl_true
            $ persistent.un_7dl_true = False
        if persistent.un_7dl_true_transit:
            $ persistent.un_7dl_true_tran = persistent.un_7dl_true_transit
            $ persistent.un_7dl_true_transit = False
        if persistent.mt_7dl_neutral:
            $ persistent.mt_7dl_neu = persistent.mt_7dl_neutral
            $ persistent.mt_7dl_neutral = False
        if persistent.us_7dl_un:
            $ persistent.us_7dl_tran_un = persistent.us_7dl_un
            $ persistent.us_7dl_un = False
        if persistent.us_7dl_mi:
            $ persistent.us_7dl_tran_mi = persistent.us_7dl_mi
            $ persistent.us_7dl_mi = False
        if persistent.us_px_true:
            $ persistent.us_px_sept = persistent.us_px_true
            $ persistent.us_px_true = False
        if persistent.us_px_rf_good:
            $ persistent.us_px_good = persistent.us_px_rf_good
            $ persistent.us_px_rf_good = False
        if persistent.neu_true:
            $ persistent.me_neu_true = persistent.neu_true
            $ persistent.neu_true = False
        if persistent.neu_loki_neu:
            $ persistent.me_neu_loki_neu = persistent.neu_loki_neu
            $ persistent.neu_loki_neu = False
        if persistent.neu_neu:
            $ persistent.me_neu_dr_neu = persistent.neu_neu
            $ persistent.neu_neu = False
        if persistent.neu_bad:
            $ persistent.me_neu_bad = persistent.neu_bad
            $ persistent.neu_bad = False
