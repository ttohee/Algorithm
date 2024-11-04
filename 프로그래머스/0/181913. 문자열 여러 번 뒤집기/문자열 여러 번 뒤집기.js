function solution(my_string, queries) {
    my_string = my_string.split("");
    for(let [s,e] of queries){
        let reP = my_string.slice(s, e+1).reverse();
        my_string.splice(s, e-s+1, ...reP);
    }
    return my_string.join('');
}