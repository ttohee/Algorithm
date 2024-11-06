function solution(my_string, n) {
    return Array.from(my_string).reverse().slice(0, n).reverse().join('');
}