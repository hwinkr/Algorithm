# 최대 랜선 길이 구하기

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

len_max = max(lst)

# n 개보다 많이 만드는것도 n개를 만드는 것에 포함이다
# 런타임 에러 .. 프로그램 비정상 종료


def cnt(start, end, target):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        len_sum = 0

        for len in lst:
            len_sum += len // mid

        if len_sum < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer


print(cnt(1, len_max, n))
