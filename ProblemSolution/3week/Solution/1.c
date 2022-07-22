#include <stdio.h>

int main (){
    // 1 : 홀수 합 짝수 합 같을때까지 더하기

    int num , oddSum = 0 , evenSum = 0 , numCount = 0;
    
    while(1){
        scanf("%d" , &num);
        if(num % 2) 
            oddSum += num;
        else 
            evenSum += num;

        numCount ++ ;

        if(oddSum == evenSum)
            break;
    }

    printf("using number count : %d" , numCount);
    
    return 0;
}