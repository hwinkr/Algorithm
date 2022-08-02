# 시간에 3 몇번 들어가는지 세기
N = int(input())

clock = []
answer = 0

for i in range(0, N + 1):
    for j in range(0, 60):
        for k in range(0, 60):
            str_i = str(i)
            str_j = str(j)
            str_k = str(k)
            count = str_i.count("3") + str_j.count("3") + str_k.count("3")
            if(count > 0):
                answer += 1
            # if '3' in str(i) + str(j) + str(k) :
            #   answer +=1

print(answer)
