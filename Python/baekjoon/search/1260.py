from collections import deque


n, m, v = map(int, input().split())

edges = []


for i in range(m):
    edges.append(list(map(int, input().split())))


visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

graph = []
for i in range(n + 1):
    graph.append([])

for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

for connect_list in graph:
    connect_list.sort()


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    que = deque()
    que.append(start)
    visited[start] = True

    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
