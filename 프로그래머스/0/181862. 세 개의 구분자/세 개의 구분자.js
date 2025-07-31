function solution(myStr) {
    let processed = myStr.replace(/[abc]/g, ' ');
    let arr = processed.split(" ").filter(str=> str.length > 0);
    return arr.length > 0 ? arr : ["EMPTY"];
}