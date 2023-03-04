from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    que = deque()
    que.append(n)
    visited[n] = True

    while que:
        x = que.popleft()

        if x == k:
            print(times[k])
        for nx in (x - 1, x + 1, x * 2):
            if (0 <= nx <= max) and not visited[nx]:
                if nx == x * 2:
                    visited[nx] = True
                    times[nx] = times[x]
                    que.appendleft(nx)
                    continue

                times[nx] = times[x] + 1
                que.append(nx)
                visited[nx] = True


# 한번 방문할때, 그 위치 까지 이동해야 하는데 걸리는 시간이 최소가 되야 한다. 그리고 다시 방문하지 않는다 -> 그리디 개념
# 순간이동을 하는 경우의, 처리가 굉장히 중요하다 어떻게 할까?
# 순간이동으로 도착한 좌표를 먼저 방문 처리를 해줘야한다, 그 이유는 순간이동이 아닌 이동에 의해서 재방문하면 시간이 증가하기 때문


if __name__ == "__main__":
    n, k = map(int, input().split())
    max = 10**5
    times = [0] * (max + 1)
    visited = [False] * (max + 1)

    bfs()
