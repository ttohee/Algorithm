function solution(my_string) {
    let str = my_string.split(" ");
    let answer = str.filter((a) => a != "");
    return answer;
}