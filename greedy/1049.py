# 기타줄

n, m = map(int, input().split())

costs_pak = []
costs_one = []

for i in range(m):
    pak, one = map(int, input().split())
    costs_pak.append(pak)
    costs_one.append(one)

pak = min(costs_pak)
one = min(costs_one)

answer = 0

if pak > one * 6:
    answer = one * n
else:
    answer += pak * (n // 6)
    if pak > (n % 6) * one:
        answer += one * (n % 6)
    else:
        answer += pak

print(answer)
