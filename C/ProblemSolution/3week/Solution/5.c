#include <stdio.h>

int main(){
    // 5 : -1 입력 될때까지 저장한 정수중 , 가장 큰 수와 두번째로 큰 수를 출력 , -1 은 입력된 정수로 취급하지 않는다.
    
    int inputNum;
    int firstNum , secondNum;
    scanf("%d" , &firstNum);
    scanf("%d" , &secondNum);
    
    if(firstNum < secondNum){
        int tmp = secondNum;
        secondNum = firstNum;
        firstNum = tmp;
    }
    printf("first : %d\n" , firstNum);
    printf("second : %d\n" , secondNum);

    while(1){
        scanf("%d" , &inputNum);
        if(inputNum == -1)
            break;
        
        if(firstNum <= inputNum){
            secondNum = firstNum;
            firstNum = inputNum;
        }else if(firstNum >= inputNum && secondNum <= inputNum)
            secondNum = inputNum;
    }
    printf("first : %d\n" , firstNum);
    printf("second : %d\n" , secondNum);
    
    return 0;
}