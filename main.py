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
from src.code.app import *
from src.code.menu import *
from src.code.game import *

pygame.init()


def run_game():
    app = App(1280, 720)
    app.run()

    # btn_test = Button(170,330,60,40,"=", 40, WHITE, GRAY, 'left', 5, WHITE)

run_game()
