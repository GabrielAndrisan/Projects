import numpy as np
import random  
import pygame as pg
import time
clock = pg.time.Clock()
pg.init()

    # dimensiune matrice
lungime=10
inaltime=10
iii=0
jjj=0
    #numarul de bombe
nr_bmb=20
bombe=0
    #initializare matrici
M=np.zeros((lungime,inaltime),dtype=int)
Mverif=np.zeros((lungime,inaltime),dtype=int)
MM=np.zeros((lungime,inaltime),dtype=int)
Mprobabil=np.zeros((lungime,inaltime),dtype=int)

    #plasare bombe
for i in range(nr_bmb): 
    Q=random.randint(0,9)
    W=random.randint(0,9)
    if M[Q][W] !=99:
        M[Q][W]=99
        bombe+=1
    else:
        i=i-1

    #plasare cifrelor in matrice
for i in range(lungime):
    for j in range(inaltime):
         if M[i][j]>=99:
            if i-1>=0:
                if j-1>=0:
                    M[i-1][j-1]+=1
                M[i-1][j]+=1
                if j+1<10:
                    M[i-1][j+1]+=1
            if j-1>=0:
                M[i][j-1]+=1
            if j+1<10:    
                M[i][j+1]+=1
            if i+1<10:
                if j-1>=0:
                    M[i+1][j-1]+=1
                M[i+1][j]+=1
                if j+1<10:
                    M[i+1][j+1]+=1

    #corectarea plasarii pt bombe                 
for i in range(lungime):                                                                                                          
    for j in range(inaltime):
         if M[i][j]>=99:
            M[i][j]=99

    # dimensiuni ecran
screen_width=759
screen_height=759

    #mouse
left = 1
mid=2
right = 3
    #dimensiuni casute
rectwidth = int((screen_width-9)/lungime)
rectheight = int((screen_height-9)/inaltime)

    #distanta dintre patrate
rectdist = 1

    #afisarea ecranului
#screen = pg.display.set_mode([screen_width,screen_height])
screen = pg.display.set_mode((screen_width,screen_height), pg.WINDOWRESIZED)

screen.fill((0,0,0))
print(M) 
    #plasarea casutelor pe ecran
block_positions = []
for i in range(lungime):
    for j in range(inaltime):
        x = i * (rectdist + rectwidth) 
        y = j * (rectdist + rectheight)
        block_positions.append((x, y)) 
for x, y in block_positions:
    pg.draw.rect(screen, (128, 128, 128), (int(x), int(y), int(rectwidth), int(rectheight)))

    #incarcarea imaginilor
imp0 = pg.image.load("../0.png").convert()
imp1 = pg.image.load("./1.png").convert()
imp2 = pg.image.load("./2.png").convert()
imp3 = pg.image.load("./3.png").convert()
imp4 = pg.image.load("./4.png").convert()
imp5 = pg.image.load("./5.png").convert()
imp6 = pg.image.load("./6.png").convert()
imp7 = pg.image.load("./7.png").convert()
imp8 = pg.image.load("./8.png").convert()
impsteag = pg.image.load("./steag.png").convert()
imppoc = pg.image.load("./poc.png").convert()
impblank = pg.image.load("./blank.png").convert()
game_over = pg.image.load("./game_over.png").convert()
win = pg.image.load("./win.png").convert()
sad= pg.image.load("./sad.png").convert()
iar= pg.image.load("./iar.png").convert()
ez= pg.image.load("./ez.png").convert()
single= pg.image.load("./sg_plyr.png").convert()
bott= pg.image.load("./bot.png").convert()
nu_i_gata=pg.image.load("./nu_i_voie.png").convert()
titlu=pg.image.load("./minesweeper.png")

