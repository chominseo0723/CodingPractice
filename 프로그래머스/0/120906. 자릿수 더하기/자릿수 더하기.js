function solution(n) {
    let str = n.toString();
    let arr = [...str];
    var answer = 0;
    for(let i = 0; i<arr.length; i++){
        answer = answer + parseInt(arr[i]);
    }
    return answer;
}