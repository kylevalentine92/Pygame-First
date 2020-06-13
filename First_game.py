#-------------------------------------------------------------------------------
# Name:        Pygame Practice
# Purpose:     Just for initial practice purposes
#
# Author:      Kyle Valentine
#
# Created:     13/04/2020
# Copyright:   (c) Kyle Valentine
#-------------------------------------------------------------------------------
### How the game works ###
#The aim of the game is to catch the green square and aviod the red squares
#The Red squares are considered as the enemy and the Green square the prize
#If you catch the Green square before being caught by the red square you lose
#If you are caught by one of the Red squares before catching the green square you lose


#Import pygame firstly
import pygame
import random
#Initialize the pygame modules
pygame.init()

#Create the window we will play in
screen_height=500
screen_width=500

win=pygame.display.set_mode((screen_height,screen_width))
#Adds a caption in the game screen
pygame.display.set_caption("First Game")

#So Now that we have the window we have to create over characters
#Creating the player character here that we would control
moekie=pygame.image.load("monster.jpg")

#Changing the size of the player square
moekie=pygame.transform.scale(moekie,(50,50))

#Defining the colour of the prize square
PrizeColor=pygame.color.Color("Green")
white = (255,255,255)

#Get the Height and Width of the image
moekie_height=moekie.get_height()
moekie_width=moekie.get_width()

#Defining the color of the enemy squares
CircleColor=pygame.color.Color("Red")


#Intialize the start postion of my player
moekie_x_position=250
moekie_y_position=250

#We have to initalize our enemy charcters
#Plan is to draw three enemy charcters on the pygame screen that would move at random
#Enemy 1  start position
position_x_enemy1=0
position_y_enemy1=0


#The change variables are created to control the speed and direction of the enemys
y_change1=random.randrange(-10,11,1)
x_change1=random.randrange(-10,11,1)

#Enemy 2 start position
position_x_enemy2=350
position_y_enemy2=0


y_change2=random.randrange(-10,11,1)
x_change2=random.randrange(-10,11,1)

#Enemy 3
position_x_enemy3=0
position_y_enemy3=350


y_change3=random.randrange(-10,11,1)
x_change3=random.randrange(-10,11,1)


#Creating a prize square that shows up after a time
position_x_prize=random.randrange(0,350,1)
position_y_prize=random.randrange(0,350,1)


y_change4=random.randrange(-10,11,1)
x_change4=random.randrange(-10,11,1)


#Initalize Key values
keyUp=False
keyDown=False
keyLeft=False
keyRight=False

#This counter will be used to add a delay of when the prize appears
counter=0

