from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] >= 0:
                break
            if abs(nums[left]) > abs(nums[right]):
                nums[left] = nums[left] ** 2
                nums.insert(right + 1, nums[left])
                nums.pop(0)
            else:
                nums[right] = nums[right] ** 2
            right -= 1

        for i in range(left, right + 1):
            nums[i] = nums[i] ** 2


        return nums
        
print(Solution().sortedSquares([-4,-1,0,3,10]))
