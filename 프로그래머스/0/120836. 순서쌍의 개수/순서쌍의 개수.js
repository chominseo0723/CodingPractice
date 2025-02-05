function solution(n) {
    let result = []
    let index = 1;
    
    while (index <= n){
        if(n % index === 0){
            result.push(index);
        }
        index++;
    }
    return result.length;
}
