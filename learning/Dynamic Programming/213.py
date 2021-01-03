class Solution:
    def rob(self, nums: List[int]) -> int:
        def myfun(nums:List[int])->int:
            cur,pre=0,0
            for num in nums:
                cur,pre=max(pre+num,cur),cur
            return cur
        return max(myfun(nums[:-1]),myfun(nums[1:])) if len(nums)!=1 else nums[0]
# 执行用时：
# 36 ms
# , 在所有 Python3 提交中击败了
# 82.13%
# 的用户
# 内存消耗：
# 14.7 MB
# , 在所有 Python3 提交中击败了
# 15.21%
# 的用户