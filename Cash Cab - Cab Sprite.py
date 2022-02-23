import pygame as pg

from sys import path
from sys import exit
import os
import random

my_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_path)
path.append(my_path)

import expy as ex

#Setup

pg.init()
screen = pg.display.set_mode((800,600)) #set your window size, (x,y)
pg.display.set_caption("Cash Cab")
clock = pg.time.Clock()

white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
red = (255,0,0)


class Cab():

    def __init__(self):
        self.image = pg.image.load('Cab.png')
        w,h = self.image.get_size()
        w,h = int(w/2), int(h/2)

        self.image_up = pg.transform.scale(self.image, (w,h))
        self.image_left = pg.transform.rotate(self.image_up, 90)
        self.image_down = pg.transform.rotate(self.image_left, 90)
        self.image_right = pg.transform.rotate(self.image_down, 90)

        self.hitbox = pg.Rect(275,375, w, h)
        self.speed_x = 0
        self.speed_y = 0


    def update(self):
        self.hitbox[0] += self.speed_x
        self.hitbox[1] += self.speed_y

    def draw(self):
        x, y = self.hitbox[0], self.hitbox[1]

        if self.speed_x > 0:
            screen.blit(self.image_right, (x,y))
            self.hitbox[2], self.hitbox[3] = self.image_right.get_size()
        if self.speed_x < 0:
            screen.blit(self.image_left, (x,y))
            self.hitbox[2], self.hitbox[3] = self.image_left.get_size()
        if self.speed_y < 0:
            screen.blit(self.image_up, (x,y))
            self.hitbox[2], self.hitbox[3] = self.image_up.get_size()
        if self.speed_y > 0:
            screen.blit(self.image_down, (x,y))
            self.hitbox[2], self.hitbox[3] = self.image_down.get_size()

        #pg.draw.rect(screen, yellow, self.hitbox)

    def offscreen(self):
        if self.hitbox[0] < 0 or self.hitbox[0] > 750 or self.hitbox[1] < 0 or self.hitbox[1] > 550:
            return 1
        else:
            return 0

class Cash():

    def __init__(self):
        self.image = pg.image.load('Cash.png')
        w,h = self.image.get_size()
        x = random.randint(0,750)
        y = random.randint(0,550)
        self.hitbox = pg.Rect(x,y, w, h)


    def respawn(self):
        x = random.randint(0,750)
        y = random.randint(0,550)
        self.hitbox = pg.Rect(x,y, 50, 50)

    def draw(self):
        x, y = self.hitbox[0], self.hitbox[1]
        screen.blit(self.image, (x,y))

        #pg.draw.rect(screen, red, self.hitbox)

speed = 10
score = 0
playing = 1

cash = Cash()
cab = Cab()
cab.speed_y = -speed

while playing:
    pg.event.pump()

    cab.update()

    keys = pg.key.get_pressed()

    if keys[pg.K_UP]:
        cab.speed_y = -speed
        cab.speed_x = 0
    elif keys[pg.K_LEFT]:
        cab.speed_y = 0
        cab.speed_x = -speed
    elif keys[pg.K_RIGHT]:
        cab.speed_y = 0
        cab.speed_x = speed
    elif keys[pg.K_DOWN]:
        cab.speed_y = speed
        cab.speed_x = 0

    if cab.hitbox.colliderect(cash.hitbox):
        cash.respawn()
        score += 1

    if cab.offscreen():
        playing = 0

    screen.fill(white)
    ex.printText(screen, black,score, 0,0,50)
    cab.draw()
    cash.draw()
    pg.display.flip()

    clock.tick(60)
