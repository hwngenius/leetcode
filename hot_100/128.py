class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        hash_table=set(nums)
        ans=1
        for num in nums:
            tmp=0
            if num-1 not in hash_table:
                while num in hash_table:
                    num+=1
                    tmp+=1
            ans=max(ans,tmp)
        return ans