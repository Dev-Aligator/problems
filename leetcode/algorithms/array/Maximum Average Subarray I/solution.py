from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = current_window = sum(nums[:k])
        for i in range(k, len(nums)):
            current_window += nums[i] - nums[i-k]
            res = max(res, current_window)
        return round(res / k, 5)
        
