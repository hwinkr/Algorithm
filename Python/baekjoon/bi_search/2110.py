# 공유기 설치하기

# 가장 인접한 두 공유기 사이의 거리 최대로 하기

# 이분탐색...

# 집 사이의 최소 거리 : 1
# 집 사이의 최대 거리 : max - min
# 좌표 + 거리 -> 좌표

import sys
input = sys.stdin.readline

n, c = map(int, input().split())
lst = [int(input()) for _ in range(n)]
lst.sort()


start = 1
end = lst[-1] - lst[0]
dist = 0

while start <= end:
    mid = (start + end) // 2
    current = lst[0]
    cnt = 1

    for i in range(1, n):
        if current + mid <= lst[i]:
            cnt += 1
            current = lst[i]

    if cnt < c:
        end = mid - 1
    else:
        dist = mid
        start = mid + 1

print(dist)

# 거리의 최대화
# 설치한 공유기의 숫자가 제한숫자보다 많다 -> 공유기의 거리가 짧다
# 설치한 공유기의 숫자가 제한숫자보다 적다 -> 공유기의 거리가 멀다

# 뽑는금액의 최소화
# 출금횟수가 제한횟수보다 많다 -> 뽑는금액이 적다
# 출금횟수가 제한횟수보다 적다 -> 뽑는 금액이 많다.

# 심사시간의 최소화
#
