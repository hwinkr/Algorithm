import sys

input = sys.stdin.readline


def sol(n: int) -> int:
    devide_num = 10007
    if n <= 2:
        return dp[n] % devide_num

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % devide_num


if __name__ == "__main__":
    n = int(input())
    dp = [0] * 1001

    dp[1] = 1
    dp[2] = 2

    print(sol(n))
