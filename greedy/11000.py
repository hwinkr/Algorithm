import sys
import heapq

input = sys.stdin.readline

n = int(input())

lectures = []
for _ in range(n):
    heapq.heappush(lectures, list(map(int, input().split())))

end_times = []
while lectures:
    current_lecture = heapq.heappop(lectures)

    if end_times and current_lecture[0] >= end_times[0]:
        heapq.heappop(end_times)
    heapq.heappush(end_times, current_lecture[1])

print(len(end_times))

# 언제 강의실을 추가 해야 하는가? -> 현재 확인하고 있는 강의가 끝나는 시간이 가장 빨리 끝나는 강의보다 빨리 시작하면
# 강의실 추가할 필요 없는 경우 -> 가장 빨리 끝나는 강의보다 현재 강의가 더 늦게 시작하는 경우
# 강의실 하나를 추가
# 우선 강의를 시작시간 기준으로 정렬을 했다 그렇다면 배열의 인덱스가 증가하는 순서대로 강의 시작시간이 늦어진다는 것이다.
# 가장 늦게 끝나는 강의에게 우선순위를 주면 강의실을 많이 사용하게 됨 -> 숫자가 커지니까 다음에 오는 강의 시작시간보다도 클 가능성이 높다 -> 그렇다면 강의실을 계속 추가하게됨
