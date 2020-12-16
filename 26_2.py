# do it 알고리즘 책 재귀함수 실습 [5-2] [유클리드 호제법으로 최대공약수 구하기]

# 보이는 대로 써 봄
# def gcd(x,y):   # 22, 8
# 	gcd(x%y, y)  # 6, 8
# 	gcd(x, y%x)  # 6, 2
# 	gcd(x%y, y)  # 0, 2

# 재귀를 적용하도록 나눠질 변을 y로 둔다

def gcd(x,y):

	if y == 0:
		return x
	gcd(y,x%y)

gcd(22, 8)
