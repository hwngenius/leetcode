class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = l = ListNode(0)
        plus = 0
        while l1 and l2:
            add = l1.val + l2.val + plus
            plus = add // 10
            add = add % 10
            l1.val = add
            l.next = l1
            l=l.next
            l1 = l1.next
            l2 = l2.next
        while l2:
            add = plus + l2.val
            plus = add // 10
            add %= 10
            l2.val = add
            l.next = l2
            l=l.next
            l2 = l2.next
        while l1:
            add = plus + l1.val
            plus = add // 10
            add %= 10
            l1.val = add
            l.next = l1
            l=l.next
            l1 = l1.next
        if plus != 0:
            l.next = ListNode(plus)

        return h.next


l1=ListNode(2)
# l1.next=ListNode(4)
# l1.next.next=ListNode(3)
l2=ListNode(8)
l2.next=ListNode(9)
l2.next.next=ListNode(9)
l=Solution().addTwoNumbers(l1,l2)
while l:
    print(l.val)
    l=l.next