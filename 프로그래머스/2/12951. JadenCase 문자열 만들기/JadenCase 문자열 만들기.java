class Solution {
    public String solution(String s) {
        String answer[] = s.split(" ", -1); // 문자 공백단위 분리
        
        for(int i=0; i<answer.length; i++){
            answer[i] = answer[i].toLowerCase();
            if(answer[i] != null && !answer[i].isEmpty()){
                answer[i] = answer[i].substring(0,1).toUpperCase() + answer[i].substring(1);
            }
            
        }
        return String.join(" ", answer);
    }
}