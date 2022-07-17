#include <stdio.h>
#include <stdbool.h>
#define MAX 100
int main (){
    // 1 : 키보드로부터 정수를 입력 받고 배열에 저장 후 출력
    // 입력 -1 이면 종료 , 중복된 정수이면 duplicate entry를 출력하고 배열에 저장하지 않는다.
    int arr[MAX];
    int i = 0;
    bool isSame = false;
    while(1){
        // 해결 순서
        // 정수 입력 -> 이미 존재하는지 판단 -> 새로운 정수이면 오름차순 정렬 -> 정렬 후 출력
        scanf("%d" , &arr[i]);
        if(arr[i] == -1){
            printf("프로그램 종료.");
            break;
        }else{
            for(int j = i - 1; j >= 0; j--){
                if(arr[j] == arr[i]){
                    isSame = true;
                }
            }
            if(!isSame){
                for(int m = 0; m < i ; m ++){
                    for(int n = m + 1; n <= i; n ++){
                        if(arr[n] < arr[m]){
                            int temp = arr[m];
                            arr[m] = arr[n];
                            arr[n] = temp;
                        }
                    }
                }
                for(int k = 0; k <= i ; k ++){
                    printf("%d ", arr[k]);
                }
                i ++;
            }else{
                printf("duplicate entry\n");
                isSame = false;
            }
        }
    }
    return 0;
}