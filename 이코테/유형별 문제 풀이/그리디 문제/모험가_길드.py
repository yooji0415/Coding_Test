n = int(input())
people = list(map(int, input().split()))

people.sort()

print(people)

cnt = 0
answer = 0

for person in people:
    cnt += 1
    if person <= cnt:
        cnt = 0
        answer += 1

print(answer)
