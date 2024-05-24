import java.util.HashMap;
import java.util.Map;
class Solution{
    public int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> complements = new HashMap<>(); 
        for(int i =0; i < nums.length; ++i){
            if (complements.containsKey(nums[i])){
                return new int[]{complements.get(nums[i]), i};
            }
            complements.put(target - nums[i], i);
        }

        return null;
    }
}

public class TwoSum{
    public static void main(String[] args){
        int[] res = new Solution().twoSum(new int[]{2,7,11, 15}, 9);
        for (int i = 0 ; i < res.length; ++i){
            System.out.print(res[i] + " ");
        }
    }
}