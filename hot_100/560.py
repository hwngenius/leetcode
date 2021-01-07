from typing import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        hash_table=defaultdict(int)
        hash_table[0]=1
        ans=0
        pre=0
        for num in nums:
            pre+=num
            if pre-k in hash_table:
                ans+=hash_table[pre-k]
            hash_table[pre]+=1
        return ans