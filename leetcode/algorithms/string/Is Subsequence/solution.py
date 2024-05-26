class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        current_search_index = 0
        s_length = len(s)
        for i in range(0, len(t)):
            if t[i] == s[current_search_index]:
                current_search_index += 1
                if current_search_index == s_length:
                    return True
        return False

        
