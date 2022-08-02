# bfs : queue로 구현

from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = []
for i in range(len(graph)):
    visited.append(False)


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    # queue가 빈 list가 아닌 동안
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)
