function solution(num, k) {
    var answer = 0;
    const str = String(num);
    const newArr = Array.from(str);
    let change = newArr.map(function(element){
        return Number(element);
    });
    if(change.includes(k)){
        answer = change.indexOf(k) + 1;
    } else {
        answer = -1;
    }
    return answer;
}