# 백준 10871 [X보다 작은 수]

n, x = input().split(' ')
n = int(n)
x = int(x)

list= input().split()
# for i in range(0, n):

for i in range(0,n):
	if int(list[i]) < x:
		print(list[i], end=' ')
