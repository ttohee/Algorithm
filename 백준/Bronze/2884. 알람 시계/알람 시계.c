#include <stdio.h>

int main() {
    int h, m;
    scanf("%d %d", &h, &m);
    m -= 45;
    if(m < 0){
        if(h > 0){
            h--;
        } else if (h == 0){
            h = 24;
            h--;
        }
        m = 60 + m;
    }
    printf("%d %d", h, m);
}