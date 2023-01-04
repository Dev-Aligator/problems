
class Solution{
    public int getNext(int n){
        int sqares_sum = 0;
        while(n > 0){
            int d = n % 10;
            sqares_sum += d*d;
            n /= 10;
        }
        return sqares_sum;
    }
    
    public boolean isHappy(int n){
        int slowRunner = n;
        int fastRunner = getNext(n);
        while (fastRunner != 1 && slowRunner != fastRunner){
            slowRunner = getNext(slowRunner);
            fastRunner = getNext(getNext(fastRunner));
        }
        return fastRunner == 1;
    }
}


