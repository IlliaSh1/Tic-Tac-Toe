import os.path
import sys
import pygame

from src.code import solve
from src.code.button import *
from src.code.label import *
from src.code.constants import *
from pygame.locals import *
import time
# import solve
from src.code.field import *

from src.code.effects import *
from src.code.app import *
from src.code.menu import *


class Game(object):
    def __init__(self):
        self.running_game = False
        self.game = True
        self.player = 'X'
        self.turn = 'X'
        self.bot = 'O'
        self.screen_width = 1280
        self.screen_height = 720
        self.cd_bot = 0
        self.cd_bot_start = pygame.time.get_ticks()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.bg_image_game = pygame.image.load('src/img/bg_game.jpg')
        self.load_game()

    def load_settings(self, run, player, turn, bot, effect_transition):
        self.game = True
        self.running_game = run
        self.player = player
        self.turn = turn
        self.bot = bot
        self.cd_bot = FPS*12
        self.cd_bot_start = pygame.time.get_ticks()

        self.effect_transition = effect_transition
        self.cd_transition = COOLDOWN_TRANSITION*1
        self.cd_transition_after = COOLDOWN_TRANSITION*2
        self.running_transition = True
        self.running_transition_after = True
        self.running_transition_start = pygame.time.get_ticks()

    def load_game(self):
        self.btn_to_menu = Button(40, 10, 280, 30, 'Вернуться в меню', 24, GREEN, GRAY, 'left', 2, WHITE)
        self.btn_new_game = Button(40, 470, 280, 80, 'НАЧАТЬ НОВУЮ ИГРУ', 24, GREEN, GRAY, 'left', 3, WHITE)
        self.btn_exit_game = Button(40, 570, 280, 80, 'ВЫЙТИ ИЗ ИГРЫ', 24, GREEN, GRAY, 'left', 3, WHITE)

        self.field_decoration = Image(0, 0, 800, 700, 'src/img/field_decoration.png', 'center')

        self.lbl_turn = Label(40, 400, 280, 50, 'Сейчас ходит: игрок', MAIN_FONT, 24, BLUE, WHITE, 'left', 'left', 2,
                              GRAY)

        # board = pygame.display.set_caption()
        self.bg_rules = Label(480, 0, 270, 600, '', MAIN_FONT, 20, WHITE, WHITE, 'center', 'center', 2, GRAY)

        self.lbls_rules = []
        self.text_rules = ['1. Игроки по очереди ставят на ', ' свободные клетки поля 3x3',
                           ' знаки (один всегда крестики,',
                           ' другой всегда нолики) ', '2. Первый, выстроивший в ряд',
                           ' 3 своих фигуры по вертикали,', ' горизонтали или диагонали,', ' выигрывает.',
                           '3. Первый ход делает игрок,', ' ставящий крестики.']
        for i in range(len(self.text_rules)):
            self.lbls_rules.append(
                Label(350, -280 + i * 20, 0, 0, self.text_rules[i], TEXT_FONT, 16, GRAY, WHITE, 'center', 'left'))

        self.bg_score = Label(40, 60, 280, 300, '', MAIN_FONT, 0, WHITE, WHITE, 'left', 'left', 3, GRAY)

        self.text_loses = ['Количество', 'проигрышей']
        self.lbls_loses = []
        for i in range(len(self.text_loses)):
            self.lbls_loses.append(
                Label(50, 80 + 25 / 2 + i * 20, 0, 0, self.text_loses[i], TEXT_FONT, 20, GRAY, BLUE, 'left', 'left'))
        self.text_draws = ['Количество', 'ничей']
        self.lbls_draws = []
        for i in range(len(self.text_draws)):
            self.lbls_draws.append(
                Label(50, 180 + 25 / 2 + i * 20, 0, 0, self.text_draws[i], TEXT_FONT, 20, GRAY, WHITE, 'left', 'left'))
        self.text_wins = ['Количество', 'побед']
        self.lbls_wins = []
        for i in range(len(self.text_wins)):
            self.lbls_wins.append(
                Label(50, 280 + 25 / 2 + i * 20, 0, 0, self.text_wins[i], TEXT_FONT, 20, GRAY, WHITE, 'left', 'left'))

        self.cnt_loses = 0
        self.lbl_cnt_loses = Label(200, 80, 110, 50, str(self.cnt_loses), MAIN_FONT, 40, WHITE, GRAY, 'left', 'center',
                                   0)
        self.cnt_draws = 0
        self.lbl_cnt_draws = Label(200, 180, 110, 50, str(self.cnt_draws), MAIN_FONT, 40, WHITE, GRAY, 'left', 'center',
                                   0)
        self.cnt_wins = 0
        self.lbl_cnt_wins = Label(200, 280, 110, 50, str(self.cnt_wins), MAIN_FONT, 40, RED, GRAY, 'left', 'center', 0)

        self.msg_loses = "Поражение"
        self.msg_draw = "Ничья"
        self.msg_win = "УРА ПОБЕДА"

        self.lbl_message = Label(0, -320, 300, 80, '', TEXT_FONT, 40, WHITE, GRAY, 'center', 'center')

        self.board = Field(0, 0, 600, 600, WHITE, 'center', 3, GREEN)

    def run_game(self):
        if self.running_transition:
            if pygame.time.get_ticks() - self.running_transition_start >= self.cd_transition:
                self.running_transition = False
                # self.transition_clear_effects()
        else :
            if pygame.time.get_ticks() - self.cd_bot_start >= self.cd_bot and self.game:

                if self.turn != self.player:
                    self.board_key = self.turn
                    for row in self.board.cells:
                        for cell in row:
                            self.board_key += cell.state
                    self.move_x, self.move_y = solve.get_move(self.board_key)
                    self.board.cells[self.move_x][self.move_y].update(self.bot)
                    self.turn = self.player
                    self.lbl_turn.change_text('Сейчас ходит: игрок')
                    click_sound = pygame.mixer.Sound('src/music/move.mp3')
                    pygame.mixer.Sound.play(click_sound)
                    self.cd_bot = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if self.running_transition:
                continue

            if self.btn_exit_game.is_hovered():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif self.btn_new_game.is_hovered():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif self.btn_to_menu.is_hovered():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if self.game:
                self.cur_board = []
                for i in range(3):
                    self.cur_board.append([])
                    for j in range(3):
                        self.cur_board[i].append(self.board.cells[i][j].state)

                self.result = solve.check_board(self.cur_board)
                if self.result != 'playing':
                    self.cd_bot = 0
                    self.game = False
                    if self.result == 'draw':
                        self.cnt_draws += 1
                        self.lbl_message.change_text(self.msg_draw)
                        if self.cnt_draws <= 999:
                            self.lbl_cnt_draws.change_text(str(self.cnt_draws))
                        else:
                            self.lbl_cnt_draws.change_text('999+')
                    elif self.result != self.player:
                        self.cnt_loses += 1
                        self.lbl_message.change_text(self.msg_loses)
                        if self.cnt_loses <= 999:
                            self.lbl_cnt_loses.change_text(str(self.cnt_loses))
                        else:
                            self.lbl_cnt_loses.change_text('999+')
                    elif self.result == self.player:
                        self.cnt_wins += 1
                        self.lbl_message.change_text(self.msg_win)
                        if self.cnt_wins <= 999:
                            self.lbl_cnt_wins.change_text(str(self.cnt_wins))
                        else:
                            self.lbl_cnt_wins.change_text('999+')
                            # cooldewn

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.btn_to_menu.is_hovered():
                    self.running_game = False
                    self.turn = 'X'
                    self.game = True
                    self.board.clear()
                if self.btn_new_game.is_hovered():
                    self.board.clear()
                    self.game = True
                    self.turn = 'X'
                    self.cd_bot = FPS * 12
                    self.cd_bot_start = pygame.time.get_ticks()
                if self.btn_exit_game.is_hovered():
                    sys.exit()

            if self.game:
                if self.turn == self.player:
                    if self.board.is_hovered():
                        for i in range(3):
                            for j in range(3):
                                if self.board.cells[i][j].is_hovered() and not self.board.cells[i][j].active:
                                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                                    if event.type == MOUSEBUTTONDOWN and event.button == 1:

                                        click_sound = pygame.mixer.Sound('src/music/move.mp3')
                                        pygame.mixer.Sound.play(click_sound)
                                        self.board.cells[i][j].update(self.player)
                                        self.turn = self.bot
                                        self.lbl_turn.change_text('Сейчас ходит: бот')
                                        self.cd_bot_start = pygame.time.get_ticks()
                                        self.cd_bot = FPS * 8


            # фоновая заливка

        # screen.fill(WHITE)

        self.game_draw_bg()
        # ^ bg

        self.game_draw_widgets()

        # btn_test.draw(screen)
        # Frame UPDATE
        if self.running_transition_after:
            self.transition_update_effects()
            if pygame.time.get_ticks() - self.running_transition_start >= self.cd_transition_after:
                self.running_transition_after = False
        pygame.display.update()

        # print('Tick')

    def game_draw_bg(self):
        cur_bg_image = pygame.transform.scale(
            self.bg_image_game, (self.screen_width, self.screen_height))
        self.screen.blit(cur_bg_image, (0, 0))

    def game_draw_widgets(self):
        self.btn_to_menu.draw(self.screen)
        self.btn_new_game.draw(self.screen)
        self.btn_exit_game.draw(self.screen)
        self.board.draw(self.screen)
        self.bg_rules.draw(self.screen)
        for i in self.lbls_rules:
            i.draw(self.screen)
        self.bg_score.draw(self.screen)
        for i in range(2):
            self.lbls_loses[i].draw(self.screen)
            self.lbls_draws[i].draw(self.screen)
            self.lbls_wins[i].draw(self.screen)

        self.lbl_cnt_loses.draw(self.screen)
        self.lbl_cnt_draws.draw(self.screen)
        self.lbl_cnt_wins.draw(self.screen)
        if self.turn == self.player:
            self.lbl_turn.change_text(str("Сейчас ходит: Игрок"))
        else:
            self.lbl_turn.change_text(str("Сейчас ходит: Бот"))
        self.lbl_turn.draw(self.screen)

        self.field_decoration.draw(self.screen)

        if not self.game:
            self.lbl_message.draw(self.screen)

    def transition_update_effects(self):
        self.effect_transition.update(self.screen, 0)

    def transition_clear_effects(self):
        self.effect_transition.clear()