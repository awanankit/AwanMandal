#include <stdio.h>

int main(void)
{
    int marks[5];
    int i;
    int total = 0;
    double average;
    char grade;

    printf("Enter marks for 5 subjects (0-100):\n");
    for (i = 0; i < 5; i++) {
        if (scanf("%d", &marks[i]) != 1) {
            printf("Invalid input.\n");
            return 1;
        }
        if (marks[i] < 0 || marks[i] > 100) {
            printf("Marks must be between 0 and 100.\n");
            return 1;
        }
        total += marks[i];
    }

    average = total / 5.0;

    if (average >= 90)
        grade = 'A';
    else if (average >= 80)
        grade = 'B';
    else if (average >= 70)
        grade = 'C';
    else if (average >= 60)
        grade = 'D';
    else if (average >= 50)
        grade = 'E';
    else
        grade = 'F';

    printf("Total marks: %d\n", total);
    printf("Average marks: %.2f\n", average);
    printf("Grade: %c\n", grade);

    return 0;
}