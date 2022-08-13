# 시리얼 번호 매기기
# 길이순 -> 시리얼에 적혀있는 번호의 합 -> 사전순

import re
import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    serial = input()
    lst.append(serial[:-1])

new_lst = []
for arr in lst:
    sum = 0
    numbers = re.findall(r'\d', arr)
    for num in numbers:
        sum += int(num)
    new_lst.append([arr, sum])
new_lst.sort(key=lambda x: (len(x[0]), x[1], x[0]))

for i in range(len(new_lst)):
    print(new_lst[i][0])
