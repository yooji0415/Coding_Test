arr = list(input())

strs = []
num = 0

for word in arr:
    if word.isdigit():
        num += int(word)
    else:
        strs.append(word)

strs.sort()

print("".join(strs) + str(num))
