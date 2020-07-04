class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ans=odd_link=ListNode(-1)
        later_link=even_link=ListNode(-2)
        counter=1
        while head:
            if counter%2==1:
                odd_link.next=head
                odd_link=odd_link.next
            else:
                even_link.next=head
                even_link=even_link.next
            counter+=1
            head=head.next
        odd_link.next=None
        even_link.next=None
        odd_link.next=later_link.next
        return ans.next


# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 98.57%
# 的用户
# 内存消耗：
# 15.7 MB
# , 在所有 Python3 提交中击败了
# 14.29%
# 的用户