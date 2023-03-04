# 같은수를 여러번 골라도 된다
# 비내림차순을 만족하면 출력

# ! 시간초과 , pypy3으로 해결하면 맞음. 근데 python3 으로 풀어야함

import sys
input = sys.stdin.readline

n, m = map(int,  input().split())

lst = []


def dfs(start):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(start, n + 1):
        lst.append(i)
        dfs(i)
        lst.pop()


dfs(1)
# import sys
# input = sys.stdin.readline

# n, m = map(int,  input().split())


# def dfs(lst):
#     if len(lst) == m:
#         arr = [num for num in lst]
#         arr.sort()
#         if arr == lst:
#             print(' '.join(map(str, lst)))
#         return

#     for i in range(1, n + 1):
#         lst.append(i)
#         dfs(lst)
#         lst.pop()


# for i in range(1, n + 1):
#     dfs([i])
