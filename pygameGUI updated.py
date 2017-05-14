import sys, os # TODO: transparent button feature, click and drag around
import glob #toolbar at bottom,
import pygame
import inputbox
from win32api import GetSystemMetrics
import requests
import pymysql
from pygame.locals import*
""" Open file
a.open("fileIDs.txt","r")
b=a.read()
b.close()
"""
hostname = '192.168.2.6'
username = 'root'
password = 'root'
database = 'angelhack'
conn = pymysql.connect(host = hostname, user = username, passwd = password, db = database)

imageChosen=False
touch=False
w=GetSystemMetrics(0)
h=GetSystemMetrics(1)
white = (255, 255, 255,0)
cyan = (0,255,255)
thomasblue = (0,182,255)#00b6ff
blueBox=(0,0,255)
pygame.init()
size=(w,h)
myfont = pygame.font.SysFont("myriadwebpro", 15)
screen = pygame.display.set_mode(size)
#screen.fill(white, None, pygame.BLEND_RGBA_MULT)
pygame.display.set_mode((w,h),pygame.FULLSCREEN)
gamestate=0
while True:
    img = pygame.image.load('whitealpha.png').convert_alpha()

    screen.fill(white)
    screen.blit(img,(0,0))
    l1=(50,50,200,50)
    l2=(w-250,50,200,50)
    l3=(int(w/2)-150,int(h/2)-50,300,100)
    l4=(50,h-100,200,50)
    l5=(w-250,h-100,200,50)
    inp=""

    
    
    if imageChosen==True:
        screen.blit(img0,(int(w/2-sz[0]*.1),int(h/2-sz[1]*.1)))
    button1=pygame.draw.rect(screen, thomasblue,l1)
    button2=pygame.draw.rect(screen, thomasblue,l2)
    button3=pygame.draw.rect(screen, thomasblue,l3)
    button4=pygame.draw.rect(screen, thomasblue,l4)
    button5=pygame.draw.rect(screen, thomasblue,l5)

    
    def getURL(uniqueid):
        cur = conn.cursor()
        cur.execute("SELECT data, active FROM images WHERE uniqueid = " + uniqueid)
        for data, active in cur.fetchall():
            if active == 1:
                    return "false"
            else:
                    #cur.execute("UPDATE images SET active = 1 WHERE uniqueid = " + uniqueid)
                    conn.commit()
                    return data

    #duplicate this for all boxes
    def words():
        label1 = myfont.render("Upload Image", 1, blueBox)
        screen.blit(label1, (75, 65))#x+25,y+15 to center in box
        label2 = myfont.render("Calibrate", 1, blueBox)
        screen.blit(label2, (w-250+25, 65))#x+5,y+15 to center in box
        label3 = myfont.render("Start Shopping", 1, blueBox)
        screen.blit(label3, (int(w/2)-150+75,int(h/2)-50+40))#x+5,y+15 to center in box
        label4 = myfont.render("Previous Photos", 1, blueBox)
        screen.blit(label4, (75, h-100+15))#x+5,y+15 to center in box
        label5 = myfont.render("Help", 1, blueBox)
        screen.blit(label5, (w-250+25, h-100+15))#x+5,y+15 to center in box
    words()
    def resetscreen():
        screen.fill((white))
        screen.blit(img,(0,0))
        pygame.display.flip()
    def detectquit():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: #Press 0key to escape for now
                    if event.key == pygame.K_0:
                        pygame.quit();
    def bgref():
        bar=pygame.draw.rect(screen, thomasblue,(0,h-150,w,h-150))
        screen.blit(img0,(int(w-50),int(h-50)))
        buttonB=pygame.draw.rect(screen, thomasblue,l1)
        buttonN=pygame.draw.rect(screen, thomasblue,l2)
        label1 = myfont.render("Cancel", 1, blueBox)
        screen.blit(label1, (75, 65))#x+25,y+15 to center in box
        label2 = myfont.render("Confirm Image", 1, blueBox)
        screen.blit(label2, (w-250+25, 65))#x+5,y+15 to center in box
        #img0=pygame.transform.scale(img0,(int(sz[0]*.02),int(sz[1]*.02)))
        pygame.display.flip()
    while gamestate==0:
        pygame.display.update()
        pygame.display.flip()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if button1.collidepoint(mouse_pos):
                        print('button1 was pressed at {0}'.format(mouse_pos)) #upload
                        pygame.draw.rect(screen, cyan,l1)
                        inp = str(inputbox.ask(screen, 'ImageID',50,65))
                        print inp
                        #words()
                        #pygame.draw.rect(screen, thomasblue,l1)
                        resetscreen()
                        gamestate=1
                    if button2.collidepoint(mouse_pos):
                        print('button2 was pressed at {0}'.format(mouse_pos)) #calibrate
                        pygame.draw.rect(screen, cyan,l2)
                        resetscreen()
                        gamestate=20
                    if button3.collidepoint(mouse_pos):
                        print('button3 was pressed at {0}'.format(mouse_pos)) #start shopping
                        pygame.draw.rect(screen, cyan,l3)
                        resetscreen()
                        gamestate=3
                    if button4.collidepoint(mouse_pos):
                        print('button4 was pressed at {0}'.format(mouse_pos)) #previous photos
                        pygame.draw.rect(screen, cyan,l4)
                        resetscreen()
                        gamestate=4
                    if button5.collidepoint(mouse_pos):
                        print('button5 was pressed at {0}'.format(mouse_pos)) #help
                        pygame.draw.rect(screen, cyan,l5)
                        resetscreen()
                        gamestate=5
            if event.type == pygame.KEYDOWN: #Press 0key to escape for now
                    if event.key == pygame.K_0:
                        pygame.quit();

    if gamestate==1:
        u=str(getURL(inp))
        if "uploadimages" not in u:
            print "Invalid ID"
            gamestate=0
            break
        dir = os.path.dirname(__file__)
        path = sys.path[0]+'\\Ham\\uploadimages\\'+u[13:]
        """
        files=glob.glob(path)
        c=0
        for name in files:
            if "C:/" in name:
                counter=str(c)
                a="img"+counter+"=pygame.image.load('C:/Users/Matthew/Desktop/"+name[25:]+"')"
                print a
                exec(a)
                exec("screen.blit(img"+counter+",(0,0))")
                break"""
        while True:
            img0=pygame.image.load(path)
            sz= img0.get_rect().size
            #print sz
            img0=pygame.transform.scale(img0,(int(sz[0]*.2),int(sz[1]*.2)))
            #picture = pygame.transform.scale(picture, (1280, 720))
            screen.blit(img0,(int(w/2-sz[0]*.1),int(h/2-sz[1]*.1)))

            buttonB=pygame.draw.rect(screen, thomasblue,l1)
            buttonN=pygame.draw.rect(screen, thomasblue,l2)
            label1 = myfont.render("Cancel", 1, blueBox)
            screen.blit(label1, (75, 65))#x+25,y+15 to center in box
            label2 = myfont.render("Confirm Image", 1, blueBox)
            screen.blit(label2, (w-250+25, 65))#x+5,y+15 to center in box
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if buttonB.collidepoint(mouse_pos):
                            print('buttonB was pressed at {0}'.format(mouse_pos)) #upload
                            pygame.draw.rect(screen, cyan,l1)
                            resetscreen()
                            gamestate=0
                            break
                        if buttonN.collidepoint(mouse_pos):
                            print('buttonN was pressed at {0}'.format(mouse_pos)) #calibrate
                            pygame.draw.rect(screen, cyan,l2)
                            resetscreen()
                            imageChosen=True
                            gamestate=0
                            break
                if event.type == pygame.KEYDOWN: #Press 0key to escape for now
                    if event.key == pygame.K_0:
                        pygame.quit();
            if gamestate==0:
                resetscreen()
                break
           #TODO: Curl the image ID, display image ID as text, resize img, detect if been used or not 

    while gamestate==20:#calibrate with rainbow thingy
        path = sys.path[0]+'\\Ham\\calibration.jpg'
        img2= pygame.image.load(path)
        screen.blit(img2,(0,0))
        pygame.display.flip()
        next1=pygame.draw.rect(screen, thomasblue,l5)
        next1f = myfont.render("Next", 1, blueBox)
        screen.blit(next1f, (w-250+25, h-100+15))#x+5,y+15 to center in box
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if next1.collidepoint(mouse_pos):
                        print('button was pressed at {0}'.format(mouse_pos)) #upload
                        screen.blit(img,(0,0))
                        #resetscreen()
                        gamestate=21
            if event.type == pygame.KEYDOWN: #Press 0key to escape for now
                    if event.key == pygame.K_0:
                        pygame.quit();

    while gamestate==21:#calibrate part B with textbox
        inp = str(inputbox.ask(screen, 'ImageID',50,65))
        print inp
        next2=pygame.draw.rect(screen, thomasblue,l5)
        next2f = myfont.render("Next", 1, blueBox)
        screen.blit(next2f, (w-250+25, h-100+15))#x+5,y+15 to center in box
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if next2.collidepoint(mouse_pos):
                            print('button1 was pressed at {0}'.format(mouse_pos)) #upload
                            #words()
                            #pygame.draw.rect(screen, thomasblue,l1)
                            resetscreen()
                            gamestate=5
                            #resetscreen()
                            #words()
                            break
                if event.type == pygame.KEYDOWN: #Press 0key to escape for now
                        if event.key == pygame.K_0:
                            pygame.quit();

    while gamestate==3:
        detectquit()
        #shopping
        #toolbar has images
        first=True
        while True:
            bar=pygame.draw.rect(screen, thomasblue,(0,h-150,w,h-150))
            if first==True:
                img0=pygame.image.load(path)
                screen.blit(img0,(int(w-50),int(h-50)))
                sz= img0.get_rect().size
                img0=pygame.transform.scale(img0,(int(sz[0]*.1),int(sz[1]*.1)))
                first=False
            if touch==False:
                screen.blit(img0,(int(w-50),int(h-50)))
                sz= img0.get_rect().size
                print sz
                #
                
            else:
                screen.blit(img0,(tempx,tempy))
                #img0=pygame.transform.scale(img0,(int(sz[0]*.05),int(sz[1]*.05)))
            buttonB=pygame.draw.rect(screen, thomasblue,l1)
            buttonN=pygame.draw.rect(screen, thomasblue,l2)
            label1 = myfont.render("Cancel", 1, blueBox)
            screen.blit(label1, (75, 65))#x+25,y+15 to center in box
            label2 = myfont.render("Next", 1, blueBox)
            screen.blit(label2, (w-250+25, 65))#x+5,y+15 to center in box
            pygame.display.flip()
            #img0=pygame.image.load(path)
            
            
            
            #print img0.get_rect()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if buttonB.collidepoint(mouse_pos):
                            print('buttonB was pressed at {0}'.format(mouse_pos)) #upload
                            pygame.draw.rect(screen, cyan,l1)
                            resetscreen()
                            gamestate=0
                            break
                        if buttonN.collidepoint(mouse_pos):
                            print('buttonN was pressed at {0}'.format(mouse_pos)) #calibrate
                            pygame.draw.rect(screen, cyan,l2)
                            resetscreen()
                            imageChosen=True
                            gamestate=0
                            break
                        #rekt=img0.get_rect()
                        #rekt=(0, 0, 80, 60)
                        else:
                            mouse_pos2 = pygame.mouse.get_pos()
                            touch=True
                            resetscreen()
                            print "yes"
                            print mouse_pos
                            screen.blit(img0,((mouse_pos2[0]),mouse_pos2[1]))
                            tempx=mouse_pos2[0]
                            tempy=mouse_pos2[1]
                            #bar=pygame.draw.rect(screen, thomasblue,(0,h-150,w,h-150))
                            bgref()
                if event.type == pygame.KEYDOWN: #Press 0key to escape for now
                    if event.key == pygame.K_0:
                        pygame.quit();
            if gamestate==0:
                break

    while gamestate==4:
        detectquit()
        #previous photos

    while gamestate==5:
        detectquit()
        #help
