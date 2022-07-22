#include <stdio.h>

int main(){
    // 7 : number of local minima , 직전에 입력된 정수보다 작거나 같고 , 다음에 입력된 정수보다도 작거나 같은 정수

    int minimaCount = 0;
    int prevNum , currentNum , inputNum ; 
    scanf("%d" , &prevNum);
    scanf("%d" , &currentNum);
    
    if(prevNum <= currentNum)
        minimaCount ++;

    while(1){
        scanf("%d" , &inputNum);
        if(inputNum == -1){
            if(currentNum <= prevNum)
                minimaCount ++;
            break;
        }
        if(currentNum <= prevNum && currentNum <= inputNum){
            minimaCount ++;
        }
        prevNum = currentNum;
        currentNum = inputNum;
    }
    
    printf("minima count : %d", minimaCount);

    return 0;
}