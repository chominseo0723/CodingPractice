function solution(n, t) {
    var time = 0
    while(t !== time){
        n *= 2;
        time++;
    }
     return n;  
}