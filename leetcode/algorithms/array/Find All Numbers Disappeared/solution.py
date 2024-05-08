class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        
        for value in nums:
            indexing = abs(value) - 1
            if nums[indexing] > 0:
                nums[indexing] = -nums[indexing]
        return [index + 1 for index, value in enumerate(nums) if value > 0]


print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))


