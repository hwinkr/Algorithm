# 촌수 세기
from collections import deque
import sys

input = sys.stdin.readline


# 목표노드의 dist 값이 0이면 -1 , 아무런 관계가 없다는 뜻
def bfs():
    n = int(input())
    start, target = map(int, input().split())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    dist = [0 for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    que = deque()
    que.append(start)

    while que:
        for _ in range(len(que)):
            x = que.popleft()
            visited[x] = True
            for i in graph[x]:
                if not visited[i]:
                    dist[i] = dist[x] + 1
                    que.append(i)

    if(dist[target] == 0):
        print(-1)
    else:
        print(dist[target])


if __name__ == '__main__':
    bfs()
