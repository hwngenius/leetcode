# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        first=ListNode(0)
        second=ListNode(0)
        t1=first
        t2=second
        while head:
            if head.val<x:
                t1.next=head
                t1=t1.next
            else:
                t2.next=head
                t2=t2.next
            head=head.next
        t2.next=None
        t1.next=second.next
        return first.next

head=ListNode(1)
head.next=ListNode(4)
head.next.next=ListNode(3)
head.next.next.next=ListNode(2)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(2)
print(Solution().partition(head,3))