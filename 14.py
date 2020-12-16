# 백준 2577 [숫자의 개수]

# 함수 list.count(item) 구현

num1 = int(input())
num2 = int(input())
num3 = int(input())

result = num1 * num2 * num3
result = str(result)
list =[]
for i in range(0, len(result)):
	list.append(result[i:i+1])

for i in range(0,10):
	count = 0
	for j in range(0, len(list)):
		if int(list[j]) == i:
			count = count+ 1
		j += 1
	print(count)
	i += 1

