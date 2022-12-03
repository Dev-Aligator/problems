
class Solution():
    def __init__(self):
        n = int(input())
        move = input()
        print(self.robot(move))
    def robot(self, move:str) -> int:
        hor = 0
        ver = 0
        for m in move:
            if m == "L":
                hor -= 1
            elif m == "R":
                hor += 1
            elif m == "U":
                ver += 1
            else:
                ver -= 1
        res = abs(hor) +abs(ver)
        if res % 2 == 1:
            return -1
        else:
            return int(res/2)

Solution()
