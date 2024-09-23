#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int odd = 0;
    int even = 0;
    for(int i = 0; i < num_list_len; i++)
    {
        if(i % 2 == 0)
        {
            even += num_list[i];
        }
        else
        {
            odd += num_list[i];
        }
    }
    if(odd>even)return odd;
    else if(odd<=even) return even;
}