# 유기농 배추

# 배추가 있는경우 , 상하좌우로 이동하면서 모든 방향에 인접한 배추가 없을때까지 탐색을 진행한다. 새로운 탐색이 시작 될 때마다 +1 을 해준다

# 1. dfs
# 백준에서는 재귀함수의 최대 반복이 1000번 으로 자동 제한이 걸려있어 런타임에러가 발생할 수 있다. 이를 처리하기위한 코드
from collections import deque
import sys
sys.setrecursionlimit(10000)


def dfs(graph, i, j):
    if(i < 0 or i > n - 1 or j < 0 or j > m - 1):
        return
    if(graph[i][j] == 0):
        return
    graph[i][j] = 0

    dfs(graph, i - 1, j)
    dfs(graph, i, j + 1)
    dfs(graph, i + 1, j)
    dfs(graph, i, j - 1)


test_dfs = int(input())
answers_dfs = []

for i in range(test_dfs):
    m, n, k = map(int, input().split())
    rec = [[0] * m for _ in range(n)]
    veg = []
    count = 0

    for i in range(k):
        veg.append(list(map(int, input().split())))

    for x in veg:
        rec[x[1]][x[0]] = 1

    for i in range(n):
        for j in range(m):
            if(rec[i][j] == 1):
                count += 1
                dfs(rec, i, j)

    answers_dfs.append(count)

for answer in answers_dfs:
    print(answer)

# 2.bfs


def bfs(x, y):
    que = deque()
    que.append((x, y))
    # que에 있는 원소의 갯수가 0 이면 함수는 종료
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if((0 <= nx < n) and (0 <= ny < m)):
                if(graph[nx][ny] == 1):
                    que.append((nx, ny))
                    graph[nx][ny] = 0
    return 1


test_bfs = int(input())
answers_bfs = []

for i in range(test_bfs):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if(graph[i][j] == 1):
                cnt += bfs(i, j)
    answers_bfs.append(cnt)

for answer in answers_bfs:
    print(answer)
