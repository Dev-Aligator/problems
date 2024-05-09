import functools
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return functools.reduce(lambda x,y : x^y , nums)

Solution().singleNumber([2,2,1])
