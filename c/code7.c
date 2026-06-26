#include<stdio.h>

int main(void)
{
    int i, j;
    int rows = 5;

    for (i = 1; i <= rows; i++) {
        for (j = 1; j <= i; j++) {
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}