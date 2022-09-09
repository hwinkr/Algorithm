#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 100

void reverseStr(char * str , int size);
int main(){
    // 1 : 문자열 뒤집기
    
    char str[MAX];
    scanf("%s" , str);

    printf("%s\n" , str);

    reverseStr(str , strlen(str));

    printf("%s\n" , str);

    return 0;
}

void reverseStr(char * str , int size){
    int middle = size / 2;
    for(int i = 0; i < middle; i++){
        int tmp = str[i];
        str[i] = str[size - i - 1];
        str[size - i - 1] = tmp;
    }
}