maze = [];
x = 1;
y = 1;

for i in range(10) : 
    maze.append(list(map(int , input().split())))
    
while True :
    if(maze[x][y] == 2) :
        maze[x][y] = 9;
        break;
    
    maze[x][y] = 9;
    
    if(maze[x + 1][y] == 1 and maze[x][y + 1] == 1) : break;
    
    if(maze[x][y + 1] == 1) : x += 1;
    elif(maze[x + 1][y] == 1) : y += 1;
    else : y += 1;
    
    
for i in range(10) :
    for j in range(10) :
        print(maze[i][j] , end=" ")
    print()
    