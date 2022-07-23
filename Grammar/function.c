#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int getRandNumber(int level);
void showQuestion(int level , int num1, int num2);
void success();
void fail();

int main () {   
    srand(time(NULL));
    int inputNumber ;
    int answerCount = 0;
    for(int i = 1; i <= 5 ; i++){
        
        int num1 = getRandNumber(i);
        int num2 = getRandNumber(i);
        int answerNumber = num1 * num2;
        showQuestion(i , num1, num2);
        
        int inputNumber;
        scanf("%d" , &inputNumber);

        if(inputNumber == answerNumber) {
            answerCount ++;
            success(answerCount);
        } else if (inputNumber == -1){
            printf("문제풀이를 종료합니다.");
            exit(0);
        } else{
            fail();
            break;
        }
    }
    printf("당신은 5 개의 문제중 %d 개를 맞췄습니다.", answerCount);
}

int getRandNumber(int level){
    return rand() % (level * 10) + 1;
}

void showQuestion(int level , int num1, int num2) {
    printf("\n\n\n ##### 현재 비밀번호 퀴즈 level : %d #####\n" , level);
    printf("\n\t %d x %d 는 ? \n\n  " , num1 , num2);
    printf("########################################\n ");
    printf("\n정답을 입력하세요 (종료 : -1) >> ");
}   

void success(int answerCount) {
    if (answerCount < 5) printf("정답 입니다!\n다음 퀴즈로 이동\n");
    else {
        printf("\n\n\n##### 축하합니다! 당신은 모든 문제를 맞췄습니다! #####\n\n\n");
        exit(0);
    }
}

void fail() {
    printf("정답이 아닙니다!\n다음 퀴즈로 이동 할 수 없습니다.\n");
}