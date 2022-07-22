#include <stdio.h>

int main (){
    // 3 : 이항계수 구하기 북쪽 , 북서쪽 값의 합
    
    int n , k;
    int arr[101][101];
    scanf("%d %d" , &n , &k);

    for(int i = 0; i < n + 1; i++){
        arr[i][0] = 1;
        arr[i][i] = 1;
    }
    int limitY = 2;
    while(limitY < n){
        for(int i = 2; i < n + 1; i++){
            for(int j = 1; j < limitY; j++){
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1];
            }
            limitY ++;
        }
    }

    printf("%d" , arr[n][k]);

    return 0;
}