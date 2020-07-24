class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c not in paren_map:
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != paren_map[c]:
                return False
        return len(stack) == 0
