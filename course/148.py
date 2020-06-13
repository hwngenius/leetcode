class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        a,b=head,head.next
        while b and b.next:a,b=a.next,b.next.next
        mid=a.next
        a.next=None
        a,b= self.sortList(head),self.sortList(mid)
        ans=h=ListNode(0)
        while a and b:
            if a.val<b.val:
                h.next=a
                a=a.next
            else:
                h.next=b
                b=b.next
            h=h.next
        h.next= a if a else b
        return ans.next

head=ListNode(4)
head.next=ListNode(2)
head.next.next=ListNode(1)
head.next.next.next=ListNode(3)
print(Solution().sortList(head))