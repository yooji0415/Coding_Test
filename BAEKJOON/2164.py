n = int(input())
test = 2
if n == 1 or n == 2:
    print(n)
else:
    while test < n:
        test *= 2

    if test == n:
        print(test)
    else:
        test /= 2
        print(2*int(n - test))
