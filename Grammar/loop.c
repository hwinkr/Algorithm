// for , while
#include <stdio.h>

int main () {
    int b = 10;
    printf("%d\n" ,++b);
    // 먼저 출력하고 다음에 더함 그래서 뒤에 ++ 이 붙음
    printf("%d\n" ,b++);
    printf("%d\n" ,++b);

    for(int i=0; i<10; i++) printf("hello\n");
    
    int j = 0;
    while(j < 10){
       printf("hello %d \n" , j ++);
    }
    //구구단
    for (int i=2; i<=9; i++){
            printf("현재 구구단 : %d 단\n",i);
        for(int j=1; j<=9; j++){
            printf("%d * %d = %d\n" , i , j , i*j);
        }
    }   
    //피라미드
    for (int k=0; k<5; k++){
        for(int l = 5 - k -1 ; l>0 ; l--) printf(" ");
        for(int j=0; j<=k; j++) printf("*");
        printf("\n");
    }

    for (int m =0; m<5 ; m++){
        for(int i=m ; i < 5 - 1; i ++) printf(" ");
        for(int j=0 ; j <= m; j ++) printf("*");
        printf("\n");
    }

    int n ; 
    printf("피라미드 층수? : ");
    scanf("%d" , &n);

    for(int i = 0; i<n; i++){
        for(int j = n - i - 1; j > 0; j --) printf(" ");
        for(int k = 0; k < i * 2 + 1 ; k ++) printf("*");
        printf("\n");
    }
    return 0;
}