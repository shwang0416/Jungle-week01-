# 백준 2438 [별 찍기 -1]

input = int(input())
tmp = 0

for i in range(0, input):
	tmp += 1
	for i in range(0, tmp):
		print('*', end='')
	print()
