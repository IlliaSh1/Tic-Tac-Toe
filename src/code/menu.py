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

from src.code.game import *

class Menu:
    def __init__(self):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running_transition = False
        self.running_transition_start = 0
        self.running_menu = False
        self.cooldown_transition = COOLDOWN_TRANSITION
        self.cooldown_transition_after = COOLDOWN_TRANSITION/2
        self.load_load()
    def load_load(self):
        self.bg_image_start = pygame.image.load('src/img/bg_start.jpg')

        p_icon_title = pygame.image.load('src/img/star.gif')
        pygame.display.set_caption('Крестики-нолики')
        pygame.display.set_icon(p_icon_title)
        self.lbl_header = Label(0, -200, 850, 100, 'КРЕСТИКИ-НОЛИКИ', MAIN_FONT, 90, WHITE, GRAY, 'center', 'center', 3,
                                WHITE)
        self.lbl_loading = Label(0, -50, 400, 80, 'Загрузка...', TEXT_FONT, 40, WHITE, GRAY, 'center', 'center', 3,
                                 WHITE)
        self.menu_load_effects()

    def run_load(self):

        is_solved = os.path.isfile('src/solve/solve.txt')
        self.runing_load = not is_solved

        while self.runing_load:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.menu_draw_bg()

            self.menu_update_effects()

            self.menu_draw_widgets_load()

            pygame.display.update()
            self.clock.tick(FPS)

            solve.start_load()
            solve.half_load()
            self.runing_load = False
        solve.load()
        self.running_menu = True

    def load_menu(self):
        self.player = 'X'
        self.bot = 'O'
        self.turn = 'X'
        self.game = True
        self.running_menu = True
        # print(len(solve.States))
        # start_screen = StartWindow(screen.get_size())

        self.lbl_choose = Label(0, 0, 270, 40, "Выберите сторону:", MAIN_FONT, 25, WHITE, GRAY, 'center', 'center', 3,
                                WHITE)

        self.btn_start = Button(0, -70, 270, 50, 'НАЧАТЬ ИГРУ', 40, WHITE, GRAY, 'center', 3, WHITE)
        self.btn_exit = Button(0, 150, 340, 60, 'ВЫЙТИ ИЗ ИГРЫ', 40, WHITE, GRAY, 'center', 3, WHITE)

        self.radio_X = Radio(-140, 60, 220, 60, True, BLUE, WHITE, GRAY, 'center', 1, WHITE)
        self.lbl_X = Label(-150, 60, 0, 0, 'Крестики', MAIN_FONT, 24, WHITE, GRAY, 'center', 'center', 3,
                                WHITE)
        # (self, x, y, width, height, active, on_color, off_color, bg_color, align='left', border_width=0,
        # border_color=WHITE):
        self.img_X = Image(-60, 60, 50, 50, "src/img/star.gif", 'center')

        self.radio_O = Radio(140, 60, 220, 60, False, BLUE, WHITE, GRAY, 'center', 1, WHITE)
        self.lbl_O = Label(130, 60, 0, 0, 'Нолики', MAIN_FONT, 24, WHITE, GRAY, 'center', 'center', 3,
                           WHITE)
        self.img_O = Image(220, 60, 40, 50, "src/img/ball.gif", 'center')

    def run_menu(self):
        if self.running_transition:
            if pygame.time.get_ticks() - self.running_transition_start >= self.cooldown_transition:
                self.running_menu = False
                self.running_transition = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if self.running_transition:
               continue

            if self.btn_start.is_hovered():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif self.btn_exit.is_hovered():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif self.radio_X.is_hovered():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif self.radio_O.is_hovered():
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.btn_start.is_hovered():
                    self.running_transition = True
                    self.running_transition_start = pygame.time.get_ticks()
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                if self.btn_exit.is_hovered():
                    sys.exit()
                if self.radio_O.is_hovered():
                    if not self.radio_O.active:
                        self.radio_O.toggle()
                        self.radio_X.toggle()
                        self.player = 'O'
                        self.bot = 'X'
                if self.radio_X.is_hovered():
                    if not self.radio_X.active:
                        self.radio_X.toggle()
                        self.radio_O.toggle()
                        self.player = 'X'
                        self.bot = 'O'

        # screen.fill(WHITE)
        self.menu_draw_bg()
        # scale_rect = scale.get_rect(center=(1280/2,720/2))
        # ^ bg
        self.menu_update_effects()

        self.menu_draw_widgets_menu()
        # if self.running_transition:
        #     self.transition_update_effects()
        # btn_test.draw(screen)
        # Frame UPDATE
        if self.running_transition:
            self.transition_update_effects()

        pygame.display.update()

    def menu_draw_bg(self):
        cur_bg_image = pygame.transform.scale(
            self.bg_image_start, (self.screen_width, self.screen_height))
        # scale_rect = scale.get_rect(center=(1280/2,720/2))
        self.screen.blit(cur_bg_image, (0, 0))

    def menu_load_effects(self):
        self.effect_snow = Snow(NUMBER_PARTICLES)
        self.effect_transition = Snow(NUMBER_PARTICLES_TRANSITION, 0)

    def menu_update_effects(self):
        self.effect_snow.update(self.screen)

    def transition_update_effects(self):
        self.effect_transition.update(self.screen)

    def transition_clear_effects(self):
        self.effect_transition.clear()
    def menu_draw_widgets_load(self):
        self.lbl_header.draw(self.screen)
        self.lbl_loading.draw(self.screen)

    def menu_draw_widgets_menu(self):
        self.lbl_header.draw(self.screen)
        self.lbl_choose.draw(self.screen)

        self.radio_X.draw(self.screen)
        self.lbl_X.draw(self.screen)
        self.img_X.draw(self.screen)
        self.radio_O.draw(self.screen)
        self.lbl_O.draw(self.screen)
        self.img_O.draw(self.screen)

        self.btn_start.draw(self.screen)
        self.btn_exit.draw(self.screen)