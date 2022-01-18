def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
gcd_num = gcd(a, b)
lcm_num = a * b // gcd_num
print(gcd_num)
print(lcm_num)
