#coding=utf-8
import random
import pygame

GAME_WINDOW = pygame.Rect(0,0,440,709)
PER_SEC = 70
TIME_EVENT = pygame.USEREVENT
TIME_EVENT_FIRE = pygame.USEREVENT + 1

class Gamesprite(pygame.sprite.Sprite):
    def __init__(self,image,speed=1):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Background(Gamesprite):
    def __init__(self,is_alt=False):
        super().__init__('./image/back.png')
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y > GAME_WINDOW.height:
            self.rect.y = -self.rect.y

class Enemy(Gamesprite):
    def __init__(self):
        super().__init__('./image/enermy.png')
        self.speed = random.randint(1,5)
        self.rect.y = -self.rect.height
        self.rect.x = random.randint(1,GAME_WINDOW.width-self.rect.width)

    def update(self):
        super().update()
        if self.rect.y > GAME_WINDOW.height:
            self.kill()

    def __del__(self):
        #print("kill")
        pass

class Hero(Gamesprite):
    def __init__(self):
        super().__init__('./image/fly.png')
        self.speed = 0
        self.rect.x = GAME_WINDOW.centerx - self.rect.width/2
        self.rect.y = GAME_WINDOW.bottom - 120
    def update(self):
        if self.rect.x > GAME_WINDOW.width - self.rect.width:
            self.rect.x = GAME_WINDOW.width - self.rect.width
        elif self.rect.x < 0:
            self.rect.x = 0
        self.rect.x += self.speed

class Zidan(Gamesprite):
    def __init__(self):
        super().__init__('./image/fire.png',-1)
