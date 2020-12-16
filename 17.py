# 백준 2675 [문자열 반복]

testcase = int(input())

for t in range(0,testcase):
	r, s = input().split()
	r = int(r)
	p =''
	for i in range(0,len(s)):
		for j in range(0, r):
			p = p + s[i]

	print(p)
