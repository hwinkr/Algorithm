#include <stdio.h>
#define MAX 100
int main(){
    // 5 : 합이 최대인 부분행렬 출력하기 , 부분행렬은 반드시 정방행렬은 아님.

    int N;
    int arr[MAX][MAX];
    FILE *file = fopen("input5.txt" , "r");
    fscanf(file , "%d" , &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++) fscanf(file , "%d" , &arr[i][j]);
    }
    fclose(file);

    int sum = 0 , sumMax = -1;
    int startX = 0 , startY = 0;
    int xCount = 2, yCount = 2;

    // 2X2 , 2X3 , 2X4 ,,,, 4X4
    while(1){
        int sum = 0;
        for(int i = startX; i < startX + xCount; i++){
            for(int j = startY; j < startY + yCount; j++) sum += arr[i][j];
        }
        startY ++;
        if(sumMax < sum) sumMax = sum;
        
        if(startY > N - yCount){
            startY = 0;
            startX ++;
        }
        if(startX > N - xCount){
            startX = 0;
            startY = 0;
            yCount++;
        }
        if(yCount > N) {
            startX = 0;
            startY = 0;
            xCount ++;
            yCount = 2;
        }
        if(xCount > N) break;
    }

    printf("%d" , sumMax);
    
    return 0;
}