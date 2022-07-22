#include <stdio.h>
#include <stdlib.h>
#define MAX 100
int main(){
    // 두 행렬의 곱 

    int mat1[MAX][MAX] , mat2[MAX][MAX] , multiMat[MAX][MAX];
    int p , q1 , q2 , r;
    FILE * file = fopen("input.txt" , "r");
    // mat1
    fscanf(file , "%d" , &p);
    fscanf(file , "%d" , &q1);
    for(int i = 0; i < p; i++){
        for(int j = 0; j < q1; j++){
            fscanf(file , "%d" , &mat1[i][j]);
        }
    }
    // mat2
    fscanf(file , "%d" , &q2);     
    fscanf(file , "%d" , &r);
    for(int i = 0; i < q2; i++){
        for(int j = 0; j < r; j++){
            fscanf(file , "%d" , &mat2[i][j]);
        }
    }

    fclose(file);
    int currentSum = 0;
    
    if(q1 != q2){
        printf("wrong input");
        return 0;
    }else{
        for(int i = 0; i < p; i++){ // p = 3
            for(int j = 0; j < r; j++){ // r = 2
                for(int k = 0; k < q1; k++){ // q1 = 4
                currentSum += mat1[i][k] * mat2[k][j];
            }
                multiMat[i][j] = currentSum ;
                currentSum = 0;
            }
        }
        for(int i = 0; i < p; i++){
            for(int j = 0; j < r; j++){
            printf("%3d" , multiMat[i][j]);
        }
            printf("\n");
        }
    }

    return 0;
}