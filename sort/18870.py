# 좌표 압축

import sys
input = sys.stdin.readline

n = int(input())
points = list(map(int, input().split()))

set_points = list(set(points))
set_points.sort()
location = dict()

for i in range(len(set_points)):
    location[set_points[i]] = i

for num in points:
    print(location[num], end=" ")
