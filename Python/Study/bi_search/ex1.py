# import sys
# input = sys.stdin.readline

# n, target = map(int, input().split())
# lst = list(map(int, input().split()))

# lst.sort()


# def search(start, end, target):
#     if start > end:
#         return None

#     mid = (start + end) // 2
#     len_total = 0
#     for length in lst:
#         if length - lst[mid] > 0:
#             len_total += length - lst[mid]

#     if len_total > target:
#         return search(mid + 1, end, target)
#     if len_total < target:
#         return search(start, mid - 1, target)
#     else:
#         return mid


# result = search(0, n - 1, target)
# if result == None:
#     print('-1')
# else:
#     print(lst[result])
import sys
input = sys.stdin.readline

n, target = map(int, input().split())
lst = list(map(int, input().split()))

result = 0
s = 0
e = max(lst)


while s <= e:
    total = 0
    m = (s + e) // 2

    for len in lst:
        if len > m:
            total += len - m

    if total < target:
        e = m - 1
    else:
        result = m
        s = m + 1


print(result)
