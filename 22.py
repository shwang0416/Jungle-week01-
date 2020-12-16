# 백준 	1978 [소수 찾기]
# 몇까지 나눠 봐야 가장 빨리 판별할까??

n = int(input())
list = list(int(i) for i in input().split())

count = 0
for num in list:
	if num == 1:
		continue
	elif num == 2:
		count += 1
	elif num == 3:
		count += 1
	else:
		for i in range(2,int(num/2)+1):
			if num % i == 0:
				break
			elif i == int(num/2):
				count = count + 1
				# 소수 발견!
print(count)
