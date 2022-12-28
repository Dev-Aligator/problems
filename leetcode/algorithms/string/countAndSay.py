class Solution(object):
    def countAndSay(self, n):
        if n == 1: return "1"
        if n == 2: return "11"
        s = "11"
        while n-2  >0:
            s = self.count(s)
            n-=1
        return s
    
    def count(self,s):
        l = list(s)
        prev_item = l[0]
        count = 1
        say = ""
        for item in l[1:]:
            if item == prev_item:
                count += 1
            else:
                say += str(count) + prev_item
                count = 1
                prev_item = item
        say += str(count) + prev_item
        return say        
        
