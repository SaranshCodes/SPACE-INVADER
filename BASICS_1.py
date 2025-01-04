import pygame
import random
import math
from pygame import mixer
pygame.init()   #initialization
# creating screen
screen= pygame.display.set_mode((800,600)) #(width,height)
#Title and icon
pygame.display.set_caption("Space Invaders")
icon1=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon1)
# Background
background=pygame.image.load("Background1.png")
#Background Sound
mixer.music.load("background-music-224633.mp3")
mixer.music.play(-1) #music for continuous sound  //-1 for loop

#Player (screen ke andar ka )
playerimg=pygame.image.load("spaceship (1).png")  # 64-bit
playerx=370  
playery=480
x_change=0
#Enemy 
enemyimg=[]  #for multiple enemies
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
no_of_enemy=5
for i in range(no_of_enemy):
    enemyimg.append(pygame.image.load("ufo.png"))
    enemyx.append(random.randint(100,700))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(0.3)
    enemyy_change.append(20)
#Bullet 
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=480
bulletx_change=0
bullety_change=1
bullet_state="ready"

#Score
score_value=0
font= pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
#Game over
over_font=pygame.font.Font("freesansbold.ttf",50)
def show_score(x,y):
    score= font.render("Score: "+ str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over_text():
    over = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over,(270,250))
def player(x,y):
    screen.blit(playerimg,(x,y)) #Drawing image in the screen
    #img + x and y axis of image
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletimg,(x+16,y-30))
def collision(enemyx,enemyy,bulletx,bullety):
    distance= math.sqrt(((enemyx-bulletx)**2)+((enemyy-bullety)**2))
    if distance<20:
        return True
    return False 
# Game loop
run= True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run= False 
        #Keystrokes left and right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-0.5
            if event.key==pygame.K_RIGHT:
                x_change=0.5
            if event.key==pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound=mixer.Sound("bullet-crack-80190.mp3")
                    bullet_sound.play()
                    bulletx=playerx
                    fire_bullet(bulletx,bullety)
                    
        if event.type==pygame.KEYUP:
            if event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
                x_change=0
    # anything we want in the screen we write it in while loop
    screen.fill((32,32,32))   #rgb= red, green , blue    {max is 255}
    screen.blit(background,(0,0))
    playerx+=x_change
    enemyx[i]+=enemyx_change[i]
    #player movement
    if playerx<0:
        playerx=0
    elif playerx>=736:      #(800-64)
        playerx=736

    #enemy movement
    
    for i in range(no_of_enemy):
        #Game over
        if enemyy[i]>300:
            for j in range(no_of_enemy):
                enemyy[j]=1000
            game_over_text()
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=0.3
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i]>=736:      #(800-64)
            enemyx_change[i]=-0.3
            enemyy[i]+=enemyy_change[i]
        #collision
        collision1=collision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision1:
            explosion_sound=mixer.Sound("impact-152508.mp3")
            explosion_sound.play()
            bullety=480
            bullet_state="ready"
            score_value+=1
            enemyx[i]=random.randint(100,700)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)
    player(playerx,playery)
    
    #Bullet movement
    if bullety<=50:
        bullety=480
        bullet_state="ready"
    if bullet_state == "fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    show_score(textx,texty)
    
    
    #now it is not updated we need to update it in screen
    pygame.display.update()
 