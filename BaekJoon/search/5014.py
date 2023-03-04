import sys
from collections import deque

input = sys.stdin.readline


def bfs(x):
    que = deque()
    que.append(x)

    while que:
        x = que.popleft()
        if x == target_height:
            return button_cnt[target_height]

        for nx in (x + up, x - down):
            if 1 <= nx <= total_height and not button_cnt[nx] and nx != start_height:
                button_cnt[nx] = button_cnt[x] + 1
                que.append(nx)

    return "use the stairs"


if __name__ == "__main__":
    total_height, start_height, target_height, up, down = map(int, input().split())
    button_cnt = [0] * (total_height + 1)
    print(bfs(start_height))
