# 두 배열곱 최소 만들기

import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

new_a = sorted(a)
new_b = sorted(b, reverse=True)
sum = 0

for i in range(n):
    sum += new_a[i] * new_b[i]

print(sum)
