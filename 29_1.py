
n,r,c = list(int(i) for i in input().split())

cnt = 0
def z(n,R,C):
	global cnt
	global r
	global c

	if R == r and C == c:
		print(cnt)
		exit(0)
	if n == 1:
		# print(str(R)+', '+str(C))
		cnt += 1
		return
	z(n/2,R,C)
	z(n/2,R,C+n/2)
	z(n/2,R+n/2,C)
	z(n/2,R+n/2,C+n/2)

z(2**n,0,0)
