#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    int a = 0;
    int* answer = (int*)malloc(((n/2)+1) * sizeof(int));
    for(int i = 1; i <= n; i = i+2)
    {
        answer[a] = i;
        a++;
    }
    return answer;
}