# 도시 이동비용 최소로 만들기

n = int(input())
load_list = list(map(int, input().split()))
oil_list = list(map(int, input().split()))

oil_list.pop()

best_city = oil_list.index(min(oil_list))


current_city = 0
next_city = 1
money = 0

while True:
    if(next_city == len(load_list)):
        money += oil_list[current_city] * load_list[next_city - 1]
        break
    if(oil_list[current_city] > oil_list[next_city]):
        money += oil_list[current_city] * load_list[current_city]
        if(next_city == best_city):
            for j in range(next_city, len(load_list)):
                money += oil_list[best_city] * load_list[j]
            break
        else:
            next_city += 1
            current_city = next_city - 1
    else:
        money += oil_list[current_city] * load_list[next_city - 1]
        next_city += 1

print(money)
