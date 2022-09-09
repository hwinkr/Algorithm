# n X n 체스판에서 n 개의 퀸이 서로 공격할 수 없게 만드는 경우의 수.
# 백트래킹 + 완탐이다
# row 배열 -> index : 행 , value : 열

# 각 퀸은 서로 같은 행, 같은 열에 위치할수 없다
# 0행 0 ~ n -1 열까지 퀸을 놓으면서 다음 행으로 내려갈수 있는지 판단하고, 모든 행에 퀸이 채워지면 경우의수를 + 1 한다

import sys
input = sys.stdin.readline


def keep_search(x):
    for i in range(x):
        # 대각선 비교
        # 행 - 행 == 열 - 열 이면 대각선에 위치한다
        if row[x] == row[i] or x - i == abs(row[x] - row[i]):
            return 0
    return 1


def dfs(x):
    global cnt
    if x == n:
        cnt += 1
    else:
        for i in range(n):
            # row[0] = 0
            row[x] = i
            if keep_search(x):
                dfs(x + 1)


n = int(input())
row = [0] * n
cnt = 0
dfs(0)
print(cnt)
