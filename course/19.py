# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a,b=head,head
        while n>0:
            b=b.next
            n-=1
        if b is None:
            return head.next
        while b.next is not None:
            a,b=a.next,b.next
        a.next=a.next.next

        return head
