# 통계학

# 평균 , 중앙값 , 최빈값 , 범위

from collections import Counter
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

print(round(sum(arr) / n))

arr.sort()
print(arr[n // 2])

# use counter library

# arr_counter = Counter(arr).most_common()
# if(len(arr_counter) > 1):
#     if(arr_counter[0][1] == arr_counter[1][1]):
#         print(arr_counter[1][0])
#     else:
#         print(arr_counter[0][0])
# else:
#     print(arr_counter[0][0])
counts = dict()
for i in range(1, n + 1):
    counts[i] = []
count = 1
maxCount = 1

if n == 1:
    counts[1].append(arr[0])
else:
    for j in range(1, n):
        if arr[j] != arr[j - 1]:
            counts[count].append(arr[j - 1])
            if count > maxCount:
                maxCount = count
            count = 1
        else:
            count += 1
        if j == n - 1:
            counts[count].append(arr[j])
            if count > maxCount:
                maxCount = count
if len(counts[maxCount]) > 1:
    print(counts[maxCount][1])
else:
    print(counts[maxCount][0])

print(arr[-1] - arr[0])
