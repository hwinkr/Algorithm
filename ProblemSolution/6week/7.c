#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int main(){
    int MAX = 100;
    // 두 정수 사전식 출력하기
    // 입력받은 정수를 배열에 한칸씩 저장해야 비교 가능.
    int num1 , num2;
    int * num1Arr =(int *)malloc(MAX * sizeof(int));
    int * num2Arr =(int *)malloc(MAX * sizeof(int));
    scanf("%d %d" , &num1 , &num2);
    int num1Storage = num1 , num2Storage = num2;
    // 자릿수 구해서 배열에 뒤에서부터 넣기
    int num1Size = 0;
    while(num1 > 0){
        num1 /= 10;
        num1Size++;
    }
    int num2Size = 0;
    while(num2 > 0){
        num2 /= 10;
        num2Size++;
    }
    for(int p = num1Size - 1; p>=0; p--){
        num1Arr[p] = num1Storage % 10;
        num1Storage /= 10;
    }
    for(int q = num2Size - 1; q>=0; q--){
        num2Arr[q] = num2Storage % 10;
        num2Storage /= 10;
    }

    int compareSize;
    if(num1Size > num2Size) compareSize = num2Size;
    else compareSize = num1Size;
    
    bool isCompared = false;

    for(int p = 0; p < compareSize; p++){
        if(num1Arr[p] < num2Arr[p]){
            for(int i=0; i<num1Size; i++) printf("%d" , num1Arr[i]);
            printf(" ");
            for(int j=0; j<num2Size; j++) printf("%d" , num2Arr[j]);
            isCompared = true;
            break;
        }else if (num1Arr[p] > num2Arr[p]){
            for(int i=0; i<num2Size; i++) printf("%d" , num2Arr[i]);
            printf(" ");
            for(int j=0; j<num1Size; j++) printf("%d" , num1Arr[j]);
            isCompared = true;
            break;
        }   
    }
    if(isCompared == false){
        if(num1 < num2){
            for(int i=0; i<num1Size; i++) printf("%d" , num1Arr[i]);
            printf(" ");
            for(int j=0; j<num2Size; j++) printf("%d" , num2Arr[j]);
        }else{
            for(int i=0; i<num2Size; i++) printf("%d" , num2Arr[i]);
            printf(" ");
            for(int j=0; j<num1Size; j++) printf("%d" , num1Arr[j]);
        }
    }

    return 0;
}