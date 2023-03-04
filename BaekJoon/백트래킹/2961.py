import sys

input = sys.stdin.readline


def solution(cnt: int, limit: int, idx: int, tmp: list) -> None:
    global res
    if cnt == limit:
        res = min(res, abs(tmp[0] - tmp[1]))
        return

    for i in range(idx, taste_cnt):
        s, b = tmp
        s *= taste_list[i][0]
        b += taste_list[i][1]
        cnt += 1
        solution(cnt, limit, i + 1, [s, b])
        s /= taste_list[i][0]
        b -= taste_list[i][1]
        cnt -= 1


if __name__ == "__main__":
    taste_cnt = int(input())
    taste_list = []
    res = 10**9

    for _ in range(taste_cnt):
        s, b = map(int, input().split())
        taste_list.append((s, b))

    for i in range(1, taste_cnt + 1):
        solution(0, i, 0, [1, 0])

    print(res)
