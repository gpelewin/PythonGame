import pygame   #Импорт библиотеки pygame

clock = pygame.time.Clock() #инициализируем внутри игровое время, от него зависит частота кадров

pygame.init()   #Инициализируем pygame

screen = pygame.display.set_mode((1920, 1080))  #Устанавливаем нужное разрешение экрана
pygame.display.set_caption("I am Survivor!") #Название игры на панели окна



"""????????????????   ПОДГРУЗКА ИЗОБРАЖЕНИЙ   ?????????????????????? """
#icon = pygame.image.load('')   #Подгружаем изображение для иконки игры
#pygame.display.set_icon()      #Устанавливаем его

#Карты
bg1 = pygame.image.load('stuff/img/map1_1.png') #Подгрузка 1й карты
bg2= pygame.image.load('stuff/img/map2_1.png')  #Подгрузка 2й карты
bg3 = pygame.image.load('stuff/img/map4.png')   #Подгрузка 3й карты
bg = bg1 #По умолчанию выбрана 1я карта

#Player
walk_left = [       #массив с анимацией героя влево
    pygame.image.load('stuff/img/left_1.png'),  #1й кадр
    pygame.image.load('stuff/img/left_2.png'),  #2й кадр
    pygame.image.load('stuff/img/left_3.png'),  #3й кадр
    pygame.image.load('stuff/img/left_1.png')   #4й кадр
]

walk_right = [      #массив с анимацией героя вправо
    pygame.image.load('stuff/img/right_1.png'), #1й кадр
    pygame.image.load('stuff/img/right_2.png'), #2й кадр
    pygame.image.load('stuff/img/right_3.png'), #3й кадр
    pygame.image.load('stuff/img/right_1.png')  #4й кадр
]

#ХП
hp = [      #массив с анимацией ХП
    pygame.image.load('stuff/img/hp_full.png'), #полное здоровье кадр
    pygame.image.load('stuff/img/hp_2.png'),    #2 сердечка кадр
    pygame.image.load('stuff/img/hp_1.png')     #1 сердечко кадр
]

#Получение урона
player_have_damage2 = pygame.image.load('stuff/img/player_damage1.png') #картинка игрока получившего урон, смотрящего влево
player_have_damage1 = pygame.image.load('stuff/img/player_damage2.png') #картинка игрока получившего урон, смотрящего вправо

#Враги(призрак)
ghost=pygame.image.load('stuff/img/ghost.png') #подгружаем призраков
ghost_list_in_game = [] #массив в котором будут хранится ректы(невидимые квадратики) призраков
"""????????????????   ПОДГРУЗКА ИЗОБРАЖЕНИЙ   ?????????????????????? """

#platform = pygame.image.load('stuff/img/platform.png') #подгружаем платформы - не используются
#platform_list =[]

score = 0  #Счётчик счёта
final_result = 0 #финальный результат

life = 3 #Кол-во жизней
hp_count = 0  #Переменная для анимации сердечек здоровья

player_anim_count =0 #Переменная для анимации персонажа

bg_x = 0 #Переменная передвижения заднего фона по оси X

player_speed = 5 #Скорость игрока
player_x = 10   #Точка спавна персонажа по оси X
player_y = 650  #Точка спавна персонажа по оси Y

lvl = 1 #переменная уровней(всего их 3), начинаем с 1
lvl_s = str(lvl)    #переменная вывода информации об активном уровне через строку
is_jump = False #переменная активности прыжка, чтоб игрок не прыгал постоянно
jump_count = 12 #сила прыжка

"""$$$$$$$$$$$$$$$$$$$$$$$$$  ЗВУКИ И МУЗЫКА ИСПОЛЬЗУЕМЫЕ В ИГРЕ   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""
bg_sound = pygame.mixer.Sound('stuff/sounds/hard drive - griffinilla.mp3')  #Подгружаем саундтрек к игре
vol_count = 0.5   #изначальная громкость нашего саундтрека

win_sound = pygame.mixer.Sound('stuff/sounds/win.mp3')  #Подгружаем звук победы
damage_sound = pygame.mixer.Sound('stuff/sounds/damage.mp3')    #Подгружаем звук получения урона
fail_sound = pygame.mixer.Sound('stuff/sounds/fail.mp3')    #Подгружаем звук проигрыша
"""$$$$$$$$$$$$$$$$$$$$$$$$$  ЗВУКИ И МУЗЫКА ИСПОЛЬЗУЕМЫЕ В ИГРЕ   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

