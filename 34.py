#백준 2309 [일곱난쟁이] 완전탐색_하

a=[]
for i in range(9):
	a.append(int(input()))

# 전략: 9개의 숫자를 합산한 데에서 100을 뺀다. => 숫자 2개를 더했을 때 나머지 숫자(left)가 되는 조합을 찾는다!

# a= [11,60,19,4,1,2,3,15,6]


# x=a
# 나머지 숫자(left)보다 큰 숫자가 있다면 걔는 무조건 일곱난쟁이에 포함되는 숫자인 것!
left = sum(a) - 100
# for i in range(9):
# 	if left < x[i]:
# 		del x[i]
# print(left)



l = len(a)   #배열의 길이 다시 설정

# bf와 dfs중에서 뭐가 더 빠를까?
# bf
def bf():
	for start in range(l-1):
		for end in range(start+1,l):
			if a[start] + a[end] == left:
				del a[start]
				del a[end-1]
				return

# dfs
def dfs(start, end):

	# 종료조건 설정
	if a[start]+a[end] == left:
		del a[start]
		del a[end-1]
		return
	# 단계마다 반복할 코드 설정
	if end >= l-1:
		dfs(start+1,start+2)
	else:
		dfs(start, end+1)

dfs(0,1)
# bf()
# 둘 다 구현해보았다. bf 76ms, dfs 72ms로 거의 비슷했다.

l = len(a)

for i in range(l-1):
	min = i
	for j in range(i, l):
		if a[min] > a[j]:
			min = j
	a[min], a[i] = a[i], a[min]

for i in range(l):
	print(a[i])
