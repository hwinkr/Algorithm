import sys

input = sys.stdin.readline


def solution(students: list, group: int) -> int:
    tmp = []
    for i in range(1, len(students)):
        tmp.append(students[i] - students[i - 1])

    tmp.sort(reverse=True)
    return sum(tmp[group - 1 :])


# 혼자 조를 짜면 비용이 발생 하지 않는다, 가장 비용이 많이 들게 하는 사람을 조에 포함 시키지 않고 혼자 구성되게 한다.
if __name__ == "__main__":
    n, group = map(int, input().split())
    students = list(map(int, input().split()))

    print(solution(students, group))
