#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 100
int main(){
    int N , T = 10000 , miro[MAX][MAX] = { 0 , };
    int escapeCnt = 0;
    scanf("%d" , &N);

    srand(time(NULL));
    
    int direction[4][2] = {{-1 , 0} , {0 , 1} , {1 , 0} , {0, -1}};

    for(int i = 0; i < T; i++){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++) miro[i][j] = 0;
        }
        int x = N / 2;
        int y = N / 2;
        while(1){
            int possibleDir[4][2] = { 0, };
            int possibleCnt = 0;
            miro[x][y] = 1;
            for(int dir = 0; dir < 4; dir++){
                int newX = x + direction[dir][0];
                int newY = y + direction[dir][1];
                if(miro[newX][newY] == 0){
                    possibleDir[possibleCnt][0] = direction[dir][0];
                    possibleDir[possibleCnt][1] = direction[dir][1];
                    possibleCnt ++;
                }
            }
            if(possibleCnt == 0){
                break;
            }else{
                int randomDir = rand() % possibleCnt;
                x = x + possibleDir[randomDir][0];
                y = y + possibleDir[randomDir][1];
                if(x == 0 || x == N - 1 || y == 0 || y == N - 1){
                    escapeCnt ++;
                    break;
                }
            }
            
        }   
    }
    printf("escape possibility : %lf" , (double)escapeCnt / T);
    return 0;
}
