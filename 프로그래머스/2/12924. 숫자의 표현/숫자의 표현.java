class Solution {
   public int solution(int n) {
        int answer = 0;
        int start = 1;
        int end = 1;
        int sum = 1;

        while(start<=n){
            if(sum < n) {
                end ++;
                sum = sum + end;
            }
            else if(sum == n){
                answer++;
                sum = sum-start;
                start++;

            }
            else {
                sum = sum-start;
                start++;
            }
        }

        return answer;
   }
}