# 좋은 수열
# 중복되는 인접한 부분수열이 있으면 나쁜수열

# 제일 처음 만들어지는 n 자리 숫자가 최솟값임

import sys
input = sys.stdin.readline


def check(tmp):
    length = len(tmp)
    for i in range(1, length // 2 + 1):
        if tmp[-i:] == tmp[-i * 2:-i]:
            return False
    return True


def dfs(num):
    if len(num) == n:
        print(num)
        # 제일처음 숫자를 출력하고 프로그램 자체를 종료 시켜야함, 종료코드 : exit()
        exit()
    # append 1, 2, 3
    # 숫자는 점점 증가하는 순서로 문자열에 추가하기 때문에 제일 처음 모든 조건을 만족하고 만들어지는 숫자가 제일 작다.
    for i in range(1, 4):
        if check(num + str(i)):
            dfs(num + str(i))


if __name__ == '__main__':
    n = int(input())
    dfs('1')
