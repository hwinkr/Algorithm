# 1 부터 n 까지 중복없이 m개를 고른 수열
# 고른 수열은 무조건 오름차순

import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def dfs(start, lst):
    if len(lst) == m:
        arr = [num for num in lst]
        arr.sort()
        if lst == arr:
            print(' '.join(map(str, lst)))
        return

    for i in range(1, n + 1):
        if i not in lst:
            lst.append(i)
            dfs(start, lst)
            lst.pop()

for i in range(1, n + 1):
    dfs(i, [i])

# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# # 1 ~ n

# lst = []


# def dfs(start):
#     if len(lst) == m:
#         print(' '.join(map(str, lst)))
#         return

#     for i in range(start, n + 1):
#         if i not in lst:
#             lst.append(i)
#             dfs(i)
#             lst.pop()


# dfs(1)
