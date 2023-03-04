import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def location_rect(curr: list) -> int:
    x, y = curr
    return (x // 3) * 3 + (y // 3)


def movable(curr: list, num: int) -> bool:
    x, y = curr
    return (
        num not in graph[x]
        and num not in [row[y] for row in graph]
        and not rect[location_rect([x, y])][num]
    )


def solution(graph: list, location_zero: list) -> None:
    if not location_zero:
        for i in range(9):
            for j in range(9):
                print(graph[i][j], end="")
            print()
        exit(0)

    x, y = location_zero[-1][0], location_zero[-1][1]
    for i in range(1, 10):
        if movable([x, y], i):
            location_zero.pop()
            graph[x][y] = i
            rect[location_rect([x, y])][i] = 1
            solution(graph, location_zero)
            location_zero.append([x, y])
            graph[x][y] = 0
            rect[location_rect([x, y])][i] = 0


if __name__ == "__main__":
    graph = [list(map(int, input().rstrip())) for _ in range(9)]
    rect = [[0] * 10 for _ in range(9)]
    location_zero = []
    for i in range(9):
        for j in range(9):
            if graph[i][j] != 0:
                rect[location_rect([i, j])][graph[i][j]] = 1
            else:
                location_zero.append([i, j])
    location_zero.reverse()
    solution(graph, location_zero)
