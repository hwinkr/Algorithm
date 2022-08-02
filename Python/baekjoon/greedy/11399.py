# wait ATM

N = int(input())
person = list(map(int, input().split()))

person.sort()

current_time = 0
wait_time = 0

for i in range(0, N):
    current_time += person[i]
    wait_time += current_time

print(wait_time)
