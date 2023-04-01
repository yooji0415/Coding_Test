def solution(s):
    answer = len(s)
    # 길이가 1일 때 부터 s의 길이의 반 까지만 돌면 될 것 같다.
    for cut in range(1, len(s) // 2 + 1):
        result = ""
        before = s[:cut]
        cnt = 0
        for i in range(0, len(s), cut):
            if before == s[i:i + cut]:
                cnt += 1
                continue
            result += before + (str(cnt) if cnt != 1 else "")
            cnt = 1
            before = s[i:i + cut]
        result += before + (str(cnt) if cnt != 1 else "")
        print(result)
        answer = min(answer, len(result))
    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("xababcdcdababcdcd"))
