# 백준 10971 외판원 순회2
# 앞서서 풀었던 35_2 [차이를 최대로]와 같이 순열 알고리즘으로 풀 수 있을 것으로 예상됨
# + 두 도시 사이에 길이 없는 경우(0)에도 return 해야 함

n = 3
a = [[0, 10, 15],[5, 0, 9],[6, 13, 0]]
picked = []
result =[]

def sum(a, n, picked):
	add = 0
	for i in range(n):
		add += a[picked[i][0], picked[i][1]]
	return add

def dfs(a, iD, jD, picked, n):
	# a: 소스 배열
	# depth: 탐색 깊이
	# picked: 선택된 경로
	# n: 선택되야 하는 경로의 숫자(도시 개수와 동일)

	# return 조건: 두 도시사이에 길이 없다 or n만큼 다 선택했다
	if (iD == n-1 and jD == n-1) or len(picked) == n-1:
		picked.append([jD, picked[0][0]])
		tmp = sum(a, n, picked)
		result.append(tmp)
		return
	for i in range(iD, n):		# i의 깊이
		for j in range(jD, n):  # j의 깊이
			if a[i][j]!=0:
				picked.append([i,j])
				print(picked)
			else:
				dfs(a, iD, jD+1, picked, n)
			dfs(a, iD+1 , jD, picked, n)

dfs(a, 0, 0, picked, n)
print(result)
