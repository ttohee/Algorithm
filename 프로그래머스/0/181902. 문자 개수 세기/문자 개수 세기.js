function solution(my_string) {
    my_string = Array.from(my_string);
    let arr = new Array(52).fill(0);
    for (let v of my_string){
        if(v == v.toLowerCase()){
            arr[v.charCodeAt() - 'a'.charCodeAt()+26]++;
        } else {
            arr[v.charCodeAt() - 'A'.charCodeAt()]++;
        }
    }
    return arr;
}