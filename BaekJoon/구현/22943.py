import sys
import math

input = sys.stdin.readline


def makePrime(prime_list: list) -> None:
    prime_list[0] = False
    prime_list[1] = False
    prime_list[2] = True

    for i in range(3, MAX + 1):
        isPrime = True
        # ! 소수는 1과 자신을 제외한 나머지 숫자로 나누어떨어지는지에 대해서 판단해주면 된다.
        # ! 연산 횟수를 줄이기 위해서 제곱근 까지만 판단해준다.
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            prime_list[i] = True


def condition_1(num: int) -> bool:  # * 서로 다른 두 소수를 더해서 num 을 만들 수 있는지 판단
    for i in range(2, num // 2 + 1):
        if i != num - i and prime_list[i] and prime_list[num - i]:
            return True

    return False


def condition_2(num: int) -> bool:  # * 두 소수를 곱해서 num 을 만들 수 있는지 판단
    while num % m == 0:
        num //= m
    # ! 소수를 구하는 과정과 마찬가지로, 제곱근 까지만 판단해준다.
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and prime_list[i] and prime_list[num // i]:
            return True

    return False


def solution(tmp: list) -> int:
    global answer
    if len(tmp) == k:
        tmp = int("".join(map(str, tmp)))
        if condition_1(tmp) and condition_2(tmp):
            answer += 1
        return

    for i in range(10):
        if i == 0 and len(tmp) == 0:
            continue
        if not visited[i]:
            tmp.append(i)
            visited[i] = True
            solution(tmp)
            tmp.pop()
            visited[i] = False


if __name__ == "__main__":
    k, m = map(int, input().split())

    MAX = 98765  # ! 만들 수 있는 최댓값
    prime_list = [False] * (MAX + 1)
    visited = [False] * 10
    tmp = []
    answer = 0

    makePrime(prime_list)
    solution(tmp)
    print(answer)
