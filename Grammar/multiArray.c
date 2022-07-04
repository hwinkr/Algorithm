#include <stdio.h>
#define N 5
#define M 3
int main(){
    // int i ; ㅁ 메모리 공간을 한칸 차지 
    // int i[5] ; ㅁㅁㅁㅁㅁ 메모리 공간을 선언한 크기 만큼 차지 Data type 이 같은 데이터끼리 묶을수 있음
    int mArr[N][M];
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++) mArr[i][j] = i+10;
    }
    for(int i=0; i<N; i++){
        for(int j=0; j<M; j++) printf("%3d" , mArr[i][j]);
        printf("\n");    
    }
    // 두 행렬의 곱
    // m X n
    return 0;
}