# 정점 n 간선 m
# dfs

# pypy3 으로 제출해야 시간초과가 나지 않네.. 왜 그런거지

# 1
import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
    graph[a].append(b)

visited = [False] * (n + 1)

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)
