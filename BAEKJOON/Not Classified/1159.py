import sys


N = int(sys.stdin.readline().strip())
alpha_dict = {}
for _ in range(N):
    name = sys.stdin.readline().strip()
    if name[0] not in alpha_dict:
        alpha_dict[name[0]] = 1
    else:
        alpha_dict[name[0]] += 1

answer_list = []
for name in alpha_dict.keys():
    if alpha_dict[name] >= 5:
        answer_list.append(name)

if not answer_list:
    print("PREDAJA")
else:
    answer_list.sort()
    print("".join(answer_list))
