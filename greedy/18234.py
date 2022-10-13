import sys

input = sys.stdin.readline

carrots_type, harvest_day = map(int, input().split())
taste_list = [list(map(int, input().split())) for _ in range(carrots_type)]
taste_list.sort(key=lambda x: (x[1], x[0]))

start_day = harvest_day - carrots_type
taste_sum = 0

for taste in taste_list:
    current_taste, add_taste = taste[0], taste[1]
    taste_sum += current_taste + add_taste * start_day
    start_day += 1

print(taste_sum)
