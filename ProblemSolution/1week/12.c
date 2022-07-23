#include <stdio.h>

int main (){
    
    //12 : 10개의 정수를 입력받고 입력 받을때마다 현재까지 입력된 수의 평균 구하기
    int getNum;
    double sum = 0;
    double average; 
    for(int i=0; i<10; i++){
        printf("숫자를 입력 하세요 :");
        scanf("%d" , &getNum);
        sum += (double)getNum;
        average = sum / (i + 1);
        printf("지금까지 입력된 수의 평균은 %.2f 입니다.\n" , average);
    }
    return 0;
}