import pygame
from pygame.locals import *
import random
import sys
import copy



class Block():
    blockSet = [
        [[2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0],[2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2],[0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2]],
        [[3,3,0,0,0,3,3,0,0,0,0,0,0,0,0,0],[0,3,0,0,3,3,0,0,3,0,0,0,0,0,0,0],[3,3,0,0,0,3,3,0,0,0,0,0,0,0,0,0],[0,3,0,0,3,3,0,0,3,0,0,0,0,0,0,0]],
        [[0,0,4,4,0,4,4,0,0,0,0,0,0,0,0,0],[0,0,4,0,0,0,4,4,0,0,0,4,0,0,0,0],[0,0,4,4,0,4,4,0,0,0,0,0,0,0,0,0],[0,0,4,0,0,0,4,4,0,0,0,4,0,0,0,0]],
        [[5,0,0,0,5,5,5,0,0,0,0,0,0,0,0,0],[5,5,0,0,5,0,0,0,5,0,0,0,0,0,0,0],[5,5,5,0,0,0,5,0,0,0,0,0,0,0,0,0],[0,5,0,0,0,5,0,0,5,5,0,0,0,0,0,0]],
        [[0,0,0,6,0,6,6,6,0,0,0,0,0,0,0,0],[0,0,6,0,0,0,6,0,0,0,6,6,0,0,0,0],[0,6,6,6,0,6,0,0,0,0,0,0,0,0,0,0],[0,0,6,6,0,0,0,6,0,0,0,6,0,0,0,0]],
        [[0,7,0,0,7,7,7,0,0,0,0,0,0,0,0,0],[7,0,0,0,7,7,0,0,7,0,0,0,0,0,0,0],[7,7,7,0,0,7,0,0,0,0,0,0,0,0,0,0],[0,7,0,0,7,7,0,0,0,7,0,0,0,0,0,0]],
        [[8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0],[8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0],[8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0],[8,8,0,0,8,8,0,0,0,0,0,0,0,0,0,0]]
    ]

    x_position = 4
    y_position = 0
    rotation = 0
    block_kind = 0
    temp_rotation=0
    block = []
    def __init__(self):
        self.block_kind = random.randrange(0,7)
        '''self.block = self.blockSet[self.block_kind][self.rotate]'''
        self.block = self.blockSet[self.block_kind][0]

    def get_x_position(self):
        return self.x_position

    def get_y_position(self):
        return self.y_position

    def set_x_position(self,num):
        self.x_position+=num

    def set_y_position(self,num):
        self.y_position+=num

    def temp_rotate_block(self):
        self.temp_rotation = self.rotation+1
        if(self.temp_rotation>=4):
            self.temp_rotation-=4
        temp_block = self.blockSet[self.block_kind][self.temp_rotation]
        return temp_block


    def rotate(self):
        self.rotation +=1
        if(self.rotation>=4):
            self.rotation-=4
        self.block = self.blockSet[self.block_kind][self.rotation]

    def get_block(self):
        return self.block




