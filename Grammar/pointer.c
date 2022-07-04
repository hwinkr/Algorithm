#include <stdio.h>
#define N 5
// C언어의 함수 선언 
// 1. main 함수 위에서 선언 + 구현
// 2. main 함수 위에서 선언 + main 함수 밑에서 구현
void swap_value (int a, int b);
void swap_addr (int * a , int * b);
void changeArr (int * ptr);
int main (){
    // 포인터
    // 변수 = 식별자 : 메모리공간에 값이 저장될때 , 그 메모리의 주소를 기억하기 위해 변수를 사용 변수를 사용해서 특정 값이 저장된 메모리 상의 주소를 식별 할 수 있다
    // 컴퓨터 공간상의 주소 
    // int = 4 byte (32 bit) 정수형 변수는 메모리 상에서 공간 4를 차지
    int f = 5;
    // 포인터 변수는 값이 저장된 메모리상의 주소를 가르킨다
    int * fPointer = &f;
    printf("%d %d\n" , fPointer , *fPointer);

    int a = 1;
    int b = 2;
    int c = 3;
    printf("a 의 주소 : %d , a의 값 : %d\n" , &a , a);
    printf("b 의 주소 : %d , b의 값 : %d\n" , &b , b);
    printf("c 의 주소 : %d , c의 값 : %d\n\n" , &c , c);


    printf("\n\n ##### 미션 수행중 ##### \n\n");
    int * pointer; // 포인터 변수
    pointer = &a;
    printf ("a의 주소 : %d , a의 값 : %d\n", pointer , *pointer);
    
    pointer = &b;
    printf ("b의 주소 : %d , b의 값 : %d\n", pointer , *pointer);

    pointer = &c;
    printf ("c의 주소 : %d , c의 값 : %d\n", pointer , *pointer);
    
    printf("\n\n ##### 곱하기 미션! ##### \n\n");
    // 포인터를 사용하면 값의 메모리 상 주소를 알수있고 , 포인터를 사용하여 그 메모리상의 주소에 찾아가서 값을 변경 할 수 있다

    pointer = &a;
    *pointer *= 3;
    printf ("a의 주소 : %d , a의 값 : %d\n" , pointer , * pointer);

    pointer = &b;
    *pointer *= 3;
    printf ("b의 주소 : %d , b의 값 : %d\n" , pointer , * pointer);

    pointer = &c;
    *pointer *= 3;
    printf ("c의 주소 : %d , c의 값 : %d\n" , pointer , * pointer);

    printf("\n\n ##### 스파이 포인터의 등장 ##### \n\n");

    int * spyPointer = pointer; // pointer = &c
    spyPointer = &a;
    *spyPointer -= 2;
    printf("%d %d\n" , spyPointer, *spyPointer);

    spyPointer = &b;
    *spyPointer -= 2;
    printf("%d %d\n" , spyPointer, *spyPointer);

    spyPointer = &c;
    *spyPointer -= 2;
    printf("%d %d\n" , spyPointer, *spyPointer);
    // 메모리상의 주소를 가르키는 포인터를 사용하여 값을 변경. 따라서 a , b , c 모든 값이 바뀜 
    printf("a 의 주소 : %d , a의 값 : %d\n" , &a , a);
    printf("b 의 주소 : %d , b의 값 : %d\n" , &b , b);
    printf("c 의 주소 : %d , c의 값 : %d\n\n" , &c , c);
    // pointer 도 하나의 변수이기 때문에 메모리상에서 공간을 차지함
    printf("pointer 변수의 주소 : %d\n", &pointer);
    printf("spyPointer 변수의 주소 : %d\n",  &spyPointer);
     
    int g = 10;
    int * gPointer = &g;
    *gPointer = 20;
    printf("g 의 값 : %d\n", g);

    // 배열과 포인터의 관계
    int arr[3] = {10 ,20 ,30};
    int * ptr = arr;   
    // 배열 arr 자체의 주소와 배열의 첫번째 인덱스 arr[0] 의 주소는 같다
    // 배열 인덱스 첫번째 주소가 곧 배열 자체의 주소를 가르킨다
    // 배열 자체가 포인터의 역할을 함 -> arr
    printf("arr의 주소 : %d\n" , arr);
    printf("arr[0]의 주소 : %d\n" , &arr[0]);
    // 메모리상에서 오른쪽으로 한칸 이동함 , 한칸이 4 byte를 차지하기 때문에 주소도 4 증가
    printf("arr[1]의 주소 : %d\n" , &arr[1]);
    printf("arr 자체의 주소가 가지는 실제 값 : %d\n" , *arr); // = arr[0]
    printf("arr[0] 의 값 : %d\n", arr[0]);

    for(int i = 0 ; i < 3; i ++) printf("배열 arr[%d]의 값 : %d\n", i , arr[i]);
    for(int i = 0 ; i < 3; i ++) printf("배열 arr[%d]의 주소 값 : %d\n", i , &arr[i]);

    for(int i = 0 ; i < 3; i ++) printf("포인터 ptr[%d]의 값 : %d\n", i , ptr[i]);
    for(int i = 0 ; i < 3; i ++) printf("포인터 배열 ptr[%d]의 주소 값 : %d\n", i , &ptr[i]);

    for(int i=0; i<3; i++) ptr[i] *= 20;
    for(int i = 0 ; i < 3; i ++) printf("배열 arr[%d]의 값 : %d\n", i , arr[i]);

    int numArr[N];
    for(int i=0; i<N; i++) numArr[i] = i + 10;
    printf("numArr 자체의 주소 : %d\n", numArr);
    printf("numArr 자체의 주소의 값 : %d\n", *numArr);
    printf("numArr[0]의 주소 : %d\n" , &numArr[0]);
    printf("numArr[1]의 주소 : %d\n" , &numArr[1]);
    for(int i=0; i<N; i++) printf("numArr[i]의 값 :%d , numArr[i]의 주소 :%d\n" , numArr[i], &numArr[i]);

    int *arrPointer = numArr;
    for (int i=0; i<N; i++) arrPointer[i] -= 5;
    for(int i=0; i<N; i++) printf("numArr[%d]의 값 : %d , numArr[%d]의 주소 :%d\n" ,i, numArr[i], i, &numArr[i]);
    for(int i=0; i<N; i++) printf("포인터 배열 arrPointer[%d]의 값 : %d , numArr[%d]의 주소 :%d\n" , i , arrPointer[i], i, &arrPointer[i]);

    //swap
    int a = 2 ;
    int b = 4;
    printf("\n\n ##### swap 이전 a 의 값 : %d / b 의 값 : %d ##### \n\n", a, b);
    printf("함수 밖 a 의 주소 : %d\n" , &a);
    printf("함수 밖 b 의 주소 : %d\n" , &b);
    // 값에 의한 복사 Call - by - value
    // 함수안의 메모리상의 값의 주소와 함수밖의 메모리상의 값의 주소가 다름
    swap_value(a , b);
    // 주소에 의한 복사 Call - by - address
    // 함수 안 , 함수 밖의 값의 메모리상 주소가 같음 함수안의 결과가 밖에도 반영
    swap_addr(&a , &b);
    printf("\n\n ##### swap 이후 a 의 값 : %d / b 의 값 : %d ##### \n\n", a, b);

    // 포인터로 배열 값 변경하기
    int newArr[3] = {10 , 20 , 30};
    printf ("%d\n" , newArr);
    printf ("%d\n" , &newArr[0]);
    changeArr(newArr);
    for (int i=0; i<3; i++) printf("newArr[%d] : %d \n" , i , newArr[i]);

    //scanf 에서 & 를 사용하는 이유
    int a; 
    printf ("값을 입력 하세요 :");
    scanf ("%d", &a); // 변수 a 가 가리키는 메모리상의 주소를 알아야지 값을 저장 할 수 있음. 값에 의한 전달은 값을 영구적으로 변경하지 못함

    return 0;
}

void swap_value (int a, int b) {
    int tmp = a ;
    a = b; 
    b = tmp;
    printf("\n\n(call by value) 함수 안 a 의 주소 : %d\n" , &a);
    printf("(call by value) 함수 안 b 의 주소 : %d\n" , &b);
}
// 값이 아닌 , 메모리 주소를 넘김 따라서 함수안에서 바뀐 값이 함수밖에도 적용 
void swap_addr (int * a , int * b){
    int tmp = * a;
    * a = * b;
    * b = tmp;
    printf("(call by address) 함수 안의 a 의 주소 : %d\n" , a);
    printf("(call by address) 함수 안의 b 의 주소 : %d\n" , b);
}
// int * ptr = arr
void changeArr (int * ptr){
    ptr[2] = 50;
}