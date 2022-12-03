class Solution():
    def __init__(self):
        n = int(input())
        print(self.walk(n)) 
    def walk(self, n:int) -> int:
        if n == 1:
            return 0
        edge = 2
        while n % edge != 0 or edge**2 < n:
            edge += 1

        min_move = edge*2
        x = 1
        while x <= edge:
            if n % x == 0:
                y = int(n/x)
                min_move = min(min_move, x + y - 2)
                edge = y-1
            x += 1
        return min_move

Solution()
