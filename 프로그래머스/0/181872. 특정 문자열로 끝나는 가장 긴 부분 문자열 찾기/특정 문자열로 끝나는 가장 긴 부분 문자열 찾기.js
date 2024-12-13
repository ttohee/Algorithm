function solution(myString, pat) {
    let answer = '';
    for(let i = 0; i < myString.length; i++){
        if(myString.slice(0, i+1).endsWith(pat)){
            answer = myString.slice(0, i+1);
        }
    }
    return answer;
}