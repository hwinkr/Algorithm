# 4방향 탐색을 모두 진행한후 위치값이 가장 큰 녀석을 고른다?
# 상 : -1 0
# 우 : 0 1
# 하 : 1 0
# 좌 : 0 -1
# 이동할 수 있는 경우에는 적힌값에 1을 더하고 que에 추가해준다
from collections import deque
n, m = map(int, input().split())

graph = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            # 폭탄이 있으면 건너뛴다
            elif graph[nx][ny] == 0:
                continue
            # 처음 방문한 경우에만 이전 노드값에 1을 더한다
            elif graph[nx][ny] == 1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

    return graph[n - 1][m - 1]


print(bfs(0, 0))
