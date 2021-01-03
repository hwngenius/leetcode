class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode,k:int=2) -> ListNode:
        if not (head and head.next):
            return head
        l=h=ListNode(0)
        stack=[]
        while head:
            index=0
            while head and index<k:
                stack.append(head)
                head=head.next
                index+=1
            if index==2:
                while stack:
                    l.next=stack.pop()
                    l=l.next
            else:
                for i in range(len(stack)):
                    l.next=stack[i]
                    l=l.next
            l.next=None
        return h.next



# 执行用时：
# 44 ms
# , 在所有 Python3 提交中击败了
# 50.76%
# 的用户
# 内存消耗：
# 13.6 MB
# , 在所有 Python3 提交中击败了
# 6.25%
# 的用户