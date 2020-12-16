# 백준 1085 [직사각형에서 탈출]

x, y, w, h = input().split(' ')

x = int(x)
y = int(y)
w = int(w)
h = int(h)

smallest = -1

if x < w - x:
	round1 = x
else:
	round1 = w - x

if y < h - y:
	round2 = y
else:
	round2 = h - y

if round1 < round2:
	smallest = round1
else:
	smallest = round2

print(smallest)
