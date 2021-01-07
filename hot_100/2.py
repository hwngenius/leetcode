# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        t=ans=ListNode(0)
        add_num=0
        while l1 and l2:
            x=l1.val+l2.val+add_num
            if x!=0:
                add_num=x//10
            else:
                add_num=0
            val=x%10
            t.next=ListNode(val)
            t=t.next
            l1=l1.next
            l2=l2.next
        while l1:
            x=l1.val+add_num
            if x!=0:
                add_num=x//10
            else:
                add_num=0
            val=x%10
            t.next=ListNode(val)
            t=t.next
            l1=l1.next
        while l2:
            x=l2.val+add_num
            if x!=0:
                add_num=x//10
            else:
                add_num=0
            val=x%10
            t.next=ListNode(val)
            t=t.next
            l2=l2.next
        if add_num:
            t.next=ListNode(add_num)
        return ans.next


# 执行用时：
# 80 ms
# , 在所有 Python3 提交中击败了
# 58.85%
# 的用户
# 内存消耗：
# 14.8 MB
# , 在所有 Python3 提交中击败了
# 8.48%
# 的用户