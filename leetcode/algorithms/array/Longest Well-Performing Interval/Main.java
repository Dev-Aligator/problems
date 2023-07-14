import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
class Solution{
    public int longestWPI(int[] hours){
        if (hours.length == 0) return 0;
        Map<Integer, Integer> map = new HashMap<>();
        int sum = 0;
        int maxLen = 0;
        for(int i = 0 ; i  < hours.length; ++i){
            sum += ( hours[i] > 8) ? 1 : -1;

            if(!map.containsKey(sum)){
                map.put(sum, i);
            }

            if(sum > 0){
                maxLen = i +  1;
            }
            else if(map.containsKey(sum-1)){
                maxLen = Math.max(maxLen, i - map.get(sum-1));
            }
        }

        return maxLen;
    }
}


public class Main {
    public static void main(String[] args){
        int[] hours = new int[100];
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for(int i = 0 ; i < n ; ++i){
            hours[i] = scanner.nextInt();
        }

        scanner.close();
        System.out.print(new Solution().longestWPI(hours));
    }
}
