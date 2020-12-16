# 백준 10989 [수 정렬하기 3]
testcase = int(input())
a = []
for i in range(testcase):
	a.append(int(input()))

# 도수 정렬 구현
max = max(a)+1
# f = [0 for i in range(max)]
# s = [0 for i in range(testcase)]
f = [0] * max
s = [0] * testcase

# 0. a의 도수 분포표 f만들기
for i in range(testcase):
	f[a[i]] += 1

# 1. 도수 분포표 f를 누적 도수 분포표로 바꾸기
for i in range(1,max):
	f[i] += f[i-1]

# 2. s에서 도수 분포 리스트 f의 값 - 1에 해당하는 인덱스에 f의 인덱스를 넣는다.
# ※ 뒤에서부터 복사해야 안정적이다!
for i in range(testcase-1, -1, -1):
	f[a[i]] -= 1		# s[f[a[i]] - 1]
	s[f[a[i]]] = a[i]


# 3. a에 s복사
for i in range(testcase):
	print(s[i])
