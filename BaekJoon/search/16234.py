from collections import deque
import sys

input = sys.stdin.readline


def calc(group: list) -> None:
    num = sum(graph[x][y] for (x, y) in group) // len(group)

    for (x, y) in group:
        graph[x][y] = num


def solution(graph: list, visited: list, start: list) -> list:
    x, y = start
    que = deque([(x, y)])
    group = [(x, y)]

    while que:
        x, y = que.popleft()
        for (dx, dy) in DIRECTION:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if min <= abs(graph[x][y] - graph[nx][ny]) <= max:
                    visited[nx][ny] = True
                    group.append((nx, ny))
                    que.append((nx, ny))

    return group


if __name__ == "__main__":
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    n, min, max = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    day = 0
    total = []
    while True:
        # ! while 문을 한번 돌 때, 무조건 모든 그래프 탐색이 완료 되어야 한다.
        visited = [[False] * n for _ in range(n)]
        flag = False
        tmp = []

        for i in range(n):
            for j in range(n):
                if (i, j) in total:
                    continue
                if not visited[i][j]:
                    visited[i][j] = True
                    group = solution(graph, visited, [i, j])
                    if len(group) > 1:
                        flag = True
                        calc(group)
                        for (x, y) in group:
                            if (x, y) not in tmp:
                                tmp.append((x, y))

        total = tmp
        if not flag:
            break

        day += 1

    print(day)
