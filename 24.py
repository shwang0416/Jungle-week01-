# 백준 1065 [한수]
# 더 효율적으로 풀 방법..?

n = int(input())

count = 0

for i in range(1, n+1):
	if i < 100:
		count += 1
	else:
		num = str(i)
		list =[]
		result = []

		for j in range(0,len(num)):
			list.append(num[j:j+1])
			# print('list['+str(j)+']:'+str(list[j]))

		for j in range(0, len(num)-1):
			result.append(int(list[j])-int(list[j+1]))
			# print(str(list[j])+' - '+str(list[j+1]))

		same = result[0]
		ans = 1
		for j in result:
			if j != same:
				ans = -1

		if ans == 1:
			count += 1

print(count)

