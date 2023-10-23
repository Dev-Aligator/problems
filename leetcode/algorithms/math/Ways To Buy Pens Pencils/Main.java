import java.util.*;

class Solution {
    public long waysToBuyPensPencils(int total, int cost1, int cost2){
        long totalWays = 0;
        int maxPens = total / cost1;
        while(maxPens >= 0){
            int maxPencils = (total - maxPens * cost1) / cost2;
            totalWays += maxPencils + 1;
            maxPens--;
        }
        return totalWays;
    }
}
public class Main {
    public static void main(String[] args){
        System.out.println(new Solution().waysToBuyPensPencils(20,10,5));
    }
}
