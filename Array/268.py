class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n+1)//2
        for i in nums:
            total-=i

        return total



# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 95.22%
# 的用户
# 内存消耗：
# 15.7 MB
# , 在所有 Python3 提交中击败了
# 5.21%
# 的用户