"""tttttttttttttttttttt  ИНИЦИАЛИЗАЦИЯ ВРЕМЕНИ ДЛЯ СПАВНА ВРАГОВ  tttttttttttttttttttttttttttttt"""
ghost_timer = pygame.USEREVENT + 1  #инициализация таймера для призраков
pygame.time.set_timer(ghost_timer, 2500)   #наши призраки будут спавнится согласно таймеру каждые 2,5 сек
"""tttttttttttttttttttt  ИНИЦИАЛИЗАЦИЯ ВРЕМЕНИ ДЛЯ СПАВНА ВРАГОВ  tttttttttttttttttttttttttttttt"""

"""..................................  ТЕКСТ ИСПОЛЬЗУЕМЫЙ В ИГРЕ   ......................................."""
label = pygame.font.Font('stuff/fonts/Zlusa _font.ttf', 72)     #Подгружаем шрифт и устанавливаем его размер
label2 = pygame.font.Font('stuff/fonts/Zlusa _font.ttf', 36)    #Подгружаем шрифт и устанавливаем его размер
label3 = pygame.font.Font('stuff/fonts/Zlusa _font.ttf', 150)   #Подгружаем шрифт и устанавливаем его размер
lose_label = label3.render('You lose!', True, 'White')          #Текст проигрыша, сглаживание и цвет
restart_label = label.render('Try again!', True, 'White')       #Текст рестарта игры, сглаживание и цвет
restart_label_rect = restart_label.get_rect(topleft=(830, 300)) #инициализируем квадрат вокруг текста по координатам
quit_game_label = label.render('Back to Menu', True, 'Red')     #Текст выхода в меню, сглаживание и цвет
quit_game_label_rect = quit_game_label.get_rect(topleft=(820, 900)) #инициализируем квадрат вокруг текста по координатам
txt1 = label.render('I am Survivor', True, 'White')             #Текст названия игры, сглаживание и цвет
txt2 = label.render('PLAY', True, 'White')                      #Текст играть(PLAY), сглаживание и цвет
txt3 = label.render('SETTINGS', True, 'White')                  #Текст Настроек(SETTINGS), сглаживание и цвет
txt4 = label.render('EXIT', True, 'White')                      #Текст выхода(EXIT), сглаживание и цвет
txt5 = label.render('RESUME', True, 'White')                    #Текст продолжить(RESUME), сглаживание и цвет
Back_to_Menu = label.render('Back to Menu', True, 'White')      #Текст назад в меню, сглаживание и цвет
Back_to_Game = label.render('Back to Game', True, 'White')      #Текст назад в игру, сглаживание и цвет
volume_label = label.render('Volume', True, 'White')            #Текст громкости, сглаживание и цвет
about = label2.render('This game maded by Markova Eva', True, 'White')  #Текст об авторе, сглаживание и цвет
winner_label = label.render('YOU WIN! CONGRATULATE!', True, 'White')    #Текст выигрыша, сглаживание и цвет

"""..................................  ТЕКСТ ИСПОЛЬЗУЕМЫЙ В ИГРЕ   ......................................."""

gameplay = True #переменная нужная дла работы основного цикла игры
running = True  #переменная нужная дла работы основного цикла игры
clock.tick(24)  #частота кадров

"""@@@@@@@@@@@@@@@@@@@@    КЛАСС ДЛЯ СОЗДАНИЯ И РИСОВАНИЯ КНОПОК   @@@@@@@@@@@@@@@@@@@@@@@@"""
class buttons:
    """ ФУНКЦИЯ ИНИЦИАЛИЗАЦИИ"""
    def __init__(self, width, height):  #В функцию передаём ссылку на экземпляр класса(self), ширину и высоту
        self.width = width  #Устанавливаем высоту
        self.height = height    #Устанавливаем ширину
        self.inactiveCLR = (0, 0, 0)    #Цвет неактивной кнопки(когда на неё не наведён курсос)
        self.activeCLR = (255,255,255)  #Цвет активной кнопки(когда на неё наведён курсос)
    """ ФУНКЦИЯ ИНИЦИАЛИЗАЦИИ"""

    """::::::::::::::::     ФУНКЦИЯ РИСОВАНИЯ КНОПОК И ВЫПОЛНЕНИЯ ДЕЙСТВИЯ   :::::::::::"""
    def draw(self, x, y, action=None):
        mouse = pygame.mouse.get_pos()  #берём позицию курсора мыши
        click = pygame.mouse.get_pressed()  #считываем нажатие кнопок мыши
        if x < mouse[0] < x + self.width and y < mouse[1] < y+self.height:  #Если была нажата кнопка ЛКМ, и курсос находился в прямоугольнике нашей кнопки
                pygame.draw.rect(screen, self.activeCLR, (x, y, self.width, self.height)) #Рисуем кнопку(невидимый прямоугольник)

                if click[0] == 1 and action is not None:
                    action()  #выполняем действие которое надо

    """::::::::::::::::     ФУНКЦИЯ РИСОВАНИЯ КНОПОК И ВЫПОЛНЕНИЯ ДЕЙСТВИЯ   :::::::::::"""

