# # 내가 이 문제를 오래 붙잡고 있었던 이유는 처음에 로직을 잘못 짜서 그 로직에 갇혀 있기 때문이기도 했지만 문제에서 제시한 메모리가 엄청 작다는 사실을 뒤늦게 발견하고 0을 이동시키면서 만들수 있는 숫자의 조합이 중복 될수 있다는걸 놓쳤기 때문이다. 2차원 배열을 중복해서 만들지 않게 하는 방법은..? -> 2차원 배열 -> 문자열 -> 문자열을 dict or set 에 저장하면 중복되지 않게 저장 가능.
# # 그렇다면 2차원 배열을 굳이 문자열로 변경하지 않고 바로 자료구조에 저장 하면 되지않을까 라는 생각을 했지만 2차원 배열을 저장하는것이 불가능 하더라.. 그래서 문자열로 변경해야한다
# # 2차원배열 -> 문자열 , 문자열 -> 2차원 배열이 자유자재로 변경 가능하다는것을 인지해놓자
from collections import deque

import sys
input = sys.stdin.readline


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    str = ''
    for _ in range(3):
        str += ''.join(list(input().split()))

    visited = set()
    visited.add(str)

    que = deque()
    que.append((str, 0))

    while que:
        curr_str, cnt = que.popleft()
        if curr_str == "123456780":
            return cnt

        # 0의 위치 구하기
        idx = curr_str.index('0')
        x, y = idx // 3, idx % 3

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 3 and 0 <= ny < 3:
                lst = list(curr_str)
                lst_idx = nx * 3 + ny
                lst[idx], lst[lst_idx] = lst[lst_idx], lst[idx]

                lst_str = ''.join(lst)

                if lst_str not in visited:
                    visited.add(lst_str)
                    que.append((lst_str, cnt + 1))
    # 0을 이동시키면서 만들수 있는 문자열을 다 만들고 나면 que가 비워진다 그때도 목표 문자열을 만들지 못하면 -1 을 반환한다
    return -1


if __name__ == "__main__":
    print(bfs())


# # check
# # 2차원 배열 -> 하나의 문자열 , 문자열 더하기 = 문자열 붙이기

# # graph = [list(input().split()) for _ in range(3)]
# # print(graph)
# # str = ''
# # for i in range(3):
# #     for j in range(3):
# #         str += graph[i][j]
# # print(str)

# # 문자열 -> 2차원 배열 queue 사용

# # lst = "123456789"
# # que = deque()
# # for i in range(len(lst)):
# #     que.append(lst[i])

# # graph = []
# # for _ in range(3):
# #     graph.append([])

# # idx = 0
# # for i in range(len(que)):
# #     if i > 1 and i % 3 == 0:
# #         idx += 1
# #     x = que.popleft()
# #     graph[idx].append(x)

# # print(graph)
