#include <stdio.h>
#include <stdlib.h>
#define MAX 100
int main(){
    FILE * file = fopen("input2.txt" , "r");
    int N;
    fscanf(file , "%d" , &N);
    
    double arr[MAX][MAX];

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N + 1; j++) fscanf(file , "%lf" , &arr[i][j]);
    }
    fclose(file);
    // 하삼각행렬
    for(int i = 0; i < N; i++){
        for(int j = i + 1; j < N; j++){
            double tmp = (double)(1) * arr[j][i] / arr[i][i];
            for(int k = 0; k < N + 1; k++){
                arr[j][k] -= tmp * arr[i][k];                
            }
        }
        //infinite solution
        for(int i = 0; i < N -1; i++){
            for(int j = i + 1; j < N; j++){
                int sameCnt = 0;
                for(int k = 0; k < N + 1; k++){
                    if(arr[i][k] == - arr[j][k]) sameCnt ++;
                }
                if(sameCnt > 3){
                    printf("infinite solution");
                    exit(0);
                }
            }
        }
        //no solution 
        for(int i = 0; i < N -1; i++){
            for(int j = i + 1; j < N; j++){
                int zeroCnt = 0;
                for(int k = 0; k < N; k++){
                    if((int)arr[j][k] == 0) zeroCnt ++;
                }
                if(zeroCnt > 2){
                    printf("no solution");
                    exit(0);
                }
            }
        }
    }   
    // 상삼각행렬
    for(int i = N - 1; i > 0; i--){
        for(int j = i - 1; j >= 0; j--){
            double tmp = (double)(1) * arr[j][i] / arr[i][i];
            for(int k = 0; k < N + 1; k++) {
                arr[j][k] -= tmp * arr[i][k];
            }
        }
        //infinite solution
        for(int i = 0; i < N -1; i++){
            for(int j = i + 1; j < N; j++){
                int sameCnt = 0;
                for(int k = 0; k < N + 1; k++){
                    if(arr[i][k] == - arr[j][k]) sameCnt ++;
                }
                if(sameCnt > 3){
                    printf("infinite solution");
                    exit(0);
                }
            }
        }
        //no solution 
        for(int i = 0; i < N -1; i++){
            for(int j = i + 1; j < N; j++){
                int zeroCnt = 0;
                for(int k = 0; k < N; k++){
                    if(arr[j][k] == 0) zeroCnt ++;
                }
                if(zeroCnt > 2){
                    printf("no solution");
                    exit(0);
                }
            }
        }
    }

    for(int i = 0 ; i < N; i++){
        arr[i][N] /= arr[i][i];
        arr[i][i] /= arr[i][i];
    }

    for(int i = 0; i < N; i++) printf("x%d = %d\n" , i + 1, (int)arr[i][N]);
        
    return 0;
}