class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach=0
        for i in range(len(nums)):
            if i>max_reach:return False
            max_reach=max(max_reach,i+nums[i])
            if max_reach>=len(nums)-1:return True
        return False


# 行用时：
# 48 ms
# , 在所有 Python3 提交中击败了
# 74.23%
# 的用户
# 内存消耗：
# 16 MB
# , 在所有 Python3 提交中击败了
# 5.11%
# 的用户