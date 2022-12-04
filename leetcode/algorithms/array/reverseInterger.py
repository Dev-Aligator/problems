
class Solution():
    def __init__(self):
        x = int(input())
        print(self.reverse(x))
    def reverse(self, x:int) -> int:
        s = str(abs(x))
        reversed = int(s[::-1])
        if reversed > 2147483647:
            return 0
        return reversed if x > 0 else -reversed

Solution()
    
            
            
            
            

