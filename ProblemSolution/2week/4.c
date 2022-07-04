#include <stdio.h>
// 모든 문제에 대하여 배열을 사용 할 수 없다.
int main (){
    //4 : 10개의 정수를 키보드로 부터 입력 받고 음이아닌 정수중 (>= 0)  최솟값을 출력하라.
    int getNum ;
    int minNum = 0;
    // 처음 값을 저장
    printf("정수를 입력하세요 : ");
    scanf("%d" , &getNum);
    minNum = getNum;
    // 9번 반복  1 + 9
    for(int i=0; i<9; i++){
        printf("정수를 입력하세요 : ");
        scanf("%d" , &getNum);
        if(getNum < minNum && getNum >= 0) minNum = getNum;
    }
    printf("음이아닌 정수중 가장 작은 값은 : %d", minNum);
    //6
    return 0;
}