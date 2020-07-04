class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k==0:
            return head
        count=0
        h=head
        while h.next and count!=k:
            h=h.next
            count+=1
        if h.next is None and count==k-1:
            return head

        if h.next is None:
            k%=(count+1)
            if k==0:
                return head
            fast=head
            while k>0:
                fast=fast.next
                k-=1
            slow=head
            while fast.next:
                fast=fast.next
                slow=slow.next
            ans=slow.next
            slow.next=None
            fast.next=head
            return ans

        else:
            slow=head
            while h.next:
                h=h.next
                slow=slow.next
            ans =slow.next
            slow.next=None
            h.next=head
            return ans


head=h=ListNode(0)

head=Solution().rotateRight(head,99)
while head:
    print(head.val)
    head=head.next


# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 19.70%
# 的用户
# 内存消耗：
# 13.7 MB
# , 在所有 Python3 提交中击败了
# 12.50%
# 的用户