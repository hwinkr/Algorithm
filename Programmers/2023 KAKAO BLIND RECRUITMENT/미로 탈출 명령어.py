def solution(n, m, x, y, r, c, k):
    answer = ""

    distance = abs(x - r) + abs(y - c)
    k -= distance
    if k < 0 or k % 2 != 0:
        return "impossible"

    directions = {
        "d": 0,
        "l": 0,
        "r": 0,
        "u": 0,
    }

    directions["u" if x > r else "d"] = abs(x - r)
    directions["l" if y > c else "r"] = abs(y - c)

    answer += "d" * directions["d"]
    additional_down = min(k // 2, n - (x + directions["d"]))
    answer += "d" * additional_down
    directions["u"] += additional_down
    k -= 2 * additional_down

    answer += "l" * directions["l"]
    additional_left = min(k // 2, y - directions["l"] - 1)
    answer += "l" * additional_left
    directions["r"] += additional_left
    k -= 2 * additional_left

    answer += "rl" * (k // 2)
    answer += "r" * directions["r"]
    answer += "u" * directions["u"]

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))

# ! 목적지 까지 가장 짧은 문자열안 'd' 를 사용해서 내려왔고, 더 내려갈 수 있는지를 판단해야함 => d 를 최대한 앞에 많이 쓸수록 문자열이 빨라지기 때문에
# * 이 시점에서 k 가 남는다는 것은 현재 (n, 1) 까지 이동을 한 상태라는 의미 따라서 더이상 짧은 문자열 'l' 을 먼저 사용할 수 없다.
