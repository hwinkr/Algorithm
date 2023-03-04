# 나무 자르기

# 필요한 나무의 길이 < 나무 길이의 합 , 항상 원하는 길이의 나무를 가져갈 수 있다.
# 적어도 필요한 나무의 길이를 가져가기 위해 설정할 수 있는 높이의 최댓값

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
answer = 0

while start <= end:
    mid = (start + end) // 2
    len_sum = 0
    for len in lst:
        if len > mid:
            len_sum += len - mid

    if len_sum < m:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(answer)
