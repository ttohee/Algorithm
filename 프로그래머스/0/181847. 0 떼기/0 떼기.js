function solution(n_str) {
    let arr = n_str.split('');
    let zero = 0
    let i = 0;
    while(arr[i] == 0){
        zero++;
        i++;
    }
    if(zero > 0){
        arr.splice(0, zero);
        return arr.join("");
    } else {
        return arr.join("");
    }
}