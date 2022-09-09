#include <stdio.h>

int main(){
    //4 : 좌표의 합이 K 이하인 좌표를 출력
    //합이 동일한 경우 x 좌표를 증가시키는 방향으로 출력    
    int x , y;
    int K;
    scanf("%d" , &K);

    for(int currentSum = 0; currentSum <= K; currentSum++){
        for(int i = 0; i <= currentSum; i++){
            for(int j = 0; j<= currentSum; j++){
                x = i;
                y = j;
                if(x + y == currentSum)
                    printf("%d %d\n" ,x, y);
            }
        }
    }

    return 0;
}