import sys

input = sys.stdin.readline


def solution(n: int, ability_list: list) -> int:
    answer = 0
    start, end = 0, n - 1

    while start + 1 < end:  # s, e 사이에 최소 1명의 개발자가 있어야 한다.
        answer = max(
            answer, (end - start - 1) * min(ability_list[start], ability_list[end])
        )

        if ability_list[start] < ability_list[end]:
            start += 1
        else:
            end -= 1

    return answer


if __name__ == "__main__":
    n = int(input())
    ability_list = list(map(int, input().split()))
    print(solution(n, ability_list))
