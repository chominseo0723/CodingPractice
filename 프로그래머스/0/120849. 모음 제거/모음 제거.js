function solution(my_string) {
    var myString = [...my_string];
    var arr = ['a','e','i','o','u'];
    
    let answer = myString.filter(x => !arr.includes(x));
    
    return answer.join('');
}