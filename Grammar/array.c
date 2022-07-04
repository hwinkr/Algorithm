#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
   
    srand(time(NULL));
    printf("\n\n ##### 아빠는 대머리 게임 ##### \n\n");
    int answer;
    int treatment = rand() % 4 ;
    // 보여줄 병의 갯수
    int cntShowBottle = 0;
    int prevCntBottle = 0;

    for(int i=0; i<3; i++){
        int bottle[4] = {0 , 0 , 0 ,0};
        
        // 보여주는 병의 숫자를 이전 병의 숫자와 다르게함
        do{
            cntShowBottle = rand() % 2 + 2;
        } while(cntShowBottle == prevCntBottle); 
        
        prevCntBottle = cntShowBottle ;
        //보여줄 병 중에 발모제가 포함인가?
        int isIncluded = 0;
        printf(" > %d 번째 시도 : ", i + 1);
        //보여줄 병 종류 선택
        for(int j=0 ; j<cntShowBottle; j++){
            int randBottle = rand() % 4;
            if (bottle[randBottle] == 0) {
                bottle[randBottle] = 1;
                if (randBottle == treatment) isIncluded = 1;
            }else j--;
        } 
        for (int k=0; k<4; k++){
            if(bottle[k] == 1) printf("%d " , k+1);
        }
        printf(" 물약을 바릅니다.\n");
        if(isIncluded ==1) printf("성공! 머리가 났어요\n");
        else printf("실패! 머리가 나지 않았습니다..\n");

        printf("\n .... 계속 하려면 아무 키나 누르세요 ....");
        // 사용자가 어떤 키를 입력하기까지 기다림 
        getchar();
    }
    
    printf("발모제는 몇번 인가요 ? :");
    scanf("%d" , &answer);
    if(answer == treatment + 1) printf("\n정답! 발모제를 맞췄습니다\n");
    else printf("\n실패 ! 발모제는 %d번째 병이였습니다..." , treatment + 1);

    return 0;
}

 /*
    //C 언어의 문자열 끝에는 끝을 의미하는 NULL 문자 "\0" 이 포함 되어야함
    // 영어 : 1 byte
    // 한글 : 3 byte

    /*
    ASCII 코드 -> 7 bit , 0~127 개의 코드 
    a : 97 (문자 a 의 아스키 코드 값)
    */

    // char kor[] = "나도코딩";
    // printf("%s\n" , kor);
    // printf("%d\n" , sizeof(kor));

    // char str[7] = "coding";
    // printf("%s\n" , str);
    // printf("%d\n" , sizeof(str));

    // for(int i = 0 ; i < sizeof(str); i++) printf("%d\n" , str[i]);
    
    // char kor[] = "나도코딩";
    // printf("%s\n" , kor);
    // printf("%d\n" , sizeof(kor));
    // for (int i = 0 ; i < sizeof(kor); i ++) printf("%d\n",kor[i]); */