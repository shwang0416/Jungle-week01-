# 백준 8958 [OX퀴즈]

testcase = int(input())

for i in range(0,testcase):
	str = input()
	list =[]
	sum = 0
	combo = 0
	for i in range(0,len(str)):
		list.append(str[i:i+1])
		if list[i] =='O':
			sum = sum + 1+ combo
			combo += 1
		else:
			combo = 0
	print(sum)




