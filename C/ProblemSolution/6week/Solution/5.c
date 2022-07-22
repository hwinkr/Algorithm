#include <stdio.h>
#include <stdlib.h>
int main(){
    // 5 : 구간순서 빠른대로 출력하기

    int N ;
    scanf("%d" , &N);
    int arrSize = N * 2;
    int *arr = (int *)malloc(arrSize * sizeof(int));
    
    for(int i = 0; i < arrSize; i ++) scanf("%d" , &arr[i]);
    // 배열에 저장된 짝수 인덱스들의 값을 비교 , 짝수 인덱스들의 값이 같은 동안은 홀수 인덱스의 값을 비교
    for(int i = arrSize - 2 ; i > 0; i -= 2){
        for(int j = 0 ; j < i ; j += 2){
            if(arr[j + 2] < arr[j]){
                int tmp1 = arr[j];
                int tmp2 = arr[j + 1];
                arr[j] = arr[j + 2];
                arr[j + 1] = arr[j + 3];
                arr[j + 2] = tmp1;
                arr[j + 3] = tmp2;
            }
            else if(arr[j + 2] == arr[j]){
                if(arr[j + 3] < arr[j + 1]){
                    int tmp1 = arr[j];
                    int tmp2 = arr[j + 1];
                    arr[j] = arr[j + 2];
                    arr[j + 1] = arr[j + 3];
                    arr[j + 2] = tmp1;
                    arr[j + 3] = tmp2;
                }
            }
        }
    }

    printf("\n\n ### 정렬된 좌표 순서 ### \n\n");
    for(int j = 0; j < arrSize; j++){
        if(!(j % 2)){
            printf("%d " ,arr[j]);
        }else{
            printf("%d\n", arr[j]);
        }
    }
    
    return 0;
}