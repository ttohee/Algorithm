#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// arr_len은 배열 arr의 길이입니다.
int solution(int arr[], size_t arr_len) {
    int answer = 0;
    bool isChanged = true;
    
    while(isChanged){
        isChanged = false;
        int temp[arr_len];
        
        for(int i = 0; i < arr_len; i++){
            temp[i] = arr[i];
            
            if(arr[i] >= 50 && arr[i] % 2 == 0){
                arr[i] /= 2;
            } else if (arr[i] < 50 && arr[i] % 2 != 0){
                arr[i] = arr[i] * 2 + 1;
            }
        }
        
        for(int i = 0; i < arr_len; i++){
            if(temp[i] != arr[i]){
                isChanged = true;
                break;
            }
        }
        if(isChanged){
            answer++;
        }
    }
    
    
    return answer;
}