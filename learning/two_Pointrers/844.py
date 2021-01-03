class Solution:
    def backspaceCompare(self, S: str, T: str):
        def handle_str(s: str):
            stack = []
            for c in s:
                if c == '#':
                    if len(stack) != 0:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(c for c in stack)

        return handle_str(S) == handle_str(T)


S = "y#fo##f"
T = "y#f#o##f"

print(Solution().backspaceCompare(S, T))
