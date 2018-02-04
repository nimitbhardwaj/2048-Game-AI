matrix = [[]]
weight = [[6, 5, 4, 3], [5, 4, 3, 2], [4, 3, 2, 1], [3, 2, 1, 0]]
moves = ['left', 'right', 'up', 'down']

def move_left(grid):
	# move left and return new grid

def move_right(grid):
	# move right and return new grid

def move_up(grid):
	# move up and return new grid

def move_down(grid):
	# move down and return new grid

def move(x, grid):
	grid1 = [[]]
	if x == 'left':
		grid1 = move_left(grid)
	elif x == 'right':
		grid1 = move_right(grid)
	elif x == 'up':
		grid1 = move_up(grid)
	else
		grid1 = move_down(grid)
	return grid1

def isOver(grid):
	c1 = 0
	for i in xrange(4):
		for j in xrange(4):
			if grid[i][j] == 0:
				c1 += 1
	if c1 == 0:
		return True
	else
		return False


def score(grid):
	a, b = 0, 0
	for i in xrange(4):
		for j in xrange(4):
			a += weight[i][j] * grid[i][j]
	for i in xrange(4);
		for j in xrange(4):
			if i > 0:
				b += abs(grid[i][j] - grid[i - 1][j])
			if i < 3:
				b += abs(grid[i][j] - grid[i + 1][j])
			if j > 0:
				b += abs(grid[i][j] - grid[i][j - 1])
			if j < 3:
				b += abs(grid[i][j] - grid[i][j + 1])
	return (a - b)

def bestMove(grid, depth, isMaxi):
	curr = 'left'
	score = 0
	lscore = expectimax(move_left(grid), depth, isMaxi)
	rscore = expectimax(move_left(grid), depth, isMaxi)
	uscore = expectimax(move_left(grid), depth, isMaxi)
	dscore = expectimax(move_left(grid), depth, isMaxi)
	if lscore > score:
		curr, score = 'left', lscore
	if rscore > score:
		curr, score = 'right', rscore
	if uscore > score:
		curr, score = 'up', uscore
	if dscore > score:
		curr, score = 'down', dscore
	return curr

def expectimax(grid, depth, isMaxi):
	if depth == 0:
		return score(grid)
	elif isMaxi == 0:
		score = 0.0
		blankCount = 0
		for i in xrange(4):
			for j in xrange(4):
				tile = grid[i][j]
				if tile != 0:
					continue
				blankCount += 1
				grid1 = grid
				grid1[i][j] = 2
				score += 0.9 * expectimax(grid1, depth - 1, !isMaxi)
				grid1 = grid
				grid1[i][j] = 4
				score += 0.1 * expectimax(grid1, depth - 1, !isMaxi)
		return score/blankCount
	elif isMaxi == 1:
		score = 0.0
		blankCount = 0
		for x in moves:
			grid1 = move(x, grid)
			score = max(score, expectimax(grid1, depth - 1, !isMaxi))
		return score

def main():
	for i in xrange(4):
		l = map(int, input().split())
		matrix.append(l)
	while !isOver(matrix):
		nextMove = bestMove(matrix, 6, 1)
		matrix = move(nextMove)

	## game over and score is %d.

if __name__ == "__main__":
	main()