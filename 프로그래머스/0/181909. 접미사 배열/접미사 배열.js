function solution(my_string) {
    let arr = [];
    for(let i = 0; i < my_string.length; i++){
        arr[i] = my_string.slice(i);
    }
    return arr.sort();
}