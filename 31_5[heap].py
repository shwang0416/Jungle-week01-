# 예제와 토씨하나 안 틀리게(변수명 빼고) 수정한 코드
# 내 코드에 문제가 있는 줄 알았는데 검색해보니까 파이썬이 원래 느려서 그렇다고 한다...
# pypy로 돌리니까 문제없이 통과함



testcase = int(input())
list = []
for i in range(testcase):
	list.append(int(input()))

def max_heap(a, n, end):
	temp = a[n]
	parent = n
	while parent < (end+1)//2:
		left = parent*2+1
		right = left+1

		biggerChild = right if right <= end and a[left] < a[right] else left
		if temp >= a[biggerChild]:
			break
		a[parent] = a[biggerChild]
		parent = biggerChild
	a[parent] = temp

l = len(list)

for i in range((l-1)//2, -1, -1):
	max_heap(list, i, l-1)

for i in range(l-1, 0, -1):
	list[0], list[i] = list[i], list[0]
	max_heap(list, 0, i-1)

for i in range(len(list)):
	print(list[i])


