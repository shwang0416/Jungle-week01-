# 백준 2751 [수 정렬하기 2]

# 목표: 퀵 정렬 구현하기



list = [5, 2, 9, 4, 1, 3, 7, 8, 6, 0] # 원소 10개인 리스트
len = len(list)


# -----------------------피벗 기준 1회 나누기--------------------------------
#  1. 피벗을 정한다. (=> 일단 /2로!)
pivot = list[len//2]
#  2. 정렬대상의 첫번째, 마지막 원소 인덱스를 만든다.
start = 0
end = len-1

while start <= end:
	while list[start] < pivot: start +=1 #list[start]가 pivot보다 클 때까지 start++
	while list[end] > pivot: end -= 1    #list[end]가 pivot보다 작을 때까지 end--
	if start <= end:
		list[start], list[end] = list[end], list[start] # 둘이 서로 바꾼다
		start += 1
		end -= 1
# ----------------------------------------------------------------------

