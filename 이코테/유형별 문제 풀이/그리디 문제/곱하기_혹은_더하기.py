n = list(map(int, list(input())))

answer = n[0]

for i in range(1, len(n)):
    if answer == 0 or n[i] == 0:
        answer += n[i]
        continue

    answer *= n[i]

print(answer)
