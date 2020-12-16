# 	백준 10872 [팩토리얼]

n = int(input())

def recrusive(n):
	if n >= 1:
		return n * recrusive(n-1)
	else:
		return 1
ans = recrusive(n)
print(ans)
