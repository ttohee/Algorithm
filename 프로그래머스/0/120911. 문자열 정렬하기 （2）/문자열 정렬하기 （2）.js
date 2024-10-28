function solution(my_string) {
    my_string = my_string.toLowerCase();
    my_string = Array.from(my_string);
    my_string = my_string.sort();
    my_string = my_string.join('');
    return my_string;
}