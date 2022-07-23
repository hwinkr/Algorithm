#include <stdio.h>
#include <stdlib.h>

int main(){
    // 7 : 겹치는 길이 가장 긴 두 구간 출력하기
    int MAX = 100;
    int *interval = (int *)malloc(sizeof(int) * MAX);
    FILE * file = fopen("input6.txt" , "r");
    int n = 0;
    while(fscanf(file , "%d" , &interval[n]) != EOF) n ++;

    int answerIndex1 = -1;
    int answerIndex2 = -1;

    int length = 0;
    int lengthMax = -1;

    for(int i = 0; i < n - 2; i += 2){
        // 겹치는지 확인
        if(interval[i + 1] < interval[i + 2]) continue;
        else{
            for(int j = i + 2; j < n; j += 2){
                for(int m = interval[i]; m <= interval[i + 1]; m ++){
                    for(int n = interval[j]; n <= interval[j + 1]; n ++){
                        if(m == n)
                            length ++;
                    }
                }
                if(lengthMax < length){
                    lengthMax = length;
                    answerIndex1 = i ; 
                    answerIndex2 = j ;
                }
                length = 0;
            }

        }
    }
    printf("%d %d\n", interval[answerIndex1] , interval[answerIndex1 + 1]);
    printf("%d %d\n", interval[answerIndex2] , interval[answerIndex2 + 1]);
    return 0;
}