#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
    // 7 : x,y 좌표 랜덤으로 증가 시키고 N에 닿으면 종료, 평균횟수 구하기
    
    int N , T = 1000;
    int total = 0;
    scanf("%d" , &N);
    srand((unsigned int)time(NULL));

    int x = 0 , y = 0 , count = 0;

    // direction : 0 is up , 1 is right , 2 is down , 3 is left -> clock direction
    for(int i = 0; i < T; i++){
        while(x < N && y < N && x > -N && y > -N){
            int direction = rand() % 4; // 0 ~ 4
            if(direction == 0)
                y ++;
            else if (direction == 1)
                x ++;
            else if (direction == 2)
                y --;
            else
                x --;
            count ++;
        }
        total += count;
        x = 0 , y = 0 , count = 0;
    }

    printf("average of try count : %d" , total / T);
    
    return 0;
}