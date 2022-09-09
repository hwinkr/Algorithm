#include <stdio.h>

int main(){
    //8 : 두 구간이 겹치는지 판단 

    int a , b , c , d;
    for(int i=0 ; i<5; i++){
        printf("구간1 을 입력 하세요 : ");
        scanf("%d %d" , &a , &b);
        printf("구간2 를 입력 하세요 : ");
        scanf("%d %d" , &c , &d);

        if(a>b || c > d) printf("input error\n");
        else{
            if (b<c || d<a) printf("No\n");
            else printf("Yes\n");
        }
    }
    
    return 0;
}