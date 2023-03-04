import sys

input = sys.stdin.readline

carrots_type, harvest_day = map(int, input().split())
taste_list = [list(map(int, input().split())) for _ in range(carrots_type)]
carrots_list = [0] * carrots_type

start_day = harvest_day - carrots_type

taste_sum = 0


for day in range(harvest_day):
    if day == 0:
        for i in range(len(taste_list)):
            carrots_list[i] = taste_list[i][0]
    else:
        for i in range(len(taste_list)):
            carrots_list[i] += taste_list[i][1]

    if day >= start_day:
        target_carrot = min(carrots_list)
        taste_sum += target_carrot
        index = carrots_list.index(min(carrots_list))
        carrots_list[index] = sys.maxsize

print(taste_sum)
