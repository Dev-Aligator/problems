from functools import reduce
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n + 1):
            if (i != n):
                res ^= nums[i]
            res ^= i
        return res

