#include <stdio.h>

int main() {
    int a, b;

    scanf("%d", &a);
    scanf("%d", &b);

    int hun = b / 100;
    b %= 100;
    int ten = b / 10;
    int one = b % 10;

    printf("%d\n", a * one);
    printf("%d\n", a * ten);
    printf("%d\n", a * hun);

    printf("%d", (a*one)+(a*ten*10)+(a*hun*100));
}