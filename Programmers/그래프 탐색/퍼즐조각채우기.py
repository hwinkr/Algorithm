from collections import deque

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(i, j, board, visited):
    limit = len(board)
    locations = [[i, j]]
    que = deque([(i, j)])
    visited[i][j] = True

    while que:
        x, y = que.popleft()

        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < limit
                and 0 <= ny < limit
                and not visited[nx][ny]
                and board[nx][ny] == 1
            ):
                visited[nx][ny] = True
                locations.append([nx, ny])
                que.append((nx, ny))

    return locations


def makes_shape(puzzle_locations: list):
    rows = []
    cols = []
    for location in puzzle_locations:
        rows.append(location[0])
        cols.append(location[1])

    min_row, max_row = min(rows), max(rows)
    min_col, max_col = min(cols), max(cols)
    puzzle_shape = [[0] * (max_col - min_col + 1) for _ in range(max_row - min_row + 1)]

    for location in puzzle_locations:
        x = location[0] - min_row
        y = location[1] - min_col
        puzzle_shape[x][y] = 1

    return puzzle_shape


def puzzle_rotate(puzzle):
    row = len(puzzle)
    col = len(puzzle[0])
    puzzle_rotated = [[0] * row for _ in range(col)]

    for r in range(row):
        for c in range(col):
            puzzle_rotated[c][row - 1 - r] = puzzle[r][c]

    return puzzle_rotated


def solution(game_board, table):
    size = len(game_board)
    visited = [[False] * size for _ in range(size)]
    puzzle_shapes = []
    puzzle_weight = []

    for i in range(size):
        for j in range(size):
            if table[i][j] == 1 and not visited[i][j]:
                puzzle_locations = bfs(i, j, table, visited)
                puzzle_weight.append(len(puzzle_locations))
                shape = makes_shape(list(puzzle_locations))
                puzzle_shapes.append(shape)

    for _ in range(4):
        puzzle = puzzle_rotate(puzzle_shapes[0])
        print(puzzle)
    answer = -1
    return answer


print(
    solution(
        [
            [1, 1, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 0, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 0],
        ],
        [
            [1, 0, 0, 1, 1, 0],
            [1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 1],
            [0, 0, 1, 0, 0, 0],
            [1, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 0],
        ],
    )
)
