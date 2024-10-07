function solution(numer1, denom1, numer2, denom2) {
    let answer = [];
    let denom = denom1 * denom2;
    let numer = numer1 * denom2 + numer2 * denom1;
    let gcd = 0;
    
    // for(let i = 0; i < numer; i++){
    //     if(numer % i == 0 && denom % i == 0){
    //         gcd = i;
    //     }
    // }
    const getGcd = (a, b) => (a % b == 0 ? b : getGcd(b, a%b));
    gcd = getGcd(numer, denom);
    answer[0] = numer / gcd;
    answer[1] = denom / gcd;
    
    return answer;
}