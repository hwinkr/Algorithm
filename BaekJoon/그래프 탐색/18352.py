from collections import deque
import sys

input = sys.stdin.readline

# * 최단거리가 정확히 k 인 도시들의 번호를 출력하세요
# * 출발도시에서 출발도시로 이동하는 거리의 가중치는 0입니다
# * 출발도시에서 최단거리가 정확히 k 인 도시가 존재하지 않은 경우, -1 출력, 존재한다면 그 도시들의 번호를 순서대로 출력


def solution(connect: list, start: int) -> list:
    que = deque([(start, 0)])
    visited[start] = True
    tmp = [0] * (city + 1)

    while que:
        curr, cost = que.popleft()
        for next in connect[curr]:
            if not visited[next]:
                tmp[next] = cost + 1
                que.append((next, cost + 1))
                visited[next] = True

    answer = []
    for i in range(1, len(tmp)):
        if tmp[i] == dist:
            answer.append(i)

    return answer


if __name__ == "__main__":
    city, road, dist, start = map(int, input().split())
    connect = [[] for _ in range(city + 1)]
    visited = [False] * (city + 1)
    for _ in range(road):
        a, b = map(int, input().split())
        connect[a].append(b)

    answer = solution(connect, start)

    if not answer:
        print(-1)
    else:
        answer.sort()
        for num in answer:
            print(num)
