# 1 부터 n 까지 중복없이 m개를 고른 수열

import sys
input = sys.stdin.readline

n, m = map(int, input().split())


def dfs(start, lst):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(1, n + 1):
        if i not in lst:
            lst.append(i)
            dfs(start, lst)
            lst.pop()

# lst = []

# def dfs2():
#     if len(lst) == m:
#         print(" ".join(map(str, lst)))

#     for i in range(1 , n + 1):
#         lst.append(i)
#         dfs()
#         lst.pop()


for i in range(1, n + 1):
    dfs(i, [i])
