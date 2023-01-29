# * 서브 문자열을 자른 시작 위치를 저장하고 있어야 한다.
# * 제일 첫 문자열은 서브문자열의 시작 위치가 0 이다 => 처음부터 끝까지를 의미함
def sol(arr: list, idx: int, result: list):
    if not arr:
        return

    result[idx + arr.index(min(arr))] = min(arr)
    print("".join(result))

    sol(arr[arr.index(min(arr)) + 1 :], idx + arr.index(min(arr)) + 1, result)
    sol(arr[: arr.index(min(arr))], idx, result)


if __name__ == "__main__":
    arr = list(input().rstrip())
    result = [""] * len(arr)
    sol(arr, 0, result)
