function solution(my_string, is_suffix) {
    let arr = [];
    for(let i = 0; i < my_string.length; i++){
        arr[i] = my_string.slice(i);
    }
    return arr.includes(is_suffix)? 1:0;
}