class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target<letters[0] or target>=letters[-1]: return letters[0]

        l,r=0,len(letters)-1
        while l<r:
            mid=(l+r)//2
            if letters[mid]<=target:
                l=mid+1
            else:
                r=mid
        return letters[l]



# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 124 ms
# , 在所有 Python3 提交中击败了
# 97.60%
# 的用户
# 内存消耗：
# 15.1 MB
# , 在所有 Python3 提交中击败了
# 5.40%
# 的用户