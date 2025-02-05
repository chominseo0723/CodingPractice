function solution(my_string, letter) {
    var arr_my_string = [...my_string];
    var arr_letter = [...letter];
    
    let answer = arr_my_string.filter(x=> !arr_letter.includes(x));
    
    return answer.join('');
}