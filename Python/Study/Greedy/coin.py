# greedy algorithm : 현재 처한 상황에서 당장 가장 좋은 것을 선택 , 이 선택을 반복적으로 진행해도 최적의 해를 구할 수 있는가?
# 일반적인 상황에서 그리디 알고리즘 자체로는 최적의 해를 보장 받을 수 없다
# 최적의 해를 무조건 보장 받을 수 있는 경우 , 그리디 알고리즘을 사용

# 거슬러 줄수 있는 가장 큰 단위의 동전이 , 항상 작은 단위들의 배수인 경우,
N = int(input())
change = [500, 100, 50, 10]
changeCnt = 0

# for i in range(0, len(change)):
#     while(N >= change[i]):
#         N -= change[i]
#         changeCnt += 1

for coin in change:
    changeCnt += N // coin
    N %= coin

print(changeCnt)

# 작은 단위들의 배수가 아닌 경우
M = int(input())
coin = [500, 400, 100]
coinCnt = 0
for i in range(0, len(coin)):
    while(M >= coin[i]):
        M -= coin[i]
        coinCnt += 1

print(coinCnt)
