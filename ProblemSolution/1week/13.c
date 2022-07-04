#include <stdio.h>

int main (){
    
    //13 : 이자율 r 복리 형태인 예금 잔고 출력
    float totalMoney = 0;
    float sumMoney = 0;
    int currentMoney;
    float r; 
    printf("이자율 선택 : ");
    scanf("%f" , &r);
    for(int i=0; i<12; i++){
        printf("예금/출금 값을 입력하세요 :");
        scanf("%d" , &currentMoney);
        totalMoney = sumMoney + (float)currentMoney;
        sumMoney = totalMoney + (totalMoney * r) ;
        printf("%d 월 말일의 예금 잔고 : %lf\n" , i+1 , sumMoney);
    }

    return 0;
}