from collections import deque
import sys

input = sys.stdin.readline

# ? 어떻게 덩어리의 수를 세지
# * 각 빙산을 반복문을 돌면서 -1 해주는 함수
# * 그 함수가 일을 끝내면 덩어리의 수를 세는 함수 만약 그 함수의 반환값이 2보다 크면 year을 반환한다
# *


def iceberg_melts():
    for x in range(row):
        for y in range(col):
            if iceberg[x][y] > 0:
                visited[x][y] = True
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (
                        0 <= nx < row
                        and 0 <= ny < col
                        and iceberg[nx][ny] == 0
                        and not visited[nx][ny]
                    ):
                        if iceberg[x][y] >= 1:
                            iceberg[x][y] -= 1


def bfs(x, y):
    que = deque()
    que.append((x, y))
    visited[x][y] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < row
                and 0 <= ny < col
                and iceberg[nx][ny] > 0
                and not visited[nx][ny]
            ):
                visited[nx][ny] = True
                que.append((nx, ny))


if __name__ == "__main__":
    row, col = map(int, input().split())
    iceberg = [list(map(int, input().split())) for _ in range(row)]
    year = 0
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while True:
        group_cnt = 0
        visited = [[False] * col for _ in range(row)]
        iceberg_melts()
        year += 1
        visited = [[False] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if iceberg[i][j] > 0 and not visited[i][j]:
                    group_cnt += 1
                    bfs(i, j)

        if group_cnt == 0:
            print(0)
            break

        if group_cnt >= 2:
            print(year)
            break
