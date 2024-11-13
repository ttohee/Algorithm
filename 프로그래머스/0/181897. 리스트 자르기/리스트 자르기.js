function solution(n, slicer, num_list) {
    let arr = [];
    function my_slice(a,b,c){
        for(let i = a; i <= b; i += c){
            arr.push(num_list[i]);
        }
        return arr;
    }
    
    switch(n){
        case 1:
            arr = num_list.slice(0,slicer[1]+1);
            break;
        case 2:
            arr = num_list.slice(slicer[0]);
            break;
        case 3:
            arr = num_list.slice(slicer[0],slicer[1]+1);
            break;
        case 4:
            arr = my_slice(slicer[0],slicer[1], slicer[2]);
    }
    return arr;
}