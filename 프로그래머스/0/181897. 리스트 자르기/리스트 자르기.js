function solution(n, slicer, num_list) {
    let arr = [];
    function my_slice(a = 0, b = num_list.length, c = 1){
        for(let i = a; i < b; i += c){
            arr.push(num_list[i]);
        }
        return arr;
    }
    
    switch(n){
        case 1:
            arr = my_slice(0,slicer[1]+1);
            break;
        case 2:
            arr = my_slice(slicer[0]);
            break;
        case 3:
            arr = my_slice(slicer[0],slicer[1]+1);
            break;
        case 4:
            arr = my_slice(slicer[0],slicer[1]+1, slicer[2]);
    }
    return arr;
}