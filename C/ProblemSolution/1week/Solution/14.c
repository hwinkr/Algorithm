#include <stdio.h>

int main (){
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
// 1week clear