# 회의실을 사용 할 수 있는 최대 회의의 수

N = int(input())
arr = []
answer = 0

for i in range(0, N):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[1])

answer = 0
end_time = -1

for i in range(0, N):
    if(end_time <= arr[i][0]):
        answer += 1
        end_time = arr[i][1]

print(answer)
