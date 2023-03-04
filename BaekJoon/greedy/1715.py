import heapq
import sys

input = sys.stdin.readline

n = int(input())
card_list = []
compare_cnt = 0

for _ in range(n):
    heapq.heappush(card_list, int(input()))

if len(card_list) == 1:
    print(0)
else:
    while len(card_list) > 1:
        comp1 = heapq.heappop(card_list)
        comp2 = heapq.heappop(card_list)
        compare_cnt += comp1 + comp2

        heapq.heappush(card_list, comp1 + comp2)

    print(compare_cnt)
