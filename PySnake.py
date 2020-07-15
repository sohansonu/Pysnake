import pygame
import time
import threading
import random
from playsound import playsound

pygame.init()

win=pygame.display.set_mode((800,600))

pygame.display.set_caption("Type em All")




def Text(st,x,y,bg=(0,0,0),color=(255,255,255),size=48):
    font = pygame.font.Font('freesansbold.ttf', size) 
      
    text = font.render(st, True, color, bg) 
      
    # create a rectangular object for the 
    # text surface object 
    textRect = text.get_rect()  
      
    # set the center of the rectangular object. 
    textRect.center = (x,y)
    win.blit(text,textRect)

    

    


def Smove(path,pos):
    global SCORE
    global POINT
    x=pos[0][0]
    y=pos[0][1]
    
    if path=='up':
        y-=10
        

    elif path=='down':
        y+=10
        

    elif path=='left':
        x-=10
        

    elif path=='right':    
        x+=10

    
    if POINT[0]==x and POINT[1]==y:
        pos.insert(0,[x,y])
        SCORE+=5
        POINT=[]
    
        
    else:    
        pos.pop()
        pos.insert(0,[x,y])
    return pos    

def Play():
    global Bsnake
    global Ysnake
    global SCORE
    global POINT
    BSM='left'
    YSM='right'
    win.fill((0,0,0))
    SCORE=0
    run=True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            
        keys=pygame.key.get_pressed()

        if keys[pygame.K_w] and BSM!='down':
            BSM='up'
        elif keys[pygame.K_s] and BSM!='up':
            BSM='down'
        elif keys[pygame.K_a] and BSM!='right':
            BSM='left'
        elif keys[pygame.K_d] and BSM!='left':
            BSM='right'
        if keys[pygame.K_UP] and YSM!='down':
            YSM='up'
        elif keys[pygame.K_DOWN] and YSM!='up':
            YSM='down'
        elif keys[pygame.K_LEFT] and YSM!='right':
            YSM='left'
        elif keys[pygame.K_RIGHT] and YSM!='left':
            YSM='right'
        elif keys[pygame.K_SPACE]:
            pygame.sleep(10)
            
        if POINT==[]:
            px=random.randrange(10,790)
            py=random.randrange(10,590)
            px=px-(px%10)
            py=py-(py%10)
            POINT=[px,py]

        Ysnake=Smove(YSM,Ysnake)
        
        if POINT==[]:
            px=random.randrange(10,790)
            py=random.randrange(10,590)
            px=px-(px%10)
            py=py-(py%10)
            POINT=[px,py]
            
        Bsnake=Smove(BSM,Bsnake)
        
        bx=Bsnake[0][0]
        by=Bsnake[0][1]
        yx=Ysnake[0][0]
        yy=Ysnake[0][1]

        
        
        if (([bx,by] in Ysnake) or ([yx,yy] in Bsnake)):
            print("snake collision")
            return SCORE
            
        if bx<0 or bx>800 or by<0 or by>600:
            return SCORE
        if yx<0 or yx>800 or yy<0 or yy>600:
            return SCORE
        
        win.fill((0,0,0))
            
        try:
                
            for i,j in Bsnake:
                pygame.draw.rect(win,(0,0,255),(i,j,10,10))
                pygame.draw.rect(win,(0,0,0),(i,j,11,11),1)
            for p,q in Ysnake:
                pygame.draw.rect(win,(255,255,0),(p,q,10,10))
                pygame.draw.rect(win,(0,0,0),(p,q,11,11),1)
        except:
            continue
        try:
            pygame.draw.rect(win,(255,0,0),(POINT[0],POINT[1],10,10))
        except:
            continue
        Text("SCORE : "+str(SCORE),700,30,size=18)
        pygame.display.update()
    print("menu")
    return SCORE                    
            
                    


POINT=[]
Bsnake=[]
Ysnake=[]
logo=pygame.image.load("logo.png")
logo=pygame.transform.scale(logo,(128,128))
SCORE=0
def MENU():
    global SCORE
    global Bsnake
    global Ysnake
    global POINT
    SCORE=0
    HIGHSCORE=0
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        
        Bsnake=[[370,250],[380,250],[390,250],[390,260],[390,270],[380,270],[370,270],[360,270],[360,280],[360,290],[360,300]]
        Ysnake=[[400,310],[390,310],[380,310],[380,300],[380,290],[390,290],[400,290],[410,290],[410,280],[410,270],[410,260]]
        
        ms=pygame.mouse.get_pressed()
        
        mx,my=pygame.mouse.get_pos()
        
        
        win.fill((0,0,0))
        win.blit(logo,(340,50))
        Text("controls :",405,420,color=(50,50,50),size=32)
        pygame.draw.rect(win,(0,0,255),(290,460,20,20))
        pygame.draw.rect(win,(255,255,0),(490,460,20,20))
        pygame.draw.circle(win,(0,0,0),(295,465),2)
        pygame.draw.circle(win,(0,0,0),(305,465),2)
        pygame.draw.circle(win,(0,0,0),(495,465),2)
        pygame.draw.circle(win,(0,0,0),(505,465),2)
        
        Text("w a s d",300,510,color=(50,50,50),size=24)
        Text("up down left right",500,510,color=(50,50,50),size=24)
        if mx>250 and mx<550 and my>200 and my<300:
            Text("EXIT",400,350)
            Text("PLAY",400,250,(0,0,0),size=64)
            Text("High score:"+str(HIGHSCORE),700,30,size=18)
            pygame.display.update()
            if ms==(1,0,0):
                try:
                    POINT=[]
                    SCORE=Play()
                except:
                    continue
                try:
                    if HIGHSCORE<SCORE:
                        HIGHSCORE=SCORE
                except:
                    continue
        elif mx>250 and mx<550 and my>300 and my<400:
            
            Text("PLAY",400,250)
            
            Text("EXIT",400,350,(0,0,0),size=64)
            Text("High score:"+str(HIGHSCORE),700,30,size=18)
            pygame.display.update()
            if ms==(1,0,0):
                run=False
        else:
            
            Text("PLAY",400,250)
            Text("EXIT",400,350)
            Text("High score:"+str(HIGHSCORE),700,30,size=18)
            
            pygame.display.update()
            
            
    pygame.quit()            
            
MENU()    
    











            
