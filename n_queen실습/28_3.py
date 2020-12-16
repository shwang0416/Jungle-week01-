# do it 알고리즘 실습 5-8
# 행과 열에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기

n = int(input())

pos = [0] * n  # 각 열에서 퀸의 위치  (행번호)
# ---------------------
flag = [False] * n
flag2 = [False] * (2*n-1)
flag3 = [False] * (2*n-1)
# ---------------------
def put():
	# 각 열에 배치한 퀸의 위치를 출력
	for j in range(n):
		for i in range(n):
			print('■' if pos[i]==j else '□', end='')
		print()
	print()

count = 0

def set(i):
	global count
	for j in range(n):
# ---------------------
		if(not flag[j]  #j행에 플래그가 없으면
			and not flag2[i+j]
			and not flag3[i-j+(n-1)]):
# ---------------------
			pos[i] = j
			if i == n-1: # n개 열에 모두 퀸을 놓았다면
				# put()
				count += 1
			else:
# ---------------------
				flag[j] = flag2[i+j] = flag3[i-j+(n-1)] = True
# ---------------------
				set(i+1)
# ---------------------
				flag[j] = flag2[i+j] = flag3[i-j+(n-1)] = False
# ---------------------

set(0)
print(count)
