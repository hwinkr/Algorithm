import sys
input = sys.stdin.readline


def fibo(n):
    length = len(zero)
    if n >= length:
        for i in range(length, n + 1):
            zero.append(zero[i - 2] + zero[i - 1])
            one.append(one[i - 2] + one[i - 1])

    print(zero[n], one[n])


zero = [1, 0, 1]
one = [0, 1, 1]

t = int(input())
for _ in range(t):
    fibo(int(input()))

zero = [1, 0, 1]
one = [0, 1, 1]
