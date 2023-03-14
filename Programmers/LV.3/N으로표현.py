# if answer > 8, return -1
# * n - 1 개를 사용해서 만든 숫자를 저장해두는 자료구조가 필요
def solution(N, number):
    # N = taget number
    # number = using number for makes target number
    made_numbers = []

    for cnt in range(1, 9):
        tmp_numbers = set()
        # using cnt
        tmp_numbers.add(int(str(N) * cnt))
        for i in range(cnt - 1):
            for num1 in made_numbers[i]:
                for num2 in made_numbers[-i - 1]:
                    tmp_numbers.add(num1 + num2)
                    tmp_numbers.add(num1 - num2)
                    tmp_numbers.add(num1 * num2)
                    if num2 != 0:
                        tmp_numbers.add(num1 / num2)

        if number in tmp_numbers:
            return cnt

        made_numbers.append(tmp_numbers)

    return -1


print(solution(5, 12))
