#include <stdio.h>
#define MAX 100
int main(){
    // 10 : 주식 최대의 이익 얻기
    int arr[MAX];
    int n = 0;
    int stockSum = 0;
    int currentPrice = 0;

    FILE * file = fopen("input2.txt" , "r");

    while(fscanf(file , "%d" , &arr[n]) != EOF) n ++;
    fclose(file);

    int i = 0;

    while(i < n){
        if(arr[i] < arr[i + 1]){
            currentPrice = arr[i];
            for(int j = i + 1; j < n; j ++){
                if(arr[j] > arr[j + 1]){
                    stockSum += arr[j] - currentPrice;
                    i = j + 1;
                    break;
                }else if (j == n - 1){
                    stockSum += arr[n - 1] - currentPrice;
                }
            }
        }
        i ++; 
    }
    printf("%d" , stockSum);
    return 0;
}
