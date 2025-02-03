function solution(n) {
    let answer = Math.sqrt(n)
    if(answer % 1 === 0){
        return 1;
    }
    else
        return 2;
}