import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def postorder(start: int, end: int) -> None:
    if start > end - 1:
        return

    idx = end
    for i in range(start + 1, end):
        if preorder_list[start] < preorder_list[i]:
            idx = i
            break

    postorder(start + 1, idx)
    postorder(idx, end)
    print(preorder_list[start])


if __name__ == "__main__":
    preorder_list = []

    while True:
        try:
            node = int(input())
            preorder_list.append(node)
        except:
            break

    postorder(0, len(preorder_list))
