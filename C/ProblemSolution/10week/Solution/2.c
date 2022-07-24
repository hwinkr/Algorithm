#include <stdio.h>
#include <stdbool.h>
#define MAX 100
int find(int *ptr , int endIndex);
void insert(int *ptr , int endIndex);
int main(){
    // 2 : 새로운값의 중복검사 + 오름차순 정렬
    
    int arr[MAX];
    int n = 0;
    while(1){
        scanf("%d" , &arr[n]);
        if(arr[n] == -1) break;
        else{
            int result = find(arr , n);
            if(result == -1){
                insert(arr, n);
                for(int i = 0; i <= n; i++) printf("%d " , arr[i]);
                n ++;
            }else{
                printf("duplicate entry : %d\n" , result);
            }
        }
    }
    
    return 0;
}

int find(int *ptr , int endIndex){
    bool isSame = false;
    int index = -1;

    for(int i = endIndex - 1; i >= 0; i--) {
        if(ptr[endIndex] == ptr[i]) {
            isSame = true;
            index = i;
            break;
        }
    }

    if(!isSame) return -1;
    else return index;
}

void insert(int * ptr , int endIndex){
    for(int i = endIndex; i > 0; i --){
        for(int j = 0; j < i; j++){
            if(ptr[j + 1] < ptr[j]){
                int tmp = ptr[j + 1];
                ptr[j + 1] = ptr[j];
                ptr[j] = tmp;
            }
        }
    }
}