// if , else
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand(time(NULL));
    int randNumber = rand() % 100 + 1;
    
    int count ;
    printf("원하는 시도 횟수를 입력하세요 : ");
    scanf("%d" , &count);

    int answerNumber ;
    while (1){
        printf("남은 시도 횟수 : %d\n" , count);

        printf("값을 입력하세요 : ");
        scanf("%d" , &answerNumber);

        if(answerNumber > randNumber) printf("DOWN!\n");
        else if (answerNumber < randNumber) printf("UP!\n");
        else {
            printf("정답!\n");
            break;
        }
        count--;
        if(count == 0 ){
            printf("아쉽지만 정답을 맞추지 못했습니다.\n");
            printf("정답은 %d 입니다" , randNumber);
        }
    }
    
    return 0;
}

   /* 
    // 숫자 맞히기 
    // 값을 입력하고 5번의 기회를 주고 up & down 을 맞춤
    int number;
    printf("숫자를 입력 하세요 :");
    scanf("%d" , &number);

    int count = 5;
    int answer;
    while(count > 0) {
        printf("남은 시도 횟수 : %d\n" , count);

        printf("숫자를 맞춰 보세요 : ");
        scanf("%d" , &answer);

        if (answer > number) printf("DOWN!\n");
        else if (answer < number) printf("UP!\n");
        else {
            printf("정답 입니다!");
            break;
        }
        count --;
    }

    for (int i=1; i<30; i++){
        printf("%d 번 학생은 발표를 준비하세요.\n" , i);
        if (i >= 6) {
            printf("나머지 학생은 집에 가세요 \n");
            break;
        }
    }
    // 7번 결석 , 7번 제외 6~10 발표 준비
    for (int i=1 ; i <=30 ; i++){
        if (i >= 6 && i <= 10){
            if(i == 7) {
                printf("%d 번 학생은 결석이니 제외하겠습니다.\n" , i);
                // 이후에 있는 문장을 실행하지 않고 바로 다음 i 로 넘어감
                continue;
            }
            printf("%d 번 학생은 발표를 준비\n" , i);
        }
    }
    
    printf("난수 초기화 이전 \n");
    for (int i = 0; i<10 ; i ++){
        printf("%d\n" , rand() % 10);
    }  
    // 난수 초기화
    srand(time(NULL));
    printf("난수 초기화 이후 \n");
    for (int i = 0; i<10 ; i ++){
        printf("%d\n" , rand() % 10);
    }        
    

    //switch
    //난수 초기화 (필수)
    srand(time(NULL));
    int i = rand() % 3;

    switch (i)
    {
    case 0 : 
        printf("가위\n");
        // 찾는 케이스가 하나 등장하면 출력후 switch 문을 종료 -> break;
        break;
    case 1 : 
        printf("바위\n");
        break;
    case 2 : 
        printf("보\n");
        break;
    default : 
        printf("몰라\n");
        break;
    }
*/
  