#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    int i = sqrt(n);
    if(i*i == n)
    {
        answer = 1;
    } else {
        answer = 2;
    }
    return answer;
}