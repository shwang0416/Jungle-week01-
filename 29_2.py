# 종료조건 : n == 0

n,r,c = list(int(i) for i in input().split())
result = 0
cnt = 0
def z(n,r,c):
	global cnt
	global result

	if n ==0 :
		return result

	# 1. n을 바탕으로 midpoint를 구한다
	# 		구하는 식: 2 * (n-1) - 1
	# 		ex) 2**(4 - 1) - 1 = 15 (0부터 시작이므로 16번째칸. 끝이 32이므로 딱 절반이다.)

	midpoint = 2**(n-1)-1
	position = 0

	# 2. Z를 기준으로 r행 c열이 사분면 0123중 어디에 위치했는지 알아낸다.

	if r > midpoint:
		if c > midpoint:
			position = 3
		else:
			position = 2
			# c < midpoint:
	else:
		# if r < midpoint
		if c > midpoint:
			position = 1
		else:
			position = 0

	# 3. 위치한 사분면(0123)을 기준으로 앞에 몇칸이 존재하는지 세어서 결과(result)값에 더한다.
	result += position * 2**(n-1) * 2**(n-1)
	#                    == 2의 2(n-1)승

	# 4. 사분면의 시작점이 0,0이 되도록 좌표를 조정한다.
	#  => 사분면 하나만 놓고 봤을 때
	#     목표지점 c행 r열 입장의 시작점이 0,0가 될 수 있도록
	#     "목표지점을 움직이는" 것!!

	if position == 3:
		c = c - (midpoint+1)
		r = r - (midpoint+1)
	elif position == 2:
		r = r - (midpoint+1)
	elif position == 1:
		c = c - (midpoint+1)
	# 	(position 0은 이미 c행 r열 입장에서 0,0의 시작점을 가지고 있다.)

	# n번만큼 4등분 할 수 있음. 이 방법을 따르면 n이 0일 때 칸 수가 1개 이므로 목표지점에 도달하는 것.
	# 따라서 종료조건: n == 0. 이에 수렴하도록 n을 1씩 뺀다. (n -= 1)
	n -= 1
	# 시작점은 0,0으로 "가정"하고 c,r과 midpoint만 0,0을 기준으로 표시하며 풀어간다.

	# result += z(n,r,c)
	# ※여기서 result값을 재귀로 합산하면 두 배로 더해진다!
	# https://siyoon210.tistory.com/58#recentComments
	# 이 블로그 글에선 합산하던데 뭐가 달라서 이렇게 되는 건지 모르겠음...
	z(n,r,c)
	return result

print(z(n,r,c))
