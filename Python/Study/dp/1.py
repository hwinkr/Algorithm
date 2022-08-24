# 개미전사
# dp : 최적 부분구조 + 중복되는 작은문제

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# i번째 창고까지 털었을 경우의 최적의 해를 구한다
# 현재까지의 최적해를 최적 부분구조를 통해서 구한다

d = [0] * n
d[0] = lst[0]
d[1] = max(lst[0], lst[1])

for i in range(2, n):
    d[i] = max(lst[i - 1], lst[i - 2] + lst[i])

print(d[n - 1])
