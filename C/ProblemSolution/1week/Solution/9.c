#include <stdio.h>

int main (){
    //9 : 파이값 근사적으로 계산하기

    int pi;
    int devideNum;
    int signNum = 1;
    double piInitNum = 4;
    double piSum = 0;

    printf("enter count :");
    scanf("%d" , &pi);

    for(int i=0; i<pi; i++){
        devideNum = (2 * i + 1) * signNum;
        piSum += 4/(double)devideNum;
        signNum *= -1;
    }
    printf("%lf" , piSum);

    return 0;
}