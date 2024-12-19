function solution(myString, pat) {
    myString = myString.split('');
    for(let i = 0; i < myString.length; i++){
        if(myString[i] == 'A'){
            myString[i] = 'B';
        } else {
            myString[i] = 'A';
        }
    }
    myString = myString.join('');
    let answer = myString.includes(pat) ? 1 : 0;
    return answer;
}