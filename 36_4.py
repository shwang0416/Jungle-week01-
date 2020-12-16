# 백준 10971 [외판원 순회2] [= TSP]
# 완전탐색 문제

# [유의점]

# global 도시 개수: N

# 재귀함수에 필요한 값:
# 				=> start 도시의 idx	: start
# 				=> next 도시의 idx	: next
# 				=> visited 도시 list	: visited =[]
# 				=> 현재까지 온 거리 cost: cost

# 재귀 리턴 조건: len(visited) = N 모든 도시 방문

# ----[input]-------------------------------------------------
import sys
sys.stdin = open('text/TSP.txt', 'r')
n = int(input())
dist =[]
for i in range(n):
	dist.append(list(int(i) for i in input().split()))
# -----------------------------------------------------------

min = 9999999

def dfs(start, next, visited, cost):
	global min

	if len(visited) == n:
		# 리턴 조건: 모든 도시 방문함?
		if dist[next][start] != 0:
			cand = cost + dist[next][start]	# 최소거리 후보
			min = min if cand > min else cand			# 둘 중 작은 값 택
		return

	else:
		# 아직 안함
		for i in range(n):
			if dist[next][i] != 0 and i not in visited:
				# and i != start 참고 코드에 이게 포함되어있는데 없어도 될 것 같음
				# 어차피 처음 함수 호출할 때 시작도시를 visited에 넣으니까
				visited.append(i)
				dfs(start, i, visited, cost + dist[next][i])
				visited.pop()

# 각 도시마다 시작
for i in range(n):
	# 시작도시를 저장하는 start변수와 별개로 next는 현재 위치한 도시를 의미하므로
	# 처음 함수를 호출할 때는 start와 next를 똑같이 할당해야 한다.
	dfs(i, i, [i], 0)

print(min)