class TetrisBoard():
    gameBoard = [
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,1,1,1,1,1,1,1,1,1,1,1,
    ]
    '''고정된 배열에다가 insertBlock 하여 출력하기 위한 배열이다.'''

    prev_gameBoard = [
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,0,0,0,0,0,0,0,0,0,0,1,
    1,1,1,1,1,1,1,1,1,1,1,1,
    ]
    '''고정된 블럭만을 저장하는 배열이다.'''

    Vertical = 16
    Horizontal = 12

    superblock = Block()
    block = superblock.block

    def newBlock(self):
        self.superblock = Block()
        self.block = self.superblock.block

    def insertBlock(self) :
        i=0
        while i < 16*12 :
            self.gameBoard[i] = self.prev_gameBoard[i]
            i+=1

        temp_Verti = 0

        block_x_position = self.superblock.get_x_position()
        block_y_position = self.superblock.get_y_position()
        while temp_Verti < 4 :
            temp_Hori = 0
            while temp_Hori < 4 :
                if(self.block[temp_Verti*4+temp_Hori]!=0):
                    self.gameBoard[ (temp_Verti+block_y_position) * 12 + temp_Hori+block_x_position ] = self.block[temp_Verti*4+temp_Hori]
                temp_Hori+=1
            temp_Verti+=1

    '''블럭의 다음상태를 받아보고 충돌하면 true 충돌하지 않는다면 false'''
    def collision(self,move_x,move_y):
        temp_Verti = 0

        block_x_position = self.superblock.get_x_position()
        block_y_position = self.superblock.get_y_position()
        while temp_Verti < 4 :
            temp_Hori = 0
            while temp_Hori < 4 :
                if(self.superblock.block[temp_Verti*4+temp_Hori]!=0):
                    if(self.prev_gameBoard[ (temp_Verti+block_y_position+move_y) * 12 + temp_Hori+block_x_position+move_x ] !=0 ):
                        return True
                temp_Hori+=1
            temp_Verti+=1
        return False


    '''블럭이 이 상태에서 회전하면 충돌하는지 안하는지 검사한다 충돌하면 true 충돌하지 않는다면 false'''
    def rotatecollision(self) :
        temp_Verti = 0

        block_x_position = self.superblock.get_x_position()
        block_y_position = self.superblock.get_y_position()
        temp_block = copy.deepcopy(self.superblock)
        temp_block.rotate()

        while temp_Verti < 4 :
            temp_Hori = 0
            while temp_Hori < 4 :
                if(temp_block.block[temp_Verti*4+temp_Hori]!=0):
                    if(self.prev_gameBoard[ (temp_Verti+block_y_position) * 12 + temp_Hori+block_x_position] !=0 ):
                        return True
                temp_Hori+=1
            temp_Verti+=1
        return False


    def fixBlock(self) :
        temp_Verti=0
        block_x_position = self.superblock.get_x_position()
        block_y_position = self.superblock.get_y_position()
        while temp_Verti < 4 :
            temp_Hori = 0
            while temp_Hori < 4 :
                if(self.block[temp_Verti*4+temp_Hori]!=0):
                    self.prev_gameBoard[ (temp_Verti+block_y_position) * 12 + temp_Hori+block_x_position ] = self.block[temp_Verti*4+temp_Hori]
                temp_Hori+=1
            temp_Verti+=1
        i = 14
        while i>0 :
            if self.CheckAndDeleteLine(i) == False :
                i-=1
        self.newBlock()

    def PrintBoard(self) :
        temp_Verti = 0
        while temp_Verti < self.Vertical :
            temp_Hori = 0
            while temp_Hori < self.Horizontal :
                screen.blit(img[self.gameBoard[temp_Verti*12+temp_Hori]],(temp_Hori*30,temp_Verti*30))
                temp_Hori+=1
            temp_Verti+=1
        pygame.display.flip()

    def GameOver(self) :
        i=1
        while i<11:
            if self.prev_gameBoard[i] != 0 :
                return False
            i+=1
        return True

    def CheckAndDeleteLine(self,Line):
        i = 1
        while i < self.Horizontal-1 :
            if(self.prev_gameBoard[Line*12+i]==0):
                return False
            i+=1

        while Line>0 :
            i = 1
            while i<self.Horizontal-1:
                self.prev_gameBoard[(Line)*12+i]=self.prev_gameBoard[(Line-1)*12+i]
                i+=1
            Line-=1

        return True






pygame.init()

screen = pygame.display.set_mode((500,500),DOUBLEBUF)
pygame.display.set_caption("Second Game : Tetris")
Game_FPS = 60

img = []
loadImage = 0
WHITE = (255,255,255)

clock = pygame.time.Clock()

while loadImage<9 :
    tempImage = pygame.image.load("Image/"+str(loadImage+1)+".png")
    img.append(tempImage)
    loadImage+=1

GameBoard = TetrisBoard();


Temp_FPS = 0
Fix_Temp_FPS=0
while GameBoard.GameOver() :


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                if (GameBoard.rotatecollision() == False):
                    GameBoard.superblock.rotate()
                    GameBoard.block = GameBoard.superblock.block
            if event.key == K_DOWN:
                if(GameBoard.collision(0,1)==False):
                    GameBoard.superblock.set_y_position(1)
            if event.key == K_LEFT:
                if(GameBoard.collision(-1,0)==False):
                    GameBoard.superblock.set_x_position(-1)
            if event.key == K_RIGHT:
                if(GameBoard.collision(1,0)==False):
                    GameBoard.superblock.set_x_position(1)

            if event.key == K_SPACE :
                while GameBoard.collision(0,1)==False :
                    GameBoard.superblock.set_y_position(1)
                GameBoard.fixBlock()

    Temp_FPS +=1
    if(Temp_FPS >30):
        Temp_FPS = 0
        if(GameBoard.collision(0,1)==False):
            GameBoard.superblock.y_position+=1

    if(GameBoard.collision(0,1)==True):
        Fix_Temp_FPS +=1
        if Fix_Temp_FPS >= 30 :
            Fix_Temp_FPS=0
            GameBoard.fixBlock()

    if(GameBoard.collision(0,1)==False):
        Fix_Temp_FPS = 0


    screen.fill(WHITE)
    GameBoard.insertBlock()
    GameBoard.PrintBoard()
    clock.tick(Game_FPS)
