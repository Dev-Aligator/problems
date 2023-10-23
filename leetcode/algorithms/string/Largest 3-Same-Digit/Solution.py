class Solution:
    def largestGoodInteger(self, num: str) ->str:
        s = ""
        for i in range(len(num) - 2):
            if num[i] == num[i+1] and num[i] == num[i+2]:
                s = max(s, num[i])
        return s*3;

print(Solution().largestGoodInteger("42352338"))