#include <stdio.h>
// 임의의 두 구간이 겹치는 영역의 길이를 구하는 함수 작성
int lenofOverlap(int sa, int ta, int sb, int tb);
int main(){
    // 1 : 두 사각형 겹치는 면적 구하기
    // X 길이 구할때 호출 , Y 길이 구할때 호출 , 함수는 한번 생성하면 여러번 호출 가능

    int square1_x1 , square1_y1 , square1_x2 , square1_y2;
    int square2_x1 , square2_y1 , square2_x2 , square2_y2;
    scanf("%d %d %d %d" , &square1_x1 , &square1_y1 , &square1_x2 , &square1_y2);
    scanf("%d %d %d %d" , &square2_x1 , &square2_y1 , &square2_x2 , &square2_y2);

    int x = lenofOverlap(square1_x1 , square1_x2 , square2_x1 , square2_x2);
    int y = lenofOverlap(square1_y1 , square1_y2 , square2_y1 , square2_y2);

    printf("%d" , x * y);

    return 0;
}
int lenofOverlap(int sa , int ta , int sb , int tb){
    int overLapLen = 0;

    if(sa > ta){
        int tmp = sa;
        sa = ta;
        ta = tmp;
    }

    if(sb > tb){
        int tmp = sb;
        sb = tb;
        tb = tmp;
    }

    for(int i = sa; i <= ta; i ++){
        for(int j = sb; j <= tb; j ++){
            if(i == j) {
                overLapLen ++;
                break;
            }
        }
    }

    return overLapLen - 1;
}