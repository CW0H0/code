#include <stdio.h>
#include <stdlib.h>

int calculate();

int main(){
    printf("欢迎来到我的世界!!\n");
    int age = 18;
    printf("你的年龄是%d岁\n",age);
    int a = 5;
    int b = 6;
    printf("a & b = %d\n", a & b);
    printf("a | b = %d\n", a | b);
    printf("a ^ b = %d\n", a ^ b);
    calculate();

    return 0;
}

int calculate(){
    float a = 10;
    int b = 20;
    printf("a + b = %f\n",  a + b);
    return 0;
}