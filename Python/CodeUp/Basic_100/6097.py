h , w = map(int, input().split())
n = int(input())

arr = [[0] * (w + 1) for _ in range(h + 1)]

        
for i in range(n) : 
    l , d , x , y = map(int , input().split());
    if(d == 0) :
        for i in range(l) : 
            arr[x][y + i] = 1;
    else :
        for i in range(l) :
            arr[x + i][y] = 1;
            
for i in range(1 , h + 1) :
    for j in range(1 , w + 1) : 
        print(arr[i][j] , end=" ")
    print()