def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)

    # 평면으로 생각하기 위해서 1번을 집는 유무로 분할
    s1 = sticker[:-1]
    s2 = sticker[1:]

    dp1 = [0] * len(s1)
    dp1[0] = s1[0]
    dp1[1] = s1[0]
    for i in range(2, len(s1)):
        dp1[i] = max(dp1[i - 2] + s1[i], dp1[i - 1])

    dp2 = [0] * len(s2)
    dp2[0] = s2[0]
    dp2[1] = max(s2[0], s2[1])
    for i in range(2, len(s2)):
        dp2[i] = max(dp2[i - 2] + s2[i], dp2[i - 1])

    return max(dp1[-1], dp2[-1])