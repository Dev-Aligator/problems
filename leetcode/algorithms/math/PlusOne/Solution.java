class Solution {
    public static void main(String[] args){
        int[] digits = {9};
        printList(plusOne(digits));
    }

    public static int[] plusOne(int[] digits){
        int i = digits.length - 1;
        while( i >= 0){
            digits[i] += 1;
            if(digits[i] == 10){
                if(i == 0){
                    int n = digits.length;
                    digits = new int[n + 1];
                    digits[0] = 1;
                    for(int j = 1; j <= n ; ++j){
                        digits[j] = 0;
                    }

                    return digits;
                }
                else{

                    digits[i] = 0;
                    i -= 1;
                }
                
            }
            else{
                break;
            }
           
        }
        return digits;
    }

    public static void printList(int[] digits){
        for(int i = 0; i < digits.length; ++i){
            System.out.print(digits[i]);
        }
    }
}