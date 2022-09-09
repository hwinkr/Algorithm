# 캠핑장 최대 이용하기

answers = []

while True:
    day = 0
    L, P, V = map(int, input().split())
    if(L == 0 and P == 0 and V == 0):
        break
    else:
        day += (V // P) * L
        if(V % P >= L):
            day += L
        else:
            day += (V % P)
    answers.append(day)

for i in range(len(answers)):
    case = i + 1
    print(f"Case {case}: {answers[i]}")
