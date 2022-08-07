# 안전영역

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x, y, height):
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if(0 <= nx < n) and (0 <= ny < n):
            if graph[nx][ny] > height and not visited[nx][ny]:
                dfs(nx, ny, height)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_height = max(max(graph))

area = []
# 비가 안온 경우도 check. 그렇지 않으면 런타임 에러 발생

for i in range(max_height):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for p in range(n):
        for q in range(n):
            if graph[p][q] > i and not visited[p][q]:
                cnt += 1
                dfs(p, q, i)
    area.append(cnt)

print(max(area))
