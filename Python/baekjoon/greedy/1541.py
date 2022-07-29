# 괄호쳐서 합 최소 만들기
# sol : 합을 최소로 만들수 있는건 , 빼기. - 뒤에 나오는 수를 최대로 만든다

x = input().split("-")

nums = []

for node in x:
    currentNum = 0
    s = node.split("+")
    for a in s:
        currentNum += int(a)
    nums.append(currentNum)

n = nums[0]

for i in range(1, len(nums)):
    n -= nums[i]

print(n)
