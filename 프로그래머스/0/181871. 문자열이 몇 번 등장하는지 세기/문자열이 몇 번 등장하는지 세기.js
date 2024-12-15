function solution(myString, pat) {
    let len = pat.length;
    let count = 0;
    for(let i = 0; i < myString.length; i++){
        if(myString.slice(i, i+len) == pat){
            count++;
        }
    }
    return count;
}