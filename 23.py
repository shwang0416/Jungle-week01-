# 백준 9020 [골드바흐의 추측]

def isPrime(n):
	for i in range(2,int(n/2)+1):
		if n % i == 0:
			return -1
	return 1

testcase = int(input())

list = []
for i in range(0, testcase):
	list.append(int(input()))


for num in list:
	for point in range(int(num/2), num):
		if isPrime(num - point) == 1 and isPrime(point) == 1:
			print(str(num - point) + ' '+ str(point))
			break




