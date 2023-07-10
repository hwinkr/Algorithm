```py
def solution(s):
    answer = ""

    for i, string in enumerate(s):
        if string.isspace():
            answer += " "
            continue

        if string.isdigit():
            answer += string
            continue

        if i == 0 or s[i - 1].isspace():
            if string.islower():
                answer += string.upper()
            else:
                answer += string
            continue

        if string.isupper():
            answer += string.lower()
            continue

        answer += string

    return answer
```

### 📌 풀이

이 문제는 조건을 잘 읽어야 했다.  
입력으로 주어지는 문자열은 알파벳, 숫자, 공백문자로 이루어져 있고 다음과 같은 조건을 가진다.

- 숫자는 **단어의 첫 문자**로만 나온다.
- 숫자로만 이루어진 단어는 없다.
- 공백문자가 **연속해서 나올 수 있다.**

JadenCase 문자열로 변경해도 **기존의 띄어쓰기, 숫자는 유지해야 한다.**

따라서 여러개의 조건문을 사용해서 문제를 해결했다.

1. 숫자인 경우 `isdigit()` 메서드 사용
2. 대문자인 경우 `isupper()`, 소문자인 경우 `islower()` 사용
