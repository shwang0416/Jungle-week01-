# 백준 4344 [평균은 넘겠지]

# https://c10106.tistory.com/2015 round가 왜 안될까?

testcase = int(input())

for j in range(0,testcase):
	inp = input().split()

	member = int(inp[0])
	sum = 0
	scorelist =[]
	for i in range(1,member+1):
		scorelist.append(int(inp[i]))
		sum = sum + int(inp[i])
	avg = sum / member
	count = 0
	for i in range(0,member):
		if scorelist[i] > avg:
			count += 1
	result = count/member *100
	print("%.3f" %result + "%")
