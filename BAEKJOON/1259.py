while True:
    num = input()
    state = "yes"
    if num == "0":
        break
    else:
        for i in range(len(num)//2):
            if num[i] != num[-(i+1)]:
                state = "no"
                break

    print(state)

