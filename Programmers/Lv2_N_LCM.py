# 유클리드 호제법을 이용한 최대공약수 함수
# a % b == 0 이라면 최대공약수는 b가 된다.
# a % b != 0 이라면 gcd(a, b) == gcd(b, a%b) 가 성립한다.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


# 최대공배수는 주어진 두 수의 곱에서
# 두 수의 최대공약수를 나누어준 것이다.
def solution(num):
    temp = 1
    for n in num:
        # 리스트 안의 수들을 하나씩 꺼내서
        # 해당 수를 포함하는 최소공배수를 만들어준다.
        temp = (n * temp) / (gcd(n, temp))

    return temp
