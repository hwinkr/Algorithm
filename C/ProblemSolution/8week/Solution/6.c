#include <stdio.h>
#define MAX 100
int main(){
    // 6 : 시계방향으로 배열 값 출력하기

    int N;
    int arr[MAX][MAX];

    FILE * file = fopen("input6.txt" , "r");
    fscanf(file , "%d" , &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++) fscanf(file , "%d" , &arr[i][j]);
    }
    
    fclose(file);

    int printCnt = 0;
    int printDir = 0;
    int startX = 0 , limitX = N - 1 ;
    int startY = 0 , limitY = N - 1;
 
    while(printCnt < N * N){
        if(printDir % 4 == 0){ // right
            for(int i = startY; i <= limitY; i ++){
                printf("%d ", arr[startX][i]);
                printCnt ++;
            }
            printDir = 1;
            startX ++;
        }else if(printDir % 4 == 1){ // down
            for(int i = startX; i <= limitX; i ++){
                printf("%d ", arr[i][limitY]);
                printCnt ++;
            }
            printDir = 2;
            limitY --;
        }else if(printDir % 4 == 2){ // left
            for(int i = limitY; i >= startY; i --){
                printf("%d ", arr[limitX][i]);
                printCnt ++;
            }
            printDir = 3;
            limitX --;
        }else  if(printDir % 4 == 3){ // up
            for(int i = limitX; i >= startX; i --){
                printf("%d " , arr[i][startY]);
                printCnt++;
            }
            printDir = 4;
            startY++;
        }
    }

    return 0;
}