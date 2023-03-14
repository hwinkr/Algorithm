from collections import deque


def solution(maps):
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    row = len(maps)
    col = len(maps[0])

    visited = [[0] * col for _ in range(row)]
    visited[0][0] = 1
    que = deque([(0, 0)])

    while que:
        x, y = que.popleft()
        if x == row - 1 and y == col - 1:
            return maps[x][y]
        for dx, dy in DIRECTION:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    visited[nx][ny] = 1
                    que.append((nx, ny))

    return -1


print(
    solution(
        [
            [1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
        ]
    )
)
