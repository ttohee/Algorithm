function solution(my_string, s, e) {
    my_string = Array.from(my_string);
    let arr = my_string.slice(s,e+1).reverse();
    arr = arr.join('');
    my_string.splice(s, arr.length, arr);
    return my_string.join('');
}