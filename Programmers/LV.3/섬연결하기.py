def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    edges = set([costs[0][0]])
    while len(edges) != n:
        for cost in costs:
            if cost[0] in edges and cost[1] in edges:
                continue
            if cost[0] in edges or cost[1] in edges:
                answer += cost[2]
                edges.update([cost[0], cost[1]])
                break
    return answer
