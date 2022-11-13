import os
import random
import sys
import time

import pygame
import win32con
import win32gui

from CONST import *
from visual_settings import *

if konsola == False:
    the_program_to_hide = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

window = pygame.display.set_mode((WIDTH, HEIGHT))
background_image = pygame.image.load("img/background-image.png")

pygame.init()

class Player():
    def __init__(self):
        self.image = pygame.image.load("img/none-box.png")
        self.x_cord = 300
        self.y_cord = 230
        self.width = 0
        self.height = 0
    
    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

    def paper(self):
        self.image = pygame.image.load("img/paper.png")

    def stone(self):
        self.image = pygame.image.load("img/stone.png")
    
    def scissors(self):
        self.image = pygame.image.load("img/scissors.png")

    def refresh(self):
        self.image = pygame.image.load("img/none-box.png")

    def scissors_event(self):
        if self.image == "img/scissors.png":
            print("Prawda2")
            return True
        
    def rock_event(self):
        if self.image == "img/stone.png":
            print("Prawda2")
            return True
        
    def paper_event(self):
        if self.image == "img/paper.png":
            print("Prawda2")
            return True
    
class Button2():
    def __init__(self):
        self.image = pygame.image.load("img/button_paper.png")
        self.image_hover = pygame.image.load("img/button_paper_hovered.png")
        self.x_cord = 420
        self.y_cord = 175
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
                 
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
            # print("Fałsz")
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))

class Button3():
    def __init__(self):
        self.image = pygame.image.load("img/button_stone.png")
        self.image_hover = pygame.image.load("img/button_stone_hovered.png")
        self.x_cord = 575
        self.y_cord = 175
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
                 
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
            # print("Fałsz")
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))

class Button4():
    def __init__(self):
        self.image = pygame.image.load("img/button_scissors.png")
        self.image_hover = pygame.image.load("img/button_scissors_hovered.png")
        self.x_cord = 730
        self.y_cord = 175
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
            
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
            # print("Fałsz")
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))

class Computer:
    def __init__(self):
        self.x_cord = 750
        self.y_cord = 230
        self.width = 0
        self.height = 0
        self.image = pygame.image.load("img/none-box.png")
        self.options = [pygame.image.load("img/paper.png"), 
                        pygame.image.load("img/stone.png"), 
                        pygame.image.load("img/scissors.png")]

    def work(self):
        self.image = random.choice(self.options) 
        window.blit(self.image, (self.x_cord, self.y_cord))
    
    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

    def refresh(self):
        self.image = pygame.image.load("img/none-box.png")

    def scissors_event(self):
        if self.image == "img/scissors.png":
            print("Prawda")
            return True
        
    def rock_event(self):
        if self.image == "img/stone.png":
            print("Prawda")
            return True
        
    def paper_event(self):
        if self.image == "img/paper.png":
            print("Prawda")
            return True
    
class Button1():
    def __init__(self):
        self.image = pygame.image.load("img/button_fight.png")
        self.image_hover = pygame.image.load("img/button_fight_hovered.png")
        self.x_cord = 550
        self.y_cord = 510
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
            
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
            # print("Fałsz")
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))
            # print("prawda")

class Gameplay():
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("img/air.png")

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

    def win(self):
        self.image = pygame.image.load("img/win.png")

    def defeat(self):
        self.image = pygame.image.load("img/defeat.png")

    def remis(self):
        self.image = pygame.image.load("img/remis.png")
    
    def clear(self):
        self.image = pygame.image.load("img/air.png")

class Wyjscie():
    def __init__(self):
        self.image = pygame.image.load("img/exit_x.png")
        self.image_hover = pygame.image.load("img/exit_x_hovered.png")
        self.x_cord = 1230
        self.y_cord = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
            
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
            # print("Fałsz")
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))

class Comunicats():
    def __init__(self):
        self.image = pygame.image.load("img/event-image.png")
        self.x_cord = -450
        self.y_cord = 550

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))
    
    def tick(self):
        self.x_cord = 300
        # time.sleep(3)
        # self.x_cord -= 460
    def ret(self):
        self.x_cord = -450

