class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int):
        n1 = num1

        for i in range(1, 64):
            n1 -= num2
            if (n1 <= 0):
                return -1

            else:
                cnt = bin(n1)[2:].count("1")
                if (cnt <= i):
                    if n1 >= i:
                        return i
                    return -1
        return -1


print(Solution().makeTheIntegerZero(3,-2))
        
            
            
