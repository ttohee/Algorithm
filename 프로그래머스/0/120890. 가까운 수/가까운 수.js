function solution(array, n) {
    array.sort((a, b) => a - b); // 숫자 순서대로 정렬
    let closest = array[0]; // 가장 가까운 숫자를 저장할 변수 초기화

    for (let num of array) {
        // 현재 숫자가 더 가까운 경우, closest 업데이트
        if (Math.abs(num - n) < Math.abs(closest - n)) {
            closest = num;
        }
    }
    return closest;
}
