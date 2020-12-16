# do it 알고리즘 실습 5-7
# 각 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

n = 8


pos = [0] * n  # 각 열에서 퀸의 위치  (행번호)


def put():
	# 각 열에 배치한 퀸의 위치를 출력
	for j in range(n):
		for i in range(n):
			print('■' if pos[i]==j else '□', end='')
		print()
	print()


def set(i):
	# i열에 퀸을 배치
	for j in range(n):
		pos[i] = j
		if i == 7:
			put()
		else:
			set(i+1) # 다음 열에 퀸을 배치


set(0)