def valori(i,j,test):
    if Mverif[i][j]==0 and test!=15 :   
        if (M[i][j]==0):
            screen.blit(imp0, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
        if (M[i][j]==1):
            screen.blit(imp1, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
        if (M[i][j]==2):
            screen.blit(imp2, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
        if (M[i][j]==3):
            screen.blit(imp3, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))    
            Mverif[i][j]=1
        if (M[i][j]==4):
            screen.blit(imp4, (j * (rectdist + rectwidth) , i * (rectdist + rectheight))) 
            Mverif[i][j]=1
        if (M[i][j]==5):
            screen.blit(imp5, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))  
            Mverif[i][j]=1
        if (M[i][j]==6):
            screen.blit(imp6, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
        if (M[i][j]==7):
            screen.blit(imp7, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
        if (M[i][j]==8):
            screen.blit(imp8, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))    
            Mverif[i][j]=1   
        if (M[i][j]==99) and test==3:
            screen.blit(imppoc, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))        
            Mverif[i][j]=3
    else:
        if (MM[i][j]==0):
            screen.blit(imp0, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==1):
            screen.blit(imp1, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==2):
            screen.blit(imp2, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==3):
            screen.blit(imp3, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))    
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==4):
            screen.blit(imp4, (j * (rectdist + rectwidth) , i * (rectdist + rectheight))) 
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==5):
            screen.blit(imp5, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))  
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==6):
            screen.blit(imp6, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==7):
            screen.blit(imp7, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
            Mverif[i][j]=1
            Mprobabil[i][j]=0
        if (MM[i][j]==8):
            screen.blit(imp8, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))    
            Mverif[i][j]=1   
            Mprobabil[i][j]=0
        if (MM[i][j]==99) and test==3:
            screen.blit(imppoc, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))        
            Mverif[i][j]=3
#def contor pentru restart
contorR=0
contormeniu=3

def matriceR():
    screen.fill((0,0,0))

        #initializare matrici
    for i in range(lungime):
        for j in range(inaltime):
            M[i][j]=0
            Mverif[i][j]=0   
        #plasare bombe
    global bombe
    for i in range(nr_bmb):
        Q=random.randint(0,9)
        W=random.randint(0,9)
        if M[Q][W] !=99:
            M[Q][W]=99
            bombe+=1
        else:
            i=i-1

        #plasare cifrelor in matrice
    for i in range(lungime):
        for j in range(inaltime):
            if M[i][j]>=99:
                if i-1>=0:
                    if j-1>=0:
                        M[i-1][j-1]+=1
                    M[i-1][j]+=1
                    if j+1<10:
                        M[i-1][j+1]+=1
                if j-1>=0:
                    M[i][j-1]+=1
                if j+1<10:    
                    M[i][j+1]+=1
                if i+1<10:
                    if j-1>=0:
                        M[i+1][j-1]+=1
                    M[i+1][j]+=1
                    if j+1<10:
                        M[i+1][j+1]+=1

        #corectarea plasarii pt bombe                 
    for i in range(lungime):                                                                                                          
        for j in range(inaltime):
            if M[i][j]>=99:
                M[i][j]=99
    #apelarea functiei de plasare a casutelor pe ecran
    for x, y in block_positions:
        pg.draw.rect(screen, (128, 128, 128), (int(x), int(y), int(rectwidth), int(rectheight)))
    #afisare de test
    print(Mverif) 
    print(M) 

def vecinii(i,j):
    vecini=0
    if i-1>=0 and j-1 >=0 and Mverif[i-1][j-1]==0:
        vecini+=1
    if i-1>=0 and Mverif[i-1][j]==0:
        vecini+=1
    if i-1>=0 and j+1<10 and Mverif[i-1][j+1]==0:
        vecini+=1
    if j-1>=0 and Mverif[i][j-1]==0:
        vecini+=1
    if j+1<10 and Mverif[i][j+1]==0:
        vecini+=1
    if i+1<10 and j-1>=0 and Mverif[i+1][j-1]==0:
        vecini+=1
    if i+1<10 and Mverif[i+1][j]==0:
        vecini+=1
    if i+1<10 and j+1<10 and Mverif[i+1][j+1]==0:
        vecini+=1
    return vecini

    #definirea bot-ului
