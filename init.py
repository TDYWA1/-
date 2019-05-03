#coding=utf-8
import os
from 飞机大战.plane_sprite import *
import pygame

pygame.init()

window = pygame.display.set_mode((440,709))
back = pygame.image.load("./image/back.png")
plane = pygame.image.load('./image/fly.png')

window.blit(back,(0,0))
window.blit(plane,(50,600))
pygame.display.update()

clock = pygame.time.Clock()
start = pygame.Rect(50,600,50,73)

enermy = Gamesprite('./image/enermy.png')
enermy1 = Gamesprite('./image/enermy.png',2)
enermy_gp = pygame.sprite.Group(enermy,enermy1)


while True:
    clock.tick(70)
    start.y -=1
    event = pygame.event.get()
    for e in event:
        if e.type==pygame.QUIT:
            pygame.quit()
            print("退出游戏")
            exit()
    if start.bottom<=0:
        start.y=709
    window.blit(back,(0,0))
    window.blit(plane,start)

    enermy_gp.update()
    enermy_gp.draw(window)

    pygame.display.update()

pygame.quit()