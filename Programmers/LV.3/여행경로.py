# check
# * a -> b 로 이동하는 중복된 티켓이 있어도 모든 티켓을 사용해서 경로를 만들 수 있어야 한다.
# * 다음 목적지로 이동했을때, 그 목적지에서 다른 경로로 이동할 수 없는 경우에 대해서도 생각 해야 한다
# * 모든 조건을 만족하는 모든 path 를 생성하고 알파벳 순으로 가장 짧은 경로를 출력한다
from collections import deque


def solution(tickets):
    answer = []
    tickets_cnt = len(tickets)
    trip = dict()

    for ticket in tickets:
        src, dst = ticket
        if src in trip:
            trip[src].append(dst)
        else:
            trip[src] = [dst]

    tmp_tickets = list(tickets)
    que = deque([(["ICN"], 0, tmp_tickets)])

    while que:
        path, cnt, list_tickets = que.popleft()
        src = path[-1]
        if cnt == tickets_cnt:
            answer.append(path)

        if src not in trip:
            continue

        for dst in trip[src]:
            if [src, dst] not in list_tickets:
                continue

            list_tickets.remove([src, dst])
            que.append((path + [dst], cnt + 1, list(list_tickets)))
            list_tickets.append([src, dst])

    answer.sort()
    return answer[0]


print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
