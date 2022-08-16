# 용돈 관리
# 정확히 m 번을 맞추기 위해 남은 금액이 그날 사용할 금액보다 많더라도 통장에 집어놓고 다시 인출 가능
# 돈은 하루에 한번 뽑을수 있다..

#  돈을 뽑을 때는 가지고 있는 돈을 모두 반환하고 뽑기 때문에 잘못된 생각.
# ex) 현재 남은돈 : 100 , 써야하는돈 : 700 인출할수 있는돈 : 500 이면, 100을 통장에 다시 넣고 500을 두번 인출하면 되지 않을까 라고 생각할 수 있지만, 500을 한번 뽑고나서 다시 500을 뽑는 시점에 남은 200을 다시 통장에 넣는다. 이돈은 남은돈이 아닌 써야하는 돈인데 통장에 넣을수 없다. 따라서 인출할 수 있는 돈은 max(lst) 보다 커야한다.... 하 계속 이생각에 빠져서 시간 개오래 잡아먹었네ㅡㅡ

# 최대 , 최소 구하는 로직이 반대임

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [int(input()) for _ in range(n)]

start = min(lst)
end = sum(lst)
temp = end

while start <= end:
    mid = (start + end) // 2

    cnt = 1
    current = mid
    bigger = False

    for i in range(n):
        if mid < lst[i]:
            bigger = True
            break
        elif current - lst[i] < 0:
            cnt += 1
            current = mid
        current -= lst[i]

    if bigger:
        start = mid + 1
    else:
        if cnt > m:
            start = mid + 1
        else:
            if mid < temp:
                temp = mid
            end = mid - 1

print(temp)


# while start <= end:
#     mid = (start + end) // 2

#     cnt = 1
#     current = mid

#     for i in range(n):
#         if current < lst[i]:
#             cnt += 1
#             current = mid

#         current -= lst[i]

#     if cnt > m or mid < max(lst):
#         start = mid + 1
#     else:
#         answer = mid
#         end = mid - 1
