function solution(num_list) {
    let answer = 0;
    for(let i of num_list){
        if(i < 0){
            answer = num_list.indexOf(i);
            break;
        } else {
            answer = -1;
        }
    }
    return answer;
}