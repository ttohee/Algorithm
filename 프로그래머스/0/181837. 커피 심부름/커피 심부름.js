function solution(order) {
    let latte = 0;
    let americano = 0;
    order.forEach((o) => {
        if(o.includes('latte')){
            latte ++;
        } else {
            americano ++;
        }
    })
    return latte*5000 + americano*4500;
}