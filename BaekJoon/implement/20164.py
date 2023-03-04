import sys

input = sys.stdin.readline


def count_odd(number: str):
    cnt = 0
    for num in number:
        if int(num) % 2:
            cnt += 1
    return cnt


def sol(number: str, cnt: int, odds: list):
    if len(number) == 1:
        cnt += count_odd(number)
        odds.append(cnt)
        return
    elif len(number) == 2:
        sol(str(int(number[0]) + int(number[1])), cnt + count_odd(number), odds)

    cnt += count_odd(number)
    for i in range(1, len(number) - 1):
        for j in range(i + 1, len(number)):
            sol(str(int(number[:i]) + int(number[i:j]) + int(number[j:])), cnt, odds)


if __name__ == "__main__":
    N = input().rstrip()
    odds_list = []
    sol(N, 0, odds_list)
    print(min(odds_list), max(odds_list))
