import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)


def sol(curr: int, idx: int) -> None:
    global max_num, min_num, add, minus, multi, devide
    if idx == n:
        min_num = min(min_num, curr)
        max_num = max(max_num, curr)
        return

    if add > 0:
        add -= 1
        sol(curr + numbers[idx], idx + 1)
        add += 1
    if minus > 0:
        minus -= 1
        sol(curr - numbers[idx], idx + 1)
        minus += 1
    if multi > 0:
        multi -= 1
        sol(curr * numbers[idx], idx + 1)
        multi += 1
    if devide > 0:
        devide -= 1
        sol(int(curr / numbers[idx]), idx + 1)
        devide += 1


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    add, minus, multi, devide = map(int, input().split())

    min_num, max_num = 10**10, -(10**10)

    sol(numbers[0], 1)

    print(max_num)
    print(min_num)
