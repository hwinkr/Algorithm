from collections import deque
import sys

input = sys.stdin.readline


def bfs(board: list, que: deque, cheeze: list) -> None:
    while que:
        x, y = que.popleft()

        for (dx, dy) in DIRECTION:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] != -1:
                if board[nx][ny] == 1:
                    cheeze.append((nx, ny))
                elif board[nx][ny] == 0:
                    que.append((nx, ny))
                board[nx][ny] = -1


if __name__ == "__main__":
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    row, col = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    que, cheeze, = (
        deque([(0, 0)]),
        [],
    )
    time = 0
    board[0][0] = -1

    while True:
        bfs(board, que, cheeze)
        if not cheeze:
            break
        time += 1
        count = len(cheeze)
        que, cheeze = deque(cheeze), []

    print(time)
    print(count)
