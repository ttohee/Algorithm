// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// int solution(const char* number) {
//     int answer = 0;
//     int i = 0;
//     int sum = 0;
//     while(*number[i] != NULL){
//         sum += *number[i];
//         i++;
//     }
//     answer = sum % 9;
//     return answer;
// }

#include <stdio.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* number) {
    int sum = 0;

    // 문자열을 끝까지 반복하면서 각 문자를 숫자로 변환하여 합산
    while (*number != '\0') {
        sum += *number - '0'; // 문자에서 숫자 값 추출
        number++; // 다음 문자로 이동
    }

    // 9로 나눈 나머지 계산
    return sum % 9;
}
