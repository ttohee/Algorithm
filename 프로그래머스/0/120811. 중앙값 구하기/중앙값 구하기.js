function solution(array) {
    array.sort(function compare(a,b){
        if(a>b) return 1;
        if(a<b) return -1;
        if(a===b) return 0;
    })
    let ind = Math.floor(array.length / 2);
    return array[ind];
}