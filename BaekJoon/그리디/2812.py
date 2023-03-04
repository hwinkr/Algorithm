# # 크게 만들기

# # N 자리 숫자 , 지워야하는 문자의 갯수가 주어졌을때 남아있는 수중 가장 큰 수는?

# 1. my sol, 시간 초과

# # 추가하는 경우 : 뒤에 나보다 큰 수가 없고 현재 배열 인덱스 + 남은 자리가 배열의 크기를 초과하지 않으면 추가 / 뒤에 나보다 큰수가 있고 그 큰수의 인덱스 + 남은자리가 배열의 크기를 초과하면 추가
# # 확인해야하는 문자의 갯수와 추가해야하는 문자의 갯수가 같으면 모두 추가하고 종료

# # 뒤에 나보다 작은 값이 없다 -> 내 인덱스와 사이즈를 더한게 <= n 이다 -> 추가한다

# 스택 안쓰면 시간초과 나온답니다.. 하지만 저는 스택을 몰라요

# import sys
# input = sys.stdin.readline
# n, k = map(int, input().split())
# lst = input().rstrip()

# answers = []
# size = n - k
# for i in range(n):
#     if n - i == size:
#         for num in lst[i:]:
#             answers.append(num)
#         break

#     index = -1
#     # index 가 -1 이라는 것은 현재 숫자보다 뒤에 더 큰 숫자가 없다는 뜻. 따라서 사이즈 조건만 만족하면 추가한다.
#     for num in lst[i + 1:]:
#         if int(lst[i]) - int(num) < 0:
#             index = lst.index(num)
#             break
#     if index == -1 and i + size <= n:
#         answers.append(lst[i])
#         size -= 1
#     elif index + size > n:
#         answers.append(lst[i])
#         size -= 1

# print("".join(answers))

# 지울지 말지를 결정해야하는 상황에서 최선의 선택을 함 -> 지울수 있는 숫자의 갯수가 0보다 큰 상황에서 스택의 마지막 숫자와 현재 입력된 숫자를 비교해서 입력된 숫자가 더 크면 스택에서 숫자 꺼내고 입력된 숫자를 넣고 k -= 1
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
del_cnt = k

lst = input().rstrip()

ans = []

for i in range(n):
    while ans and k > 0:
        # 현재 스택에 추가되어있는 마지막 숫자와 추가될지 말지 결정해야하는 숫자를 비교
        if int(ans[-1]) < int(lst[i]):
            k -= 1
            ans.pop()
        else:
            break
    ans.append(lst[i])

# 주어진 숫자가 내림차순 정렬이 된 경우도 있기 때문에, n-k 만큼만 출력한다
print(''.join(ans[:n-del_cnt]))
