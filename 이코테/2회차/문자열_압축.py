def solution(s):
    if len(s) == 1:
        return 1

    answer = int(1e9)

    for length in range(1, len(s) // 2 + 1):
        word = ""
        cnt = 0
        result = ""

        for i in range(0, len(s), length):
            if word == "":
                word = s[i:i + length]
                cnt = 1
                continue

            if word == s[i:i + length]:
                cnt += 1
                continue

            # 여기까지 왔다는 것은 구간이 달라졌다는 뜻이다.
            # 그러면 카운트가 1인 경우와 아닌 경우를 나누자
            if cnt == 1:
                result += word
            else:
                result += str(cnt) + word
            word = s[i:i + length]
            cnt = 1

        # 나와서도 한번 처리해줘야 한다.
        if cnt == 1:
            result += word
        else:
            result += str(cnt) + word

        if answer > len(result):
            # print(result)
            answer = len(result)

    return answer
