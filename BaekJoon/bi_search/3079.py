# 랜선자르기 문제와 매우 유사하죠..

# 입국심사
# 모든 인원이 입국심사를 완료하는데 걸리는 최소시간
# 심사 시간의 최소화


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
times = [int(input()) for _ in range(n)]
times.sort()

start = times[0]
end = times[-1] * m
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for time in times:
        cnt += mid // time

    if cnt < m:
        start = mid + 1
    else:
        end = mid - 1
        ans = mid

print(ans)

# 이분탐색에서 최솟값 구하기 : 조건을 만족하는 큰 값부터 줄여나가면서 찾는다
# 이분탐색에서 최댓값 구하기 : 조건을 만족하는 작은값 부터 키워나가면서 찾는다
# 중요한 로직
# 용돈뽑는 횟수가 제한횟수보다 적다 -> 한번에 뽑는 금액이 많다 -> 줄여서 최소화
# 현재 시간에 대한 사람의 수가 검사해야하는 사람의 수보다 적다 -> 시간이 적다 -> 시간을 늘린다
# 많다 -> 시간이 많다 -> 줄여서 최소화
