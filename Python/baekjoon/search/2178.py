from collections import deque

n, m = map(int, input().split())

maze = []

for i in range(n):
    maze.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = 0, 0


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
            elif maze[nx][ny] == 0:
                continue

            if(maze[nx][ny] == 1):
                que.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

    return maze[n - 1][m - 1]


print(bfs(0, 0))
