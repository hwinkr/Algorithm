def solution(m, n, puddles):
    devide_num = 1000000007
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                continue

            if j == 1 and i == 1:
                continue
            else:  # j != 1 and i != 1
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n][m] % devide_num


print(solution(4, 3, [[2, 2]]))
