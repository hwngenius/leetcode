class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def tracback(idx):
            if idx==len(nums):
                ans.append(nums[:])
            else:
                for i in range(idx,len(nums)):
                    nums[i],nums[idx]=nums[idx],nums[i]
                    tracback(idx+1)
                    nums[i],nums[idx]=nums[idx],nums[i]
        
        tracback(0)
        return ans

# 执行用时：
# 24 ms
# , 在所有 Python3 提交中击败了
# 99.91%
# 的用户
# 内存消耗：
# 15 MB
# , 在所有 Python3 提交中击败了
# 8.20%
# 的用户