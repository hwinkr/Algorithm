# 동전 갯수 최소값 찾기

n, k = map(int, input().split())

coins = []

answer = 0

for i in range(0, n):
    coins.append(int(input()))

coins.reverse()

for coin in coins:
    answer += (k // coin)
    k %= coin

print(answer)
