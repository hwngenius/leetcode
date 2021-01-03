class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        target,rem=divmod(total,2)
        if rem:return False
        def traceback(idx,n):
            if n==target:return True
            if idx < len(nums):
                if traceback(idx+1,n+nums[idx]): return True
                if traceback(idx+1,n):return True
            return False
        return traceback(0,0)


# out of time