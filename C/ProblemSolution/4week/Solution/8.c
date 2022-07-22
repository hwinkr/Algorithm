#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    // 8 : 1,000,000번 의 실험을 반복하여 6번 던져서 적어도 1이 한번 나오는것 , 12번 던져서 적어도 2번 나오는 확률 비교

    int T = 1000000 , case_one = 6 , case_two = 12;
    int case_one_count = 0, case_two_count = 0;
    int appear_one , appear_two = 0;
    srand((unsigned int)time(NULL));
    
    for(int i = 0; i < T; i++){
        for(int j = 0; j < case_one; j++){
            int diceNumber_one = rand() % 6 + 1;
            if(diceNumber_one == 1)
                appear_one ++;
        }
        if(appear_one >= 1) case_one_count ++;
        appear_one = 0;
        for(int k = 0; k < case_two; k ++){
            int diceNumber_two = rand() % 6 + 1;
            if(diceNumber_two == 1)
                appear_two ++;
        }
        if(appear_two >= 2) case_two_count ++;
        appear_two = 0;
    }

    printf("case 1 : %lf\n" , (double)case_one_count / T);
    printf("case 2 : %lf\n" , (double)case_two_count / T);
    
    return 0;
}