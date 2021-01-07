from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left,right=0,len(height)-1
        while left<right:
            product=min(height[left],height[right])*(right-left)
            ans=max(product,ans)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans


# 执行用时：
# 92 ms
# , 在所有 Python3 提交中击败了
# 22.66%
# 的用户
# 内存消耗：
# 16.2 MB
# , 在所有 Python3 提交中击败了
# 5.10%
# 的用户