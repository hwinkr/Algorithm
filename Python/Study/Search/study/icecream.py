n, m = map(int, input().split())

graph = []
answer = 0
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(graph, i, j):
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return

    if(graph[i][j] == 1):
        return
    else:
        graph[i][j] = 1
    # 탐색을 4방향 모두 진행
    dfs(graph, i - 1, j)
    dfs(graph, i + 1, j)
    dfs(graph, i, j - 1)
    dfs(graph, i, j + 1)


for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            answer += 1
            dfs(graph, i, j)

print(answer)
