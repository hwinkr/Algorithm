//12
#include <stdio.h>

int main (){
    // 11 : 3개의 좌표 각 좌표는 x or y 좌표가 같다
    // 2번째 좌표에서 3번째 좌표로 가는 방향을 출력
    int x1, y1;
    int x2, y2;
    int x3, y3;
    
    int straightCnt , uTurnCnt , rightCnt , leftCnt = 0;
    
        printf("첫번째 좌표를 입력 하세요 : ");
        scanf("%d %d" , &x1, &y1);

        printf("두번째 좌표를 입력 하세요 : ");
        scanf("%d %d" , &x2, &y2);

        printf("세번째 좌표를 입력 하세요 : ");
        scanf("%d %d" , &x3, &y3);

        //straight , right , left , u-turn
        if(x1 != x2 && y1 != y2 || x2 != x3 && y2 != y3) printf("input error");
        else{
            if(x1 == x2){
                if (y1 < y2){
                    if(x2 < x3) rightCnt =1;
                    else if(x2 > x3) leftCnt =1;
                    else if(y2 < y3) straightCnt =1;
                    else uTurnCnt =1;
                }else if (y1 > y2){
                    if(x2 < x3) leftCnt =1;
                    else if(x2 > x3) rightCnt =1;
                    else if(y2 < y3) uTurnCnt =1;
                    else straightCnt =1;
                }
            }else if(y1 == y2){
                if (x1 < x2){
                    if(y2 < y3) leftCnt =1;
                    else if(y2 > y3) rightCnt =1;
                    else if(x2 < x3) straightCnt =1;
                    else uTurnCnt =1;
                }else if(x1 > x2){
                    if(y2 < y3) rightCnt =1;
                    else if (y2 > y3) leftCnt =1;
                    else if (x2 < x3) uTurnCnt =1;
                    else straightCnt =1;
                }
            }
        }

        if(straightCnt == 1){
            printf("straight\n");
        }else if(uTurnCnt == 1){
            printf("u-turn\n");
        }else if(rightCnt == 1){
            printf("right\n");
        }else if(leftCnt ==1){
            printf("left\n");
        }
    return 0;
}