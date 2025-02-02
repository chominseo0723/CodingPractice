function solution(numbers) {
    let sum = 0;
    let answer = 0;
    for(var i = 0; i<numbers.length; i++){
        sum += (numbers[i]);
    }
    answer = sum / numbers.length;
    return answer.toFixed(1);
}