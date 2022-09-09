# 단어 수학
# 알파벳을 0 ~ 9 까지의 숫자중 하나로 변경
# N개의 단어가 N개의 숫자가 된다
# ! 같은 알파벳은 같은 숫자, 두개 이상의 알파벳이 같은 숫자로 바뀌어서는 안됨

# A를 0 ~ 9 중 가장 큰 숫자인 9로 바꾸는 이유
# ACDEB, GCF를 숫자로 변경했다는 가정하에 자릿수가 가장 크기 때문에 그럼 모든 알파벳을 숫자로 변경했을때, 자릿수를 저장해주는 자료구조가 있다면!!!


import sys
input = sys.stdin.readline

n = int(input())
lst = []
digit = dict()
ans = 0

for _ in range(n):
    word = input()
    lst.append(word[: -1])

for word in lst:
    tmp = len(word) - 1
    for c in word:
        if c not in digit:
            digit[c] = 10 ** tmp
        else:
            digit[c] += 10 ** tmp
        tmp -= 1

sorted_digit = sorted(digit.values())
multi_num = 9 - len(digit) + 1

for num in sorted_digit:
    ans += num * multi_num
    multi_num += 1

print(ans)
