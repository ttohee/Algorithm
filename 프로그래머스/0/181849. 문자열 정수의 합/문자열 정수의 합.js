function solution(num_str) {
    let arr = num_str.split('');
    let sum = 0;
    
    arr.forEach((e)=>{
        let num = parseInt(e);
        sum += num;
    })
    
    return sum;
}