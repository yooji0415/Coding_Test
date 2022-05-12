def solution(m, n, puddles):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 1
    # 웅덩이의 좌표를 표시해둔다
    for p in puddles:
        p_x, p_y = p[0], p[1]
        dp[p_y][p_x] = -1

    # 각 경로 확인
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if dp[y][x] < 0:
                continue
            if dp[y][x - 1] > 0:
                dp[y][x] += dp[y][x - 1]
            if dp[y - 1][x] > 0:
                dp[y][x] += dp[y - 1][x]

    return dp[n][m] % 1000000007
