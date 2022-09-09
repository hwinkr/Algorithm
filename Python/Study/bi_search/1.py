# 이분탐색 : 데이터를 하나씩 추적할떄마다 추적 범위를 절반으로 줄여가면서 더 효율적으로 데이터를 찾는 방법
from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

# 1. 재귀


def binary_search(s, e, target):
    if s > e:
        return None
    m = (s + e) // 2

    if target == arr[m]:
        return m

    if target > arr[m]:
        return binary_search(m + 1, e, target)
    else:
        return binary_search(s, m - 1, target)

# 2. 반복문


def binary_search2(s, e, target):
    while s <= e:
        mid = (s + e) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return None


n, target = map(int, input().split())
arr = list(map(int, input().split()))
result = binary_search(0, n - 1, target)

if result == None:
    print('해당 원소가 존재 하지 않습니다')
else:
    print(result + 1)


new_arr = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(new_arr, x))
print(bisect_right(new_arr, x))

# 값이 특정 범위에 속하는 데이터의 갯수 구하기


def count_range(left_value, right_value):
    left_idx = bisect_left(lst, left_value)
    right_idx = bisect_right(lst, right_value)
    return right_idx - left_idx


lst = [1, 2, 3, 3, 3, 3, 4, 8, 9]
cnt = count_range(2, 4)
print(cnt)

# parametric search 최적화 문제 -> 결정문제
