function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let bridge = Array(bridge_length).fill(0);
    let totalWeight = 0;
    
    while(bridge.length > 0){
        time ++;
        totalWeight -= bridge.shift();
        
        if(truck_weights.length > 0){
            if(totalWeight + truck_weights[0] <= weight){
                const truck = truck_weights.shift();
                bridge.push(truck);
                totalWeight += truck;
            } else {
                bridge.push(0);
            }
        }
    }
    return time;
}