import sys
input = sys.stdin.readline

test_cnt = int(input())
ans = []


def dfs(index):
    visited[index] = True
    if not visited[lst[index]]:
        dfs(lst[index])


for _ in range(test_cnt):
    n = int(input())
    nums = list(map(int, input().split()))

    lst = [0] * (n + 1)
    visited = [False] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        lst[i] = nums[i - 1]

    for i in range(1, n + 1):
        if not visited[i]:
            cnt += 1
            dfs(i)

    ans.append(cnt)

for num in ans:
    print(num)
