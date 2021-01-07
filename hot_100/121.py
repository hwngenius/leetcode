from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        current_min=1e9
        for p in prices:
            current_min=min(current_min,p)
            ans=max(ans,p-current_min)
        return ans


# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 78.71%
# 的用户
# 内存消耗：
# 15.4 MB
# , 在所有 Python3 提交中击败了
# 26.75%
# 的用户