#include <stdio.h>
#define MAX 100
int calSum(int *ptr , int size , int a);
int main(){
    // 6 : 다항식 만들어 계산하기
    
    int arr[MAX];
    int n;
    scanf("%d" , &n);
    
    for(int i = 0; i < n * 2; i ++) scanf("%d" , &arr[i]);
    
    int x;
    scanf("%d" , &x);
    int answer = calSum(arr , n * 2 , x);
    printf("%d" , answer);

    return 0;
}

int calSum(int *ptr , int size , int a){
    int sum = 0;

    for(int i = 0; i < size; i += 2){
        int multiNum = 1;
        for(int j = 0; j < ptr[i + 1]; j++) multiNum *= a;
        sum += ptr[i] * multiNum;
    }
    
    return sum;
}