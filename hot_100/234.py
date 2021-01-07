class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node:
                if not recursively_check(current_node.next):
                    return False
                if current_node.val!=self.front_pointer.val:
                    return False
                self.front_pointer=self.front_pointer.next
            return True

        return recursively_check()
