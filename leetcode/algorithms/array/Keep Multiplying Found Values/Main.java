import java.util.*;

class Solution {
    public int findFinalValue(int[] nums, int original) {
        
        Arrays.sort(nums);

        HashSet<Integer> set = new HashSet<>();

        for(int i = 0; i < nums.length; i++){

            set.add(nums[i]);

        }

        boolean valid = true;

        while (valid == true){

            if (set.contains(original) == true){

                valid = true;
                original = 2 * original;
                continue;

            }else{

                valid = false;

            }

        }

        return original;

    }
}


public class Main {
    public static void main(String[] args){
        System.out.print(new Solution().findFinalValue(new int[]{914,894,448,946,7,835,858,896,56,224,565,971,112,14,116,196,28}, 7));
    }
}
