# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참가해야함
# 여행을 떠날수 있는 그룹의 수의 최댓값

# 모든 모험가가 여행을 떠나야 하는 경우
N = int(input())
lst = list(map(int, input().split()))

groupCnt = 0

while True:
    membetCnt = max(lst)

    groupCnt += 1

    for i in range(0, membetCnt):
        target = max(lst)
        lst.remove(target)

    if(len(lst) == 0):
        break

print(groupCnt)

# 모든 모험가가 여행을 떠날 필요는 없는 경우
# 오름차순 정렬 -> 그룹을 결성하는 멤버의 수를 작은 인원부터 만들수 있기때문에 그룹을 최대한으로 만들 수 있다.
size = int(input())
member = list(map(int, input().split()))
member.sort()
#  1 2 2 2 3
count = 0
answer = 0
for i in member:
    count += 1
# 현재 그룹에 포함되어 있는 멤버의수가 확인하고 있는 멤버의 공포도보다 크면,,
    if(count >= i):
        answer += 1
        count = 0

print(answer)
