from collections import deque
import sys

input = sys.stdin.readline

# * 도착지점에 도착한다면, 즉시 While 문을 종료 해야 한다, 그렇지 않으면 다른 곳을 방문하고 돌아오는 경우가 생겨서 graph[x][y] 의 값이 달라짐.
def bfs(graph: list, que: deque, visited: list) -> int:
    tmp = 10**4 + 1
    while que:
        x, y = que.popleft()
        if x == row - 1 and y == col - 1:
            tmp = min(tmp, graph[x][y])
            break
        for (dx, dy) in DIRECTION:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    que.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1
                elif graph[nx][ny] == 2:
                    tmp = graph[x][y] + 1 + (row - 1 - nx) + (col - 1 - ny)
                visited[nx][ny] = 1

    return tmp


if __name__ == "__main__":
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    row, col, time = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    visited[0][0] = 1
    que = deque([(0, 0)])

    result = bfs(graph, que, visited)

    print("Fail" if result > time else result)
