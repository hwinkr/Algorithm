# 피보나치 수 1

# 할당 되기 전에 참조됨

import sys
input = sys.stdin.readline


def fibo_re(n):
    global cnt_re
    if n != 1 and n != 2:
        cnt_re += 1
    if n == 1 or n == 2:
        return 1
    return fibo_re(n - 1) + fibo_re(n - 2)


def fibo_dp(n):
    cnt_dp = 0
    d[0], d[1] = 0, 0
    for i in range(2, n):
        cnt_dp += 1
        d[i] = d[i - 1] + d[i - 2]
    return cnt_dp


n = int(input())
d = [0] * n
cnt_re = 0

fibo_re(n)
print(cnt_re + 1, fibo_dp(n))
