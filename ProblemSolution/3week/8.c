#include <stdio.h>

int main(){
    // 8 : 세금 계산하기
    double salary;
    int taxSum = 0;
    scanf("%lf" , &salary); 
    if(salary <= 1200){
        taxSum += salary * 0.06 ; 
    }else{
        taxSum += 1200 * 0.06;
        if(salary <= 4600){
            taxSum += (salary - 1200) * 0.15;
        }else{
            taxSum += 3400 * 0.15;
            if(salary <= 8800){
                taxSum += (salary - 1200 - 3400) * 0.24;
            }else{
                taxSum += 4200 * 0.24;
                if(salary <= 15000){
                    taxSum += (salary - 1200 - 3400 - 4200) * 0.35;
                }else{
                    taxSum += 6200 * 0.35;
                    if(salary <= 50000){
                        taxSum += (salary - 1200 - 3400 - 4200 - 6200) * 0.38;
                    }else{
                        taxSum += 35000 * 0.38 + (salary - 1200 - 3400 - 4200 - 6200 - 35000) * 0.40;
                    }
                }
            }
        }
    }
    printf("세금 : %d\n" , taxSum);
    
    return 0;
}