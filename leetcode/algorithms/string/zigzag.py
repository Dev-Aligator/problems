
class Solution():
    def __init__(self):
        s = input()
        numRows = int(input())
        print(self.convert(s, numRows))
    def convert(self, s: str , numRows:int) ->str:
        li = list(s)
        row = []
        for i in range(numRows):
            row.append("")
        while li:
            for i in range(numRows):
                if not li:
                    break
                row[i] += (li[0])
                li.pop(0)
            for i in reversed(range(1, numRows-1)):
                if not li:
                    break
                row[i] += (li[0])
                li.pop(0)
        res = ""
        for r in row:
            res += r;
        return res

Solution()


                
                
                
