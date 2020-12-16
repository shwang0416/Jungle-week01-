# 백준 2751 [수 정렬하기 2]

# 목표: 퀵 정렬 구현하기

# 값 받기
testcase = int(input())
list = []
for i in range(testcase):
	list.append(int(input()))

# list = [5, 2, 9, 4, 1, 3, 7, 8, 6, 0] # 원소 10개인 리스트

def choosePivot(start, end):
	three =[]
	startP = list[start]
	middleP = list[(start+end)//2]
	endP = list[end]

	if endP < startP:
		endP, startP = startP, endP
	if startP > middleP:
		middleP, startP = startP, middleP
	elif middleP > endP:
		endP, middleP = middleP, endP

	three.append(startP)
	three.append(middleP)
	three.append(endP)

	return three
	# if startP >= middleP:
	# 	if middleP >= endP:
	# 		return middleP
	# 	elif startP >= endP:
	# 		return endP
	# 	else:
	# 		return startP
	# elif startP >= endP:
	# 	if endP >= middleP:
	# 		return endP
	# 	else:
	# 		middleP
	# else:
	# 	return startP

def quicksort(list, left, right):
	start = left +1
	end = right -2
	# -----------------------피벗 기준 1회 나누기--------------------------------
	#  1. 피벗을 정한다. (list[start], list[end], list[(start+end)//2]  중  중앙값 택)

	three = choosePivot(left, right)
	list[left] = three[0]
	list[(left+right)//2] = list[right-1]
	list[right-1] = three[1]
	list[right] =three[2]
	pivot = three[1]
	#  2. 정렬대상의 첫번째, 마지막 원소 인덱스를 만든다.

	while start <= end:
		while list[start] < pivot: start +=1 #list[start]가 pivot보다 클 때까지 start++
		while list[end] > pivot: end -= 1    #list[end]가 pivot보다 작을 때까지 end--
		if start <= end:
			list[start], list[end] = list[end], list[start] # 둘이 서로 바꾼다
			start += 1
			end -= 1
	# --------------------------------------------------------------------------
	if left < end: quicksort(list, left, end)
	if start < right:  quicksort(list, start, right)

quicksort(list,0,len(list)-1)

for i in range(len(list)): #range(x) : 0부터 x미만의 숫자
	print(list[i])
