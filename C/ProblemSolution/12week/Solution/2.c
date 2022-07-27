#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX 100

void sortStr(char * str , int size);
int main(){
    // 문자열 사전식 출력하기 , 아스키코드 오름차순 정렬

    char str[MAX];
    scanf("%s" , str);
  
    printf("%s\n" , str);

    sortStr(str , strlen(str));

    printf("%s\n" , str);

    return 0;
}

void sortStr(char * str , int size){
    for(int i = size - 1; i > 0 ; i --){
        for(int j = 0; j < i; j++){
            int strToNum1 = str[j] - '0';
            int strToNum2 = str[j + 1] - '0';
            if(strToNum2 < strToNum1){
                int tmp = str[j + 1];
                str[j + 1] = str[j];
                str[j] = tmp;
            }
        }
    }
}
