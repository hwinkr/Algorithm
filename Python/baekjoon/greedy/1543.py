# 크게 만들기

# N 자리 숫자 , 지워야하는 문자의 갯수가 주어졌을때 남아있는 수중 가장 큰 수는?

# sol
# 현재 위치에서의 문자를 지울건지 말건지를 판단할수 있어야함

# 지우는 경우 :
# 추가하는 경우 : 뒤에 나보다 큰 수가 없고 현재 배열 인덱스 + 남은 자리가 배열의 크기를 초과하지 않으면 추가 / 뒤에 나보다 큰수가 있고 그 큰수의 인덱스 + 남은자리가 배열의 크기를 초과하면 추가
# 확인해야하는 문자의 갯수와 추가해야하는 문자의 갯수가 같으면 모두 추가하고 종료

# 뒤에 나보다 작은 값이 없다 -> 내 인덱스와 사이즈를 더한게 <= n 이다 -> 추가한다

# 스택 안쓰면 시간초과 나온답니다.. 하지만 저는 스택을 몰라요
n, k = map(int, input().split())
input = input()

for num in input:
    print(num)

answers = []
size = n - k
for i in range(n):
    if(n - i == size):
        for num in input[i:]:
            answers.append(num)
        break

    index = -1

    for num in input[i + 1:]:
        if(input[i] - num < 0):
            index = input.index(num)
            break
    if(index == -1 and i + size <= n):
        answers.append(input[i])
        size -= 1
    elif(index + size > n):
        answers.append(input[i])
        size -= 1

print("".join(answers))
