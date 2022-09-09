# 바이러스
from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    n = int(input())
    lst = int(input())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    for i in range(lst):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    que = deque()
    que.append(1)
    visited[1] = True

    cnt = 0

    while que:
        x = que.popleft()

        for i in graph[x]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                que.append(i)

    print(cnt)


if __name__ == "__main__":
    bfs()