"""
def bot(contor_bot):
    clock.tick()
    if contor_bot==1:
        contorR=0
        bombe=0
        contormeniu=0
        matriceR()
        contor_bot+=1
    k=1
    for qq in range(lungime):
        for ww in range(inaltime):
            if M[qq][ww]==0 and k==1:
                MM[qq][ww]=0
                Mverif[qq][ww]=1
                Mprobabil[qq][ww]==0
                k+=1
                screen.blit(imp0, (ww *(rectdist + rectwidth) ,qq *(rectdist + rectheight)))    
            else:
                MM[qq][ww]=-1
                Mprobabil[qq][ww]=-1

    GG=100
    while GG>=0:             
        for i in range(lungime):
            for j in range(inaltime):
                if MM[i][j]==0 and Mverif[i][j]==1:
                    if i-1>=0 and j-1>=0 and Mverif[i-1][j-1]==0:
                        valori(i-1,j-1,15)
                        Mprobabil[i-1][j-1]=0
                    if i-1>=0 and Mverif[i-1][j]==0:
                        valori(i-1,j,15)    
                        Mprobabil[i-1][j]=0
                    if i-1>=0 and j+1<10 and Mverif[i-1][j+1]==0:
                        valori(i-1,j+1,15)
                        Mprobabil[i-1][j+1]=0
                    if j-1>=0 and Mverif[i][j-1]==0:
                        valori(i,j-1,15)
                        Mprobabil[i][j-1]=0
                    if j+1<10 and Mverif[i][j+1]==0:
                        valori(i,j+1,15)
                        Mprobabil[i][j+1]=0
                    if i+1<10 and j-1>=0 and Mverif[i+1][j-1]==0:
                        valori(i+1,j-1,15)
                        Mprobabil[i+1][j-1]=0
                    if i+1<10 and Mverif[i+1][j]==0:
                        valori(i+1,j,15)
                        Mprobabil[i+1][j]=0
                    if i+1<10 and j+1<10 and Mverif[i+1][j+1]==0:
                        valori(i+1,j+1,15)
                        Mprobabil[i+1][j+1]=0
        GG-=1
        
    for i in range(lungime):
        vecini=0
        for j in range(inaltime):
            vecini=vecinii(i,j)
            if Mverif[i][j]==0:
                if i-1>=0 and j-1 >=0 and Mverif[i-1][j-1]==0:
                    Mprobabil[i-1][j-1]+=(M[i-1][j-1])*100/vecini
                if i-1>=0 and Mverif[i-1][j]==0:
                    Mprobabil[i-1][j]+=(M[i-1][j])*100/vecini
                if i-1>=0 and j+1<10 and Mverif[i-1][j+1]==0:
                    Mprobabil[i-1][j+1]+=(M[i-1][j+1])*100/vecini
                if j-1>=0 and Mverif[i][j-1]==0:
                    Mprobabil[i][j-1]+=(M[i][j-1])*100/vecini
                if j+1<10 and Mverif[i][j+1]==0:
                    Mprobabil[i][j+1]+=(M[i][j+1])*100/vecini
                if i+1<10 and j-1>=0 and Mverif[i+1][j-1]==0:
                    Mprobabil[i+1][j-1]+=(M[i+1][j-1])*100/vecini
                if i+1<10 and Mverif[i+1][j]==0:
                    Mprobabil[i+1][j]+=(M[i+1][j])*100/vecini
                if i+1<10 and j+1<10 and Mverif[i+1][j+1]==0:
                    Mprobabil[i+1][j+1]+=(M[i+1][j+1])*100/vecini
    for i in range(lungime):
        for j in range(inaltime):
            if Mverif[i][j]==1:
                Mprobabil[i][j]==0

    #started = time() # ora
    #time.sleep(2)# timp pauza
"""

