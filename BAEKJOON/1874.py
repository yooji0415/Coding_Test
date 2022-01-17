cycle = int(input())
input_arr = []
stack = []
answer = ""
num = 1
flag = True
for i in range(cycle):
    input_arr.append(int(input()))

for i in range(cycle):
    while num <= input_arr[i]:
        stack.append(num)
        answer += "+"
        num += 1

    if stack[-1] == input_arr[i]:
        stack.pop()
        answer += "-"
    else:
        flag = False
        break

if flag:
    for i in range(len(answer)):
        print(answer[i])
else:
    print("NO")
