#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX 100
int main (){
    // 4 : 행 , 열의 평균과 표준편차

    int N;
    FILE * file = fopen("input.txt" , "r");
    fscanf(file , "%d" , & N);
    int arr[MAX][MAX];

    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            fscanf(file , "%d" , &arr[i][j]);
        }
    }
    fclose(file);

    int sum;
    double average , despersionSum , devitation ;
    //행
    for(int i = 0; i < N; i++){
        sum = 0;
        average = 0;
        despersionSum = 0;
        devitation = 0;
        for(int j = 0; j < N; j++){
            sum += arr[i][j];
        }
        average = (double)sum / N;
        for(int k = 0; k < N; k ++){
            despersionSum += pow(average - arr[i][k] , 2);
        }
        devitation = sqrt(despersionSum / N);
        for(int p = 0; p < N; p ++){
            printf("%2d  " , arr[i][p]);
        }
        printf("%lf ", average);
        printf("%lf ", devitation);
        printf("\n");
    } 
    // 열
    for(int i = 0; i < N; i++){
        sum = 0;
        average = 0;
        despersionSum = 0;
        devitation = 0;
        for(int j = 0; j < N; j++){
            sum += arr[j][i];
        }
        average = (double)sum / N;
        for(int k = 0; k < N; k ++){
            despersionSum += pow(average - arr[k][i] , 2);
        }
        devitation = sqrt(despersionSum / N);
        printf("%lf ", average);
        printf("%lf ", devitation);
        if(i%2) printf("\n");
    } 
    
    return 0;
}