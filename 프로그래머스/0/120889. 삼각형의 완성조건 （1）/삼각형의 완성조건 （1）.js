function solution(sides) {
    sides = Array.from(sides);
    sides.sort(function(a,b){
        if(a>b) return 1;
        if(a<b) return -1;
        if(a===b) return 0;
    })
    if(sides[2]<sides[0]+sides[1]) return 1;
    else return 2;
}