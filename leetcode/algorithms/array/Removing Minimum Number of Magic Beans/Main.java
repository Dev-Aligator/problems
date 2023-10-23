import java.util.*;
import java.math.BigInteger;

class Solution{
    public long minimumRemoval(int[] beans) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        BigInteger sum = BigInteger.ZERO;
        BigInteger minimum = BigInteger.valueOf(Long.MAX_VALUE);
        int n = beans.length;

        for (int i = 0; i < n; ++i) {
            pq.add(beans[i]);
            sum = sum.add(BigInteger.valueOf(beans[i]));
        }

        while (n > 0) {
            int element = pq.poll();
            BigInteger elementN = BigInteger.valueOf(element).multiply(BigInteger.valueOf(n));
            minimum = minimum.min(sum.subtract(elementN));
            n--;
        }

        return minimum.longValue();
    }
}

public class Main {
    public static void main(String[] args){
        System.out.print(new Solution().minimumRemoval(new int[]{4,1,6,5}));
    }
}
