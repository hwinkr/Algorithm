# 단어 정렬

import sys
input = sys.stdin.readline

n = int(input())
lst = [input() for _ in range(n)]


lst = sorted(list(set(lst)))
lst.sort(key=lambda x: len(x))

for char in lst:
    print(char[:-1])
