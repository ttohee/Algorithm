function solution(arr, queries) {
    for(let a of queries){
        for(let i = a[0]; i <= a[1]; i++){
            arr[i]++;
        }
    }
    return arr;
}