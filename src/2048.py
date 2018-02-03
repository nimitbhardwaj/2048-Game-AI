import pygame
from pygame.locals import *
import random
from constant import *
import util

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

	while running:
		for e in pygame.event.get():
			if e.type == QUIT:
				running = False

		pygame.display.flip()
		FPSCLOCK.tick(FPS)
	pygame.exit()
	sys.exit()

if __name__ == "__main__":
	main()