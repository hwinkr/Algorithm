#include <stdio.h>
//1, 3 , 5 , 7 ,8
//모든 문제에 대해 배열 , 중첩된 반목문 까지만 사용 가능
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