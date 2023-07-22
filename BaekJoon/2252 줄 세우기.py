import sys

input = sys.stdin.readline


def dfs(graph: list, node: int, visited: list, answer: list) -> None:
    visited[node] = True
    for next in graph[node]:
        if not visited[next]:
            dfs(graph, next, visited, answer)
    answer.append(node)


def solution(n: int, graph: list, visited: list) -> list:
    answer = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(graph, i, visited, answer)

    return answer[::-1]


if __name__ == "__main__":
    vertex, edge = map(int, input().split())
    graph = [[] for _ in range(vertex + 1)]
    visited = [False] * (vertex + 1)
    for _ in range(edge):
        a, b = map(int, input().split())
        graph[a].append(b)

    print(*solution(vertex, graph, visited))
