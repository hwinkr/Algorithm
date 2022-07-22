#include <stdio.h>
#include <stdlib.h>

int main(){
    // 6 : 순열 사이클 갯수 출력하기
    
    int testCount;
    scanf("%d" , &testCount);

    for(int i = 0; i < testCount; i++){
        int N;
        int cycleCount = 0;
        scanf("%d" , &N);

        int * arr = (int * )malloc(sizeof(int) * N + 1);
        int * visited = (int *)malloc(sizeof(int) * N + 1);

        for(int i = 1; i< N + 1; i++) scanf("%d" , &arr[i]);
        for(int i = 1; i < N + 1; i++) visited[i] = 0;

        for(int i = 1; i < N + 1; i++){
            int node = i;
            if(!(visited[i])){
                cycleCount ++;
                while(!visited[node]){
                    visited[node] = 1;
                    node = arr[node];
                }
            }
        }
        printf("%d\n" , cycleCount);
    } 

    return 0;
}