# # 토마토

#  내 풀이

from collections import deque
import sys

# m, n = map(int, sys.stdin.readline().split())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


# def bfs_my(que):
#     day = 0
#     size = len(que)
#     cnt = 0
#     while que:
#         x, y = que.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if((0 <= nx < n) and (0 <= ny < m)):
#                 if(graph[nx][ny] == 0):
#                     graph[nx][ny] = 1
#                     que.append((nx, ny))
#         cnt += 1

#         if(cnt == size):
#             day += 1
#             size += len(que)

#     return day - 1


# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# day_que = deque()

# for i in range(n):
#     for j in range(m):
#         if(graph[i][j] == 1):
#             day_que.append((i, j))

# result = bfs_my(day_que)
# success = 1

# for i in range(n):
#     for j in range(m):
#         if(graph[i][j] == 0):
#             success = 0
#             break
# if(success):
#     print(result)
# else:
#     print(-1)

# 좀 더 나은 풀이
# 상자에 안익은 토마토를 얼마나 가지고 있는지 세고 출발하는 것도 좋은 방법
# 함수의 반환값에 따라서 출력값이 달라지는 경우에는 그 함수의 반환값을 변수로 사용해서 그 변수를 이용하는것 보다 함수 안에서 모든 출력값을 조절할 수 있도록 설정하면 더 나은 코드와 효율적인 매모리 사용이 가능하다.
# 내 코드와 비교하면 메모리 사용이 거의 절반임

from collections import deque
import sys


def bfs():
    m, n = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    tmt_cnt = 0
    tmt = deque()

    day = 0

    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 0):
                tmt_cnt += 1
            elif(graph[i][j] == 1):
                tmt.append((i, j))

    while tmt and tmt_cnt:
        for _ in range(len(tmt)):
            x, y = tmt.popleft()

            if x > 0 and graph[x - 1][y] == 0:
                graph[x - 1][y] = 1
                tmt.append((x - 1, y))
                tmt_cnt -= 1
            if x < n - 1 and graph[x + 1][y] == 0:
                graph[x + 1][y] = 1
                tmt.append((x + 1, y))
                tmt_cnt -= 1
            if y > 0 and graph[x][y - 1] == 0:
                graph[x][y - 1] = 1
                tmt.append((x, y - 1))
                tmt_cnt -= 1
            if y < m - 1 and graph[x][y + 1] == 0:
                graph[x][y + 1] = 1
                tmt.append((x, y + 1))
                tmt_cnt -= 1
        day += 1

    if tmt_cnt:
        print(-1)
    else:
        print(day)


if __name__ == '__main__':
    bfs()
