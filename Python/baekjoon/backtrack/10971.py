# TSP

# 방문하지 않는 노드중에 최소값을 찾고 저장

# 방문할 수 있는 다음 도시들을 check
# 다음 도시로 가는데 필요한 비용이 0이 아님 -> 다음 도시로 갈수 있다.
# i 가 시작 도시가 아님 -> 모든 도시들을 방문하지 않고는 시작도시로 돌아가지 않는다

# 모든 도시를 탐색하며 비교할때, 처음 도시로 다시 돌아가야하는 순간에 w[next][start] == 0 이면 순회를 하지 못하므로 바로 return 해준다
import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
res = sys.maxsize


def dfs(start, next, value, visited):
    global res

    if len(visited) == n:
        if w[next][start] != 0:
            res = min(res, value + w[next][start])
        return

    for i in range(n):
        if w[next][i] != 0 and i not in visited and i != start:
            visited.append(i)
            dfs(start, i, value + w[next][i], visited)
            visited.pop()


for i in range(n):
    dfs(i, i, 0, [i])

print(res)
