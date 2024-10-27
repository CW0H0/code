#include <stdio.h>
#include <string.h>

struct Student {  
    char name[20]; // 学生姓名  
    int age;       // 学生年龄  
    float score;   // 学生成绩  
};  
  
int main() {  
    struct Student stu1 = {"Alice", 20, 92.5}; // 定义并初始化结构体变量  
    printf("Name: %s, Age: %d, Score: %.2f\n", stu1.name, stu1.age, stu1.score); // 访问并打印结构体成员  
    return 0;  
}