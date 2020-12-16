# 백준 2562 [최댓값]

list=[]
result = -1
index = -1

for i in range(0,9):
	list.append(int(input()))
for i in range(0,9):
	if list[i] > result:
		result = list[i]
		index = i


print(result)
print(index+1)
