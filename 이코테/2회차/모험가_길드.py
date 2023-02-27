n = int(input())
people = list(map(int, input().split()))
people.sort()

answer = 0
cnt = 0
for person in people:
    cnt += 1
    if person <= cnt:
        answer += 1
        cnt = 0

print(answer)
