#include<Stdio.h>
int main()  
{
    int a,b,c;
    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);
    c = a * b;
    printf("The product is: %d", c); 
    return 0;
}