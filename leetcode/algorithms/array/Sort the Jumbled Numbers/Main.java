import java.util.*;
class Solution{
    public int[] sortJumbled(int[] mapping, int[] nums) {
        
        List<Integer> arr = new ArrayList<>();
		
		//Copying numbers to arraylist - O(N)
        for (int i = 0; i < nums.length; i++) {
            arr.add(nums[i]);
        }
        
		//sorting arraylist as per mapping using custom comparator - O(N log  N)
        Collections.sort(arr, new Comparator<Integer>() {
           public int compare(Integer a, Integer b) {
               
			   //evalute equivalent value after mapping
               int val1 = evaluate(a, mapping);
               int val2 = evaluate(b, mapping);
               
               return Integer.compare(val1, val2);
           } 
        });
		
		//pack up - O(N)
        for (int i = 0; i < nums.length; i++) {
            nums[i] = (int) arr.get(i);
        }
		
		//return
        return nums;
    }
    
	//evaluate number's value after mapping
    int evaluate(Integer num, int mapping[]) {
        String str = Integer.toString(num);
        StringBuilder val = new StringBuilder();
        
        for (int i =0 ; i < str.length(); i++) {
            val.append((mapping[str.charAt(i) - '0']));
        }
        
        return Integer.parseInt(val.toString());
    }
}

public class Main{
    public static void main(String[] args){
        int[] nums = {0,1,2,3,4,5,6,7,8,9};
        int[] mapping = {9,8,7,6,5,4,3,2,1,0};
        new Solution().sortJumbled(mapping, nums);
        for(int i = 0 ; i < nums.length; ++i){
            System.out.print(nums[i] + " ");
        }
    }
}