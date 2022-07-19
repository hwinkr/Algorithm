#include <stdio.h>
#define MAX 100
int main(){
    // 폭탄 찾기
    int N ;
    char mat[MAX][MAX];
    FILE * file = fopen("input2.txt" , "r");
    fscanf(file , "%d " , &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            fscanf(file , "%c " , &mat[i][j]);
        }
    }
    int answer = 0;
    // 1
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(mat[i][j] == '*') printf("* ");
            else{
                // 극혐...
                if(mat[i - 1][j - 1] == '*') answer ++;
                if(mat[i - 1][j] == '*') answer ++;
                if(mat[i - 1][j + 1] == '*') answer ++;
                if(mat[i][j + 1] == '*') answer ++;
                if(mat[i + 1][j + 1] == '*') answer ++;
                if(mat[i + 1][j] == '*') answer ++;
                if(mat[i + 1][j - 1] == '*') answer ++;
                if(mat[i][j - 1] == '*') answer ++;
                printf("%d ", answer);
                answer = 0;
            }
        }
        printf("\n");
    }
    printf("\n");
    //2
    int direction[][2] ={{-1 , -1} , {-1 , 0} , {-1 , 1} , {0 , 1} , {1 , 1} , {1 , 0} , {1 , -1} , {0 , -1}};
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(mat[i][j] == '*') printf("* ");
            else{
                for(int dir = 0 ; dir < 8; dir++){
                    int r = i + direction[dir][0];
                    int c = j + direction[dir][1];
                    if(r >= 0 && r < N && c >= 0 && c < N){
                        if(mat[r][c] == '*') answer ++;
                    }
                }
                printf("%d " , answer);
            }
            answer = 0;
        }
        printf("\n");
    }

    return 0;
}