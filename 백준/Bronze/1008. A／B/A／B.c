#include <stdio.h>

int main() {
    double a;
    scanf("%lf", &a);
    double b;
    scanf("%lf", &b);

    printf("%.20lf", a / b);
}