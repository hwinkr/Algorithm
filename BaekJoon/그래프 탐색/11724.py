# 정점 n 간선 m
# dfs

# map(int, sys.stdin.readline().split()) 을 사용하면 시간초과 안남

# 1
from collections import deque
import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    visited[start] = True
    que = deque()
    que.append(start)

    while que:
        x = que.popleft()

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                que.append(i)


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
        bfs(i)

print(cnt)
