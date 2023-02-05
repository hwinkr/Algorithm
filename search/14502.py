import copy

# * 가로, 세로 크기가 그렇게 크지가 않다..? 완탐이 예상된다
# * 벽을 3개 다 사용한다면, 그 때 안전영억의 갯수를 카운팅 하는 함수를 호출해서 이전 값과 비교해서 update

from collections import deque
import sys

input = sys.stdin.readline


def count_area(tmp: list) -> int:
    cnt = 0
    for i in range(row):
        for j in range(col):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


def solution(tmp: list, virus: list) -> int:
    que = deque(virus)

    while que:
        x, y = que.popleft()

        for (dx, dy) in DIRECTION:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < col and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                que.append([nx, ny])

    area = count_area(tmp)
    return area


if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(row)]
    DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    result = 0
    zero = []
    virus = []

    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0:
                zero.append([i, j])
            elif graph[i][j] == 2:
                virus.append([i, j])

    for i in range(len(zero) - 2):
        for j in range(i + 1, len(zero) - 1):
            for k in range(j + 1, len(zero)):
                tmp = copy.deepcopy(graph)
                tmp[zero[i][0]][zero[i][1]] = tmp[zero[j][0]][zero[j][1]] = tmp[
                    zero[k][0]
                ][zero[k][1]] = 1

                result = max(result, solution(tmp, virus))

    print(result)
