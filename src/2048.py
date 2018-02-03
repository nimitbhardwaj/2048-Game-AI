import pygame
from pygame.locals import *
import random
from constant import *
import util
from color import colors


'''def move_left():
	ok = True
	for i in range(1, 4):
		for j in range(4):
			if move[j][i] and move[j - 1][i]:
				if Mat[j - 1][i] == 0:
					Mat[j - 1][i] = Mat[j][i]
					Mat[j][i] = 0
				else if Mat[j - 1][i] == Mat[j][i] and Mat[j][i] > 0:
					Mat[j - 1][i] = 2 * Mat[j][i]
					Mat[j][i] = 0
					move[j][i] = 0
			else if Mat[j - 1][i] == 0:
				Mat[j - 1][i] = Mat[j][i]
				Mat[j][i] = 0
	# compare

	return Mat, ok;'''

def main():
	SCR = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	pygame.display.set_caption('2048 AI')

	SCR.fill((255, 255, 255))
	FPSCLOCK = pygame.time.Clock()
	running = True
	makeBoard(SCR)
	while running:
		for e in pygame.event.get():
			if e.type == QUIT:
				running = False
		makeBoard(SCR)
		pygame.display.flip()
		FPSCLOCK.tick(FPS)
	pygame.exit()
	sys.exit()

def makeBoard(srf):
	r1 = pygame.Rect(WINMARGIN - 10, WINMARGIN - 10, BOARDSIDE + 20, BOARDSIDE + 20)

	pygame.draw.rect(srf, colors['antiquewhite1'], r1)
	for i in range(4):
		for j in range(4):
			if Mat[i][j] == 0:
				r = pygame.Rect(WINMARGIN + BOXSIZE * i + GAPSIZE * i,
					WINMARGIN + BOXSIZE * j + GAPSIZE * j, BOXSIZE, BOXSIZE)
				#pygame.draw.rect(srf, colors['antiquewhite3'], r)
				util.BOX(srf, r, colors['antiquewhite3'], 0.4, 0)

if __name__ == "__main__":
	main()