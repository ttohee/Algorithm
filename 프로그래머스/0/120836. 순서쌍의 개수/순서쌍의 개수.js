function solution(n) {
    var answer = 0;
    for(let i = 0; i*i <= n; i++){
        if(n % i === 0){
            answer++;
            if(i !== n / i){
                answer++;
            }
        }
    }
    return answer;
}