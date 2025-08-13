function solution(num_list) {
    let list =  num_list.sort((a,b)=>a<b ? -1 : 1)
    list.splice(0, 5)
    return list
}