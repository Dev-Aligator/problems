class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        mid_ele = sorted_nums[len(nums) // 2]
        moves = 0
        for num in nums:
            moves += abs(mid_ele - num)
        return moves

print(Solution().minMoves2([1,10,2,9]))
            
            

            
            
