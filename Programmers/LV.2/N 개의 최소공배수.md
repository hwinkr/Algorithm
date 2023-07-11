```py
def gcd(a, b):
    if not a % b:
        return b
    return gcd(b, a % b)


def lcm(a, b):
    if a > b:
        return a * b // gcd(a, b)
    else:
        return a * b // gcd(b, a)


def solution(arr):
    answer = arr[0]

    for num in arr[1:]:
        answer = lcm(answer, num)

    return answer
```

### 📌 풀이

a, b 두 수의 곱은 a _ b = (두 수의 최소 공약수) _ (두 수의 최소 공배수) 로 나타낼 수 있다.  
따라서, (a \* b) // (두 수의 최소 공약수) = (두 수의 최소 공배수)가 된다.  
유클리드 호제법을 사용해서 두 수의 최소 공약수를 구하고, 이를 통해서 두 수의 최소 공배수를 구하면 문제를 해결할 수 있다.
