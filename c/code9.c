#include &lt;stdio.h&gt;

int main() {
    int rows = 5;
    for(int i = 1; i &lt;= rows; i++) {
        for(int j = 1; j &lt;= rows - i; j++) {
            printf(" ");
        }
        for(int j = 1; j &lt;= 2*i - 1; j++) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}