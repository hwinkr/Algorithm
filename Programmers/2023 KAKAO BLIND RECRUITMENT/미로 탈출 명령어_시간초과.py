from collections import deque


possible_path = "z" * 2500
DIRECTION = [(1, 0), (0, -1), (0, 1), (-1, 0)]
DIRECTION_str = ["u", "r", "d", "l"]  # ! 문자열 빠른 순 : d, l, r, u


def bfs(que: deque, size: list, destination: list, k: int) -> None:
    global possible_path
    row, col = size
    r, c = destination
    while que:
        x, y, tmp = que.popleft()
        if len(tmp) == k:
            if x == r and y == c:
                possible_path = min(possible_path, tmp)
            continue

        for i in range(4):
            dx, dy = DIRECTION[i]
            nx = x + dx
            ny = y + dy

            if 1 <= nx <= row and 1 <= ny <= col:
                que.append((nx, ny, tmp + DIRECTION_str[i]))


def solution(n, m, x, y, r, c, k):
    que = deque([(x, y, "")])
    size = [n, m]
    destination = [r, c]
    bfs(que, size, destination, k)
    return possible_path if possible_path else "impossible"


print(solution(3, 3, 1, 2, 3, 3, 4))

# * (x, y) -> (r, c) 로 이동해야 하는데, 이동하는 거리가 총 k 여야 한다.
# ! (x, y), (r, c) 를 포함해서 같은 좌표를 2번이상 방문해도 된다, visited 배열의 사용 유무?
# TODO : 미로에서 탈출하는데 사용한 경로를 문자열로 나타냈을 때, 문자열이 사전순으로 가장 빠른순이여야 한다.
