
class Solution:
    def __init__(self):
        nums = [int(item) for item in input("Enter the array: ").split()]
        print(self.threeSum(nums))
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        if len(nums) <3:
            return res
        if nums[0] > 0:
            return res

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            low = i+ 1
            high = len(nums) - 1 
            target = -nums[i]
            
            while low < high:
                sum = nums[low] + nums[high]
                if sum > target:
                    high-=1
                elif sum < target:
                    low+=1
                else:
                    res.append([nums[i], nums[low], nums[high]])
                    last_low = nums[low]
                    last_high = nums[high]

                    while low < high and nums[low] == last_low:
                        low+=1
                    while low < high and nums[high] == last_high:
                        high-=1
            
        
        return res
Solution()

