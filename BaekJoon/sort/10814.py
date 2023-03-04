# 회원들 나이순 정렬하기

import sys
input = sys.stdin.readline

n = int(input())
users = []
for i in range(n):
    age, name = map(str, input().split())
    users.append([int(age), name])
users.sort(key=lambda x: x[0])

for user in users:
    print(user[0], user[1])
