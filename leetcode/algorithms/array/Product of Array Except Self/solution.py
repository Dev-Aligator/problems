from typing import List
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        cumulative_right = 1
        for i in range(n-2, -1, -1):
            cumulative_right *= nums[i+1]
            res[i] *= cumulative_right

        return res

print(Solution().productExceptSelf([1,2,3,4]))
