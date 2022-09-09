# 나를 제외한 다른 모든사람과 비교 다른 사람보다 서류심사 등수의 숫자가 크다 -> 그 사람의 면접 등수의 숫자보다 크다 -> 불합격

import sys

testCnt = int(input())
pass_lst = []

for i in range(0, testCnt):
    n = int(input())
    lst = []

    for j in range(0, n):
        lst.append(list(map(int, sys.stdin.readline().split())))

    lst.sort(key=lambda x: x[0])

    pass_cnt = 1
    move_index = 0

    for i in range(1, len(lst)):
        if(lst[move_index][1] > lst[i][1]):
            pass_cnt += 1
            move_index = i

    pass_lst.append(pass_cnt)

for pass_cnt in pass_lst:
    print(pass_cnt)
