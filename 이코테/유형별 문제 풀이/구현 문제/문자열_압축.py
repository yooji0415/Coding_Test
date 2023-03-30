def solution(s):
    answer = int(1e9)
    if len(s) == 1:
        return 1
    # 문자열 길이는 최대 총 길이의 절반이다.
    for i in range(1, len(s) // 2 + 1):
        cnt_list = []
        word_list = []

        for j in range(0, len(s), i):
            now_word = s[j:j + i]

            if not word_list:
                word_list.append(now_word)
                cnt_list.append(1)
                continue

            if now_word == word_list[-1]:
                cnt_list[-1] += 1
            else:
                word_list.append(now_word)
                cnt_list.append(1)

        result = ""

        for i in range(len(word_list)):
            if cnt_list[i] != 1:
                result += str(cnt_list[i])
            result += word_list[i]

        answer = len(result) if len(result) < answer else answer

    return answer
