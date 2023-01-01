from collections import deque
import sys

input = sys.stdin.readline

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(que, graph, visited):
    result = 10**4 + 1
    while que:
        x, y = que.popleft()
        if x == row - 1 and y == col - 1:
            result = min(result, graph[x][y])
            break
        for dx, dy in DIRECTIONS:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    que.append((nx, ny))
                elif graph[nx][ny] == 2:
                    tmp = graph[x][y] + 1 + (row - 1 - nx) + (col - 1 - ny)
                    if tmp <= time:
                        result = tmp
                visited[nx][ny] = 1

    if result > time:
        return "Fail"
    else:
        return result


if __name__ == "__main__":
    row, col, time = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0 for _ in range(col)] for _ in range(row)]
    visited[0][0] = 1
    que = deque([(0, 0)])

    result = bfs(que, graph, visited)
    print(result)
