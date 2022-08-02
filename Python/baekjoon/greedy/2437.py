# 나올수 없는 무게중 최소값
# 오름차순 정렬후 값을 더해나가면 현재까지 더한 값이 만들수 있는 무게중 최소이다. 그 최소값에 1을 더한 무게를 만들수 있는지 없는지 판단.

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

weight_sum = 0

if(lst[0] > 1):
    print(1)
else:
    for i in range(len(lst)):
        weight_sum += lst[i]
        if(i == len(lst) - 1):
            print(weight_sum + 1)
        elif(weight_sum + 1 < lst[i + 1]):
            print(weight_sum + 1)
            break
