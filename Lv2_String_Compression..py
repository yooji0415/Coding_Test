def solution(s):
    result_list = []
    # 길이의 절반일 경우까지만 본다
    for i in range(1, len(s) // 2 + 1):
        result = 0
        cnt = 1
        idx = 0
        while idx + i <= len(s):
            while idx + i * 2 <= len(s):
                if s[idx:idx + i] == s[idx + i:idx + i * 2]:
                    cnt += 1
                    idx += i
                else:
                    break

            if cnt != 1:
                result = result + len(str(cnt)) + i
                idx += 1
            else:
                result += 1
                idx += 1

        result_list.append(result)

    return min(result_list)