import pygame

# initilize the pygame 
pygame.init()

# Create the screen
screen = pygame.display.set_mode((600,600))


# Title and Icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("tic-tac-toe (1).png")
pygame.display.set_icon(icon)

# Board
board = pygame.image.load("tic tac toe board.png")
boardX = 42
boardY = 42

# board coordinates == screen coordinates - 42
#
# player1 coordinates == screen coordinates - 222
#
# player2 coordinate == screen coordinate x - 222 & screen coordinate y - 217 

first = pygame.draw.rect(screen, (255, 255, 255), (60, 60, 150, 150))
second = pygame.draw.rect(screen, (255, 255, 255), (222, 60, 150,150))
third = pygame.draw.rect(screen,(255,255,255),(387,60,150,150))

fourth = pygame.draw.rect(screen, (255,255,255), (60, 222,150,150))
fifth = pygame.draw.rect(screen,(255,255,255), (222,222,150,150)) # board = (180,180)
sixth = pygame.draw.rect(screen,(255,255,255), (387,222,150,150)) #

seventh = pygame.draw.rect(screen,(255,255,255),(60,387,150,150))
eighth = pygame.draw.rect(screen, (255,255,255), (222,387,150,150))
ninth = pygame.draw.rect(screen, (255,255,255), (387,387,150,150))

boxes = [first,second,third,fourth,fifth,sixth,seventh,eighth,ninth]
coordinateP1 = [(first,-162,-162), (second,0,-162),(third,165,-162),(fourth,-162,0),(fifth,0,0),(sixth,165,0),(seventh,-162,165),(eighth,0,165),( ninth, 165,165)]
coordinateP2 = [(first,-162,-157),(second,0,-157),(third,165,-157),(fourth,-162,5),(fifth,0,5),(sixth,165,5),(seventh,-162,170),(eighth,-0,170),(ninth,165,170)]

# Player 1
player1Img = pygame.image.load("tic tac toe cross.png")
p1_boxes = []

def player1(x, y):
    board.blit(player1Img, (x, y))


# player 1 win screen
player1_winsImg = pygame.image.load("p1 wins.png")

def wins1():
    board.blit(player1_winsImg,(75,60))

# Player 2
player2Img = pygame.image.load("tic tac toe circle.png")
p2_boxes = []


def player2(x,y):
    board.blit(player2Img, (x, y))

# player 2 win screen
player2_winsImg = pygame.image.load("p2 wins.png")

def wins2():
    board.blit(player2_winsImg,(75,60))


# draw screen
drawImg = pygame.image.load("draw.png")

def draw():
    board.blit(drawImg,(90,80))

# variable that checks if someone has won
won = False


i = 1
# Game Loop
done = False
while not done:

    # Background RGB - Red, Green, Blue
    screen.fill((173, 216, 230))

    # board 
    screen.blit(board, (boardX, boardY))

    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            for j in boxes:
                if j.collidepoint(pos) and i%2 == 0:
                    for item in coordinateP2:
                        if item[0] == j:
                            z,x,y = item
                            player2(x,y)
                            i += 1
                            break
                    boxes.remove(j)
                    coordinateP2.remove(item)
                    p2_boxes.append(j)
                elif j.collidepoint(pos) and i%2 !=0:
                    for item in coordinateP1:
                        if item[0] == j:        
                            z,x,y = item
                            player1(x,y)
                            i += 1
                            break
                    boxes.remove(j)
                    coordinateP1.remove(item)
                    p1_boxes.append(j)

        # if ((first in p1_boxes and second in p1_boxes and third in p1_boxes) or (fourth in p1_boxes and fifth in p1_boxes and sixth in p1_boxes) or (seventh in p1_boxes and eighth in p1_boxes and ninth in p1_boxes) or (first in p1_boxes and fourth in p1_boxes and seventh in p1_boxes) or (second in p1_boxes and fifth in p1_boxes and eighth in p1_boxes) or (third in p1_boxes and sixth in p1_boxes and ninth in p1_boxes) or (first in p1_boxes and fifth in p1_boxes and ninth in p1_boxes) or (third in p1_boxes and fifth in p1_boxes and seventh in p1_boxes)):
        
        # checks all possible win conditins for player one with the current boxes occupied by player 1
        if first in p1_boxes:
            if second in p1_boxes:
                if third in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True
            elif fourth in p1_boxes:
                if seventh in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True
            elif fifth in p1_boxes:
                if ninth in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True
        if second in p1_boxes:
            if fifth in p1_boxes:
                if eighth in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True
        if third in p1_boxes:
            if sixth in p1_boxes:
                if ninth in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True
            elif fifth in p1_boxes:
                if seventh in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True
        if fourth in p1_boxes:
            if fifth in p1_boxes:
                if sixth in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True
        if seventh in p1_boxes:
            if eighth in p1_boxes:
                if ninth in p1_boxes:
                    board.fill((173, 216, 230))
                    wins1()
                    won = True

        # checks all possible win conditins for player 2 with the current boxes occupied by player 2
        if first in p2_boxes:
            if second in p2_boxes:
                if third in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
            elif fourth in p2_boxes:
                if seventh in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
            elif fifth in p2_boxes:
                if ninth in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
        if second in p2_boxes:
            if fifth in p2_boxes:
                if eighth in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
        if third in p2_boxes:
            if sixth in p2_boxes:
                if ninth in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
            elif fifth in p2_boxes:
                if seventh in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
        if fourth in p2_boxes:
            if fifth in p2_boxes:
                if sixth in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
        if seventh in p2_boxes:
            if eighth in p2_boxes:
                if ninth in p2_boxes:
                    board.fill((173, 216, 230))
                    wins2()
                    won = True
        
        
        # Checks for a draw case and then displays the draw screen 
        if (len(p2_boxes) == 4) and (len(p1_boxes) == 5) and won == False:
            board.fill((173, 216, 230))
            draw()
            


 

    pygame.display.update()

pygame.quit()

# to prevent double entry use a list and pop once a player uses that box 
# make a draw screen
