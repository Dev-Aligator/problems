import java.util.*;

class Solution{
    public int halveArray(int[] nums){
        Comparator<Double> descendingComparator = Comparator.reverseOrder();
        PriorityQueue<Double> pq = new PriorityQueue<>(descendingComparator);
        double halve = 0;
        for(int i = 0 ; i < nums.length; i++){
            pq.add((double)nums[i]);
            halve+= nums[i];
        }

        halve /= 2;
        double reduced = 0;
        int operations = 0;
        while(reduced < halve){
            double head = pq.poll() / 2;
            reduced += head;
            pq.add(head);
            operations++;
        }

        return operations;
    }
}

public class Main {
    public static void main(String[] args){
        System.out.println(new Solution().halveArray(new int[]{5,19,8,1}));
    }    
}
