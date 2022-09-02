import sys
input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
nums = []


def dfs(x):
    global cnt
    sum = 0
    if len(nums):
        for num in nums:
            sum += num
        if sum == s:
            cnt += 1

    for i in range(x, n):

        if lst[i] not in nums:
            nums.append(lst[i])
            dfs(i + 1)
            nums.pop()
        # 같은 값의 숫자가 이미 배열에 있더라도, 인덱스 값이 다르면 계속해서 탐색을 진행할 수 있도록 해준다.
        else:
            if nums.index(lst[i]) != i:
                nums.append(lst[i])
                dfs(i + 1)
                nums.pop()


dfs(0)
print(cnt)
