# 숫자카드

# n 개의 가드중 m 이 적인 카드를 몇개 가지고 있는가

import sys
input = sys.stdin.readline


def start(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if target == card[mid]:
            if target != card[mid - 1] or mid - 1 < 0:
                return mid
            else:
                end = mid - 1
        elif target > card[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return - 1


def end(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if target == card[mid]:
            if mid + 1 > n - 1 or target != card[mid + 1]:
                return mid
            else:
                start = mid + 1
        elif target > card[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return - 1


n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
find = list(map(int, input().split()))

answers = []

for num in find:
    result = start(0, n - 1, num)
    if result == - 1:
        answers.append(0)
    else:
        answers.append(end(0, n - 1, num) - start(0, n - 1, num) + 1)

for answer in answers:
    print(answer, end=" ")
