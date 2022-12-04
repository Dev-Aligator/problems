
class Solution():
    def __init__(self):
        x,y = input().split()
        print(self.multiply(x, y))
    def multiply(self, num1:str, num2:str) -> str:
        return str(int(num1) * int(num2))
        
        
Solution()
