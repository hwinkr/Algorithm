# # 토마토

# 상자에 안익은 토마토를 얼마나 가지고 있는지 세고 출발하는 것도 좋은 방법
# 함수의 반환값에 따라서 출력값이 달라지는 경우에는 그 함수의 반환값을 변수로 사용해서 그 변수를 이용하는것 보다 함수 안에서 모든 출력값을 조절할 수 있도록 설정하면 더 나은 코드와 효율적인 매모리 사용이 가능하다.

from collections import deque
import sys
m, n = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def bfs(que):
    day = 0
    size = len(que)
    cnt = 0
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if((0 <= nx < n) and (0 <= ny < m)):
                if(graph[nx][ny] == 0):
                    graph[nx][ny] = 1
                    que.append((nx, ny))
        cnt += 1

        if(cnt == size):
            day += 1
            size += len(que)

    return day - 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

day_que = deque()

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 1):
            day_que.append((i, j))

result = bfs(day_que)
success = 1

for i in range(n):
    for j in range(m):
        if(graph[i][j] == 0):
            success = 0
            break
if(success):
    print(result)
else:
    print(-1)
