class ListNode:
    def __init__(self,x):
        self.x=x
        self.next=None

class Solution:
    def reverseList(self,head:ListNode)->ListNode:
        if head is None or head.next is None:
            return head
        cur=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return cur