class Music_button():
    def __init__(self):
        self.image = pygame.image.load("img/button_music.png")
        self.image_hover = pygame.image.load("img/button_music_hovered.png")
        self.x_cord = 0
        self.y_cord = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
                
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))

class Music1_button():
    def __init__(self):
        self.image = pygame.image.load("img/button_music.png")
        self.image_hover = pygame.image.load("img/button_music_hovered.png")
        self.x_cord = 200
        self.y_cord = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
                
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))

class Refresh():
    def __init__(self):
        self.image = pygame.image.load("img/refresh.png")
        self.image_hover = pygame.image.load("img/refresh_hovered.png")
        self.x_cord = 1175
        self.y_cord = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True       
            
    def draw(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.image_hover, (self.x_cord, self.y_cord))
        else:
            window.blit(self.image, (self.x_cord, self.y_cord))

class VS():
    def __init__(self):
        self.image = pygame.image.load("img/vs-icon.png")
        self.x_cord = 550
        self.y_cord = 280

    def draw(self):
        window.blit(self.image, (self.x_cord, self.y_cord))

def update():
    pygame.display.update()

def main():
    player = Player()
    computer = Computer()
    button1 = Button1()
    button2 = Button2()
    button3 = Button3()
    button4 = Button4()
    wyjscie = Wyjscie()
    refresh = Refresh()
    gameplay = Gameplay()
    comunicats = Comunicats()
    music = Music_button()
    music1 = Music1_button()
    vs = VS()
    score_computer = 0
    score_player = 0
    run = True
    varrible_work = True
    clock = 0
    while run:
        clock += pygame.time.Clock().tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        font = pygame.font.SysFont("arial", 25)
        text = font.render(f"User: {score_player}", False, [0,0,0])

        font2 = pygame.font.SysFont("arial", 25)
        text2 = font2.render(f"Computer: {score_computer}", False, [0,0,0])
        
        window.blit(background_image, (0,0))

        
        player.draw()
        computer.draw()
        if varrible_work == True:
            if button1.tick():
                varrible_work = False
                computer.work()
                time.sleep(0.1)
                update()



        if varrible_work == True:
            if button2.tick():
                player.paper()
                update()

        if varrible_work == True:
            if button3.tick():
                player.stone()
                update()

        if varrible_work == True:
            if button4.tick():
                player.scissors()
                update()

        if refresh.tick():
            varrible_work = True
            comunicats.ret()
            player.refresh()
            computer.refresh()

        if wyjscie.tick():
            run = False

        if player.paper_event() == True and computer.scissors_event() == True:
            gameplay.defeat()
            score_computer += 1
            update()
        if player.paper_event() == True and computer.stone_event() == True:
            gameplay.win()
            score_player += 1
            update()
        if player.paper_event() == True and computer.paper_event() == True:
            gameplay.remis()
            score_player += 1
            score_computer += 1
            update()
        if player.rock_event() == True and computer.paper_event() == True:
            gameplay.defeat()
            score_computer += 1
            update()
        if player.rock_event() == True and computer.scissors_event() == True:
            gameplay.win()
            score_player += 1
            update()
        if player.rock_event() == True and computer.rock_event() == True:
            gameplay.remis()
            score_player += 1
            score_computer += 1
            update()
        if player.scissors_event() == True and computer.rock_event() == True:
            gameplay.defeat()
            score_computer += 1
            update()
        if player.scissors_event() == True and computer.paper_event() == True:
            gameplay.win()
            score_player += 1
            update()
        if player.scissors_event() == True and computer.scissors_event() == True:
            gameplay.remis()
            score_player += 1
            score_computer += 1
            update()

        
            
    

        button1.draw()
        button2.draw()
        button3.draw()
        button4.draw()
        wyjscie.draw()
        refresh.draw()
        comunicats.draw()
        gameplay.draw()
        vs.draw()
        update()

if __name__ == "__main__":
    main()