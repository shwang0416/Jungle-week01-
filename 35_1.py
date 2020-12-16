# 백준 10819 [차이를 최대로] 완전탐색_중

# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|


# 1 2 3 4 5 6 7 8 9
# 1 9 2 8 7 3 7 4 6 5
# => 8 7 6 5 4 3 2 1 => 36
# 값이 오름차순으로 정렬된 리스트의 길이가 n일때
# 0, n-1, 1, n-2, 2, n-3... 의 순으로 정렬하면 최댓값을 구할 수 있다.
# => 왜??

a =[20, 1, 15, 8,4,10]
l = len(a)

for start in range(l-1):
	min = start
	for end in range(start+1,l):
		if a[min] > a[end]:
			min = end
	a[min], a[start] = a[start], a[min]

s= []
m= []

half = (l+1)//2
for i in range(half):
	s.append(a[i])

if l % 2 !=0: 			#홀수면
	for i in range(half,l-1):
		m.append(a[i])
	m.append(0)
else:
	for j in range(half,l): #짝수면
		m.append(a[j])

print(s)
print(m)

r= []
for i in range(half):
	r.append(s[i])
	r.append(m[half-1-i])

sum = 0
for i in range(len(r)-1):
	val = abs(r[i]-r[i+1])
	print(val)
	sum += val
print(sum)