#Game Loop
while 1:

    win.fill(0) # Clears the screen.
    win.blit(moekie, (moekie_x_position, moekie_y_position))# This draws the player image to the screen at the postion specfied. I.e. (250, 250).

    # Making sure that the enemeys stay within the boundaries
    #Movements and boundaries for enemy 1

    pygame.time.delay(100)
    increment_x=random.randrange(0,10,1)
    increment_y=random.randrange(0,10,1)
    position_x_enemy1+=increment_x*x_change1
    position_y_enemy1+=increment_y*y_change1
    if position_x_enemy1<=0:
        x_change1=random.randrange(0,6,1)
        position_x_enemy1+=increment_x*x_change1
        y_change1=random.randrange(-5,6,1)

    if position_x_enemy1>=400:
        x_change1=random.randrange(-5,0,1)
        position_x_enemy1+=increment_x*x_change1
        y_change1=random.randrange(-5,6,1)

    if position_y_enemy1<=0:
        y_change1=random.randrange(0,6,1)
        position_y_enemy1+=increment_y*y_change1
        x_change1=random.randrange(-5,6,1)

    if position_y_enemy1>=400:
        y_change1=random.randrange(-5,0,1)
        position_y_enemy1-=increment_y*y_change1
        x_change1=random.randrange(-5,6,1)
    #screen.blit(enemy, (position_x_enemy1, postition_y_enemy))
    tangle=pygame.draw.rect(win,CircleColor,(position_x_enemy1,position_y_enemy1,50,50),5)


    #Movements and boundaries for enemy 2
    position_x_enemy2+=increment_x*x_change2
    position_y_enemy2+=increment_y*y_change2
    if position_x_enemy2<=0:
        x_change2=random.randrange(0,6,1)
        position_x_enemy2+=increment_x*x_change2
        y_change2=random.randrange(-5,6,1)

    if position_x_enemy2>=400:
        x_change2=random.randrange(-5,0,1)
        position_x_enemy2+=increment_x*x_change2
        y_change2=random.randrange(-5,6,1)

    if position_y_enemy2<=0:
        y_change2=random.randrange(0,6,1)
        position_y_enemy2+=increment_y*y_change2
        x_change2=random.randrange(-5,6,1)

    if position_y_enemy2>=400:
        y_change2=random.randrange(-5,0,1)
        position_y_enemy2-=increment_y*y_change2
        x_change2=random.randrange(-5,6,1)
    #screen.blit(enemy, (position_x_enemy1, postition_y_enemy))
    tangle_2=pygame.draw.rect(win,CircleColor,(position_x_enemy2,position_y_enemy2,50,50),5)


    #Movements and boundaries for enemy 3
    position_x_enemy3+=increment_x*x_change3
    position_y_enemy3+=increment_y*y_change3
    if position_x_enemy3<=0:
        x_change3=random.randrange(0,6,1)
        position_x_enemy3+=increment_x*x_change3
        y_change3=random.randrange(-5,6,1)

    if position_x_enemy3>=400:
        x_change3=random.randrange(-5,0,1)
        position_x_enemy3+=increment_x*x_change3
        y_change3=random.randrange(-5,6,1)

    if position_y_enemy3<=0:
        y_change3=random.randrange(0,6,1)
        position_y_enemy3+=increment_y*y_change3
        x_change3=random.randrange(-5,6,1)

    if position_y_enemy3>=400:
        y_change3=random.randrange(-5,0,1)
        position_y_enemy3-=increment_y*y_change3
        x_change3=random.randrange(-5,6,1)
    #screen.blit(enemy, (position_x_enemy1, postition_y_enemy))
    tangle_3=pygame.draw.rect(win,CircleColor,(position_x_enemy3,position_y_enemy3,50,50),5)

    if counter >= 20:
        position_x_prize+=increment_x*x_change4
        position_y_prize+=increment_y*y_change4
        if position_x_prize<=0:
            x_change4=random.randrange(0,6,1)
            position_x_prize+=increment_x*x_change4
            y_change4=random.randrange(-5,6,1)

        if position_x_prize>=400:
            x_change4=random.randrange(-5,0,1)
            position_x_prize+=increment_x*x_change4
            y_change4=random.randrange(-5,6,1)

        if position_y_prize<=0:
            y_change4=random.randrange(0,6,1)
            position_y_prize+=increment_y*y_change4
            x_change4=random.randrange(-5,6,1)

        if position_y_prize>=400:
            y_change4=random.randrange(-5,0,1)
            position_y_prize-=increment_y*y_change4
            x_change4=random.randrange(-5,6,1)
        #screen.blit(enemy, (position_x_enemy1, postition_y_enemy))
        prize=pygame.draw.rect(win,PrizeColor,(position_x_prize,position_y_prize,50,50),5)
    pygame.display.update()# This updates the screen.

    for event in pygame.event.get():

        # This event checks if the user quits the program, then if so it exits the program.

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.

        if event.type == pygame.KEYDOWN:

            # Test if the key pressed is the one we want.

            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant.
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        # This event checks if the key is up(i.e. not pressed by the user).
        if event.type == pygame.KEYUP:

            # Test if the key released is the one we want.

            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.

    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    if keyUp == True:
        if moekie_y_position > 0 : # This makes sure that the user does not move the player above the window.
            moekie_y_position -= 30
    if keyDown == True:
        if moekie_y_position< screen_height - moekie_height:# This makes sure that the user does not move the player below the window.
            moekie_y_position += 30
    if keyLeft == True:
        if moekie_x_position > 0 :
            moekie_x_position -=30
    if keyRight == True:
        if moekie_x_position<screen_width-moekie_width:
            moekie_x_position +=30


    # Bounding box for the player:
    #Checking whether player collids with any of the enemys

    playerBox = pygame.Rect(moekie.get_rect())

    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image.

    playerBox.top = moekie_y_position
    playerBox.left = moekie_x_position




    if playerBox.colliderect(tangle):

        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(tangle_2):

        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    if playerBox.colliderect(tangle_3):

        # Display losing status to the user:

        print("You lose!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)

    #Increasing a counter that would delay the appearance of the prize
    if counter>=20:
     if playerBox.colliderect(prize):

        # Display losing status to the user:

        print("You WIN!!!")

        # Quite game and exit window:

        pygame.quit()
        exit(0)
    counter+=1


### Future improvements for the game  ###
#Make the green square move faster than the red square
#Add a clock timer in the game
#Add a function that would bring in more squares( This would allow us to be able to add levels)
#Movement of the squares are abit predictable