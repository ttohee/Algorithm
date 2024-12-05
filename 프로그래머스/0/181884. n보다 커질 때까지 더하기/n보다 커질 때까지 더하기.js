function solution(numbers, n) {
    let sum = 0;
    let a = 0;
    while(sum<=n){
        sum += numbers[a];
        a++;
    }
    return sum;
}