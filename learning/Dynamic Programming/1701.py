class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n=len(customers)
        ans=0
        time=0
        for customer in customers:
            if time<customer[0]:
                time=customer[0]+customer[1]
                ans+=customer[1]
            else:
                time+=customer[1]
                ans+=time-customer[0]
        return ans/n

# 执行用时：
# 140 ms
# , 在所有 Python3 提交中击败了
# 63.75%
# 的用户
# 内存消耗：
# 40 MB
# , 在所有 Python3 提交中击败了
# 92.81%
# 的用户