# ! 각 사람들 까지의 거리의 합이 최소가 되는 위치에 우체국을 위치시킨다.
# 사람의 수가 결과에 영향을 준다
# ! 핵심은 현재 위치에서 양 옆에 있는 사람들의 수를 가장 균등하게 나누자, 최대한 균등하게 나누면서 거리 계산에 포함되는 마을사람들의 수를 최대한 적게 해야함
import sys

input = sys.stdin.readline

N = int(input())
people_total = 0
datas = []

for _ in range(N):
    viliage, people = map(int, input().split())
    datas.append([viliage, people])
    people_total += people

datas.sort(key=lambda x: x[0])

people_tmp = 0
mid = people_total / 2

for i in range(N):
    people_tmp += datas[i][1]
    if people_tmp >= mid:
        print(datas[i][0])
        break
