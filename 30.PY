# 백준 2750 [수 정렬하기]


# 목표: 이진 삽입 정렬 알고리즘 구현

testcase = int(input())

list =[]
for i in range(testcase):
	list.append(int(input()))

# list = [5, 9, 6, 4, 2, 1, 7]

def binary_insertion_sort(a):

	n = len(a)
	for i in range(1, n):
	# index 1부터 리스트 끝까지 비교
		key = a[i]
		# print('------i: '+ str(i)+', key: '+str(key))
		# 검색할 key값 저장
		start = 0
		# 검색범위의 맨 앞 원소 인덱스
		end = i - 1
		# 검색범위의 맨 끝 원소 인덱스
		# print('start: '+str(start) + ' end:'+str(end))

		while True:
			middle = (start+end) // 2
			#  // : 나머지 버리고 나누기
			# print('middle: '+str(middle) +', a[middle]: '+str(a[middle]))

			if a[middle] == key:
				# print('key: '+ str(key)+' 검색 성공')
				break			# 검색 성공

			elif a[middle] < key:
				start = middle + 1

			else: # a[middle] > key:
				end = middle - 1

			# print('start: '+str(start) + ' end:'+str(end))
			if start > end:
				break
		insert = middle + 1 if start <= end else end + 1 	# 삽입할 위치의 인덱스
							# 검색을 성공했다면 middle + 1자리, 아니라면 end + 1자리에 삽입
		for j in range(i, insert, -1):
			a[j] = a[j-1]
		a[insert] = key
		# print(list)/


binary_insertion_sort(list)
for i in range(len(list)):
	print(list[i])
