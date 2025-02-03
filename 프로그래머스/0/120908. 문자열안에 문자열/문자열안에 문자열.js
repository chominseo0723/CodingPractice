function solution(str1, str2) {
    for(let i = 0; i<str1.length; i++){
        if(str1.includes(str2))
            return 1;
        else
            return 2;
    }
}