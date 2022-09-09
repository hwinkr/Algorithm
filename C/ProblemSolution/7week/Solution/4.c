#include <stdio.h>
#include <stdlib.h>
int main(){
    // 4 : 오름차순으로 정렬된 가장 긴 길이 출력하기
    int N;
    scanf("%d" , &N);
    int *arr = (int *)malloc(sizeof(int) * N);
    for(int i = 0; i < N; i++) scanf("%d" , &arr[i]);

    int length = 1;
    int lengthMax = -1;

    int i = 0;
    int j = 0;

    while(i < N){
        if(arr[i] <= arr[i + 1]){
            j = i;
            while(arr[j] <= arr[j + 1]){
                length ++;  
                j ++;     
            }
            i = j + 1;
        }else{
            i ++;
        }
        if(lengthMax < length) lengthMax = length;
        length = 1;
    }
    
    printf("max of length : %d" , lengthMax);
    
    return 0;
}