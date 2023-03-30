target = input()
target = list(target.upper())

num_sum = 0
answer = []
for word in target:
    if word.isalpha():
        answer.append(word)
    else:
        num_sum += int(word)

print("".join(sorted(answer)) + str(num_sum))
