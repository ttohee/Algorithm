function solution(my_string) {
    let answer = [];
    let a = 0;
    for(i of my_string){
        if(isNaN(i) === false){
            answer.push(Number(i))
        }
    }
    answer.sort();
    return answer;
}