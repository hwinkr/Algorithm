import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

distance_start = [INF] * (n + 1)
distance_v1 = [INF] * (n + 1)
distance_v2 = [INF] * (n + 1)


def dijkstra(start, distance):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1, distance_start)
dijkstra(v1, distance_v1)
dijkstra(v2, distance_v2)

ans = min(distance_start[v1] + distance_v1[v2] + distance_v2[n],
          distance_start[v2] + distance_v2[v1] + distance_v1[n])

print(ans if ans < INF else -1)
