class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        if not (head and head.next):
            return head
        tmp=head.next
        cur=self.swapPairs(tmp.next)
        tmp.next=head
        head.next=cur
        return tmp