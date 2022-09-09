from collections import deque
import sys


def bfs(x, y):
    que = deque()
    que.append((x, y))

    cnt = 1
    graph[x][y] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if((0 <= nx < n) and (0 <= ny < n)):
                if(graph[nx][ny]):
                    que.append((nx, ny))
                    cnt += 1
                    graph[nx][ny] = 0
    answers.append(cnt)


n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answers = []

for i in range(n):
    for j in range(n):
        if(graph[i][j] == 1):
            bfs(i, j)

print(len(answers))
answers.sort()
for answer in answers:
    print(answer)
