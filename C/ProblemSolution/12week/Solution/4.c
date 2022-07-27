#include <stdio.h>
#define MAX 100
int main(){
    // 텍스트파일 왼쪽 정렬하기
    // C 언어에서는 띄어쓰기도 문자 , 줄바꿈 문자도 문자
    // 
    FILE * file = fopen("input4.txt" , "r");
    int N;
    char str[MAX][MAX];
    fscanf(file , "%d" , &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            fscanf(file , "%c" , &str[i][j]);
        }
    }
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            printf("%c " , str[i][j]);
        }
        printf("\n");
    }
    return 0;
}