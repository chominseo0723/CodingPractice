function solution(numbers) {
    let max1 = Math.max(...numbers);
    numbers.splice(numbers.indexOf(max1), 1);
    let max2 = Math.max(...numbers);
    return max1 * max2;
}