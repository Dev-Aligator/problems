from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            i_value = abs(nums[i])
            if nums[i_value - 1] < 0:
                res.append(i_value)
            else:
                nums[i_value - 1] *= -1
        return res
print(Solution().findDuplicates([2,2]))
