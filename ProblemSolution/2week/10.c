//11,12
#include <stdio.h>
// 10 : polyLine 계산
int main (){
    int pointNum ;
    printf("점의 갯수를 입력 하세요 : ");
    scanf("%d" , &pointNum);

    int x , y;
    int currentX , currentY;

    printf("좌표를 입력하세요 : ");
    scanf("%d %d" , &x , &y);
  
    currentX = x;
    currentY = y;
    int correctCnt = 0;
    int polyLine = 0;

    for(int i=0; i<pointNum -1; i++){
        
        printf("좌표를 입력하세요 : ");
        scanf("%d %d" , &x , &y);

        if(currentX == x || currentY == y){
            correctCnt ++;
            if (currentX == x) polyLine += (y - currentY);
            else if(currentY == y) polyLine += (x - currentX);
        }
            
        currentX =x;
        currentY =y;
    }
    if(pointNum -1 == correctCnt) printf("polyLine : %d" , polyLine);
    else printf("input error");

    return 0;
}