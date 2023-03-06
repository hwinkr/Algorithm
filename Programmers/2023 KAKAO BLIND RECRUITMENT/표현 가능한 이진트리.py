def condition(tmp: str, node: str) -> bool:
    # * 말단 노드 까지 확인 한 경우, return True
    if len(tmp) == 1:
        return True

    if node == "0":
        for child in tmp:
            if child != "0":
                return False

    mid = len(tmp) // 2

    return condition(tmp[:mid], tmp[(mid - 1) // 2]) and condition(
        tmp[mid + 1 :], tmp[(len(tmp) + mid) // 2]
    )


def make_binary_number(number: int) -> str:
    reversed_number = []

    while number > 0:
        reversed_number.append(str(number % 2))
        number //= 2

    binary_number = "".join((reversed_number[::-1]))

    length = 0
    for i in range(1, 13):
        if 2**i - 1 >= len(binary_number):
            length = 2**i - 1
            break

    # * 포화 이진트리 형태로 표현 가능한 문자열을 return
    return "0" * (length - len(binary_number)) + binary_number


def solution(numbers: list) -> list:
    answer = []

    for number in numbers:
        binary_number = make_binary_number(number)
        answer.append(
            1 if condition(binary_number, binary_number[len(binary_number) // 2]) else 0
        )

    return answer


# TODO : 문제 조건에 맞는 이진트리는..?
# 1. 입력으로 주어지는 숫자를 이진수로 된 문자열로 변경한다
# ! 문자열에 속해 있는 하나의 숫자가 하나의 노드라고 생각을 해야 한다.
# ! 만약 부모노드가 0이라면 그 아래에 있는 모든 자식 노드 또한 0 이여야 한다 -> 모두 더미 노드이기 때문이다
# ! 모든 노드를 탐색 할 때 까지 조건을 만족하면 1을, 아니면 0을 append 후 return
# 2. 입력으로 주어지는 숫자가 포화 이진트리가 되도록 해야한다.

# * 포화 이진트리 : 마지막 depth 까지 모든 노드가 있는 이진 트리
