#include <stdio.h>

int main () {
    // 3 : 두 정수의 최대 공약수 구하기 , 재귀함수 사용 X 

    int x , y ;
    int gcd ; 
    scanf("%d" , &x);
    scanf("%d" , &y);
    
    if(x < y){
        int tmp = y ; 
        y = x; 
        x = tmp;
    }

    while((x % y) != 0){
        int tmp = x % y;
        x = y;
        y = tmp;
    }
    
    gcd = y;
    
    printf("gcd : %d" , gcd);

    return 0;
}