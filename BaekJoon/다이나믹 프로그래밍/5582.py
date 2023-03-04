import sys

input = sys.stdin.readline


# * 기존의 배열 보다, dp 가 index 가 1 앞서있다. 이걸 잘 처리 해줘야 한다.
# ! 문제를 해결해 나가는 과정은, dp 2차원 배열을 업데이트 해가는 과정이라고 할 수 있다.
def solution(str1: str, str2: str) -> int:
    answer = 0

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                answer = max(answer, dp[i + 1][j + 1])

    return answer


if __name__ == "__main__":
    str1 = str(input())
    str2 = str(input())

    str1 = str1[:-1]  # * 파이썬 문자열을 입력으로 받는 경우, 줄바꿈 문자 \n 을 제거하기 위함
    str2 = str2[:-1]

    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    print(solution(str1, str2))
