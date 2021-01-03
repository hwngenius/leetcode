class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:return []
        res=[]
        for num in nums:
            index=abs(num)-1
            if nums[index]>0:
                nums[index]*=-1
            
        for i in range(1,len(nums)+1):
            if nums[i-1]>0:
                res.append(i)
        return res


# 执行结果：
# 通过
# 显示详情
# 执行用时：
# 392 ms
# , 在所有 Python3 提交中击败了
# 89.84%
# 的用户
# 内存消耗：
# 22.7 MB
# , 在所有 Python3 提交中击败了
# 27.79%
# 的用户