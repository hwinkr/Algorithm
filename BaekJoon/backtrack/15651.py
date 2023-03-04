# 1 부터 n 까지 중복없이 m개를 고른 수열 , 같은수를 여러번 골라도 된다

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def dfs(lst):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    for i in range(1, n + 1):
        lst.append(i)
        dfs(lst)
        lst.pop()
        
for i in range(1, n + 1):
    dfs([i])
