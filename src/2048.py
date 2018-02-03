import pygame
from pygame.locals import *
import sys
import random
from constant import *
from color import colors
import box
from enum import Enum

MAT = [[box.Box(i, j) for i in range(4)] for j in range(4)]
M_ABLE = [[False for i in range(4)] for j in range(4)]
BLOCK = [[False for i in range(4)] for j in range(4)]

class Move(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    NULL = 0

def main():
    SCR = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('2048 AI')

    FPSCLOCK = pygame.time.Clock()
    running = True
    inMotion = False
    emptyList = []
    for i in range(4):
        for j in range(4):
            if MAT[i][j].val == 0:
                emptyList.append((i, j))
    bleedingEffect(emptyList)
    bleedingEffect(emptyList)
    mv = Move.NULL
    makeBoard(SCR)
    while running:
        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            elif e.type == KEYDOWN:
                if not inMotion and e.key == K_LEFT:
                    inMotion = True
                    mv = Move.LEFT
                    moveLeft()
                elif not inMotion and e.key == K_RIGHT:
                    inMotion = True
                    mv = Move.RIGHT
                    moveRight()
                elif not inMotion and e.key == K_UP:
                    inMotion = True
                    mv = Move.UP
                    moveUp()
                elif not inMotion and e.key == K_DOWN:
                    inMotion = True
                    mv = Move.DOWN
                    move(Down)
                elif e.key == K_ESCAPE:
                    running = False
        makeBoard(SCR)
        pygame.display.flip()
        FPSCLOCK.tick(FPS)
    pygame.quit()
    sys.exit()

def makeBoard(srf):
    r1 = pygame.Rect(WINMARGIN - 10, WINMARGIN - 10, BOARDSIDE + 20, BOARDSIDE + 20)
    srf.fill((255, 255, 255))

    pygame.draw.rect(srf, colors['antiquewhite1'], r1)
    for i in range(4):
        for j in range(4):
            box.Box(i, j, 0).draw(srf)
    for i in range(4):
        for j in range(4):
            MAT[i][j].draw(srf)

def moveLeft():
    pass

def moveRight():
    pass

def moveUp():
    pass

def moveDown():
    pass

def bleedingEffect(lst):
    kapa = random.choice(lst)
    MAT[kapa[0]][kapa[1]].val = 4 if random.random() - 0.1 <= 0 else 2
    lst.remove(kapa)

if __name__ == '__main__':
    main()
