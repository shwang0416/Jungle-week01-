# 하노이의 탑 retry

# 재귀를 이용한 하노이의 탑 풀기
# dfs? > 아마 O..?  완전탐색? > O 백트래킹? > 아닐듯

n = 3

def hanoi(n, start, end, left):
	# 리턴 조건
	if n == 1:
		print(f'{n}번째 원판을 {start}에서 {end}로 이동')
		return

	else:
	# 재귀문에서 반복할 것
		hanoi(n-1, start, left, end)
		print(f'{n}번째 원판을 {start}에서 {end}로 이동')
		hanoi(n-1, left, end, start)

hanoi(n, 1, 3, 2)
