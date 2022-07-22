#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int main(){
    // 1 : K 보다 작으면서 가장큰 정수와 K 의 차이의 절댓값

    int N , K;
    int answerNumber , answerIndex  , absoluteNumber ; 
    scanf("%d" , &N);    
    int * arr = (int *)malloc(N * sizeof(int));

    for(int i = 0; i < N; i++) scanf("%d" , &arr[i]);

    scanf("%d" , &K);

    bool isSmaller = false;

    int n = 0 ;

    while(1) {
        if(arr[n] <= K){
            isSmaller = true;
            break;
        }else if (n == N -1){
            break;
        }
        n ++;
    }

    answerIndex = n ;
    answerNumber = arr[n];

    for(int j = n + 1; j < N ; j ++){
        if((arr[j] <= K) && (answerNumber < arr[j])){
            answerNumber = arr[j];
            answerIndex = j;
        }
    }

    absoluteNumber = answerNumber - K;
    if(absoluteNumber < 0) absoluteNumber = -absoluteNumber;
    
    if(!isSmaller)
        printf("-1");
    else
        printf("index : %d / answer : %d / absoluteNumber : %d\n" , answerIndex , answerNumber , absoluteNumber);
        
    return 0;
}