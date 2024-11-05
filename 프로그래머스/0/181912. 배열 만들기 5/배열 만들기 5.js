function solution(intStrs, k, s, l) {
    let box = [];
    let answer = [];
    let a = 0;
    let b = 0;
    for(let i = 0; i < intStrs.length; i++){
        box[a] = parseInt(intStrs[i].slice(s, s+l));
        a++;
    }
    for(let j = 0; j < box.length; j++){
        if(box[j] > k){
            answer[b] = box[j];
            b++;
        }
    }
    return answer;
}