import sys
import datetime
import time
import pygame
import inputbox
import requests #curl, text on the boxes, color
from pygame.locals import*
""" Open file
a.open("fileIDs.txt","r")
b=a.read()
b.close()
"""
white = (255, 64, 64)
bright_red = (255,0,0)
bright_green = (0,182,255)#00b6ff
pygame.init()
w = 1280
h = 800
size=(w,h)
myfont = pygame.font.SysFont("monospace", 15)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
screen.fill(white)
#pygame.display.set_mode()
pygame.display.set_mode((w,h),pygame.FULLSCREEN)
gamestate=0
img = pygame.image.load('white.jpg')

screen.fill(white)
screen.blit(img,(0,0))
l1=(50,50,200,50)
l2=(1030,50,200,50)
l3=(490,350,300,100)
l4=(50,700,200,50)
l5=(1030,700,200,50)


button1=pygame.draw.rect(screen, bright_green,l1)
button2=pygame.draw.rect(screen, bright_green,l2)
button3=pygame.draw.rect(screen, bright_green,l3)
button4=pygame.draw.rect(screen, bright_green,l4)
button5=pygame.draw.rect(screen, bright_green,l5)

#duplicate this for all boxes
label1 = myfont.render("Upload Image", 1, (0,0,255))
screen.blit(label1, (155, 465))#x+5,y+15 to center in box
label2 = myfont.render("Calibrate", 1, (0,0,255))
screen.blit(label2, (155, 465))#x+5,y+15 to center in box
label3 = myfont.render("Start Shopping", 1, (0,0,255))
screen.blit(label3, (155, 465))#x+5,y+15 to center in box
label4 = myfont.render("Previous Photos", 1, (0,0,255))
screen.blit(label4, (155, 465))#x+5,y+15 to center in box
label5 = myfont.render("Help", 1, (0,0,255))
screen.blit(label5, (155, 465))#x+5,y+15 to center in box

while gamestate==0:
    pygame.display.update()
    pygame.display.flip()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos):
                    print('button1 was pressed at {0}'.format(mouse_pos)) #upload
                    pygame.draw.rect(screen, bright_red,l1)
                    inp = int(inputbox.ask(screen, 'ImageID'))
                    print inp
                if button2.collidepoint(mouse_pos):
                    print('button2 was pressed at {0}'.format(mouse_pos)) #calibrate
                    pygame.draw.rect(screen, bright_red,l2)
                if button3.collidepoint(mouse_pos):
                    print('button3 was pressed at {0}'.format(mouse_pos)) #start shopping
                    pygame.draw.rect(screen, bright_red,l3)
                if button4.collidepoint(mouse_pos):
                    print('button4 was pressed at {0}'.format(mouse_pos)) #previous photos
                    pygame.draw.rect(screen, bright_red,l4)
                if button5.collidepoint(mouse_pos):
                    print('button5 was pressed at {0}'.format(mouse_pos)) #help
                    pygame.draw.rect(screen, bright_red,l5)
        if event.type == pygame.KEYDOWN: #Press 0key to escape for now
            if event.key == pygame.K_0:
                pygame.quit();

                    

    """for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                pygame.quit();
                #print("Correct! ")
                #gamestate=1
                break
    #print gamestate
    if gamestate==1:
        break

    if gamestate==6:
        break

"""


sys.exit()
