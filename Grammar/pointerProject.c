#include <stdio.h>
#include <time.h>
#include <stdlib.h>
// ### pointer project
// 물고기 6마리 어항이 사막에 있다 사막은 너무 더워서 물이 빨리 증발
// 물이 다 증발하기전에 어항에 물을 줘서 물고기를 계속 살려야함
// 레벨이 올라갈수록 물이 증발 하는 속도가 빨라짐.

// 전역변수 설정
int level;
int arrFish[6];
int *cursor; // 현재 물을 주고있는 어항을 가르킴

void initData();
void printFishes();
void decreaseWater();
int isFishAlive();

int main (){
    long startTime = 0; 
    // 게임을 진행하고 있는 총 시간
    long totalElapsedTime = 0;
    // 최근에 물을 주는데 걸린 시간 물을 빨리 증발 시키는 기준
    long prevElapsedTime = 0; 
    int num;
    // 게임 데이터 초기화 -> level 1  + 어항의 물을 다시 100
    initData(); 
    
    cursor = arrFish; // 배열과 똑같이 활용 가능 cursor[0] , cursor[1], ...
    // int * cursor = &arrFish[0];
    startTime = clock();
    while(1){
        printFishes();
        printf("몇번 어항에 물을 주시겠어요? : ");
        scanf("%d" , &num);
        if (num < 1 || num > 6){
            printf("입력값이 잘못 되었습니다\n");
            continue;
        }
        
        totalElapsedTime = (clock() - startTime) / CLOCKS_PER_SEC;
        printf("총 경과 시간 : %ld\n" , totalElapsedTime);
        
        prevElapsedTime = totalElapsedTime - prevElapsedTime;
        printf("직전 경과 시간 : %ld\n" , prevElapsedTime);

        decreaseWater(prevElapsedTime);    
        // 입력한 어항에 물을 준다
        // 어항에 물이 없다면 물을 주지 않도록
        if (cursor[num-1] == 0 ) printf("%d번 물고기는 이미 죽었습니다...물을 줄수 없습니다\n", num);
        else if (cursor[num-1] < 100 ) {
            printf("%d번 어항에 물을 줍니다...\n" , num);
            cursor[num -1] += 5;
        }
        // 레벨업? 20초를 버티면 다음 level 로 넘어가도록
        if (totalElapsedTime / 15 > level -1) {
            printf(" *** 축! 레벨업! 기존 %d 레벨에서 %d 레벨로 상승했습니다! ***\n" , level , level +1);
            level ++ ;
            if(level == 5 ) {
                printf(" *** 축! 물고기를 1마리 이상 살렸습니다. 맛있는 식사를 할 수 있습니다! ***\n");
                exit(0);
            }
        }
 
        if (isFishAlive() == 0) {
            printf(" ... 모든 물고기가 사망했습니다 ... 게임을 종료합니다.\n");
            exit(0);
        } else printf(" !!! 아직 물고기가 살아 있어요 !!! 화이팅 !!\n");

        prevElapsedTime = totalElapsedTime ;
    }
    return 0;
}

void initData() {
    level = 1;
    for (int i=0; i<6; i++) arrFish[i] = 100 ; // 어항의 물 높이
} 

void printFishes(){
    printf("%3d번 %3d번 %3d번 %3d번 %3d번 %3d번\n" , 1,2,3,4,5,6);
    for(int i=0; i<6; i++) printf(" %4d ", arrFish[i]);
    printf("\n");
}

void decreaseWater(long prevElapsedTime) {
    for (int i=0; i<6; i++){
        arrFish[i] -= (level * 3 * (int)prevElapsedTime);
        if(arrFish[i] < 0) arrFish[i] = 0;
    }
}

int isFishAlive () {
    for(int i=0; i<6; i++){
        if(arrFish[i] > 0) return 1;
    }
    return 0;
}