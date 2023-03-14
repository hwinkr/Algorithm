def dfs(idx, limit, numbers, number, target):
    if idx == limit and number == target:
        return 1
    if idx == limit:
        return 0

    return dfs(idx + 1, limit, numbers, number + numbers[idx], target) + dfs(
        idx + 1, limit, numbers, number - numbers[idx], target
    )


def solution(numbers, target):
    answer = dfs(
        0,
        len(numbers),
        numbers,
        0,
        target,
    )

    return answer


print(solution([4, 1, 2, 1], 4))
