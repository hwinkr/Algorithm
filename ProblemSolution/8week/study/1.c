#include <stdio.h>
#include <stdlib.h>
#define MAX 100
int main(){
    // 전치행렬 구하기
    int m , n;
    int mat[MAX][MAX];
    int tMat[MAX][MAX];
    FILE * file = fopen("input.txt" , "r");

    fscanf(file , "%d" , &m);
    fscanf(file , "%d" , &n);

    for(int i = 0; i < m; i++){
        for (int j = 0; j < n; j ++){
            fscanf(file , "%d" , &mat[i][j]);
        }
    }

    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j ++){
            tMat[j][i] = mat[i][j];
        }
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j ++){
            printf("%d " , tMat[i][j]);
        }
        printf("\n");
    }

    fclose(file);
    return 0;
}