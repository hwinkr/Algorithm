def solution(numbers, target):
    answer = 0
    tmp_numbers = [0]

    for num in numbers:
        tmp = []
        for tmp_number in tmp_numbers:
            tmp.append(tmp_number + num)
            tmp.append(tmp_number - num)
        tmp_numbers = tmp

    for num in tmp_numbers:
        if num == target:
            answer += 1

    return answer


print(solution([4, 1, 2, 1], 4))
