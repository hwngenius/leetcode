from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        nums.sort()
        def traceback(idx,tmp):
            ans.append(tmp)
            for i in range(idx,n):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                traceback(idx+1,tmp+[nums[i]])
        traceback(0,[])
        return ans
nums=[1,2,2]
print(Solution().subsetsWithDup(nums))

# 执行用时：
# 40 ms
# , 在所有 Python3 提交中击败了
# 74.86%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 5.67%
# 的用户