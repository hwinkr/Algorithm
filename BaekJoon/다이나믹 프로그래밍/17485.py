import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

max = 10**5 + 1


def movable(next_c: int, curr_dir: int, next_dir: int):
    return 0 <= next_c < col and curr_dir != next_dir


def solution(loc: list, curr_dir: int) -> int:
    curr_r, curr_c = loc

    if curr_r == row:
        return 0

    if dp[curr_r][curr_c][curr_dir] != max:
        return dp[curr_r][curr_c][curr_dir]

    for next_dir, dc in enumerate(DIRECTION):
        next_r, next_c = curr_r + 1, curr_c + dc
        if movable(next_c, curr_dir, next_dir):
            dp[curr_r][curr_c][curr_dir] = min(
                dp[curr_r][curr_c][curr_dir],
                graph[curr_r][curr_c] + solution([next_r, next_c], next_dir),
            )

    return dp[curr_r][curr_c][curr_dir]


if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(row)]
    dp = [[[max] * 3 for _ in range(col)] for _ in range(row)]
    DIRECTION = [-1, 0, 1]
    result = max

    for i in range(col):
        for j in range(3):
            result = min(result, solution([0, i], j))

    print(result)
