width, height = input().split()

width = int(width)
height = int(height)

count = int(input())

list0 =[0, height]
list1 =[0, width]
# 양 끝 모서리값을 리스트에 넣음

for i in range(count):
	tmp = list(int(i) for i in input().split())


	#  가로 점선을 따라 자를 경우 (y축 point)
	if tmp[0] == 0:
		list0.append(tmp[1])
	#  세로 점선을 따라 자를 경우 (x축 point)
	else:
		# tmp[0] == 1:
		list1.append(tmp[1])

# def sort(list):
# 	for i in range(1,len(list)):
# 		for j in range(i, len(list)):
# 			num1 = list[j-1]
# 			num2 = list[j]
# 			if num1 > num2:
# 				list[j-1], list[j] = list[j], list[j-1]
list0.sort()
list1.sort()
# 끊어지는 point를 순서대로 정렬


def findLen(list):
	lenList=[]
	for i in range(len(list)-1):
		lenList.append(list[i+1] - list[i])
	lenList.sort()
	biggest = lenList[len(lenList)-1]
	return biggest

heightB = findLen(list0)
widthB = findLen(list1)
# 각 point사이의 길이가 가장 긴 변을 선택

print(heightB * widthB)

