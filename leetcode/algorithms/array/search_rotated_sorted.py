
class Solution:
    def __init__(self):
        nums = [int(x) for x in input().split()]
        target = int(input())
        print(self.search(nums,target))
    def search(self, nums: list[int], target:int) -> int:
        return self.binary_search(nums, target, 0 , len(nums)-1)
    def binary_search(self, nums:list[int], target:int, left, right) ->int:
        if left > right:
            return -1

        mid = left + (-left+right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if nums[mid] > target and nums[left] <= target:
                return self.binary_search(nums, target, left, mid - 1)
            else:
                return self.binary_search(nums, target, mid + 1 , right)
        else:
            if nums[mid] < target and nums[right] >= target:
                return self.binary_search(nums, target, mid + 1, right)
            else:
                return self.binary_search(nums, target , left, mid - 1)
        
                


Solution()
