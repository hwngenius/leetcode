# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        hash_table=set()
        while headA:
            hash_table.add(headA)
            headA=headA.next
        while headB:
            if headB in hash_table:
                return headB
            headB=headB.next
        return None