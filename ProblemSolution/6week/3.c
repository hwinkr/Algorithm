#include <stdio.h>
#define MAX 100
int main(){
    // 3 : 선택정렬 알고리즘 
    int arr[MAX];
    int n = 0;
    int currentMAX = -1;
    int currentINDEX = -1;
    FILE * file = fopen("input3.txt" , "r");
    while(fscanf(file , "%d" , &arr[n]) != EOF) n ++;
    
    for(int i = n - 1; i > 0; i--){
        for(int j = 0; j <= i; j++){
            if(currentMAX < arr[j]){
                currentMAX = arr[j];
                currentINDEX = j;
            }
        }
        int tmp = arr[i];
        arr[i] = currentMAX;
        arr[currentINDEX] = tmp;
        currentMAX = -1;
    }  

    for(int i = 0; i < n; i++) printf("%d " ,arr[i]);

    return 0;
}