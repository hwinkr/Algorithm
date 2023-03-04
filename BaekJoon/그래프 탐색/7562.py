# 나이트의 이동
# bfs

from collections import deque
import sys


def bfs():
    input = sys.stdin.readline
    test = int(input())
    answers = []
    dirs = [[-1, -2], [-2, -1], [-2, 1], [-1, 2],
            [1, 2], [2, 1], [2, -1], [1, -2]]

    for _ in range(test):
        n = int(input())
        curr_x, curr_y = map(int, input().split())
        dest_x, dest_y = map(int, input().split())

        graph = [[0] * n for _ in range(n)]

        que = deque()
        que.append((curr_x, curr_y))

        while que:
            x, y = que.popleft()
            if((x == dest_x) and (y == dest_y)):
                answers.append(graph[x][y])
                break

            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]

                if((0 <= nx < n) and (0 <= ny < n)):
                    if(graph[nx][ny] == 0):
                        graph[nx][ny] = graph[x][y] + 1
                        que.append((nx, ny))

    for answer in answers:
        print(answer)


if __name__ == "__main__":
    bfs()
