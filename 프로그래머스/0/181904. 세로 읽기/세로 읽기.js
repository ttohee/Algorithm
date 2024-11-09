function solution(my_string, m, c) {
    my_string = Array.from(my_string);
    let answer = [];
    let a = 0;
    for(let i = 0; i < my_string.length; i += m){
        answer[a] = my_string[i + c-1];
        a++;
    }
    return answer.join('');
}