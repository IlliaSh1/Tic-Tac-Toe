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

from src.code.menu import *
from src.code.game import *

class App:
    def __init__(self, screen_width, screen_height):
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()

        self.running_menu = False
        self.running_game = False
        self.running_load = True
        self.load_music()

        self.menu = Menu()
        self.menu.load_load()
        self.menu.run_load()

        self.game = Game()



    def run(self):
        self.menu.load_load()
        self.menu.run_load()

        self.menu.load_menu()
        self.game.load_game()
        while True:
            if self.menu.running_menu:
                self.menu.run_menu()

                if not self.menu.running_menu:
                    self.game.load_settings(not self.menu.running_menu, self.menu.player,self.menu.turn,self.menu.bot, self.menu.effect_transition)

            elif self.game.running_game:
                self.game.run_game()
                if not self.game.running_game:
                    self.menu.running_menu = True
                    self.menu.transition_clear_effects()
            self.clock.tick(FPS)



    def load_music(self):
        pygame.mixer.music.load('src/music/bg_music.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

