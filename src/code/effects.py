from src.code.constants import *
from math import *
from src.code.label import *
import random
import pygame

pygame.init()
class Snow:
    def __init__(self, number_particles, flag = 1):
        self.number_particles = number_particles
        self.particles = []
        self.imgs = []
        self.flag = flag
        for i in range(self.number_particles):
            self.particles.append(self.new_particle())
    def update(self, screen, flag_update = 1):
        for i in range(len(self.particles)):
            self.particles[i] = self.update_particle(self.particles[i])

            pygame.draw.circle(screen, WHITE, (self.particles[i]['x'], self.particles[i]['y']), self.particles[i]['r'])
            if flag_update:
                if self.particles[i]['y'] - self.particles[i]['r'] > 720 or self.particles[i]['x'] - self.particles[i]['r'] > 1280 or \
                        self.particles[i]['x'] + self.particles[i]['r'] < 0:
                    self.particles[i] = self.new_particle()

    def new_particle(self):
        if self.flag:
            cur_particle = {'speed' : 0.6 + random.random() * (4), 'angle':30 + random.random()*(120),
                            'x': random.random() * 1280 , 'y':0, 'r': 5 + random.random()*(7),
                            "alpha" : random.random()}
        else:
            # if random.randint(0,3):
            cur_particle = {'speed': 8 + random.random() * (2), 'angle':30 + random.random()*(120),
                        'x': random.random() * 1280, 'y': random.random() * (-200), 'r': 8 + random.random()*(10),
                        "alpha": random.random()}
            # else:
            #     cur_particle = {'speed': 1 + random.random() * (3), 'angle': 90 + random.random() * (90),
            #                     'x': 1280, 'y': random.random() * 720, 'r': 7 + random.random() * (9),
            #                     "alpha": random.random()}
        return cur_particle

    def update_particle(self, cur_particle):
        cur_particle['x'] += cur_particle['speed'] * cos(cur_particle['angle']*pi/180)
        cur_particle['y'] += cur_particle['speed'] * sin(cur_particle['angle']*pi/180)

        return cur_particle

    def clear(self):
        for i in range(len(self.particles)):
            self.particles[i] = self.new_particle()
