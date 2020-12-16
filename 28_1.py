# nqueen 실습 공부 후 혼자 다시 해보기

# [유의점]
# 열을 기준으로 각 열마다 하나의 퀸이 놓인다.
# 각 행마다 퀸이 놓였는 지 기록할 리스트를 만들어 flag를 세운다.

# 재귀 리턴 조건: 퀸이 전부 놓였을 때, 기록 or count [=> col = 0에서 시작하여 if col == 7이면]
# 재귀 반복 코드: 	※ 재귀문 하나는 인자로 받아온 해당 열을 작업하고 있음을 의미한다.

# 					(0) for 문을 돌며 0부터 n개의 row(행번호)를 확인
# 					(1) if flag가 false라면
# 							=> rowInCol[col(열)] = row(행번호)
#					(2) if col == 7이면
# 							=> 기록 or count
# 						else
# 							=>	(1) 퀸을 놓고 flag를 True로 설정,
	# 							(2) col+1 로 다음 열 재귀문 호출,
	# 							(3) (위의 재귀문에서 리턴했을 경우를 고려해) flag 회수
# Col : 열
# Row : 행

n = 8

rowInCol = [0] * n	# 각 열에 해당하는 인덱스에 '행'번호 저장
flag = [False] * n	# 각 열에 해당하는 인덱스에 queen의 유무 저장
					# 대각선 리스트의 숫자는 2*n-1
flag2 = [False] *(2*n -1)
flag3 = [False] *(2*n -1)

def put():
	for row in range(n):
		for col in range(n):
			print('●' if rowInCol[col]== row else '○', end='')
		print()
	print()

def set(Col):				# Col 번째 열 작업중

	for row in range(n):		# '행'번호가 0부터 n-1까지 증가

		if(not flag[row]		# row 행에 플래그가 없으면
			and not flag2[Col+row]	# && 대각선 아래로 플래그가 없으면
			and not flag3[Col-row+(n-1)]): # && 대각선 위로 플래그가 없으면

			rowInCol[Col] = row		# Col번째 열에 '행'번호 저장	[중요!]

			if Col == 7:			# 8열 모두 채웠다면
				put()
			else:
				# 만약 Col이 7이라 출력할거라면 바로 flag를 회수해 다음인덱스로 진행해야하므로
				# col이 7이 아닌 경우에만 flag를 놓는다!
				flag[row] = flag2[Col+row] = flag3[Col-row+(n-1)] = True
				set(Col+1)
				flag[row] = flag2[Col+row] = flag3[Col-row+(n-1)] = False

set(0)
