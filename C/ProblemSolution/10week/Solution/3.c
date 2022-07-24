#include <stdio.h>
#include <stdbool.h>
#define MAX 100
int intersect(int * ptr1 , int * ptr2);
int main(){
    // 3 : 두 선분의 교차점을 x 좌표기준 오름차순으로 정렬해서 출력

    int n = 0 , arr[MAX][4];
    int k = 0 , locationArr[MAX];
    
    FILE * file = fopen("input3.txt" , "r");
    int N ;
    fscanf(file , "%d" , &N);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < 4; j++) fscanf(file , "%d" , &arr[i][j]);
    }

    for(int i = 0; i < N -1; i++){
        for(int j = i + 1; j < N; j++){
            int result = intersect(arr[i] , arr[j]);
            if(result == 1){
                if(arr[i][0] == arr[i][2]){
                    locationArr[k] = arr[i][0];
                    k++;
                    locationArr[k] = arr[j][1];
                    k++;
                }else if(arr[i][1] == arr[i][3]){
                    locationArr[k] = arr[j][0];
                    k++;
                    locationArr[k] = arr[i][1];
                    k++;
                }
            }
        }
    }

    for(int i = k - 2; i > 0; i -= 2){
        for(int j = 0; j < i; j += 2){
            if(locationArr[j + 2] < locationArr[j]){
                int tmp1 = locationArr[j + 2];
                locationArr[j + 2] = locationArr[j];
                locationArr[j] = tmp1;
                int tmp2 = locationArr[j + 3];
                locationArr[j + 3] = locationArr[j + 1];
                locationArr[j + 1] = tmp2;
            }else if(locationArr[j + 2] == locationArr[j]){
                if(locationArr[j + 3] < locationArr[j + 1]){
                    int tmp1 = locationArr[j + 2];
                    locationArr[j + 2] = locationArr[j];
                    locationArr[j] = tmp1;
                    int tmp2 = locationArr[j + 3];
                    locationArr[j + 3] = locationArr[j + 1];
                    locationArr[j + 1] = tmp2;
                }
            }
        }
    }

    for(int i = 0; i < k; i++){
        if(i % 2) printf("%d\n" , locationArr[i]);
        else printf("%d " , locationArr[i]);
    }

    return 0;
}

int intersect(int * ptr1 , int * ptr2){

    int i = 0;
    bool isIntersect1 = false;
    bool isIntersect2 = false;

    if(ptr1[i] == ptr1[i + 2] && ptr2[i] == ptr2[i + 2]) return 0;
    else if(ptr1[i + 1] == ptr1[i + 3] && ptr2[i + 1] == ptr2[i + 3]) return 0;
    else{
        if(ptr1[i] == ptr1[i + 2]){
            for(int m = ptr1[i + 1]; m <= ptr1[i + 3]; m++){
                if(m == ptr2[i + 1])isIntersect1 = true;
            }
            if(isIntersect1){
                for(int n = ptr2[i]; n <= ptr2[i + 2]; n++){
                        if(n == ptr1[i]) isIntersect2 = true;
                }
                if(isIntersect2) return 1;
                else return 0;
            }else return 0;
        }else if(ptr1[i + 1] == ptr1[i + 3]){
            for(int m = ptr1[i]; m <= ptr1[i + 2]; m++){
                if(m == ptr2[i]) isIntersect1 = true;
            }
            if(isIntersect1){
                for(int n = ptr2[i + 1]; n <= ptr2[i + 3]; n++){
                    if(n == ptr1[i + 1]) isIntersect2 = true;
                }
                if(isIntersect2) return 1;
                else return 0;
            }else return 0;
        }
    }
}