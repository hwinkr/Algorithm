# 1. using library
# from bisect import bisect_left, bisect_right
# import sys
# input = sys.stdin.readline

# n, target = map(int, input().split())
# lst = list(map(int, input().split()))


# def cnt_search(left, right):
#     val_left = bisect_left(lst, left)
#     val_right = bisect_right(lst, right)
#     return val_right - val_left


# result = cnt_search(target, target)
# if result == 0:
#     print(-1)
# else:
#     print(result)
# input = sys.stdin.readline

# 2. no using library

import sys
input = sys.stdin.readline

# 끝 인덱스 - 시작 인덱스 + 1 -> answer


def search_start(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            if lst[mid - 1] != target or mid - 1 < 0:
                return mid
            else:
                end = mid - 1
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return - 1


def search_end(start, end, target):
    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            if lst[mid + 1] != target or mid + 1 > n - 1:
                return mid
            else:
                start = mid + 1
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


n, x = map(int, input().split())
lst = list(map(int, input().split()))

if search_start(0, n - 1, x) == -1:
    print(-1)
else:
    print(search_end(0, n - 1, x) - search_start(0, n - 1, x) + 1)
