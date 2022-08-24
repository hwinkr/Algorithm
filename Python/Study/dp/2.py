# from collections import deque
# import sys

# # 한번 연산을 마친후 얻을수 있는 최적의값

# # 1. 완전탐색


# def bfs():
#     input = sys.stdin.readline
#     x = int(input())
#     dist = [0] * (x + 1)

#     que = deque()
#     que.append(x)
#     while que:
#         num = que.popleft()
#         if num == 1:
#             print(dist[num])
#             break
#         if not dist[num - 1]:
#             que.append(num - 1)
#             dist[num - 1] = dist[num] + 1
#         if num % 5 == 0 and not dist[num // 5]:
#             que.append(num // 5)
#             dist[num // 5] = dist[num] + 1
#         if num % 3 == 0 and not dist[num // 3]:
#             que.append(num // 3)
#             dist[num // 3] = dist[num] + 1
#         if num % 2 == 0 and not dist[num // 2]:
#             que.append(num // 2)
#             dist[num // 2] = dist[num] + 1


# if __name__ == "__main__":
#     bfs()

# 2. dp

import sys
input = sys.stdin.readline

x = int(input())
d = [0] * 1000001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)


print(d[x])
