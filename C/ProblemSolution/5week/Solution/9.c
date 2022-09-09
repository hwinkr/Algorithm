#include <stdio.h>
#include <stdlib.h>
#define MAX 100
int main(){
    // 9 : 파일 읽어와서 배열에 저장하고 리더 정수 배열에 저장하기
    // 리더 정수 : 자신보다 먼저나온 모든 정수들보다 크거나 같은 정수 , 첫번째 정수는 무조건 리더 
    
    // 파일 읽기
    int arr[MAX];
    int n = 0;
    FILE * file = fopen("input.txt" , "r");

    int leaderCount = 0;
    int biggerCount = 0;
    
    // 반복의 횟수가 정해져있지 않음 -> while 사용하는게 효율적
    while(fscanf(file , "%d" , &arr[n]) != EOF) n ++;
    fclose(file);
    
    int *leaderArr = (int *)malloc(sizeof(int) * n);
    leaderArr[0] = arr[0];
    leaderCount ++;
    int leaderIndex = 1;
    for(int i = 1; i < n; i++){
        for(int j = i-1; j >= 0; j--){
            if(arr[j] <= arr[i])
                biggerCount ++;
        }
        if(biggerCount == i){
            leaderCount ++ ;
            leaderArr[leaderIndex] = arr[i];
            leaderIndex ++;
        }
        biggerCount = 0;
    }

    printf("%d :" , leaderCount);

    for(int i = 0; i < leaderCount; i ++){
        if(leaderArr[i] >= 100)
            printf("%4d" , leaderArr[i]);
        else if(leaderArr[i] >= 10 && leaderArr[i] < 100){
            printf("%3d" , leaderArr[i]);
        }else{
            printf("%2d" , leaderArr[i]);
        }
    }

    return 0;
}