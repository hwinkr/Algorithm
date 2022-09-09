# 1이 될때까지
# N , K 가 주어지고 N이 1이 될때까지 2가지 연산을 수행
# 주어진 N에 대하여 최대한 많이 나누기 , 빼는것 보다 나누는 것이 게산횟수를 훨씬 줄일 수 있음

n, k = map(int, input().split())

count = 0

while True:
    target = (n // k) * k
    count += (n - target)

    n = target

    if(n < k):
        break

    n //= k
    count += 1

count += (n - 1)
print(count)
