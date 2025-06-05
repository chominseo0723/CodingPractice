import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Solution {
    public static int solution(String dartResult) {
        
        Pattern p = Pattern.compile("(\\d{1,2})([SDT])([*#]?)");
        Matcher m = p.matcher(dartResult);

    
        int total = 0;
        int prevScore = 0; 

     
        while (m.find()) {

            int base = Integer.parseInt(m.group(1));

            String bonus = m.group(2);
            if (bonus.equals("S")) {
                base = (int) Math.pow(base, 1);
            } 
            else if (bonus.equals("D")) {
                base = (int) Math.pow(base, 2);
            }
            else  base = (int) Math.pow(base, 3);
    
            String option = m.group(3);
            if (option.equals("*")) {
                base *= 2;
                total += prevScore;
            }
            else if (option.equals("#")) {
                base = -base;
            }
            
            total += base;
            prevScore = base;
        }
        return total;
    }
}