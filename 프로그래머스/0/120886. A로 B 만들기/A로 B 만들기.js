function solution(before, after) {
    before = Array.from(before);
    after = Array.from(after);
    before = before.sort();
    after = after.sort();
    
    before = before.join('');
    after = after.join('');
    if(before.includes(after)) return 1;
    else return 0;
}