import sys
class Solution():
    def threeSumCloset(self, nums: list[int], target:int) ->int:
        # -4 -1 1 2
        nums.sort()
        closet = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n):
            low = i +1
            high = n - 1
            while low < high:

                sum = nums[i] + nums[low] + nums[high]
                if sum == target:
                    return sum
                if abs(sum-target) < abs(closet - target):
                    closet = sum
                if sum > target:
                    high -= 1
                elif sum < target:
                    low += 1
                else:
                    return 0
        return closet

print(Solution().threeSumCloset([int(x) for x in input().split()], int(input())))
                
                
            

