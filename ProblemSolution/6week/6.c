#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
int arr[101];
bool visited[101] ={false, };
int main(){
    // 8 : 인덱스 수열의 사이클 찾기
    // DFS 맛보기
    // 방문을 시작한다면 cycleCount ++;
    // cycle에 해당하는 모든 노드를 방문한다면 반복 탈출 
    int cycleCount = 0;
    int N;
    scanf("%d" , &N);
    for(int i = 0; i < N; i++) scanf("%d" , &arr[i]);
    
    for(int i = 0; i < N; i++){
        int node = i;
        if(!(visited[i])){
            cycleCount ++;
            while(!(visited[node])){
                visited[node] = true;
                node = arr[node];
            }
        }
    }
    printf("cycle count : %d" , cycleCount);
    
    return 0;
}