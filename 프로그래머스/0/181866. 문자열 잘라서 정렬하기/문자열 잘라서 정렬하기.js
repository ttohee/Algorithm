function solution(myString) {
    myString = myString.split("x").sort();
    myString = myString.filter((a) => a != "");
    return myString;
}