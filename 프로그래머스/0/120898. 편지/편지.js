function solution(message) {
    var answer = 0;
    var arr = [...message];
    
    for(let i = 0; i<arr.length; i++){
        answer++;
    }
    return answer * 2;
}