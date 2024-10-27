#include <stdio.h>
#include <stdlib.h>

int main(){
    int x = -1;
    if( x > 0){
        printf("x是正数\n");
    }else if ( x ==0 ){
        printf("x是零\n");
    }else{
        printf("x是负数\n");
    }
    //三元运算符
    int y = 1;
    y % 2 ==1 ? printf("y是奇数\n") : printf("y是偶数\n");
    return 0;
}