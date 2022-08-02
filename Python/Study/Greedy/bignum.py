# 곱하기 혹은 더하기 -> 가장 큰 수 만들기

# 1
s = "567"
lst = []

for num in s:
    lst.append(int(num))

answer = 0

for j in range(len(lst)):
    if((answer + lst[j]) < (answer * lst[j])):
        answer *= lst[j]
    else:
        answer += lst[j]

print(answer)

# 2
numList = input()

result = int(numList[0])

for i in range(1, len(numList)):
    num = int(numList[i])
    if(num <= 1 or result <= 1):
        result += num
    else:
        result *= num

print(result)
