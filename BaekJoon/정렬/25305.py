# 커트라인
# 상을 받는 사람중 가장 낮은 사람의 점수

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
print(nums[k - 1])
