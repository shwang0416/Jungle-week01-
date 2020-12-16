# 백준 2468 안전 영역


# ----[input]-------------------------------------------------
import sys
sys.stdin = open('text/37.txt', 'r')
sys.setrecursionlimit(10**9) # 재귀의 깊이를 10^8 까지 늘림.


n = int(input())
ground =[]
for i in range(n):
	ground.append(list(int(i) for i in input().split()))
# -----------------------------------------------------------

#  2 <= n <= 100
#  1 <= ground[][] <= 100

#----[print]-------------------------------------------------
# def put():
# 	for j in range(n):
# 		for i in range(n):
# 			print(str(board[j][i]) + ' ', end='')
# 			# print(str(flag[j][i]) + ' ', end='')
# 		print()
# -----------------------------------------------------------
def setBoard(rainAmount):
	board = [[1 for col in range(n)] for row in range(n)]		# 비가 안 온 땅 1으로 초기화
	for j in range(n):
		for i in range(n):
			if ground[j][i] <= rainAmount:
				board[j][i] = 0		#잠김
	return board

count = 0
dc = [0, 0, -1, 1]# 상하좌우 탐색용	col
dr = [-1, 1, 0, 0]# 상하좌우 탐색용	row

highest = max(max(ground))		# 0부터 가장 높은 땅까지 max(max(ground))
largest = 0

# Col : 열
# Row : 행
def dfs(c, r): # c열 r행의 좌표
	global count

	if r < 0 or r >= n or c < 0 or c >= n or flag[r][c] == True:	# 재귀 리턴조건 : 도착한 좌표가 범위 밖 or 이미 탐색한 좌표
		return
	else:
		flag[r][c] = True

		for i in range(4):
			nr = r+dr[i]
			nc = c+dc[i]
			if nr >= 0 and nr < n and nc >= 0 and nc < n and board[nr][nc] == 1:	# 좌표에 들어가고 안 잠겼으면
				dfs(nc,nr)			#탐색

# [main]
for rainAmount in range(highest):
	# if rainAmount == 0:
	# 	count = 1
	# elif rainAmount >= highest:
	# 	count = 0
	# else:

	flag = [[False for col in range(n)] for row in range(n)]		# rainAmount가 변할 때마다 새로 만듬  	# matrix = [[0 for col in range(n)] for row in range(n)]
	board = setBoard(rainAmount)

	for row in range(n):
		for col in range(n):
			if board[row][col] == 1 and flag[row][col] == False:	#잠기지 않았고 탐색하지 않은 곳만 탐색
				dfs(col,row)
				count +=1
	largest = largest if largest > count else count
	count = 0

print(largest)






