# 정점 n 간선 m
# dfs
import sys
sys.setrecursionlimit(10000)


def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())
edges = []

for i in range(m):
    edges.append(list(map(int, input().split())))

visited = [False] * (n + 1)
graph = []

for i in range(n + 1):
    graph.append([])
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

cnt = 0

for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)
