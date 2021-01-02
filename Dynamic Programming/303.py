class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=[0]
        for num in nums:
            self.nums.append(self.nums[-1]+num)


    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1]-self.nums[i]


# 执行用时：
# 64 ms
# , 在所有 Python3 提交中击败了
# 97.60%
# 的用户
# 内存消耗：
# 18 MB
# , 在所有 Python3 提交中击败了
# 9.86%
# 的用户