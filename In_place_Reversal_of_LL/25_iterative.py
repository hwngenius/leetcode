class Solution:
    def swapPairs(self, head: ListNode,k:int=2) -> ListNode:
        l=h=ListNode(0)
        stack=[]
        while head:
            index=0
            while head and index<k:
                stack.append(head)
                head=head.next
                index+=1
            if index==k:
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
# 56 ms
# , 在所有 Python3 提交中击败了
# 68.61%
# 的用户
# 内存消耗：
# 14.6 MB
# , 在所有 Python3 提交中击败了
# 7.69%
# 的用户