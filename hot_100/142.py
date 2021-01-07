# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        hash_table=set()
        while head:
            if head in hash_table:
                return head
            hash_table.add(head)
            head=head.next
        return None
