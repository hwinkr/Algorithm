import sys

input = sys.stdin.readline

sys.setrecursionlimit(100000)


def solution(curr: int, parent: bool) -> None:
    global answer

    for node in graph[curr]:
        if node == -1:
            continue
        answer += 1
        solution(node, True)

    if last == curr:
        print(answer)
        return

    if parent:
        answer += 1


def inorder(curr) -> None:
    if curr != -1:
        inorder(graph[curr][0])
        inorder_list.append(curr)
        inorder(graph[curr][1])


if __name__ == "__main__":
    nodes = int(input())
    graph = [[] for _ in range(nodes + 1)]

    for _ in range(nodes):
        curr, left, right = map(int, input().split())
        graph[curr].append(left)
        graph[curr].append(right)
    # * 유사 중위 순회가 아닌, 그냥 중위 순회를 했을 경우의 마지막 노드를 구한다.
    inorder_list = []
    inorder(1)
    last = inorder_list[-1]

    answer = 0

    solution(1, False)
