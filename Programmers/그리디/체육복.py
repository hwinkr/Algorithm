import sys

input = sys.stdin.readline

# * 도난당한 학생 리스트, 여벌의 체육복이 있는 학생들의 리스트
# ! 여벌의 체육복이 있는 학생이여도, 도난을 당했다면 빌려줄 수 없음


def solution(n, lost, reserve):
    answer = 0
    uniforms = [1] * (n + 1)

    for number in range(1, n + 1):
        if number in lost:
            uniforms[number] -= 1
        if number in reserve:
            uniforms[number] += 1

    for number in range(1, n + 1):
        if uniforms[number] >= 1:
            answer += 1
        else:
            for x in (number - 1, number + 1):
                if 1 <= x <= n and uniforms[x] > 1:
                    uniforms[number] += 1
                    uniforms[x] -= 1
                    answer += 1
                    break
    return answer


def solution(n, lost, reserve):
    # ! 중복 제거
    _reserve_students = [r for r in reserve if r not in lost]
    _lost_students = [l for l in lost if l not in reserve]

    for student in _reserve_students:
        i = student - 1
        j = student + 1

        if i in _lost_students:
            _lost_students.remove(i)
        elif j in _lost_students:
            _lost_students.remove(j)

    return n - len(_lost_students)


print(solution(5, [2, 4], [1, 3, 5]))
