import pygame
from src.code.constants import *

class Label(object):
    def __init__(self, x, y, width, height, text, font_family, font_size, color, bg_color, align = 'left',text_align = 'center', border_width=0, border_color=BLUE):
        self.width=width
        self.height=height
        self.align=align
        self.border_width = border_width
        self.border_color = border_color
        if align == 'left':
            self.rect = pygame.Rect(x,y,width, height)
        elif align == 'center':
            self.rect = pygame.Rect(x+SCREEN_WIDTH/2-width/2,y+SCREEN_HEIGHT/2-height/2,width, height)

        self.font = pygame.font.Font(font_family, font_size)
        self.text = self.font.render(text, True, color)
        self.text_align = text_align
        self.bg_color = bg_color
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect)
        if self.border_width:
            pygame.draw.rect(screen, self.border_color,self.rect, self.border_width)
        # print(screen)
        width = self.text.get_width()
        height = self.text.get_height()
        # Calculate the posX and posY
        if self.text_align == 'center':
            posX = self.rect.centerx - (width / 2)
            posY = self.rect.centery - (height / 2)
        elif self.text_align == 'left':
            posX = self.rect.x+10
            posY = self.rect.centery - self.text.get_height()/2
        # Draw the image into the screen
        screen.blit(self.text, (posX, posY))


    def is_hovered(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            return True
        else:
            return False

    def change_text(self, text):
        self.text = self.font.render(text, True, self.color)

class Image(object):
    def __init__(self, x, y, width, height, img, align = 'left'):
        self.width=width
        self.height=height
        self.align=align
        if align == 'left':
            self.x= x
            self.y=y
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

    def change_bg_img(self, color):
        self.bg_color = color