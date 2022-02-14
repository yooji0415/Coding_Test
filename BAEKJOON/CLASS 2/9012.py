n = int(input())
answer = []
for _ in range(n):
    is_ok = True
    word = input()
    cnt = 0
    for i in range(len(word)):
        if word[i] == "(":
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            is_ok = False
            break

    if cnt == 0 and is_ok:
        print("YES")
    else:
        print("NO")
