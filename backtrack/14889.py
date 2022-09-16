import sys


def make_team(start):
    if len(tmp) == n // 2:
        team.append(list(tmp))
        return

    for i in range(start, n):
        tmp.append(i)
        make_team(i + 1)
        tmp.pop()


def ability(team, sum):
    if len(team) == 2:
        sum += lst[team[0]][team[1]]
        sum += lst[team[1]][team[0]]
    else:
        for i in range(len(team) - 1):
            for j in range(i + 1, len(team)):
                sum += lst[team[i]][team[j]]
                sum += lst[team[j]][team[i]]

    return sum


n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize
tmp = []
team = []

make_team(0)

for i in range(len(team) // 2):
    ans = min(ans, abs(ability(team[i], 0) - ability(team[-1-i], 0)))

print(ans)
