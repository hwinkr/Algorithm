# r , g , b = map(int, input().split())

# for i in range(r) :
#     for j in range(g) :
#         for k in range(b) :
#             print(i , j , k)

# print(r * g * b)

# a , d , n = map(int , input().split())
# sum = 0
# sum += a
# for i in range(0 , n - 1) :
#     sum += d

# print(sum)

# a , r , n = map(int , input().split())

# answer = a;
# for i in range(0 , n - 1) :
#     answer *= r;

# print(answer)

# a , m , d , n = map(int, input().split())

# answer = a;
# for i in range(0 , n - 1) :
#     answer = answer * m + d;

# print(answer);

# a , b , c = map(int , input().split())

# answer = 2;

# while True :
#     if(answer % a == 0 and answer % b == 0 and answer % c == 0) :
#         print(answer)
#         break;
#     else :
#         answer += 1

# n = int(input())
# a = list(map(int, input().split()))

# d = []

# for i in range(24) :
#     d.append(0)

# for i in range(n) :
#     d[a[i]] += 1;

# for i in range(1,24) :
#     print(d[i] , end=" ")

# n = int(input())
# a = list(map(int , input().split()))

# m = int(len(a) / 2);
# for i in range(0 , m) :
#     tmp = a[i];
#     a[i] = a[len(a) - i - 1]
#     a[len(a) - i - 1] = tmp

# for i in range(len(a)) :
#     print(a[i] , end=" ")

# n = int(input())
# a = list(map(int , input().split()))

# print(min(a))

# 20 * 20 크기의 바둑판을 만들고 출력은 19 19

# n = 19
# d = []
# for i in range(0, n + 1) :
#     d.append([])
#     for j in range(0 , n + 1):
#         d[i].append(0) # 0을 뒤에서부터 계속 추가

# cnt = int(input())

# for i in range(cnt) :
#     x , y = map(int, input().split())
#     d[x][y] = 1;

# for i in range(1 , n + 1) :
#     for j in range(1 , n + 1) :
#         print(d[i][j] , end=" ")
#     print()


n = 19
d = []

for i in range(0, n):
    d.append(list(map(int, input().split())))

reverseCnt = int(input())

for i in range(0, reverseCnt):
    x, y = map(int, input().split())
    for j in range(0, n):
        if(d[x - 1][j] == 1):
            d[x - 1][j] = 0
        else:
            d[x - 1][j] = 1

    for j in range(0, n):
        if(d[j][y - 1] == 1):
            d[j][y - 1] = 0
        else:
            d[j][y - 1] = 1

for i in range(0, n):
    for j in range(0, n):
        print(d[i][j], end=" ")
    print()
