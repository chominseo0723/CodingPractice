function solution(arr) {
    let result = 1;
    for(let i = 0; i<arr.length; i++){
        result = lcm(result, arr[i])
    }
    return result;
}

function gcd(a, b) {
  return b === 0 ? a : gcd(b, a % b);
}

function lcm(a, b) {
  return (a * b) / gcd(a, b);
}