running = True
while running:  
    mx,my=pg.mouse.get_pos()
    clock.tick(60)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
   
    #variabila = f(actiune_mouse)
    #left, middle, right = pg.mouse.get_pressed()
  
    #afisarea casutelor apasate cu click stanga
    if event.type == pg.MOUSEBUTTONUP and event.button == left:
        #mx,my=pg.mouse.get_pos()
        for i in range(lungime):
            for j in range(inaltime):
                if my >= i * (rectdist + rectwidth) and my < (i+1) * (rectdist + rectwidth):
                    if mx >= j * (rectdist + rectheight) and mx < (j+1) * (rectdist + rectheight):
                        if Mverif[i][j]==0 :   
                            if (M[i][j]==0):
                                screen.blit(imp0, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
                                Mverif[i][j]=1
                            if (M[i][j]==1):
                                screen.blit(imp1, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
                                Mverif[i][j]=1
                            if (M[i][j]==2):
                                screen.blit(imp2, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
                                Mverif[i][j]=1
                            if (M[i][j]==3):
                                screen.blit(imp3, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))    
                                Mverif[i][j]=1
                            if (M[i][j]==4):
                                screen.blit(imp4, (j * (rectdist + rectwidth) , i * (rectdist + rectheight))) 
                                Mverif[i][j]=1
                            if (M[i][j]==5):
                                screen.blit(imp5, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))  
                                Mverif[i][j]=1
                            if (M[i][j]==6):
                                screen.blit(imp6, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
                                Mverif[i][j]=1
                            if (M[i][j]==7):
                                screen.blit(imp7, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
                                Mverif[i][j]=1
                            if (M[i][j]==8):
                                screen.blit(imp8, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))    
                                Mverif[i][j]=1
                            if (M[i][j]==99):
                                screen.blit(imppoc, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))    
                                Mverif[i][j]=3
                                for gata in range(lungime):
                                    for joaca in range(inaltime):
                                        valori(gata,joaca,3)   
                                #screen.blit(sad, (0 , 0))   
                                screen.blit(game_over, (((screen_width/2)-95)/2 , (screen_height/2)-95))
                                screen.blit(iar, (((screen_width/2)-95)*3/2 , (screen_height/2)-95))
                                #running=False
                                contorR=1
                                contormeniu=1
        
    #functie de restart
    if contorR ==1:
        if event.type == pg.MOUSEBUTTONUP and event.button == left:
            #mx,my=pg.mouse.get_pos() 
            if contormeniu == 1:
                if my >=  (screen_height/2)-95 and my < (screen_height/2)+190:
                    if mx >= ((screen_width/2)-95)*3/2 and mx < ((screen_width/2)+190)*3/2:  
                        contorR=0
                        bombe=0
                        contormeniu=0
                        matriceR()
                if my >=  (screen_height/2)-95 and my < (screen_height/2)+190:
                    if mx >= ((screen_width/2)-95)/2 and mx < ((screen_width/2)+95)/2+190: 
                        contormeniu=3
            if contormeniu==2:
                if my >=  (screen_height/2)+125 and my < (screen_height/2)+190:
                    if mx >= ((screen_width/2)-95) and mx < ((screen_width/2)+190):  
                        contorR=0
                        bombe=0
                        contormeniu=0
                        matriceR()
                if my >=  (screen_height/2)-125 and my < (screen_height/2)+125:
                    if mx >= ((screen_width/2)-125) and mx < ((screen_width/2)+125): 
                        contormeniu=3
                        bombe+=1

            if contormeniu==3:
                screen.fill((0,100,100))
                screen.blit(single, (( screen_width/2)-309 , (screen_height/2)+90))
                screen.blit(bott, (( screen_width/2)+103 , (screen_height/2)+90))
                screen.blit(titlu, (0,0))

                if my >=  (screen_height/2)+90 and my < (screen_height/2)+296:
                    if mx >= (screen_width/2)-309 and mx < (screen_width/2)-103: 
                        contorR=0
                        bombe=0
                        contormeniu=0
                        matriceR()
                if my >=  (screen_height/2)+90 and my < (screen_height/2)+296:
                    if mx >= (screen_width/2)+103 and mx < ( screen_width/2)+309:
                        screen.blit(nu_i_gata, (( screen_width/2)+103 , (screen_height/2)+90))
                        contor_bot=1
                        """for ibot  in range(lungime):
                            for jbot in range(inaltime):
                                bot(contor_bot)
                                contor_bot+=1
                        print(Mprobabil)
                        print(Mverif)
                        """
                        #bot()
                        #np.savetxt('text.txt',mat,fmt='%.2f') 

    #afisarea steagurilor pentru click dreapta
    if event.type == pg.MOUSEBUTTONUP and event.button == right:                      
        mx,my=pg.mouse.get_pos()
        for i in range(lungime):
            for j in range(inaltime):    
                if Mverif[i][j] == 0:
                    if my >= i * (rectdist + rectwidth) and my < (i+1) * (rectdist + rectwidth):
                        if mx >= j * (rectdist + rectheight) and mx < (j+1) * (rectdist + rectheight):
                            screen.blit(impsteag, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
                            Mverif[i][j]=5
             
    #eliminarea steagurilor cu click pe rotita
    if event.type == pg.MOUSEBUTTONUP and event.button == mid:                      
        #mx,my=pg.mouse.get_pos()
        for i in range(lungime):
            for j in range(inaltime):
                if Mverif[i][j] == 5:
                         if my >= i * (rectdist + rectwidth) and my < (i+1) * (rectdist + rectwidth):
                            if mx >= j * (rectdist + rectheight) and mx < (j+1) * (rectdist + rectheight):
                                screen.blit(impblank, (j * (rectdist + rectwidth) , i * (rectdist + rectheight)))
                                Mverif[i][j]=0
    
    #deblocarea blocurilor vecine in cazul gasirii casutelor cu 0 bombe in vecinatate
    GG=100
    while GG>=0:             
        for i in range(lungime):
            for j in range(inaltime):
                if M[i][j]==0 and Mverif[i][j]==1:
                    if i-1>=0 and j-1 >=0 and Mverif[i-1][j-1]==0:
                        valori(i-1,j-1,0)
                    if i-1>=0 and Mverif[i-1][j]==0:
                        valori(i-1,j,0)
                    if i-1>=0 and j+1<10 and Mverif[i-1][j+1]==0:
                        valori(i-1,j+1,0)
                    if j-1>=0 and Mverif[i][j-1]==0:
                        valori(i,j-1,0)
                    if j+1<10 and Mverif[i][j+1]==0:
                        valori(i,j+1,0)
                    if i+1<10 and j-1>=0 and Mverif[i+1][j-1]==0:
                        valori(i+1,j-1,0)
                    if i+1<10 and Mverif[i+1][j]==0:
                        valori(i+1,j,0)
                    if i+1<10 and j+1<10 and Mverif[i+1][j+1]==0:
                        valori(i+1,j+1,0)
        GG-=1
    contor=0
    contor2=0
    for i in range(lungime):
        for j in range(inaltime):
            if Mverif[i][j]==5 and M[i][j]==99:
                contor+=1
            if Mverif[i][j]==0:
                contor2=1
    if contor==bombe and contor2==0:
        #screen.blit(ez, (0 , 0))
        screen.blit(win, (((screen_width/2)-125) , (screen_height/2)-125))
        contorR=1
        screen.blit(iar, (((screen_width/2)-95) , (screen_height/2)+125))
        contormeniu=2
    pg.display.flip()

pg.quit()

    #afisare de test
