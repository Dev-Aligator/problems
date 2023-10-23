import java.util.*;

class Solution {
    public int minimumCost(int[] cost){
        Arrays.sort(cost); 
        for (int i = 0, j = cost.length - 1; i < cost.length / 2;i++) {
            int tmp = cost[i];
            cost[i] = cost[j];
            cost[j] = tmp;
            j--;
        }



        int totalCost = 0;
        int discountTimes = cost.length / 3;
        for( int i = 0 ; i < discountTimes; i++){
            totalCost += cost[3*i + 1] + cost[3*i + 2];
        }

        for (int i = discountTimes * 3; i < cost.length; ++i ){
            totalCost += cost[i];
        }

        return totalCost;
    }
}
public class Main {
    public static void main(String[] args){
        System.out.print(new Solution().minimumCost(new int[]{3,3,3,1}));
    }
}
