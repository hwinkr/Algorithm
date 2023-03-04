# 예산

# 배정을 받지 못하는 지방은 없다

import sys
input = sys.stdin.readline

n = int(input())
area = list(map(int, input().split()))
m = int(input())

start = 0
end = max(area)
answer = 0

while start <= end:
    mid = (start + end) // 2

    cost = 0
    for money in area:
        if money > mid:
            money = mid
        cost += money

    if cost <= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
