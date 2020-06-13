# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        L = l
        forward = 0
        while l1 is not None and l2 is not None:
            t = l1.val + l2.val + forward
            add = t % 10
            forward = t // 10
            l.next = ListNode(0)
            l.next.val = add
            l1, l2 = l1.next, l2.next
            l = l.next

        while l1 is not None:
            t = l1.val + forward
            add = t % 10
            forward = t // 10
            l.next = ListNode(0)
            l.next.val = add
            l, l1 = l.next, l1.next
        while l2 is not None:
            t = l2.val + forward
            add = t % 10
            forward = t // 10
            l.next = ListNode(0)
            l.next.val = add
            l, l2 = l.next, l2.next
        if forward!=0:
            l.next=ListNode(forward)
        return L.next

l1=ListNode(1)
l2=ListNode(9)
l2.next=ListNode(9)

l = Solution().addTwoNumbers(l1, l2)
print(l)