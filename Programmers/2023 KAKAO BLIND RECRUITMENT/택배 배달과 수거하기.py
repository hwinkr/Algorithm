def remove_zero(deliveries: list, pickups: list) -> None:
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()
    while pickups and pickups[-1] == 0:
        pickups.pop()


def solution(cap: int, n: int, deliveries: list, pickups: list) -> int:
    answer = 0
    remove_zero(deliveries, pickups)

    while deliveries or pickups:
        answer += max(len(deliveries), len(pickups)) * 2

        if deliveries:
            if deliveries[-1] > cap:
                deliveries[-1] -= cap
            else:
                tmp = 0
                while deliveries and tmp + deliveries[-1] <= cap:
                    tmp += deliveries.pop()
                if deliveries:
                    deliveries[-1] -= cap - tmp

        if pickups:
            if pickups[-1] > cap:
                pickups[-1] -= cap
            else:
                tmp = 0
                while pickups and tmp + pickups[-1] <= cap:
                    tmp += pickups.pop()
                if pickups:
                    pickups[-1] -= cap - tmp

    return answer
