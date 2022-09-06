# 암호의 자릿수 : L
# 사용할 수 있는 알파벳 종류의 갯수 : C
# ! 최소 한개의 모음 (a, e, i, o, u)
# ! 최소 두개의 자음
import sys
input = sys.stdin.readline

l, c = map(int, input().split())
lst = list(map(str, input().split()))
check_lst = ['a', 'e', 'i', 'o', 'u']

lst.sort()
word = []


def dfs(x):
    if len(word) == l:
        # 모음 자음 갯수 체크
        cntMo = 0
        cntJa = 0
        isMo = False
        for char in word:
            for check in check_lst:
                if char == check:
                    isMo = True
                    cntMo += 1
                    break
            if not isMo:
                cntJa += 1
            isMo = False
        if cntMo >= 1 and cntJa >= 2:
            print(''.join(word))
        return

    for i in range(x, c):
        if lst[i] not in word:
            word.append(lst[i])
            dfs(i + 1)
            word.pop()


dfs(0)