"""@@@@@@@@@@@@@@@@@@@@    КЛАСС ДЛЯ СОЗДАНИЯ И РИСОВАНИЯ КНОПОК   @@@@@@@@@@@@@@@@@@@@@@@@"""

"""!!!!!!!!!!!!!!!!!    ФУНКЦИЯ ОТОБРАЖЕНИЯ СЧЁТА И ИНОЙ ИНФОРМАЦИИ НА ДИСПЛЕЙ ВО ВРЕМЯ ИГРЫ   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""
def score_display(screen, txt, size, x,y): #объявляем функцию и закидываем в неё: где пишем(на каком экране), что пишем(txt), размер(size), координаты(x,y)
    score_font = pygame.font.Font('stuff/fonts/Zlusa _font.ttf', size)  #ПОДГРУЖАЕМ ШРИФТ
    score_surface = score_font.render(txt, True, 'WHITE') #Устанавливаем параметры текста , сглаживание и цвет
    score_rect = score_surface.get_rect()  #получаем прямоугольник вокруг нашего текста
    score_rect.midtop = (x,y)   #Устанавливаем координаты нашего прямоугольника с текстом
    screen.blit(score_surface, score_rect)  #рисуем наш текст
"""!!!!!!!!!!!!!!!!!    ФУНКЦИЯ ОТОБРАЖЕНИЯ СЧЁТА И ИНОЙ ИНФОРМАЦИИ НА ДИСПЛЕЙ ВО ВРЕМЯ ИГРЫ   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"""

"""------------------------------------------------------  ОСНОВНАЯ ФУНКЦИЯ ИГРЫ(ДВИЖОК)   ----------------------------------------------"""
def run_game():
    bg_sound.set_volume(vol_count)  #Устанавливаем громкость саундтрека
    bg_sound.play() #Включаем саундтрек

    pygame.init()   #инициализируем pygame
    global player_x, player_y, score, gameplay, running, life, jump_count, is_jump, player_anim_count, bg_x, final_result, bg, lvl, lvl_s, hp_count #обозначаем глобальные переменные
    next_level = False #Переменная перехода на следующий уровень
    while running:  #Запускаем цикл пока running TRUE
        damage = False  #Индикатор получения урона
        if score < 799: #пока счёт меньше 799 находимся на 1й карте
            bg=bg1  #фон первой карты
            lvl = 1 #цифра активного уровня
            lvl_s = str(lvl)    #переводим цифру активного уровня в строку
            score_display(screen, str("Level" + lvl_s), 48, 950, 100)   #пишем какой у нас сейчас активный уровень
        if score > 800: #Если мы набрали больше 800 очков то переходим на 2й уровень
            bg = bg2    #подгружаем 2й фон
            lvl = 2     #меняем цифру активного уровня
            lvl_s = str(lvl)       #переводим её в строку
            score_display(screen, str("Level" + lvl_s), 48, 950, 100)   #рисуем инфу об активном уровне
            next_level = True   #переход на следующий уровень индикатор
        if score > 1700:    #когда станет счёт больше 1700 переходим на 3й уровень
            bg = bg3 #подгружаем фон 3 уровня
            lvl = 3 #меняем цифру активного уровня
            lvl_s = str(lvl)    #переводим в строку
            score_display(screen, str("Level" + lvl_s), 48, 950, 100) #отображаем инфу об активном уровне
            next_level = True   #индикатор перехода дальше
        if score > 3000:    #если счёт больше 3000 то мы победили
            Winner_Screen()     #вызываем функцию отображения экрана выигрыша

        screen.blit(bg, (bg_x, 0))  #рисуем задний фон
        screen.blit(bg, (bg_x+1920, 0))     #двигаем задний фон
        screen.blit(hp[hp_count], (1600, 50))   #рисуем кол-во здоровья(ХП)
        score_display(screen, str(score), 48, 50, 50)   #рисуем кол-во очков
        score_display(screen, str("Level" + lvl_s), 48, 950, 100)   #рисуем инфу об активном уровне
        if gameplay:    #если gameplay = TRUE
            player_rect = walk_left[0].get_rect(topleft=(player_x, player_y)) #считываем прямоугольник игрока и его координаты

            if ghost_list_in_game:  #Если список наших призраков не пустой
                for (i, el) in enumerate(ghost_list_in_game):  #цикл создания призраков
                    screen.blit(ghost, el)  #рисуем призраков
                    el.x -=15 #Скорость призрака

                    if el.x < 0:    #если скорость(координата призрака меньше нуля), то удаляем его)
                        ghost_list_in_game.pop(i)   #удаляем призрака из нашего массива согласно его номеру

                    if player_rect.colliderect(el):     # Если мы столкнулись с противником
                        life -= 1   #отнимаем 1 жизнь
                        damage = True   #индикатор получения урона, чтобы отобразить анимацию получения урона
                        damage_sound.play() #проигрываем звук получения урона
                        ghost_list_in_game.clear()      #Чтобы мы не получали урон постоянно противник исчезнет
                    if life < 1:    #проиграли
                            gameplay = False    #приостанавливаем игру
                            final_result = score    #запоминаем итоговое кол-во очков
                            bg_sound.stop() #останавливаем саундтрек
                            fail_sound.play()   #включаем звук поражения
            '''if platform_list:
                for (i, elem) in enumerate(platform_list):
                    screen.blit(platform, elem)
                    elem.x -= 10
                if elem.x < 0:
                    platform_list.pop(i)

                if player_y > elem.y - 32 and player_x <= elem.x and is_jump:
                    player_y= elem.y - 236 - 32
            '''
            if life == 3: #условие отображения кол-ва жизней на экране
                hp_count = 0    #переменная счётчик для анимации кол-ва жизней
            elif life == 2: #условие отображения кол-ва жизней на экране
                hp_count = 1    #переменная счётчик для анимации кол-ва жизней
            elif life == 1: #условие отображения кол-ва жизней на экране
                hp_count = 2    #переменная счётчик для анимации кол-ва жизней

            keys = pygame.key.get_pressed() #считываем нажатие клавиш
            if keys[pygame.K_LEFT]: #если нажали левую кнопку
                screen.blit(walk_left[player_anim_count // 2], (player_x, player_y))    #рисуем анимацию передвижения персонажа на его координатах
                if damage:
                    screen.blit(player_have_damage2, (player_x, player_y))  #срабатывает если мы получили урон игрок красится в красный

            else:
                screen.blit(walk_right[player_anim_count // 2], (player_x, player_y))    #рисуем анимацию передвижения персонажа на его координатах
                if damage:
                    screen.blit(player_have_damage2, (player_x, player_y))   #срабатывает если мы получили урон игрок красится в красный
            if keys[pygame.K_LEFT] and player_x > 50:   #ограничиваем размеры экрана, чтобы игрок не мог выбежать не меньше 50 пикселей
                player_x -= player_speed   #выключаем скорость, дальше игрок не пойдёт
            elif keys[pygame.K_RIGHT] and player_x < 1770:  #ограничиваем размеры экрана, чтобы игрок не мог выбежать не больше 1770 пикселей
                player_x += player_speed   #выключаем скорость, дальше игрок не пойдёт
            if keys[pygame.K_ESCAPE]:    #если нажали ESC то показываем меню паузы
                Pause() #вызов функции МЕНЮ ПАУЗЫ
            if not is_jump: #проверка нахождения игрока в воздухе
                if keys[pygame.K_SPACE]:    #если нажали пробел не то прыгаем
                    is_jump = True
            else:   #если нажали пробел и не в воздухе то прыгаем
                if jump_count >= -12:   #доп проверка
                    if jump_count > 0 and player_y > 236 :  #Условия прыжка
                        player_y -= (jump_count ** 2) / 2   #прыжок и гравитация

                    else:
                        player_y += (jump_count ** 2) / 2   #прыжок и гравитация
                    jump_count -= 1 #прыжок и гравитация
                else:
                    is_jump = False
                    jump_count = 12

            if player_anim_count == 3:  #счётчик кадров анимации если доходит до 3 - обнуляем
                player_anim_count = 0
            else:
                player_anim_count += 1  #счётчик кадров анимации прибавляем

            bg_x -= 2   #двигаем карту на 2 пикселя каждый кадр
            if bg_x == -1920: #обнуляем если прокрутили всю карту
                bg_x = 0
        else: #экран проигрыша
            screen.fill('BLACK')   #заливаем чёрным экран
            screen.blit(lose_label, (750, 500))     #рисуем текст проигрыша
            screen.blit(restart_label, restart_label_rect)  #рисуем текст и кнопку рестарта
            screen.blit(quit_game_label, quit_game_label_rect)  #рисуем текст и кнопку выхода в меню
            score_display(screen, str(final_result), 72, 950, 100)  #показываем финальный счёт

            mouse = pygame.mouse.get_pos()  #считываем положение мыши
            if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:    #проверяем какая кнопка была нажата, если нажали на рестарт, то запускаем игру снова
                gameplay = True #возвращаем работоспособность цикла игры
                player_x = 10   #возвращаем игрока в исходное положение
                ghost_list_in_game.clear()  #очищаем экран от призраков
                score = 0   #обнуляем очки
                life = 3    #восстанавливаем жизни
                hp_count = 0    #восстанавливаем отображение жизней
                bg_sound.play() #запускаем саундтрек

            if quit_game_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:  #если нажали выйти в главное меню
                GlobalMenu()    #вызываем главное меню
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #если пользователь нажал на закрытие окна
                running = False #выключаем цикл
                gameplay = False  #выключаем цикл
                pygame.quit()   #выходим из pygame
            if event.type == ghost_timer:   #условие появления призраков
                ghost_list_in_game.append(ghost.get_rect(topleft=(player_x+500, 720)))  #спавн призраков от положения игрока
                '''platform_list.append(platform.get_rect(topleft=(player_x + 300, player_y)))'''
        score += 10  #увеличиваем очки
        clock.tick(24)  #устанавливаем частоту кадров
        pygame.display.update() #обновляем экран
"""------------------------------------------------------  ОСНОВНАЯ ФУНКЦИЯ ИГРЫ(ДВИЖОК)   ----------------------------------------------"""

"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   ГЛАВНОЕ МЕНЮ   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""
def GlobalMenu():
    startBG = pygame.image.load('stuff/img/bgMenu.jpg')
    menu=True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(startBG, (0, 0))    #отрисовка заднего фона
        screen.blit(txt1, (752,200))    #отрисовка текста названия игры
        screen.blit(about, (1500, 1000))    #отрисовка текста информации об авторе

        screen.blit(txt2, (50, 510))  # отрисовка текста кнопки
        StartButton = buttons(150, 70)  #размеры кнопки
        StartButton.draw(50, 520, run_game) #расположение и что она вызывает

        screen.blit(txt3, (50, 650))  # отрисовка текста кнопки
        SettingsButton = buttons(300, 70)  #размеры кнопки
        SettingsButton.draw(50, 660, Settings1) #расположение и что она вызывает

        screen.blit(txt4, (50, 790))  # отрисовка текста кнопки
        ExitButton = buttons(150, 70)  # размеры кнопки
        ExitButton.draw(50, 800, Exit)  # расположение и что она вызывает

        pygame.display.update()     #обновляем экран
        clock.tick(60)  #частота кадров
"""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   ГЛАВНОЕ МЕНЮ   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"""

"""********************************МЕНЮ ПАУЗЫ*************************************************************"""
def Pause() :   #Меню паузы
    bg_sound.stop()    #Останавливаем музыку
    global esc  #Глобальная переменная esc с короторой получаем значение была ли нажата кнопка
    PauseMenu = pygame.image.load('stuff/img/bgMenu.jpg') #подгружаем фон меню
    pause = True    #переменная для работы цикла ниже
    while pause:    #цикл , до тех пор пока pause = True
        for event in pygame.event.get():    #проверяем не нажал ли пользователь крестик закрытия окна
            if event.type == pygame.QUIT:   #Если нажал то выходим
                pygame.quit()   #выключаем pygame
                quit()  #выходим из игры

        screen.blit(PauseMenu, (0, 0))  #рисуем фон меню паузы

        screen.blit(txt5, (50, 510))  # отрисовка текста кнопки Resume
        PauseButton = buttons(200, 70)  # создаем кнопку через наш класс и задаём размеры кнопки
        PauseButton.draw(50, 510, run_game) # расположение и что она вызывает

        screen.blit(txt3, (50, 650))  # отрисовка текста кнопки Settings
        SettingsButton = buttons(320, 70)  # создаем кнопку через наш класс и задаём размеры кнопки
        SettingsButton.draw(50, 650, Settings2)  # расположение и что она вызывает

        screen.blit(txt4, (50, 790))  # отрисовка текста кнопки Exit
        ExitButton = buttons(170, 70)  # создаем кнопку через наш класс и задаём размеры кнопки
        ExitButton.draw(50, 790, Exit)  # расположение и что она вызывает

        pygame.display.update()  #обновляем дисплей
        esc = False #останавливаем цикл
        clock.tick(60) #частота обновления экрана
"""********************************МЕНЮ ПАУЗЫ*************************************************************"""

"""=====================МЕНЮ НАСТРОЕК========================================="""
def Settings1() :
    settings = True
    BGsettings = pygame.image.load('stuff/img/bgMenu.jpg')
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(BGsettings, (0, 0))
        screen.blit(Back_to_Menu,(800, 400))
        screen.blit(volume_label, (850, 600))
        volume_mute = buttons(150, 70)
        volume_mute.draw(850, 600, Audio_mute)
        Settings = buttons(300, 70)
        Settings.draw(800, 400, GlobalMenu)
        pygame.display.update()
        clock.tick(60)
"""=====================МЕНЮ НАСТРОЕК========================================="""

"""+++++++++++++++++++++МЕНЮ НАСТРОЕК 2+++++++++++++++++++++++++++++++++++++++++++++"""
def Settings2() :
    bg_sound.stop()
    settings = True
    BGsettings = pygame.image.load('stuff/img/bgMenu.jpg')
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(BGsettings, (0, 0))
        screen.blit(Back_to_Game, (800, 400))
        Settings = buttons(300, 70)
        Settings.draw(800, 400, run_game)
        screen.blit(volume_label, (850, 600))
        volume_mute = buttons(150, 70)
        volume_mute.draw(850, 600, Audio_mute)
        pygame.display.update()
        clock.tick(60)
"""+++++++++++++++++++++МЕНЮ НАСТРОЕК 2+++++++++++++++++++++++++++++++++++++++++++++"""

"""ххххххххххххххххххх  ФУНКЦИЯ ВЫХОДА  ххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххх"""
def Exit():
    pygame.quit()
    quit()
"""ххххххххххххххххххх  ФУНКЦИЯ ВЫХОДА  ххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххххх"""

"""_______________________ ФУНКЦИЯ ИЗМЕНЕНИЯ ПАРАМЕТРОВ ГРОМКОСТИ ЗВУКА  __________________________"""
def Audio_mute():
    global vol_count
    if vol_count != 0:
        vol_count = 0
    else:
        vol_count = 0.5
"""_______________________ ФУНКЦИЯ ИЗМЕНЕНИЯ ПАРАМЕТРОВ ГРОМКОСТИ ЗВУКА  __________________________"""

"""***************  ФУНКЦИЯ ОТОБРАЖЕНИЯ ЭКРАНА ВЫИГРЫША  **************************"""
def Winner_Screen():
    win_screen = True
    bg_sound.stop()
    win_sound.play()
    winner_bg = pygame.image.load('stuff/img/win.jpg')
    while win_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.blit(winner_bg, (0,0))
        screen.blit(winner_label, (650, 550))
        screen.blit(txt4, (900, 1000))
        ExitButton = buttons(150, 70)  # размеры кнопки
        ExitButton.draw(900, 1000, Exit)  # расположение и что она вызывает
        pygame.display.update()
        clock.tick(60)

"""***************  ФУНКЦИЯ ОТОБРАЖЕНИЯ ЭКРАНА ВЫИГРЫША  **************************"""

GlobalMenu() #Вызов главного меню(когда запускаем игру)





