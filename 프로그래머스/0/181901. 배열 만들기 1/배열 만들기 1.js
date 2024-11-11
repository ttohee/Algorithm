function solution(n, k) {
    let arr = [];
    let a = 0;
    for(let i = 1; i <= n; i++){
        if(i % k == 0){
            arr[a] = i;
            a++;
        }
    }
    return arr;
}