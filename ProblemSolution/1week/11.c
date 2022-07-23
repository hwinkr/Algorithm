#include <stdio.h>

int main (){
    
    //11 : 2로나눈 차례로 몫 출력하기
    int targetNUm ;
    int shareNum ; 
    printf("숫자를 입력 하세요 : ");
    scanf("%d" , &targetNUm);
    //언제까지 반복?
    //반복 횟수를 임의로 정할수 없는 경우 주어진 숫자를 사용
    for (int i = targetNUm; i > 1; i/=2){
        shareNum = targetNUm / 2;
        targetNUm /= 2;
        printf("%d\n", shareNum);
    }

    return 0;
}