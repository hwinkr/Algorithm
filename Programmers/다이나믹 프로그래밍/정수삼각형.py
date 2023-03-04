def solution(triangle):
    size = len(triangle)

    dp = [[0] * size for _ in range(size)]
    dp[0][0] = triangle[0][0]

    idx = 2
    for i in range(1, size):
        for j in range(idx):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i - 1][j]
                continue
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        idx += 1

    return max(dp[size - 1])
