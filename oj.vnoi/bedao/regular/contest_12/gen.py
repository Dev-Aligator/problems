
class Solution():
    def __init__(self):
        n = int(input())
        remain = []
        for i in range(n):
            remain.append(input())
        self.gen(remain) 
    def gen(self, remain:list[str]):
        length = len(remain[0]) 
        possible_min = int("1" + "0"*(length-1))
        max_file = "9" * length
        min_file = max(possible_min, int(max(remain)))
        print(min_file)
        print(max_file)
        
Solution()
