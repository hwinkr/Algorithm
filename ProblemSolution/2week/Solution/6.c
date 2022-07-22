#include <stdio.h>

int main (){
    // 6 : 두개의 날짜를 입력 받은 후 첫 번째 날짜가 더 이르면 -1 , 두 번째 날짜가 더 이르면 1 , 날짜가 동일하면 0 을 출력
    
    int year1 , month1 , day1;
    int year2 , month2, day2;

    for(int i=0; i<5; i++){
        printf("첫번째 날짜를 입력하세요 : ");
        scanf("%d %d %d" , &year1 , &month1 ,&day1);

        printf("두번째 날짜를 입력하세요 : ");
        scanf("%d %d %d" , &year2 , &month2 ,&day2);

        if (year1 < year2) printf("-1\n");
        else if (year1 == year2 && month1 < month2) printf("-1\n");
        else if (year1 == year2 && month1 == month2 && day1 < day2) printf("-1\n");
        else if (year1 == year2 && month1 == month2 && day1 == day2) printf("0\n");
        else printf("1\n");

    }
    
    return 0;
}