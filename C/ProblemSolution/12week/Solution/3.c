#include <stdio.h>
#include <string.h>
#define MAX 100

int isAnagram(char * str1 , char * str2 , int size1 , int size2);
int main(){
    // 아나그램 : 문자열의 순서를 재배열 하여 동일하게 만들수 있는지 판단

    char orgStr[MAX];
    char compareStr[MAX];
    scanf("%s" , orgStr);
    scanf("%s" , compareStr);
    
    strupr(orgStr);
    strupr(compareStr);

    int result = isAnagram(orgStr , compareStr , strlen(orgStr) , strlen(compareStr));
    if(result == 1) printf("yes");
    else printf("no");

    return 0;
}

int isAnagram(char * str1 , char * str2 , int size1 , int size2){
    int sameIndex = -1;
    int sameCnt = 0;
    if(size1 != size2) return 0;
    else{
        for(int i = 0; i < size1; i++){
            for(int j = 0; j < size1; j++){
                if(j == sameIndex) continue;
                else{
                    if(str1[i] == str2[j]){
                        sameCnt ++;
                        sameIndex = j;
                        break;
                    }
                }
            }
        }
    }
    if(sameCnt == size1) return 1;
    else return 0;
}