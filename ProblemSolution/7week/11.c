#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int main(){
    // 11 : 최대 하나의 0 을 1로 교체해서 만들수 있는 가장 긴 연속된 1의 갯수 출력
    int N ;
    scanf("%d" , &N);
    int * arr = (int *)malloc(sizeof(int) * N);
    for(int i = 0; i < N; i++) scanf("%d" , &arr[i]);
    int zeroCount = 0;
    int length = 0;
    int lengthMax = -1;
    // 0 을 1로 바꿀수 있는 횟수는 1번으로 제한한다.
    // 0 을 만날때마다 1로 바꾼다. 그리고 다시 0을 만난다면 길이를 저장하고 다음 인덱스로 넘어간다
    for(int i = 0; i < N - 1; i++){
        for(int j = i; j < N; j++){
            if(arr[j] == 1) length ++;
            else if(arr[j] == 0){
                zeroCount ++;
                if(zeroCount > 1) break;
                length ++;
            }
        }
        if(lengthMax < length) lengthMax = length;
        length = 0;
        zeroCount = 0;
    }

    printf("max of length : %d" , lengthMax);

    return 0;
}