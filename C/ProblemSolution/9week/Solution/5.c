#include <stdio.h>
#define MAX 100

int compareLexicograph(int a, int b);
int main(){
    // 5 : 입력된 정수 사전식 출력하기
    
    FILE * file = fopen("input5.txt" , "r");
    int arr[MAX];
    int n = 0;
    while(fscanf(file , "%d" , &arr[n]) != EOF) n ++;
    fclose(file);
    
    for(int i = n - 1; i > 0; i--){
        for(int j = 0; j < i; j++){
            int result = compareLexicograph(arr[j] , arr[j + 1]);
            if(result == 1){
                int tmp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = tmp;
            }
        }
    }
    
    for(int i = 0; i < n; i++) printf("%d " ,arr[i]);

    return 0;
}

int compareLexicograph(int a, int b){
    
    if(a == b) return 0;
    else{
        int aStorage = a , bStorage = b;
        int a_size = 0 , b_size = 0;
        int aArr[MAX] = {0, }, bArr[MAX] = {0, };

        while(a > 0){
            a_size ++;
            a /= 10;
        }
        while(b > 0){
            b_size ++;
            b /= 10;
        }

        for(int i = a_size - 1; i >= 0; i--){
            aArr[i] = aStorage % 10;
            aStorage /= 10;
        }
        for(int j = b_size - 1; j >= 0; j--){
            bArr[j] = bStorage % 10;
            bStorage /= 10;
        } 

        int limit = a_size >= b_size ? b_size : a_size;
        int isCompare = 0;

        for(int i = 0; i < limit; i++){
            if(aArr[i] == bArr[i]) {
                continue;
            }else if(aArr[i] > bArr[i]){
                isCompare = 1;
                return 1;
            }else{
                isCompare = 1;
                return -1;
            }   
        }

        if(!isCompare){
            if(a_size < b_size) return -1;
            else return 1;
        }
    }
}