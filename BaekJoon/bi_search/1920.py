# 수 찾기

import sys
input = sys.stdin.readline

# 한번 비교할때마다 비교 횟수가 절반이 되므로 시간복잡도가 O(log n) !

# search_lst 에 있는 각 원소들이 탐색해야하는 target


def bi_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return 1
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
search_lst = list(map(int, input().split()))

for num in search_lst:
    result = bi_search(0, n - 1, num)
    print(result)
