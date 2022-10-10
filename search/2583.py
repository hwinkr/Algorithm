from collections import deque
import sys

input = sys.stdin.readline


def bfs(i, j, cnt):
    que = deque()
    que.append((i, j))
    table[i][j] = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if (0 <= new_x < m) and (0 <= new_y < n):
                if table[new_x][new_y] == 0:
                    table[new_x][new_y] = 1
                    cnt += 1
                    que.append((new_x, new_y))

    return cnt


if __name__ == "__main__":
    m, n, k = map(int, input().split())
    table = [[0] * (n) for _ in range(m)]
    rects = [list(map(int, input().split())) for _ in range(k)]
    areas_cnt = 0
    areas = []

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for rect in rects:
        y1, x1, y2, x2 = rect[0], rect[1], rect[2], rect[3]
        for x in range(x1, x2):
            for y in range(y1, 2):
                table[x][y] = 1

    for i in range(m):
        for j in range(n):
            if table[i][j] == 0:
                areas_cnt += 1
                area = bfs(i, j, 1)
                areas.append(area)

    print(areas_cnt)
    areas.sort()
    for area in areas:
        print(area, end=" ")
