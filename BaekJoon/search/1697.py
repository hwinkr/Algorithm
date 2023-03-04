# # 걷기 : 현재위치 -1 or +1
# # 순간이동 : 현재위치 * 2
# # bfs 로 풀었다

# 이미 방문한 노드는 재방문 할 수 없다
# 문제의 범위를 초과하는 값을 방문해야 하는 경우 그렇지 못하게 한다 -> 초과하면 원래 자리를 넣는다

from collections import deque
# n, k = map(int, input().split())
# visited = [False] * 100001

# # 내 풀이


# def bfs_my(n, k):
#     if(n >= k):
#         return n - k

#     que = deque()
#     que.append(n)

#     count = 0

#     while True:
#         lst = []
#         while que:
#             i = que.popleft()
#             lst.append(i)
#         count += 1
#         for num in lst:
#             visited[num] = True
#             if(num == k):
#                 return count - 1
#             if(num - 1 > 0 and not visited[num - 1]):
#                 que.append(num - 1)
#             if(num + 1 <= 100000 and not visited[num + 1]):
#                 que.append(num + 1)
#             if(num * 2 <= 100000 and not visited[num * 2]):
#                 que.append(num * 2)


# print(bfs_my(n, k))

# 좋은 풀이


def bfs():
    que = deque()
    que.append(n)

    while que:
        x = que.popleft()
        if x == k:
            print(dist[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                # 다음 노드에 현재 확인하고 있는 노드값에 1을 더해준다
                # dist 노드에는 이동 횟수가 저장되는 것
                dist[nx] = dist[x] + 1
                que.append(nx)


MAX = 10 ** 5
dist = [0] * (MAX + 1)
n, k = map(int, input().split())


bfs()
