# 백준 2869 [달팽이는 올라가고 싶다]

list = list(int(i) for i in input().split())
a = list[0]
b = list[1]
v = list[2]

point = 0
day = 1

skip = int((v-a)/(a-b))
day += skip * day
point += skip * (a - b)

while point < v:
	point += a
	if point >= v:
		break
	point -= b
	day += 1
print(day)
