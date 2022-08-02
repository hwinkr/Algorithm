# stack : 선입 후출

from collections import deque
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])

# 선입선출 (대기열)
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)

# 재귀함수 : 메모리에 함수 호출을 스택으로 쌓음 함수 또한 선입후출

# ex1 : factorial


def n_fact(n):
    if(n == 1):
        return 1
    else:
        return n * n_fact(n-1)


print(n_fact(5))

# ex2 : print


def rec_print(i):
    if i == 5:
        return
    print(i, '번째 재귀함수 에서', i + 1, '번째 재귀함수를 호출 합니다')
    rec_print(i + 1)
    print(i, '번째 재귀함수를 종료합니다')


rec_print(1)


# 재귀함수 종료
# 함수가 자신을 다시 호출하는 것과 자신을 반환해주는 것은 다르다

def gcd(a, b):
    if(a % b == 0):
        return b
    else:
        return gcd(b, a % b)


result = gcd(192, 162)
print(result)
