# 인접한 두 집을 털면 안됨
# 돈이 담긴 배열 => 도둑이 훔칠 수 있는 돈의 최댓값
# * 도둑이 훔칠 수 있는 집의 수를 구하자
# ! 첫번째 집을 포함 시키면, 마지막 집을 빼야하고 / 마지막 집을 포함 시키면 첫번째 집을 빼야 함.
# * 계산을 편하게 하기 위해서 앞에 0 추가!


def solution(money):
    money_start = [0] + [num for num in money[:-1]]
    money_end = [0] + [num for num in money[1:]]

    for i in range(2, len(money)):
        money_start[i] = max(money_start[i] + money_start[i - 2], money_start[i - 1])
        money_end[i] = max(money_end[i] + money_end[i - 2], money_end[i - 1])

    return max(money_start[-1], money_end[-1])
