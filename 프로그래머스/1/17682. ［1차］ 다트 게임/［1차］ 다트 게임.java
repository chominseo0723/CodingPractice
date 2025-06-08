import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public int solution(String dartResult) {
      
        List<Integer> scores = new ArrayList<>();

     
        Pattern p = Pattern.compile("(\\d{1,2})([SDT])([*#]?)");
        Matcher m = p.matcher(dartResult);

        while (m.find()) {
            int baseScore = Integer.parseInt(m.group(1));
            char bonus = m.group(2).charAt(0);
            String option = m.group(3);

            int score = 0;
            switch (bonus) {
                case 'S': score = baseScore; 
                    break;
                case 'D': score = baseScore * baseScore; 
                    break;
                case 'T': score = baseScore * baseScore * baseScore;
                    break;
                default: break;
            }

            if ("*".equals(option)) {
                
                if (!scores.isEmpty()) {
                    int idx = scores.size() - 1;
                    scores.set(idx, scores.get(idx) * 2);
                }
                score *= 2;
                
            } else if ("#".equals(option)) 
            {
                score *= -1;
            }

         
            scores.add(score);
        }

    
        int total = 0;
        for (int s : scores) {
            total += s;
        }
        return total;
    }
}
