#encoding=utf-8
import pygame
from 飞机大战.plane_sprite import *




class Planemain:
    def __init__(self):
        print("game init")
        #创建游戏窗口
        self.window = pygame.display.set_mode(GAME_WINDOW.size)
        #创建游戏时钟
        self.clock = pygame.time.Clock()
        #初始化精灵族
        self.__createsprite()
        #创建敌机事件
        pygame.time.set_timer(TIME_EVENT,1000)
        pygame.time.set_timer(TIME_EVENT_FIRE,500)




    def __createsprite(self):
        back1 = Background()
        back2 = Background(True)
        self.gropback = pygame.sprite.Group(back1,back2)
        # 创建敌机精灵组
        self.enemygroup = pygame.sprite.Group()
        #创建hero
        self.hero = Hero()
        self.herogrop = pygame.sprite.Group(self.hero)
        #创建fire
        self.ziangroup = pygame.sprite.Group()

    def __event_hander(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()

            elif event.type == TIME_EVENT:
                enemy = Enemy()
                self.enemygroup.add(enemy)
            elif event.type == TIME_EVENT_FIRE:
                print("zidan")
                fire = Zidan()
                fire.rect.y = self.hero.rect.y - fire.rect.height
                fire.rect.x = self.hero.rect.x + self.hero.rect.width/2 - fire.rect.width/2
                self.ziangroup.add(fire)


           # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #    print("right")
        keypress = pygame.key.get_pressed()
        if keypress[pygame.K_RIGHT]:
            #print("right")
            self.hero.speed = 2
        elif keypress[pygame.K_LEFT]:
            #print("left")
            self.hero.speed = -2
        else :
            self.hero.speed = 0


    def __check_collide(self ):
        pygame.sprite.groupcollide(self.ziangroup,self.enemygroup,True,True)
        ennemy = pygame.sprite.spritecollide(self.hero,self.enemygroup,True)
        if len(ennemy) > 0:
            self.hero.kill()
            self.__game_over()
            

    def __update_sprite(self):
        self.gropback.update()
        self.gropback.draw(self.window)

        self.enemygroup.update()
        self.enemygroup.draw(self.window)

        self.herogrop.update()
        self.herogrop.draw(self.window)

        self.ziangroup.update()
        self.ziangroup.draw(self.window)

    @staticmethod
    def __game_over():
        pygame.quit()
        print("游戏结束")
        exit()

    def start_game(self):
        print("game start...")
        while True:
            #设置刷新帧率
            self.clock.tick(PER_SEC)
            #事件监听
            self.__event_hander()
            #碰撞检测
            self.__check_collide()
            #更新/绘制精灵组
            self.__update_sprite()
            #更新显示
            pygame.display.update()
            pass

if __name__ == '__main__':
    game = Planemain()
    game.start_game()