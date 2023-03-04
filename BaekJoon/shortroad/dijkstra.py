# 방문여부 체크 배열 생성
# 최단경로를 저장하는 배열 생성
import sys
input = sys.stdin.readline
INF = int(1e9)

# 정점, 간선의 갯수
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

dist = [INF] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    # a에서 b로 가는 비용이 c임을 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


# 그리디 + 완탐

def smallest_node():
    max_value = INF
    idx = 0
    for i in range(1, n + 1):
        if dist[i] < max_value and not visited[i]:
            max_value = dist[i]
            idx = i
    return idx


def dijkstra(start):
    visited[start] = True
    dist[start] = 0

    for j in graph[start]:
        dist[j[0]] = j[1]

    # 모든 노드를 방문하면서, start 노드에서 앞으로 방문할 모든 노드에 대한 최단거리 테이블 초기화 작업 진행
    for _ in range(n - 1):
        now = smallest_node()
        graph[now] = True

        for j in graph[now]:
            cost = dist[now] + j[1]
            if cost < dist[j[0]]:
                dist[j[0]] = cost


for i in range(1, n + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
