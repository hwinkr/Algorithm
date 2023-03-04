# 1로 만들기

# 그리디가 아닌 완탐 or dp로 풀어야 하는 이유.
# 선택지가 2개가 아닌 3개이기 때문에 만약 가능하다면 그 경우를 모두 탐색해야하기 때문에.


# 1. bfs
from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    n = int(input())
    temp = [0] * (n + 1)

    que = deque()
    que.append(n)

    while que:
        num = que.popleft()
        if num == 1:
            return temp[num]
        # n - 1 은 항상 연산 가능

        if not temp[num - 1]:
            que.append(num - 1)
            temp[num - 1] = temp[num] + 1

        for x in 2, 3:
            if num % x == 0 and not temp[num // x]:
                que.append(num // x)
                temp[num // x] = temp[num] + 1


if __name__ == '__main__':
    print(bfs())

# 2. dp
