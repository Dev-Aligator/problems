class Solution():
    def longestCommonPrefix(self, strs:list[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        
        minLen = len(min(strs, key = len))
        
        low = 1
        high = minLen
        
        while low <= high:
            middle = int((low + high)/2)
            if(self.isCommonPrefix(strs, middle)):
                low = middle + 1
            else:
                high = middle - 1
        return strs[0][: int((low+high)/2)]
    
    def isCommonPrefix(self, strs:list[str], n:int) -> bool:
        s = strs[0][0:n]
        for string in strs:
            if not string.startswith(s):
                return False
        return True
        
