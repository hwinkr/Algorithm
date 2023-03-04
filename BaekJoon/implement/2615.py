import sys

input = sys.stdin.readline
DIRECTION = [(-1, 1), (0, 1), (1, 1), (1, 0)]


def is_win(board: list, color: int, x: int, y: int) -> bool:
    for (dx, dy) in DIRECTION:
        if (
            not (0 <= x - dx < 19 and 0 <= y - dy < 19)
            or board[x - dx][y - dy] != color
        ):
            nx = x + dx
            ny = y + dy
            cnt = 1
            while (0 <= nx < 19 and 0 <= ny < 19) and board[nx][ny] == color:
                cnt += 1
                nx += dx
                ny += dy
            if cnt == 5:
                return True
    return False


def sol(board: list) -> list:
    for i in range(19):
        for j in range(19):
            if board[i][j] == 1:
                if is_win(board, 1, i, j):
                    return [1, i, j]
            elif board[i][j] == 2:
                if is_win(board, 2, i, j):
                    return [2, i, j]
    return [0]


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(19)]
    result = sol(board)

    if len(result) == 1:
        print(result[0])
    else:
        print(result[0])
        print(result[1] + 1, result[2] + 1)
