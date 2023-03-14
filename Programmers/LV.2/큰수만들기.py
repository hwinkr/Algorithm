import sys

input = sys.stdin.readline

# 문자열 형식으로 숫자 number, 제거할 수의 갯수 k
# 2 <= number <= 1000000
# 1 <= k < number

# ! 숫자를 문자열 형태로 return


def solution(number, k):
    stack = []
    del_count = k
    for num in number:
        while stack and del_count > 0 and stack[-1] < num:
            stack.pop()
            del_count -= 1
        stack.append(num)
    return "".join(stack[: len(number) - k])
