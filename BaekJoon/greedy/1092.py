# 각 크레인은 동시에 1분을 소모하면서 작동하고, 한번의 작동에 하나의 박스만 옮길 수 있다.
# 크레인의 제한 무게를 넘은 박스는 크레인이 옮길 수 없다.
# 모든 박스를 배로 옮기는데 걸리는 시간의 최소
# ! 그리디 : 주어진 1분동안 최대한 많은 크레인을 사용할 수 있도록 해야한다

# python 3
import sys

input = sys.stdin.readline

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane.sort(reverse=True)
box.sort(reverse=True)


box_moved = [0] * m
crane_next = [0] * n

move_count = 0
time = 0

if box[0] > crane[0]:
    print(-1)
else:
    while move_count < m:
        for i in range(n):
            while crane_next[i] < m:
                if not box_moved[crane_next[i]] and crane[i] >= box[crane_next[i]]:
                    box_moved[crane_next[i]] = 1
                    crane_next[i] += 1
                    move_count += 1
                    break

                crane_next[i] += 1

        time += 1

    print(time)

# pypy3
import sys

input = sys.stdin.readline

n = int(input())
crane_list = list(map(int, input().split()))
m = int(input())
box_list = list(map(int, input().split()))

crane_list.sort(reverse=True)
box_list.sort(reverse=True)


if box_list[0] > crane_list[0]:
    print(-1)
else:
    time = 0
    while box_list:

        for crane in crane_list:
            for box in box_list:
                if crane >= box:
                    box_list.remove(box)
                    break

        time += 1

    print(time)
