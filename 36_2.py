# 백준 10971 [외판원 순회2]
# 앞서서 풀었던 35_2 [차이를 최대로]와 같이 순열 알고리즘으로 풀 수 있을 것으로 예상됨
# + 두 도시 사이에 길이 없는 경우(0)에도 return 해야 함

# 이전 시도에서 했던 실수 2가지

# 1. 앞서 36_1에서는 visited에 배열로 받은 경로별 값을 그대로 저장했는데,
# 그러면 이전에 방문했던 도시인지 아닌지 체크할 방법이 없다.
# => 방문한 도시의 인덱스 값을 받아와서 이전에 방문했던 도시인지 체크하고 패스해야 함!

# 2. 값을 저장하려고 하다보니 자연스럽게 도시를 오갔던 방향까지 체크해야됐고
#  		i와 j를 분리해 저장하다보니 이중 for문을 사용해서 코드가 복잡해졌다
# => 방향과 상관없이 방문한 도시의 인덱스를 한 번만 저장하면 visited가 이중리스트가 아닌 단일리스트로 저장된다. 검사for문도 이중이 아닌 단일로 구성가능.

# 참고 : https://seongjaemoon.github.io/algorithm/2018/03/03/algorithmTSP.html, https://ybdeveloper.tistory.com/19
# https://shoark7.github.io/programming/algorithm/introduction-to-tsp-and-solve-with-exhasutive-search
n = 4
dist = [[0, 10, 15, 20],[5, 0, 9, 10],[6, 13, 0, 12],[8, 8, 9, 0]]
ret = 99999999

def tsp(path, visited, currentLength):
	# a: 소스 배열
	# path:
	# visited: 방문했던 도시 저장 리스트
	# n: 선택되야 하는 경로의 숫자(도시 개수와 동일)
	# currentLength: 현재까지 온 거리

	# return 조건: n 만큼 다 선택했다    # Q. 왜 n-1까지만 하고 출발도시로 back은 직접 설정하지 않을까?? => A. 첫번째 도시에 간 것도 이동숫자에 포함되기 때문에 n이 내가 생각한 n-1이었던 것!
																									#  이후에 back은 직접 설정한다
	if len(path) == n:
		ret = currentLength + dist[path[0]][path[len(path)-1]]
		print(ret)
		print(path)
		return ret
	ret = 99999999  # 임의의 큰 값으로 초기화.

	for next in range(n):
		# 방문한 적 있는 도시인가?
		if visited[next]: continue
		if dist[len(path) -1][next] == 0: continue # 거리가 0이라면 못가는 길인것! continue
		# if visited[next]: continue
		# if dist[len(path) -1][next] == 0: continue # 거리가 0이라면 못가는 길인것! continue

		# 아니라면 방문, 기록 (visitedd 리스트의 next 인덱스(도시 번호)에 True값 저장)
		here = len(path) -1   # 현재 설정된 경로의 마지막 도시 == 현재 위치한 도시


		path.append(next)     # path에 방문한 도시 인덱스 기록
		visited[next] = True # Q. visited의 next인덱스에 True 기록 # 꼭 next인덱스에 해야하나?
							# A. => 인덱스값을 찾아서 방문했는지 체크하는 것이기 때문에 꼭 next인덱스에 해줘야 함.

							# Q. path 리스트만 가지고 풀 수 없나?
							# => 내가 혼자 다시 구현해보면서 시도해보자!

		# 출발도시에서 현재도착도시까지 온 거리 구함
		# Q. dist[here][here]이면 무슨값이던 0이 되는 게 아닌가??
			# dist[출발도시][도착도시(=here)] 이렇게 써야할 것 같은데...?

		# => 참고자료의 오타였음
		# dist[here(현재위치)][next(앞으로갈위치)]가 맞다

		cand = tsp(path, visited, currentLength + dist[here][next]) #candidate : min 후보경로

		# 이전까지의 최단경로와 현재 계산 경로중 더 작은 값을 리턴 값으로
		ret = ret if ret < cand else cand


		visited[next] = False # 다음 재귀문에서 방문할 때를 대비해 false 할당
		path.pop() # path의 마지막 요소 삭제

	return ret

visited = [False for i in range(n)]   #n만큼 False로 초기화
path =[]

# visited[0] = True  # 첫번째 도시를 제일 먼저 방문한 걸로 스타트
# path.append(0)  #첫번째 도시도 경로에 표시

for i in range(n):
	visited[i] = True
	path.append(i)
	tmp = tsp(path, visited, 0)
	# print(tmp)
	ret = tmp if ret > tmp else ret
	visited[i] = False
	path.pop()

# print(ret)
