class Solution {
    public int solution(int n) {
        int answer = n+1;
        
        while(true){
            int answerCount = Integer.bitCount(answer);
            int count = Integer.bitCount(n); // n의 2진수 결과나옴
            if(count == answerCount){
                break;
            }
            answer++;
        }   
        
        return answer;
    }
}