# 두 수 묶기
# 코드보다 문제 이해가 핵심!

N = int(input())

nums = []

for i in range(0, N):
    nums.append(int(input()))

nums_pos = []
nums_neg = []
nums_one = []

answer = 0

for num in nums:
    if(num > 1):
        nums_pos.append(num)
    elif(num == 1):
        nums_one.append(num)
    else:
        nums_neg.append(num)


nums_pos.sort(reverse=True)
nums_neg.sort()

if(len(nums_pos) % 2 == 0):
    for i in range(0, len(nums_pos), 2):
        answer += nums_pos[i] * nums_pos[i + 1]
else:
    for i in range(0, len(nums_pos) - 1, 2):
        answer += nums_pos[i] * nums_pos[i + 1]
    answer += nums_pos[len(nums_pos) - 1]

if(len(nums_neg) % 2 == 0):
    for i in range(0, len(nums_neg), 2):
        answer += nums_neg[i] * nums_neg[i + 1]
else:
    for i in range(0, len(nums_neg) - 1, 2):
        answer += nums_neg[i] * nums_neg[i + 1]
    answer += nums_neg[len(nums_neg) - 1]

for one in nums_one:
    answer += one

print(answer)
