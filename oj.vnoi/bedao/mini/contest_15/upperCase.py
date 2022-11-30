
class Solution():
    def __init__(self):
        s = input().split()
        print(self.upperCase(s))
        
    def upperCase(self, s:list[str]) -> str:
        res = ""
        for x in s:
            res+=  x[0].upper() + x[1:]
            
        return res

Solution()
