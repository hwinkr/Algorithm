# dp : 다이나믹 프로그래밍

# 1. 최적 부분구조 : 큰 문제를 작은 문제로 분할해나가면서 작은 문제의 답으로 큰 문제의 답을 찾는다
# 2. 중복되는 부분문제 : 동일한 작은 문제들을 반복적으로 해결한다

# top-down vs bottom-up

# 1.top - down 재귀함수 이용
# 하향식 , 큰 문제를 작은 문제로 분할해가면서 작은 문제의 답들을 큰 문제의 답을 구하는데 사용한다, 여기서 memoization (cach, memo , d, d) 메모리 공간을 하나 만들어서 중복되는 작은 문제의 답들을 저장하면서 사용한다

# ! memoizaion 방법은 dp만을 해결하기 위한 방법이 아님

# 2.bottom-up 반복문 이용 , dp의 전형적인 형태
# 상향식 , 처음부터 작은문제부터 해결해나가면서 메모리 공간에 값을 저장한다

# ex) fivo
# 1. 재귀
# 피보나치 수열을 단순 재귀함수로 값을 구하면 시간복잡도 : 2^n

# def fivo(n):
#     # 재귀함수 종료 조건
#     if n == 1 or n == 2:
#         return 1
#     return fivo(n - 1) + fivo(n - 2)

# print(fivo(5))


# 계산된 결과를 담기 위해서 배열을 사용
# 1. top-down : 큰 문제 -> 작은문제 쪼개기 -> 큰 문제 답
# import sys
# input = sys.stdin.readline
# n = int(input())
# dp = [0] * 100


# def fivo(n):
#     if n == 1 or n == 2:
#         return 1

#     if dp[n] != 0:
#         return dp[n]

#     dp[n] = fivo(n - 1) + fivo(n - 2)
#     return dp[n]

# print(fivo(5))


# # 2. bottom-up : 작은문제 -> 큰 문제

# input = sys.stdin.readline

# n = int(input())
# dp = [0] * 100

# dp[1], dp[2] = 1, 1

# for i in range(3, n + 1):
#     dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[n])

# 이미 계산된 값을 확인하고 가져가면 그 시간복잡도는 상수

# n이 굉장히 큰 값이더라도 n 만큼의 메모리 공간을 확보할 수 있으면 시간복잡도는 o(n) 이다.
# memo = [0] * 100


# def fiboF(n):
#     print('f(' + str(n) + ')', end=" ")
#     if n == 1 or n == 2:
#         return 1

#     if memo[n] != 0:
#         return memo[n]

#     memo[n] = fiboF(n - 1) + fiboF(n - 2)
#     return memo[n]


# fiboF(6)
