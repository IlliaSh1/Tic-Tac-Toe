import os.path
import sys
import pygame
from math import *
from pygame.locals import *

from src.code import solve
from src.code.button import *
from src.code.label import *
from src.code.constants import *
import time
# import solve
from src.code.effects import *
from src.code.field import *
pygame.init()


# pygame.mouse.set_visible(False)
# cursor_img_rect = cursor_img.get_rect()

def run_game():
    run_load = True

    screen_width = 1280
    screen_height = 720
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.mixer.music.load('src/music/bg_music.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)
    bg_image_start = pygame.image.load('src/img/bg_start.jpg')
    bg_image_game = pygame.image.load('src/img/bg_game.jpg')
    p_icon_title = pygame.image.load('src/img/star.gif')
    pygame.display.set_caption('Крестики-нолики')
    pygame.display.set_icon(p_icon_title)

    clock = pygame.time.Clock()

    effect_snow = Snow(NUMBER_PARTICLES)

    lbl_header = Label(0,-200,850,100,'КРЕСТИКИ-НОЛИКИ',MAIN_FONT, 90, WHITE, GRAY,'center','center', 3, WHITE)

    lbl_loading = Label(0,-50,400,80,'Загрузка...',TEXT_FONT, 40, WHITE, GRAY,'center','center', 3, WHITE)


    is_solved=os.path.isfile('src/solve/solve.txt')
    while run_load:
        if is_solved:
            solve.load()
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Закрывает игру

                sys.exit()

        w, h = screen.get_size()
        cur_bg_image = pygame.transform.scale(
                bg_image_start, (w, h))
        # scale_rect = scale.get_rect(center=(1280/2,720/2))
        screen.blit(cur_bg_image, (0, 0))
        # ^ bg

        effect_snow.update(screen)
        lbl_header.draw(screen)
        lbl_loading.draw(screen)

        pygame.display.update()
        clock.tick(FPS)

        solve.start_load()
        solve.half_load()
        solve.load()
        break


    player = 'X'
    bot = 'O'
    turn = 'X'
    game = True
    run_menu = True
    # print(len(solve.States))
    # start_screen = StartWindow(screen.get_size())

    lbl_choose = Label(0,0,270,40,"Выберите сторону:",MAIN_FONT, 25, WHITE, GRAY,'center','center', 3, WHITE)



    btn_start = Button(0, -70, 270, 50, 'НАЧАТЬ ИГРУ', 40, WHITE, GRAY, 'center', 3, WHITE)
    btn_exit = Button(0, 150, 340, 60,'ВЫЙТИ ИЗ ИГРЫ', 40, WHITE, GRAY, 'center', 3, WHITE)


    radio_X = Radio(-60, 60, 100, 60, True, BLUE, WHITE, GRAY, 'center', 1, WHITE)
    # (self, x, y, width, height, active, on_color, off_color, bg_color, align='left', border_width=0,
    # border_color=WHITE):
    img_X = Image(-40, 60, 50, 50, "src/img/star.gif",'center')

    radio_O = Radio(60, 60, 100, 60, False, BLUE, WHITE, GRAY, 'center', 1, WHITE)
    img_O = Image(80, 60, 40, 50, "src/img/ball.gif", 'center')

    # btn_test = Button(170,330,60,40,"=", 40, WHITE, GRAY, 'left', 5, WHITE)
    btn_new_game = Button(40, 470, 280, 80, 'НАЧАТЬ НОВУЮ ИГРУ', 24, GREEN, GRAY, 'left', 3, WHITE)
    btn_exit_game = Button(40, 570, 280, 80, 'ВЫЙТИ ИЗ ИГРЫ', 24, GREEN, GRAY, 'left', 3, WHITE)

    field_decoration = Image(0, 0, 700, 700, 'src/img/field_decoration.png', 'center')

    lbl_turn = Label(40, 400, 280, 50, 'Сейчас ходит: игрок',MAIN_FONT,24,BLUE,WHITE,'left','left',2,GRAY)

    # board = pygame.display.set_caption()
    bg_rules = Label(480,0,270,600,'',MAIN_FONT,20,WHITE,WHITE,'center','center',2,GRAY)

    lbls_rules = []
    text_rules = ['1. Игроки по очереди ставят на ', ' свободные клетки поля 3x3', ' знаки (один всегда крестики,',
                  ' другой всегда нолики) ', '2. Первый, выстроивший в ряд',
                  ' 3 своих фигуры по вертикали,',' горизонтали или диагонали,',' выигрывает.',
                  '3. Первый ход делает игрок,',' ставящий крестики.']
    for i in range(len(text_rules)):
        lbls_rules.append(Label(350,-280 + i*20, 0, 0, text_rules[i], TEXT_FONT, 16, GRAY, WHITE, 'center', 'left'))

    bg_score = Label(40, 60, 280, 300,'',MAIN_FONT,0,WHITE,WHITE,'left','left',3,GRAY)

    text_loses = ['Количество', 'проигрышей']
    lbls_loses = []
    for i in range(len(text_loses)):
        lbls_loses.append(
            Label(50, 80+25/2 + i * 20, 0, 0, text_loses[i], TEXT_FONT, 20, GRAY, BLUE, 'left', 'left'))
    text_draws = ['Количество', 'ничей']
    lbls_draws = []
    for i in range(len(text_draws)):
        lbls_draws.append(
            Label(50, 180+25/2 + i * 20, 0, 0, text_draws[i], TEXT_FONT, 20, GRAY, WHITE, 'left', 'left'))
    text_wins = ['Количество', 'побед']
    lbls_wins = []
    for i in range(len(text_wins)):
        lbls_wins.append(
            Label(50, 280+25/2 + i * 20, 0, 0, text_wins[i], TEXT_FONT, 20, GRAY, WHITE, 'left', 'left'))

    #
    cnt_loses = 0
    lbl_cnt_loses = Label(200, 80, 110, 50, str(cnt_loses), MAIN_FONT, 40, WHITE, GRAY, 'left', 'center',0)
    cnt_draws = 0
    lbl_cnt_draws = Label(200, 180, 110, 50, str(cnt_draws), MAIN_FONT, 40, WHITE, GRAY, 'left', 'center',0)
    cnt_wins = 0
    lbl_cnt_wins = Label(200, 280, 110, 50, str(cnt_wins), MAIN_FONT, 40, RED, GRAY, 'left', 'center',0)



    # lbls_text_wins =
    #
    # lbl_text_draws =
    # lbls_text_loses =
    # lbl_score_wins =
    # lbl_score_draws =
    # lbls_score_loses =
    msg_loses = "Поражение"
    msg_draw = "Ничья"
    msg_win = "УРА ПОБЕДА"

    lbl_message = Label(0,-320, 300, 80, '', TEXT_FONT, 40, WHITE, GRAY, 'center', 'center')


    board = Field(0,0,600,600,WHITE,'center',3,GREEN)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Закрывает игру
                print(player)
                sys.exit()
            # keys = pygame.keys.get_pressed()

            if run_menu:


                if btn_start.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif btn_exit.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif btn_new_game.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif btn_exit_game.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif radio_X.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif radio_O.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if event.type == MOUSEBUTTONDOWN:
                    if btn_start.is_hovered():
                        run_menu=False
                        turn = 'X'
                    if btn_exit.is_hovered():
                        sys.exit()
                    if radio_O.is_hovered():
                        if not radio_O.active:
                            radio_O.toggle()
                            radio_X.toggle()
                            player = 'O'
                            bot = 'X'
                    if radio_X.is_hovered():
                        if not radio_X.active:
                            radio_X.toggle()
                            radio_O.toggle()
                            player = 'X'
                            bot = 'O'
            else:
                if btn_exit_game.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                elif btn_new_game.is_hovered():
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if game:

                    cur_board = []
                    for i in range(3):
                        cur_board.append([])
                        for j in range(3):
                            cur_board[i].append(board.cells[i][j].state)
                    result = solve.check_board(cur_board)
                    if result != 'playing':
                        game = False
                        if result == 'draw':
                            cnt_draws+=1
                            lbl_message.change_text(msg_draw)
                            if cnt_draws<=999:
                                lbl_cnt_draws.change_text(str(cnt_draws))
                            else:
                                lbl_cnt_draws.change_text('999+')
                        elif result != player:
                            cnt_loses+=1
                            lbl_message.change_text(msg_loses)
                            if cnt_loses<=999:
                                lbl_cnt_loses.change_text(str(cnt_loses))
                            else:
                                lbl_cnt_loses.change_text('999+')
                        elif result == player:
                            cnt_wins+=1
                            lbl_message.change_text(msg_win)
                            if cnt_wins<=999:
                                lbl_cnt_wins.change_text(str(cnt_wins))
                            else:
                                lbl_cnt_wins.change_text('999+')
                    else:
                        if turn != player:
                            board_key = turn
                            for row in board.cells:
                                for cell in row:
                                    board_key += cell.state
                            move_x, move_y = solve.get_move(board_key)
                            board.cells[move_x][move_y].update(bot)
                            turn = player
                            lbl_turn.change_text('Сейчас ходит: игрок')
                            # cooldewn


                if event.type == MOUSEBUTTONDOWN:
                    if btn_new_game.is_hovered():
                        board.clear()
                        game = True
                        turn = 'X'
                    if btn_exit_game.is_hovered():
                        run_menu = 1
                        game = True
                        turn = 'X'
                        board.clear()

                if game:
                    if turn == player:
                        if board.is_hovered():
                            for i in range(3):
                                for j in range(3):
                                    if board.cells[i][j].is_hovered() and not board.cells[i][j].active:
                                        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                        if event.type == MOUSEBUTTONDOWN:
                                            click_sound = pygame.mixer.Sound('src/music/move.mp3')
                                            pygame.mixer.Sound.play(click_sound)
                                            board.cells[i][j].update(player)
                                            turn = bot
                                            lbl_turn.change_text('Сейчас ходит: бот')


        # фоновая заливка

        mouse_x,mouse_y=pygame.mouse.get_pos()

        # screen.fill(WHITE)
        w,h=screen.get_size()
        if run_menu:
            cur_bg_image = pygame.transform.scale(
                bg_image_start, (w, h))
        else:
            cur_bg_image = pygame.transform.scale(
                bg_image_game, (w, h))


        # scale_rect = scale.get_rect(center=(1280/2,720/2))
        screen.blit(cur_bg_image, (0, 0))
        # ^ bg

        if run_menu:

            effect_snow.update(screen)


            lbl_header.draw(screen)
            lbl_choose.draw(screen)

            radio_X.draw(screen)
            img_X.draw(screen)
            radio_O.draw(screen)
            img_O.draw(screen)

            btn_start.draw(screen)
            btn_exit.draw(screen)


        else:
            btn_new_game.draw(screen)
            btn_exit_game.draw(screen)
            board.draw(screen)
            bg_rules.draw(screen)
            for i in lbls_rules:
                i.draw(screen)
            bg_score.draw(screen)
            for i in range(2):
                lbls_loses[i].draw(screen)
                lbls_draws[i].draw(screen)
                lbls_wins[i].draw(screen)

            lbl_cnt_loses.draw(screen)
            lbl_cnt_draws.draw(screen)
            lbl_cnt_wins.draw(screen)
            lbl_turn.draw(screen)

            field_decoration.draw(screen)

            if not game:
                lbl_message.draw(screen)
        # btn_test.draw(screen)
        # Frame UPDATE
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(FPS)
        # print('Tick')



run_game()