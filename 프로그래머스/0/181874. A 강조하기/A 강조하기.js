function solution(myString) {
    myString = myString.split('');
    for(let i = 0; i < myString.length; i++){
        if(myString[i] === 'a'){
            myString[i] = myString[i].toUpperCase();
        } else if (myString[i] <= 'Z' && myString[i] > 'A') {
            myString[i] = myString[i].toLowerCase();
        }
    }
    return myString.join('');
}