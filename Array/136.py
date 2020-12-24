class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set={}
        for num in nums:
            if num not in set:
                set[num]=1
                ans=num
            else:
                set[num]+=1
        for k in set:
            if set[k]==1:
                return k



# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 52 ms
# , 在所有 Python3 提交中击败了
# 53.20%
# 的用户
# 内存消耗：
# 16.6 MB
# , 在所有 Python3 提交中击败了
# 5.20%
# 的用户