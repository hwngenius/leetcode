# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        ans=self.reverseList(head.next)
        head.next.next=head
        return ans