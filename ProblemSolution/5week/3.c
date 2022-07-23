#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main (){
    // 3 : 평균과 표준편차 계산
    int sum = 0;
    double despersionSum = 0;
    double devitation = 0;
    int N ;
    scanf("%d" , &N);
    int *arr = (int *)malloc(N * sizeof(int));

    for(int i = 0; i < N ; i ++){
        scanf("%d" , &arr[i]);
        sum += arr[i];
    }
    double average = (double)sum / N;
    
    for(int j = 0; j < N; j ++){
        despersionSum += pow(arr[j] - average, 2);
    }
    devitation = sqrt(despersionSum / N);

    printf("%lf %lf" , average , devitation);
    
    return 0;
}