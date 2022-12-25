import pygame
from src.code.constants import *

class Button(object):
    def __init__(self, x, y, width, height, text, font_size, color, bg_color, align='left', border_width=0,
                 border_color=WHITE):
        self.width = width
        self.height = height
        self.align = align
        self.border_width = border_width
        self.border_color = border_color
        if align == 'left':
            self.rect = pygame.Rect(x, y, width, height)
        elif align == 'center':
            self.rect = pygame.Rect(x + SCREEN_WIDTH / 2 - width / 2, y + SCREEN_HEIGHT / 2 - height / 2, width, height)
        self.font = pygame.font.Font("src/font/a_simplerstrs.ttf", font_size)
        self.text = self.font.render(text, True, color)

        self.bg_color = bg_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
        # print(screen)
        width = self.text.get_width()
        height = self.text.get_height()
        # Calculate the posX and posY

        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)

        # Draw the image into the screen
        screen.blit(self.text, (posX, posY))

    def is_hovered(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def change_bg_color(self, color):
        self.bg_color = color


class ButtonImg(object):
    def __init__(self, x, y, width, height, img, align = 'left'):
        self.width=width
        self.height=height
        self.align=align
        if align == 'left':
            self.x = x
            self.y = y
        elif align=='center':
            self.x = x + SCREEN_WIDTH / 2 - width / 2
            self.y = y + SCREEN_HEIGHT / 2 - height / 2
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, (width, height))
        self.rect = pygame.Rect(self.x,self.y,width, height)

        self.font = pygame.font.Font(None, 40)




    def draw(self, screen):
        # print(screen)
        # Calculate the posX and posY

        # Draw the image into the screen
        screen.blit(self.img, (self.x, self.y))



    def is_hovered(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False





class Radio(object):
    def __init__(self, x, y, width, height, active, on_color, off_color, bg_color, align='left', border_width=0,
                 border_color=WHITE):
        self.width = width
        self.height = height
        self.active = active
        self.on_color = on_color
        self.off_color = off_color
        self.align = align
        self.border_width = border_width
        self.border_color = border_color

        if align == 'left':
            self.rect = pygame.Rect(x, y, width, height)
        elif align == 'center':
            self.rect = pygame.Rect(x + SCREEN_WIDTH / 2 - width / 2, y + SCREEN_HEIGHT / 2 - height / 2, width, height)

        self.r = round(min(width,height)*0.2)
        self.R = round(min(width,height)*0.24)

        self.bg_color = bg_color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        pygame.draw.rect(screen, self.border_color, self.rect, self.border_width)
        # print(screen)
        # Calculate the posX and posY

        # posX = self.rect.centerx - (width / 2)
        # posY = self.rect.centery - (height / 2)
        posX = self.rect.x + self.R + 5
        posY = self.rect.y + self.height/2
        posX_r = self.rect.x + self.R + 5
        posY_r = self.rect.y + self.height/2
        # Draw the image into the screen
        if self.active:
            pygame.draw.circle(screen, self.on_color, (posX_r, posY_r), self.r-5,width=10)
            pygame.draw.circle(screen, self.on_color, (posX, posY), self.R, 2)
        else:
            pygame.draw.circle(screen, self.off_color, (posX_r, posY_r), self.r - 5, width=10)
            pygame.draw.circle(screen, self.off_color, (posX, posY), self.R, 2)

    def is_hovered(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def change_bg_color(self, color):
        self.bg_color = color

    def toggle(self):
        self.active^=1