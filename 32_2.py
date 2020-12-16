# 백준 10989 [수 정렬하기 3]

# 문제의 경우 testcase의 범위가 1부터 10,000,000이므로 리스트에 그대로 담으면 메모리를 초과한다	=>왜?
# 숫자의 범위가 1부터 10000까지이므로 이를 이용해 도수 분포표를 만들어야 한다.
import sys

testcase = int(sys.stdin.readline())		# 시간을 줄이기 위해 input()대신 sys.stdin.readline() 사용
max = 10000
f = [0] * (max + 1) # index 0부터 max까지

# 도수분포리스트
for i in range(testcase):
	tmp = int(sys.stdin.readline())
	f[tmp] += 1

# 바로 프린트하면 되므로 누적도수분포표는 필요없음
for i in range(1,max+1):	# 1부터 10000까지
	for _ in range(f[i]):
		print(i)
