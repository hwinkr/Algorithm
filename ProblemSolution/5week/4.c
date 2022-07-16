#include <stdio.h> 
#include <stdlib.h>
int main(){
    // 4 : 0 ~ 9 나온 횟수 구하기
    
    int N = 0;
    int arrSize = 0;
    scanf("%d" , &N);
    
    int arr[10] = {0, };

    while(N > 0){
        switch(N % 10){
            case 0 :
                arr[0]++;
                break;
            case 1 :
                arr[1]++;
                break;
            case 2 :
                arr[2]++;
                break;
            case 3 :
                arr[3]++;
                break;
            case 4 :
                arr[4]++;
                break;
            case 5 :
                arr[5]++;
                break;
            case 6 :
                arr[6]++;
                break;
            case 7 :
                arr[7]++;
                break;
            case 8 :
                arr[8]++;
                break;
            case 9 :
                arr[9]++;
                break;
            default : 
                break;
        }
        N /= 10;
    }
    for(int i = 0; i < 10; i++)
        printf("%2d" , arr[i]);

    return 0;
}