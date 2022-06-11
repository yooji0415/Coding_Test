import sys


N = int(sys.stdin.readline())
answer = []
fn_list = []
for _ in range(N):
    flag = False
    word_list = sys.stdin.readline().split()
    for i in range(len(word_list)):
        if word_list[i][0].lower() not in fn_list:
            fn_list.append(word_list[i][0].lower())
            flag = True
            word_list[i] = "[" + word_list[i][0] + "]" + word_list[i][1:]
            break

    if not flag:
        for i in range(len(word_list)):
            for j in range(len(word_list[i])):
                if word_list[i][j].lower() not in fn_list:
                    fn_list.append(word_list[i][j].lower())
                    flag = True
                    word_list[i] = word_list[i][:j] + "[" + word_list[i][j] + "]" + word_list[i][j + 1:]
                    break

            if flag:
                break

    answer.append(" ".join(word_list))

for word in answer:
    print(word)
