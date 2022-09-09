#include <stdio.h>
#define MAX 100

int check(int *ptr1 , int *ptr2);
int main(){
    // 5 : 사용자의 입력을 받아서 좌표 이동시키기
    // 현재까지 이동한 좌표의 궤적을 기억 , 새로운 이동궤적이 현재까지의 궤적과 교차하면 invalid move 출력
    int currentX = 0 , currentY = 0;
    int dir , length;
    int n = 0 , moveStorage[MAX][4] = {0, };
    int compareStorage[4];

    while(1){
        scanf("%d %d" , &dir , &length);
        if(dir == -1 && length == -1) break;
        else{
            compareStorage[0] = currentX;
            compareStorage[1] = currentY;
            if(dir == 0) currentY += length;
            else if(dir == 1) currentX += length;
            else if(dir == 2) currentY -= length;
            else if(dir == 3) currentX -= length;
            compareStorage[2] = currentX;
            compareStorage[3] = currentY;
        }  
        int intersectCnt = 0;
        if(n == 0){
            for(int i = 0; i < 4; i++) moveStorage[n][i] = compareStorage[i];
            printf("%d %d\n" , moveStorage[n][2] , moveStorage[n][3]);
            n ++;
        }else{
            for(int i = n - 1; i >= 0; i--){
                int result = check(moveStorage[i] , compareStorage);
                if(result == 1) intersectCnt ++;
            }
            if(intersectCnt == 0){
            for(int i = 0; i < 4; i++) moveStorage[n][i] = compareStorage[i];
                printf("%d %d\n" , moveStorage[n][2] , moveStorage[n][3]);
                n ++;
            }else {
                printf("invalid move\n");
                currentX = moveStorage[n - 1][2];
                currentY = moveStorage[n - 1][3];
            }
        } 
    }

    return 0;
}
// 교차할 경우 1 , 교차하지 않는 경우 0
int check(int *ptr1 , int *ptr2){
    int i = 0;
    int isIntersect = 0;
    // 비교하는 두 선분이 평행한 경우
    if((ptr1[i] == ptr1[i + 2]) && (ptr2[i] == ptr2[i + 2])){
        if(ptr1[i] != ptr2[i]) return 0;
        else{
            if(ptr1[i + 1] < ptr1[i + 3]){
                for(int m = ptr1[i + 1]; m <= ptr1[i + 3]; m++){
                    if(ptr2[i + 1] < ptr2[i + 3]){
                        for(int n = ptr2[i + 1]; n <= ptr2[i + 3]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }else{
                        for(int n = ptr2[i + 3]; n <= ptr2[i + 1]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }
                }
            }else{
                for(int m = ptr1[i + 3]; m <= ptr1[i + 1]; m ++){
                    if(ptr2[i + 1] < ptr2[i + 3]){
                        for(int n = ptr2[i + 1]; n <= ptr2[i + 3]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }else{
                        for(int n = ptr2[i + 3]; n <= ptr2[i + 1]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }
                }
            }
        }
    }else if((ptr1[i + 1] == ptr1[i + 3]) && (ptr2[i + 1] == ptr2[i + 3])){
        if(ptr1[i + 1] != ptr2[i + 1]) return 0;
        else{
            if(ptr1[i] < ptr1[i + 2]){
                for(int m = ptr1[i]; m <= ptr1[i + 2]; m++){
                    if(ptr2[i] < ptr2[i + 2]){
                        for(int n = ptr2[i]; n <= ptr2[i + 2]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }else{
                        for(int n = ptr2[i + 2]; n <= ptr2[i]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }
                }
            }else{
                for(int m = ptr1[i + 2]; m <= ptr1[i]; m ++){
                    if(ptr2[i] < ptr2[i + 2]){
                        for(int n = ptr2[i]; n <= ptr2[i + 2]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }else{
                        for(int n = ptr2[i + 2]; n <= ptr2[i]; n++){
                            if(m == n){
                                return 1;
                            }
                        }
                    }
                }
            }
        }
    }
    // 비교하는 두 선분이 수직인 경우
    if(ptr1[i] == ptr1[i + 2]){
        if(ptr1[i + 1] == ptr2[i + 1] || ptr1[i + 3] == ptr2[i + 1]) return 0;
        else{
            if(ptr2[i] < ptr2[i + 2]){
                if(ptr2[i + 2] < ptr1[i] || ptr2[i] > ptr1[i]) return 0;
                else return 1;
            }else{
                if(ptr2[i] < ptr1[i] || ptr2[i + 2] > ptr1[i]) return 0;
                return 1;
            }
        }
    }else if(ptr1[i + 1] == ptr1[i + 3]){
        if(ptr1[i] == ptr2[i] || ptr1[i + 2] == ptr2[i]) return 0;
        else{
            if(ptr2[i + 1] < ptr1[i + 3]){
                if(ptr2[i + 3] < ptr1[i + 1] || ptr2[i + 1] > ptr2[i + 1]) return 0;
                else return 1;
            }else{
                if(ptr2[i + 1] < ptr1[i + 1] || ptr2[i + 3] > ptr2[i + 1]) return 0;
                else return 1;
            }
        }
    }
}