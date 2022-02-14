import sys

n, k = map(int, sys.stdin.readline().split())
member = list(range(1, n+1))

index = k - 1
print("<", end="")
while len(member) > 1:
    if index < len(member):
        print("{}, ".format(member[index]), end="")
        member.pop(index)
    else:
        index = index % len(member)
        print("{}, ".format(member[index]), end="")
        member.pop(index)

    index += k - 1

print("{}>".format(member[0]), end="")
        