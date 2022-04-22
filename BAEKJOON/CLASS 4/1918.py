import sys

in_str = sys.stdin.readline().strip()
answer = []
operator = []
priority = {
    '*': 3,
    '/': 3,
    '+': 2,
    '-': 2,
    '(': 1
}
for i in range(len(in_str)):
    if in_str[i].isalpha():
        answer.append(in_str[i])
    elif in_str[i] == '(':
        operator.append(in_str[i])
    elif in_str[i] == ')':
        while operator[-1] != '(':
            answer.append(operator.pop())
        operator.pop()
    else:
        while operator and priority[in_str[i]] <= priority[operator[-1]]:
            answer.append(operator.pop())
        operator.append(in_str[i])

while len(operator):
    answer.append(operator.pop())

print("".join(answer))
