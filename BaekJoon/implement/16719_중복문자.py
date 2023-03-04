import sys

input = sys.stdin.readline


def sol(arr: list, sliced_arr: list, tmp: list, start: int) -> None:
    if not sliced_arr:
        return

    tmp[arr.index(min(sliced_arr))] = min(sliced_arr)  # 이 줄이 문제다
    print("".join(tmp))

    sol(
        arr,
        arr[arr.index(min(sliced_arr)) + 1 :],
        tmp,
        arr.index(min(sliced_arr)) + 1,
    )
    sol(arr, arr[start : arr.index(min(sliced_arr))], tmp, start)


if __name__ == "__main__":
    arr = list(input().rstrip())
    print(arr)
    tmp = [""] * len(arr)
    sol(arr, arr, tmp, 0)
