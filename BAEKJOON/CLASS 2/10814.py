cycle = int(input())
member = []
for _ in range(cycle):
    age, name = input().split()
    member.append([int(age), name])

member.sort(key=lambda x: x[0])
for info in member:
    print("{} {}".format(info[0], info[1]))
