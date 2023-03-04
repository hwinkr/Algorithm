# ! 보트는 최대 2명의 사람만 태울 수 있다


from collections import deque


def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    answer = 0

    while people:
        if len(people) == 1:
            answer += 1
            break

        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.popleft()

    return answer
