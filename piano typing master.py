 # importing libraries
import pygame
from random import *
import os
pygame.mixer.init()
pygame.init()

# window geometry
win_height=700
win_width=400
win=pygame.display.set_mode((win_width,win_height))

# colors defining
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

#system varibles
fps=55
clock=pygame.time.Clock()

#Background Image
homepagebg = pygame.image.load("homepage.png")    #for homescreen
homepagebg = pygame.transform.scale(homepagebg, (win_width, win_height)).convert_alpha()
gameoverbg = pygame.image.load("gameover.png")    #for gameover screen
gameoverbg = pygame.transform.scale(gameoverbg, (win_width, win_height)).convert_alpha()
creditbg = pygame.image.load("creditbg.png")    #for credit screen
creditbg = pygame.transform.scale(creditbg, (win_width, win_height)).convert_alpha()

#gameIcon
icon= pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Game Title
pygame.display.set_caption("PIANO MASTER")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

# homescreen variable page
def homescreen():
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    exit_game = False
    while not exit_game:
        win.fill(white)
        win.blit(homepagebg,(0,0))
        screen_text = font.render("HIGHEST SCORE:"+str(highscore), True, white)
        win.blit(screen_text, (10,30)) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pygame.mixer.music.load('bgmusic.mp3')
                    pygame.mixer.music.play(1000)
                    pygame.mixer.music.set_volume(6)
                    pianotiles()
                if event.key==pygame.K_c:
                    credit()
                if event.key==pygame.K_q:
                    quit()
        pygame.display.update()
        clock.tick(fps)
# game screen variable
def pianotiles():
    # drawing rectangle
    font = pygame.font.SysFont(None, 55)
    rect1=pygame.Rect(0,0,100,200)
    rect2=pygame.Rect(100,randint(-500,-30),100,200)
    rect3=pygame.Rect(200,randint(-500,-30),100,200)
    rect4=pygame.Rect(300,randint(-500,-30),100,200)
    score=0
    vel=3
    game_over = False
    # high score file
    if (not os.path.exists("highscore.txt")):
        with open ("highscore.txt","w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    while not game_over:
        win.fill(white)
        #For black lines between the tiles
        pygame.draw.rect(win, black,(100,0,2,win_height))
        pygame.draw.rect(win, black,(200,0,2,win_height))
        pygame.draw.rect(win, black,(300,0,2,win_height))
        pygame.draw.rect(win, black,(400,0,2,win_height))

        pygame.draw.rect(win, black, rect1)
        rect1.y+=vel     
        pygame.draw.rect(win, black, rect2)
        rect2.y+=vel
        pygame.draw.rect(win, black, rect3)
        rect3.y+=vel      
        pygame.draw.rect(win, black, rect4)
        rect4.y+=vel
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                exit_game = True
            if event.type==pygame.MOUSEBUTTONUP:
                if  rect1.collidepoint(event.pos):
                    pygame.mixer.music.load('k1music.mp3')
                    pygame.mixer.music.play()
                    rect1.y=randint(-500,-100)
                    score+=1
                if  rect2.collidepoint(event.pos):
                    pygame.mixer.music.load('k2music.mp3')
                    pygame.mixer.music.play()
                    rect2.y=randint(-500,-100)
                    score+=1
                if  rect3.collidepoint(event.pos):
                    pygame.mixer.music.load('k3music.mp3')
                    pygame.mixer.music.play()
                    rect3.y=randint(-500,-100)
                    score+=1
                if  rect4.collidepoint(event.pos):
                    pygame.mixer.music.load('k4music.mp3')
                    pygame.mixer.music.play()
                    rect4.y=randint(-500,-100)
                    score+=1
                if score>int(highscore):
                    highscore=score
                
        with open ("highscore.txt","w") as f:
            f.write(str(highscore))
        if rect1.y>win_height-200 or rect2.y>win_height-200 or rect3.y>win_height-200 or rect4.y>win_height-200:
            pygame.mixer.music.load('buzzer.mp3')
            pygame.mixer.music.play()
            end_screen(score)

        screen_text = font.render("score:"+str(score), True, red)
        win.blit(screen_text, (2,2))  
        screen_text = font.render("highscore:"+str(highscore), True, red)
        win.blit(screen_text, (2,30)) 
        pygame.display.update()
        clock.tick(fps)

# Game over page 
def end_screen(score):
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    exit_game=False
    while not exit_game:
        win.fill(white)
        win.blit(gameoverbg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pianotiles()
                if event.key== pygame.K_SPACE:
                    homescreen()
        screen_text = font.render("highscore:"+str(highscore), True, white)
        win.blit(screen_text, (2,30)) 
        screen_text = font.render("your score:"+str(score), True, white)
        win.blit(screen_text, (2,2))  
        pygame.display.update()
        clock.tick(fps)

#credit window
def credit():
    exit_game = False
    while not exit_game:
        win.fill(white)
        win.blit(creditbg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                exit_game = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                    homescreen()
        pygame.display.update()
        clock.tick(fps)
homescreen()
quit()