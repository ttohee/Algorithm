function solution(rny_string) {
    rny_string = rny_string.split('');
    for(let i = 0; i < rny_string.length; i++){
        if(rny_string[i] == "m"){
            rny_string[i] = "rn";
        }
    }
    return rny_string.join('');
}