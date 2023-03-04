from collections import deque
import sys

input = sys.stdin.readline


def sol(start: list) -> int:
    r, c = start
    graph[r][c] = 0
    visited[r][c] = 1
    que = deque([(r, c)])

    while que:
        x, y = que.popleft()

        for (dx, dy) in DIRECTION:
            nx = x + dx
            ny = y + dy

            if (
                0 <= nx < row
                and 0 <= ny < col
                and graph[nx][ny] != 1
                and not visited[nx][ny]
            ):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    visited[nx][ny] = 1
                    que.append((nx, ny))
                else:
                    return graph[x][y] + 1

    return 0


if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = [list(map(int, input().rstrip())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 2:
                start = [i, j]
                break

    result = sol(start)
    if result == 0:
        print("NIE")
    else:
        print("TAK")
        print(result)
