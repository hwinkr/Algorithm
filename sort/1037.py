# 1과 n이 아닌 n의 약수가 주어질때 n을 구하시오

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(lst[0] * lst[-1])
