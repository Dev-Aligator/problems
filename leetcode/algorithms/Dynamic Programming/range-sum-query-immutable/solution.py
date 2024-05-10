class NumArray:
    def __init__(self, nums: list[int]):
        self.dp_sum = [0] 
        for i in range(len(nums)):
            self.dp_sum.append(self.dp_sum[-1] + nums[i])
    def sumRange(self, left: int, right: int) -> int:
        return self.dp_sum[right+1] - self.dp_sum[left]


obj = NumArray([-2,0,3,-5,2,-1])
print(obj.sumRange(0,5))
