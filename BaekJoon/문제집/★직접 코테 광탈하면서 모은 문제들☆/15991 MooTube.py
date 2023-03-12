from collections import deque
import sys

input = sys.stdin.readline

# * 시작 노드부터 목표 노드 까지의 경로중 가장 적은 가중치의 간선 값을 저장해놓아야함.
# * 조건을 만족 하면, que 에 넣고 방문 처리 하고 탐색을 계속한다.
# * 조건을 만족하지 못한다는 것은 모든 경로의 가중치 중에서의 최솟값이 usado 보다 작다는 것이기 때문에 다음 노드를 탐색 할 필요가 없다


def solution(usado: int, start: int) -> int:
    answer = 0
    visited = [False] * (n + 1)
    visited[start] = True
    que = deque([(start, MAX)])

    while que:
        curr_node, curr_usado = que.popleft()

        for next_node, next_usado in graph[curr_node]:
            tmp = min(curr_usado, next_usado)

            if tmp >= usado and not visited[next_node]:
                answer += 1
                visited[next_node] = True
                que.append((next_node, tmp))

    return answer


if __name__ == "__main__":
    # 유사도 리스르를 만들면 되는거 아님?
    n, question = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    MAX = 10**9 + 1

    for _ in range(n - 1):
        a, b, weight = map(int, input().split())
        graph[a].append((b, weight))
        graph[b].append((a, weight))

    # 자신을 제외한 나머지 동영상과 동영상 쌍을 이룸.
    # 만약 1이면
    # (1, 2) (1, 3), (1, 4) => 1에서 2 까지 가는 모든 경로중 간선의 최솟값
    for _ in range(question):
        usado, start = map(int, input().split())
        print(solution(usado, start))
