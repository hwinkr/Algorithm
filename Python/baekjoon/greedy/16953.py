# 같은수 만들기

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
