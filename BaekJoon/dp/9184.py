# 신나는 함수 실행 ,, 전혀 신나지 않음

import sys
input = sys.stdin.readline

# 3차원 배열
temp = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    # a b c 중 하나라도 값이 20 보다 크면 w(20, 20, 20)을 반환한다. 이후 w(20, 20, 20)을 다시 실행할 일은 없다.
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if temp[a][b][c]:
        return temp[a][b][c]

    if a < b < c:
        temp[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return temp[a][b][c]

    temp[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + \
        w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return temp[a][b][c]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break

    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
