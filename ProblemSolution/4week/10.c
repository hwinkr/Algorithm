#include <stdio.h>

int main(){
    int square1posx1 , square1posy1 , square1posx2, square1posy2;
    int square2posx1 , square2posy1 , square2posx2, square2posy2;
    int overlapX = 0 , overlapY = 0;
    scanf("%d %d %d %d", &square1posx1 , &square1posy1 , &square1posx2 , &square1posy2);
    scanf("%d %d %d %d", &square2posx1 , &square2posy1 , &square2posx2 , &square2posy2);

    if(square2posx2 < square2posx1){
        int tmp = square2posx2;
        square2posx2 = square2posx1;
        square2posx1 = tmp;
    }

    if(square2posy2 < square2posy1){
        int tmp = square2posy2;
        square2posy2 = square2posy1;
        square2posy1 = tmp;
    }

    // calculating overlapX
    for(int i = square2posx1; i <= square2posx2; i++){
        if(square1posx1 <= square1posx2){
            for(int j = square1posx1; j <= square1posx2; j++){
                if(i == j)
                    overlapX ++;
            }
        }else{
            for(int j = square1posx2; j <= square1posx1; j++){
                if(i == j)
                    overlapX ++;
            }   
        }
    }
    // calculating overlapX
    for(int i = square2posy1; i <= square2posy2; i++){
        if(square1posy1 <= square1posy2){
            for(int j = square1posy1; j <= square1posy2; j++){
                if(i == j)
                    overlapY ++;
            }
        }else{
            for(int j = square1posy2; j <= square1posy1; j++){
                if(i == j)
                    overlapY ++;
            }
        }
    }

    printf("overlapping area : %d" , (overlapX -1) * (overlapY -1));

    return 0;
}