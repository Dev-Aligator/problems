class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)
        dp_increasing = [0] * n
        dp_decreasing = [0] * n
        res = []
        for i in range(1, n):
            if security[i-1] >= security[i]:
                dp_decreasing[i] = dp_decreasing[i-1] + 1
        for i in range(n-2,-1, -1):
            if security[i+1] >= security[i]:
                dp_increasing[i] = dp_increasing[i+1] + 1

        for i in range(time, n - time):
            if dp_increasing[i] >= time and dp_decreasing[i] >= time:
                res.append(i)
        return res

print(Solution().goodDaysToRobBank([1,2,3,4,5,6], 2))


            
