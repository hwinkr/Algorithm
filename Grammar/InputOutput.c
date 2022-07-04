// input , output
#include <stdio.h>

int main (){
    // 정수
    int age = 12;
    printf("%d\n" , age);
    // 실수 
    float weight = 46.5;
    printf("%.3f\n" , weight);
    double percent = 92.45;
    printf("%.2f\n" ,  percent);
    // 값 입출력
    // 1. 숫자
    int one , two ,three ;
    printf("3개의 정수를 입력하시오 : ");
    scanf("%d %d %d" , &one , &two , &three);
    printf("입력값은 %d %d %d 입니다" , one , two , three);
    // 2. 문자 , 문자열
    char c[256] ; 
    printf("문장을 입력 하시오 : ");
    scanf("%[^\n]s" , &c , sizeof(c));
    printf("입력 문장 : %s" , c);

    // 이름 , 나이 , 몸무게 , 키 , 범죄
    char name[256];
    printf("이름이 뭐죠? :");
    scanf("%s" , name ,sizeof(name));

    int age; 
    printf("나이 ? :");
    scanf("%d" , &age);

    float weight;
    printf("몸무게 ? : ");
    scanf("%f" , &weight);

    float height;
    printf("키? : ");
    scanf("%f" , &height);

    char crime[256];
    printf("범죄? : ");
    scanf("%s", crime , sizeof(crime));

    printf("\n\n -- 범죄자 정보 --- \n\n");
    printf(" 이름 : %s\n 나이 : %d\n 몸무게 : %f\n 키 : %f\n 범죄 : %s\n" ,name , age , weight , height , crime);
    return 0;
}