#include <stdio.h>

int main(){
    //7 : 0.5 중첩해서 더하고 빼기
    // int num;   
    // double initNum = 1;
    // double minusNum = 0.5;
    // double signMinusNum = -0.5;
    // int signNum = -1;
    // printf("정수 입력 : ");
    // scanf("%d" , &num);
    // for(int i=1; i<=num; i++){
    //     initNum -= minusNum ;
    //     minusNum *= signMinusNum;
    // }
    // printf("%lf" , initNum);

    //9 : 파이값 근사적으로 계산하기
    // int pinum;
    // int devideNum;
    // int signNum = 1;
    // double piInitNum = 4;
    // double piSum = 0;
    // printf("얼마만큼 근사적으로 파이값을 구할것인가요? :");
    // scanf("%d" , &pinum);

    // for(int i=0; i<pinum; i++){
    //     devideNum = (2 * i + 1) * signNum;
    //     piSum += 4/(double)devideNum;
    //     signNum *= -1;
    // }
    // printf("%lf" , piSum);

    //11 : 2로나눈 차례로 몫 출력하기
    // int targetNUm ;
    // int shareNum ; 
    // printf("숫자를 입력 하세요 : ");
    // scanf("%d" , &targetNUm);
    // //언제까지 반복?
    // //반복 횟수를 임의로 정할수 없는 경우 주어진 숫자를 사용
    // for (int i = targetNUm; i > 1; i/=2){
    //     shareNum = targetNUm / 2;
    //     targetNUm /= 2;
    //     printf("%d\n", shareNum);
    // }
    
    //12 : 10개의 정수를 입력받고 입력 받을때마다 현재까지 입력된 수의 평균 구하기
    // int getNum;
    // double sum = 0;
    // double average; 
    // for(int i=0; i<10; i++){
    //     printf("숫자를 입력 하세요 :");
    //     scanf("%d" , &getNum);
    //     sum += (double)getNum;
    //     average = sum / (i + 1);
    //     printf("지금까지 입력된 수의 평균은 %.2f 입니다.\n" , average);
    // }

    //13 : 이자율 r 복리 형태인 예금 잔고 출력
    // float totalMoney = 0;
    // float sumMoney = 0;
    // int currentMoney;
    // float r; 
    // printf("이자율 선택 : ");
    // scanf("%f" , &r);
    // for(int i=0; i<12; i++){
    //     printf("예금/출금 값을 입력하세요 :");
    //     scanf("%d" , &currentMoney);
    //     totalMoney = sumMoney + (float)currentMoney;
    //     sumMoney = totalMoney + (totalMoney * r) ;
    //     printf("%d 월 말일의 예금 잔고 : %lf\n" , i+1 , sumMoney);
    // }

    //14 : taylor 시리즈 sin x cos x 계산 입력값 x : radian
    double x ;
    printf("라디안 입력 : ");
    scanf("%lf",&x);

    double sinX = x;
    double cosX = 1;
    double x_radian = x ;

    int factNum = 1;
    int currentFactNum = 1;
    int signNum = 1;
    
    for(int i=1; i<=100; i++){
        factNum ++;
        x_radian *= x * signNum;
        currentFactNum = factNum * currentFactNum;
        cosX -= (x_radian/currentFactNum);

        x_radian *= x * signNum;
        factNum ++;
        currentFactNum = factNum * currentFactNum;
        sinX -= (x_radian/currentFactNum);

        signNum = -signNum;
    }
    printf("sinX : %lf\n" , sinX);
    printf("cosX : %lf\n" , cosX);
    return 0;
}