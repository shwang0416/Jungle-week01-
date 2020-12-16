# 백준 9663 [N-Queen]
# 혼자 애써봄

n = 4
width = n
height = n

board = []
for i in range(n):
	board.append([])
	for j in range(n):
		board[i].append('ㅁ')


queen = 0

def printBoard():
	for i in range(n):
		print(board[i])

def setFlag(x,y):
	# queen =+ 1
	# for i in range(n):
	# 	board[y][i] = 'X'
	# 	board[i][x] = 'X'
	# printBoard()

		# 대각선 해결
	for i in range(0, n):
		# board[x-i][y-i] = 'X'
		# board[x+i][y-i] = 'X'
		# board[x-i][y+i] = 'X'
		# board[x+i][y+i] = 'X'
		# print(str(x+i)+', '+str(y+i))
		printBoard()


	for i in range(-x, n-x):
		board[y+i][x+i] = 'X'
		print(str(x+i)+', '+str(y+i))
		# board[x+i][y+i] = 'X'   x(0)=> 0, 1, 2, 3   i는 0 에서 시작
		# board[x+i][y+i] = 'X'   x(1)=> -1, 0, 1, 2  i는 -1에서 시작
		# board[x+i][y+i] = 'X'   x(2)=> -2, -1, 0, 1  i는 -2에서 시작
	printBoard()

setFlag(1,0)


# for y in range(0, n):
# 	for x in range(0, n):
# 		setFlag(x,y)
