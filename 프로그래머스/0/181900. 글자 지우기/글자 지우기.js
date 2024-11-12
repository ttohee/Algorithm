function solution(my_string, indices) {
    my_string = Array.from(my_string);
    for(const i of indices){
        my_string.splice(i, 1, null);
    }
    return my_string.join('');
}