#include <stdio.h>
#include <stdlib.h>
int main(){
    // 2: 역전된 3중쌍 갯수구하기

    int answer = 0;
    int N;
    scanf("%d" , &N);
    int *arr = (int *)malloc(sizeof(int) * N);
    
    for(int i = 0; i < N; i++) scanf("%d" , &arr[i]);

    for(int p = 0; p < N - 2; p++){
        for(int q = p + 1; q < N - 1; q ++){
            for(int r = q + 1; r < N; r ++){
                if( (arr[p] > arr[q]) && (arr[q] > arr[r] ))
                    answer ++;
            }  
        }
    }

    printf("answer : %d" , answer);
    return 0;
}