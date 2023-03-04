# 설탕배달 : 정확하게 n kg 배달 + 5 , 3 이용해서 봉지 적게 사용하기

n = int(input())

answer = 0

target = (n // 5) * 5

while True:
    if n % 5 == 0:
        answer = n // 5
        break
    elif (n - target >= 3) and (n - target % 3 == 0):
        answer = target // 5 + (n - target) // 3
        break
    else:
        target -= 5
        if(target == -5):
            break

if target == -5:
    print(-1)
else:
    print(answer)
