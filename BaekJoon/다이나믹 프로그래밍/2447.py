import sys

input = sys.stdin.readline


def sol(N: int) -> None:
    if N == 3:  # 제일 작은 사각형을 먼저 구하고 시작한다.
        stars[0][:3] = stars[2][:3] = ["*"] * 3
        stars[1] = ["*", " ", "*"]
        return

    devied_number = N // 3

    sol(devied_number)

    for row in range(0, N, devied_number):
        for col in range(0, N, devied_number):
            if not (row == devied_number and col == devied_number):
                for idx in range(devied_number):
                    stars[row + idx][col : col + devied_number] = stars[idx][
                        :devied_number
                    ]


if __name__ == "__main__":
    N = int(input())
    stars = [[" " for _ in range(N)] for _ in range(N)]  # ! 문자열 곱셉은 문자열이 합쳐짐.. 주의해야함

    sol(N)

    for i in range(N):
        for j in range(N):
            print(stars[i][j], end="")
        print()
