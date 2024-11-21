function solution(arr) {
    let answer = [];
    let num1 = arr.indexOf(2);
    let num2 = arr.lastIndexOf(2);
    if(num1||num2){
        answer = arr.slice(num1, num2+1);
    }
    if(num1 == -1) {
        answer[0] = -1;
    }
    return answer;
}