# 백준 2751 [수 정렬하기 2]

# 목표: 힙 정렬 구현하기

# --------------------------------------------------------------------------------------------------------
#  <31_3.py파일 heap구조의 issue>

# 백준에서 채점해보면 시간초과가 뜨는데 다음과 같은 문제 때문인 것으로 추정!
#
# 1. 부모노드를 정렬할 때마다 힙구조가 깨지는 것을 방지하기 위해 넣었던 재귀 구조(max_heap 아래)
# 2. 최초 배열에서 최소값이 맨 마지막 인덱스에 있으면 최소값이 맨 앞으로 오지 않는 문제 해결하기 위해 넣었던 마지막 if문

# =>

# --------------------------------------------------------------------------------------------------------



# 값 받기
# testcase = int(input())
# list = []
# for i in range(testcase):
# 	list.append(int(input()))

list = [1,2,3,4,5,6,7,8,9,10] # 원소 10개인 리스트

# 1. 배열을 힙 상태로 만들기
def max_heap(a, n, end):

	parent = n
	temp = a[parent]
	while parent < (end+1)//2: # 니가 부모가 맞니?
		left = parent*2+1
		right = parent*2+2

		biggerChild = right if right <= end and a[left] < a[right] else left #a[right]이 존재하는지 확인하지 않으면 index에러 발생할 수 있음
		if temp >= a[biggerChild]:
			break
		# 이제 매번 swap하지 않고 큰 자식을 부모자리에 복사하고 기준인덱스(부모)는 복사했던 자식 자리로 내려가다가
		# 저장해뒀던부모(temp)가 자식보다 클 경우에만 break하고 그 자리에 부모값(temp) 넣는다 +물론 기준인덱스에게 자식이 없어도(while문 조건) 종료
		a[parent] = a[biggerChild]
		parent = biggerChild
	a[parent] = temp

l = len(list)

# 부모 노드의 인덱스만 넣어야 함(자식없으면 안됨)
# 완전 이진 트리에서 부모의 개수(단말이 아닌 노드의 개수)는 len // 2(나머지 버림)
for i in range(l//2-1, -1, -1): # 부모노드의 개수-1, 이 -1이 될 때까지, -1씩 반복
														# (부모노드의 개수, 0, -1)이렇게 하지않고 부모노드의 개수에서 -1을 해준 이유는 i를 리스트의 인덱스로 넣어야했기 때문(0부터 시작하므로 개수-1)
	max_heap(list, i, l-1)
	# print(list)

for i in range(l-1, 0, -1):
	# print(str(a[0]),str(a[i]))
# 2. 힙의 루트를 배열의 맨 뒤로 밀고 힙의 단말에 있던(맨 뒤에 있던) 값을 루트에 넣는다.
	list[0], list[i] = list[i], list[0]
# 3. 자식노드 2개와 비교해 더 큰 자식과 swap한다.(본인값이 가장 클 때까지 || 단말에 도달해 자식이 더 이상 없을 때 까지 반복)
	max_heap(list, 0, i-1)
	# print(list)
# if list[0] > list[1]:   #최초 배열에서 최소값이 맨 마지막 인덱스에 있으면 최소값이 맨 앞으로 오지 않는 문제 해결
# 	list[0], list[1] = list[1], list[0]
	# print(list)
for i in range(len(list)):
	print(list[i])


