# 로봇 , n번의 행동

# 상 하 좌 우 방향중 하나를 임의로 선택 임의...? rand
# 로봇이 방문했던 자리를 다시 방문하지 않는 경우 경로가 단순하다

# 로봇의 이동경로가 단순할 확률 -> 단순한 경우 / n
# 로봇이 시작한 위치 : 처음 방문한 위치

# 확률이 0만 아니면 이동할 확률은 모두 같음
# E   W   S   N
# 25  25  25  25
# 0  33  33  33
# 0   0  50  50


# 방문한 곳을 모두 방문하고 경로 이동이 끝났을때 경로상에 같은 좌표가 있으면 단순하지 않다
# 1번 방문한 곳을 재방문 하지 않는다 -> 방문 좌표 리스트에 중복되는 값이 없다 -> cnt += 1

import sys
input = sys.stdin.readline

input_lst = list(map(int, input().split()))
n = input_lst[0]
dir_lst = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# 이동할 수 있는 방향값
move_lst = []
# 이동할 수 있는 방향에 대한 확률값
per = []

for i in range(1, len(input_lst)):
    if input_lst[i] != 0:
        move_lst.append(dir_lst[i - 1])
        per.append(input_lst[i] / 100)

visited = [(14, 14)]
ans = 0


def dfs(x, y, total):
    global ans
    if len(visited) == n + 1:
        ans += total
        return

    # 이동할 수 있는 좌표에 대해서만 탐색을 진행함
    for i in range(len(move_lst)):
        nx = x + move_lst[i][0]
        ny = y + move_lst[i][1]
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny, total * per[i])
            visited.pop()


dfs(14, 14, 1)
print(ans)
