#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string answer = gets("What's your name? ");
    printf("hello, %s\n", answer);
}