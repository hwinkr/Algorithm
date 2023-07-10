```py
def promising(level: int, queens: list) -> bool:
    return all(
        queens[level] != queens[i] and level - i != abs(queens[level] - queens[i])
        for i in range(level)
    )


def nQueen(n: int, level: int, queens: list) -> int:
    if level == n:
        return 1

    cnt = 0

    for i in range(n):
        queens[level] = i
        if promising(level, queens):
            cnt += nQueen(n, level + 1, queens)

    return cnt


def solution(n):
    queens = [0 for _ in range(n)]
    return nQueen(n, 0, queens)
```

### 📌 풀이

2차원 배열의 각 행의 열에 퀸을 두고 이 위치에 퀸을 둘 수 있는지를 확인하는 함수 `promising`을 사용한다.  
만약 둘 수 있다면 퀸을 둔 상태에서 **다음 행(level)으로 넘어가고** 둘 수 없다면 **다음 열에 퀸을 두고 promising을 호출**해서 둘 수 있는지 없는지에 대한 확인을 한다.  
체스판은 2차원 배열로 표현되지만, 퀸을 둔 자리는 1차원 배열으로 표현할 수 있다.  
1차원 배열의 **인덱스는 2차원 배열의 행**이 되고, 1차원 배열의 **값은 2차원 배열의 열**이 된다.

예) queens[0] = 3은 체스판[0][3]에 퀸이 놓인것과 같다.
