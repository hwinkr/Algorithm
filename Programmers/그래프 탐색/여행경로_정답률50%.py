# 주어진 항공 티켓을 모두 사용
# 항상 ICN 에서 출발
# 경로가 2개 이상 나온다면 알파벳 순서가 앞서는 경로를 return

# 주어진 항공권을 모두 사용하는지 check
# 방문한 도시를 처리

# 주어진 항공권을 모두 사용해서 여행 경로를 짜야 하고, 여행 경로중 알파벳 순서가 짧은 경로를 return
# ! 방문한 도시를 다시 방문할 수 있다,
# ! 방문한 도시를 visited 처리 하는게 아닌 사용한 티켓을 used 처리

# ! 사전식 순으로 정렬하고 이동 했을 경우, 길이 막혀서 다른길로 이동해야 하는 경우도 고려 해야 함.

# ! 중복 티켓을 고려해야 한다, a -> b 로 이동하는 티켓이 2개 주어진 경우에도 문제 조건에서 모든 티켓을 사용 해야 한다고 했기 때문에 2개를 모두 사용해야 함.


# def dfs(data, city, count_ticket, limit_ticket, total_path):
#     total_path.append(city)
#     if count_ticket >= limit_ticket:
#         return total_path

#     for next_city in data[city]:
#         data[city].remove(next_city)
#         return dfs(data, next_city, count_ticket + 1, limit_ticket, total_path)


# def solution(tickets):
#     path = dict()
#     for ticket in tickets:
#         a, b = ticket[0], ticket[1]
#         if a not in path:
#             path[a] = [b]
#         else:
#             path[a].append(b)

#         if b not in path:
#             path[b] = []

#     for key in path:
#         path[key].sort()

#     tmp = []
#     return dfs(path, "ICN", 0, len(tickets), tmp)

global answer
answer = []


def dfs(routes: dict, path: list, tickets: list):
    global answer
    src = path[-1]
    if len(tickets) == 0:
        answer.append(path)

    if src not in routes:
        return None

    for dst in routes[src]:
        if [src, dst] not in tickets:
            continue

        tickets.remove([src, dst])
        dfs(routes, path + [dst], tickets)
        tickets.append([src, dst])


def solution(tickets):
    global answer
    answer = []
    routes = dict()
    for ticket in tickets:
        src, dst = ticket
        if src in routes:
            routes[src].append(dst)
        else:
            routes[src] = [dst]

    for src in routes:
        routes[src].sort()

    dfs(dict(routes), list(["ICN"]), list(tickets))
    answer.sort()
    return answer[0]


print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
