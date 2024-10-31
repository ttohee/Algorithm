function solution(array) {
    array = array.join('');
    array = Array.from(array);
    let answer = 0;
    array.map(function(element){
        if(element === '7'){
            return answer++;
        }
    })
    return answer;
}