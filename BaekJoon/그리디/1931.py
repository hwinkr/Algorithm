# 회의실을 가장 많이 사용할 수 있는 회의 수

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간을 기준으로 정렬하되, 만약에 끝나는 시간이 같다면 시작시간이 빠른순으로 정렬한다.
arr.sort(key=lambda x: (x[1], x[0]))

cnt = 1
end_time = arr[0][1]

for i in range(1, N):
    if(end_time <= arr[i][0]):
        cnt += 1
        end_time = arr[i][1]

print(cnt)
