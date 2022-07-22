#include <stdio.h>

int main (){
     //7 : 0.5 중첩해서 더하고 빼기

    int num;   
    double initNum = 1;
    double minusNum = 0.5;
    double signMinusNum = -0.5;
    int signNum = -1;
    
    printf("정수 입력 : ");
    scanf("%d" , &num);
    
    for(int i=1; i<=num; i++){
        initNum -= minusNum ;
        minusNum *= signMinusNum;
    }
    printf("%lf" , initNum);

    return 0;
}