from collections import deque
import sys

input = sys.stdin.readline


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))
            elif iceberg[nx][ny] == 0:
                melt_count[x][y] += 1


if __name__ == "__main__":
    row, col = map(int, input().split())
    iceberg = [list(map(int, input().split())) for _ in range(row)]
    year = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        group_cnt = 0
        melt_count = [[0] * col for _ in range(row)]
        visited = [[False] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if iceberg[i][j] > 0 and not visited[i][j]:
                    group_cnt += 1
                    bfs(i, j)

        if group_cnt == 0:
            print(0)
            break
        if group_cnt > 1:
            print(year)
            break

        for i in range(row):
            for j in range(col):
                iceberg[i][j] -= melt_count[i][j]
                if iceberg[i][j] < 0:
                    iceberg[i][j] = 0

        year += 1
