import java.util.Scanner;
class Solution{
    public int maxProfit(int[] prices, int fee){
     int n = prices.length;
     int[] free = new int[n];
     int[] hold = new int[n];
    
    free[0] = 0;
    hold[0] = -prices[0];
    for(int i = 1 ; i < n ; ++i){
        free[i] = Math.max(free[i-1], hold[i-1] + prices[i] - fee);
        hold[i] = Math.max(hold[i-1], free[i-1] - prices[i]);
    }

    return free[n-1];
    
    }
}


public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] prices = new int[n];
        for(int i = 0 ; i < n ; ++i){
            prices[i] = scanner.nextInt();
        }

        int fee = scanner.nextInt();
        scanner.close();
        System.out.print(new Solution().maxProfit(prices, fee));
    }
}
