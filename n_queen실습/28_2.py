# do it 알고리즘 실습 5-8
# 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

n = 3

pos = [0] * n  # 각 열에서 퀸의 위치  (행번호)
# ---------------------
flag = [False] * n
# ---------------------
def put():
	# 각 열에 배치한 퀸의 위치를 출력
	for j in range(n):
		for i in range(n):
			print('■' if pos[i]==j else '□', end='')
		print()
	print()

def set(i):
	for j in range(n):
# ---------------------
		if not flag[j]:  #j행에 플래그가 없으면
# ---------------------
			pos[i] = j
			if i == n-1: # n개 열에 모두 퀸을 놓았다면
				put()
			else:
# ---------------------
				flag[j] = True
# ---------------------
				set(i+1)
# ---------------------
				flag[j] = False
# ---------------------

set(0)
