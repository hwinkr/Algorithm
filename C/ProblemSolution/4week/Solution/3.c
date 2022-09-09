#include <stdio.h>

int main (){
    // 3: 0~N 의 좌표 출력
    // y 좌표가 짝수이면 x 좌표가 증가하는 순서대로 출력
    // y 좌표가 홀수이면 x 좌표가 감소하는 순서대로 출력
    int x , y;
    int N;
    scanf("%d" , &N);

    for(int i = 0; i <= N; i++){
        if(i % 2 == 0){
            for(int j = 0; j <= N; j++){
                x = j;
                y = i;
                printf("%d %d\n",x, y);
            }
        }else{
            for(int j = N; j >= 0; j--){
                x = j;
                y = i;
                printf("%d %d\n",x, y);
            }
        }
    }
    
    return 0;
}