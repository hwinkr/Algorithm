# 같은수 만들기
# a -> b 로 결과가 만들어 진 상태이기 때문에 다시 b -> a 로 작아지는 경우로 풀이

a, b = map(int, input().split())
count = 0

while True:
    if(b % 10 == 1):
        count += 1
        b //= 10
    else:
        count += 1
        b /= 2

    if(b <= a):
        break

if(b == a):
    print(count + 1)
else:
    print(-1)
