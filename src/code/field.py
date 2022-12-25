import pygame
from src.code.constants import *

class Field:
    def __init__(self, x, y, width, height, bg_color, align, border_width, border_color ):

        self.width = width
        self.height = height
        self.align = align
        self.border_width = border_width
        self.border_color = border_color

        if align == 'left':
            self.rect = pygame.Rect(x, y, width, height)
            self.x=x
            self.y=y
        elif align == 'center':
            self.rect = pygame.Rect(x + SCREEN_WIDTH / 2 - width / 2, y + SCREEN_HEIGHT / 2 - height / 2, width,
                                        height)
            self.x=x + SCREEN_WIDTH / 2 - width / 2
            self.y=y + SCREEN_HEIGHT / 2 - height / 2
        self.cells = []
        for i in range(3):
            self.cells.append([])
            for j in range(3):
                self.cells[i].append(Cell( self.x + width/3*j, self.y + height/3*i, width/3, height/3,0, WHITE, 'left', 3, LIGHT_GRAY ))
        self.bg_color = bg_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

        for i in range(3):
            for j in range(3):
                self.cells[i][j].draw(screen)

    def is_hovered(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.cells[i][j].clear()

class Cell:
    def __init__(self, x, y, width, height, active=0, bg_color=WHITE, align='left', border_width=0,
                 border_color=WHITE):
        self.width = width
        self.height = height

        self.img_X = pygame.image.load("src/img/star.gif")
        self.img_X = pygame.transform.scale(self.img_X, (width*0.8, height*0.8))
        self.img_O = pygame.image.load("src/img/ball.gif")
        self.img_O = pygame.transform.scale(self.img_O, (width*0.8, height*0.8))

        if align == 'left':

            self.rect = pygame.Rect(x, y, width, height)
        elif align == 'center':
            self.rect = pygame.Rect(x + SCREEN_WIDTH / 2 - width / 2, y + SCREEN_HEIGHT / 2 - height / 2, width, height)

        self.bg_color = bg_color
        self.border_color = border_color
        self.border_width = border_width

        self.active = active
        self.state = 'e'
        self.img = self.img_X
        self.empty = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)

        if self.active:
            screen.blit(self.img, (self.rect.x+self.width*0.1, self.rect.y+self.height*0.1))

    def is_hovered(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def update(self, val):
        self.active = 1
        if (val == 'X'):
            self.img = self.img_X
            self.state = 'X'
        else:
            self.img = self.img_O
            self.state = 'O'

    def clear(self):
        self.active = 0
        self.state = 'e'
