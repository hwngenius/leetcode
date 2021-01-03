from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target,rem=divmod(sum(nums),k)
        if rem:return False
        nums.sort()
        if nums[-1]>target:return False
        while nums and nums[-1]==target:
            k-=1
            nums.pop()
        def myfun(groups):
            if not nums:return True
            v=nums.pop()
            for i,group in enumerate(groups):
                if group+v<=target:
                    groups[i]+=v
                    if myfun(groups):return True
                    groups[i]-=v
            nums.append(v)
            return False
        return myfun(k*[0])


# 执行用时：
# 1404 ms
# , 在所有 Python3 提交中击败了
# 19.76%
# 的用户
# 内存消耗：
# 14.7 MB
# , 在所有 Python3 提交中击败了
# 26.09%
# 的用户