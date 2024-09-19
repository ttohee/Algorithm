#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//97
char* solution(int age) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(sizeof(char)*4);
    sprintf(answer, "%d",age);
    int i;
    for(i = 0; i < strlen(answer); i++)
    {
        answer[i] = answer[i]+49;
    }
    answer[i] = NULL;
    return answer;
}