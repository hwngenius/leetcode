class Solution:
    def isSubsquence(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        s_index, t_index = 0, 0
        while s_index < s_len:
            while t_index < t_len and s[s_index] != t[t_index]:
                t_index += 1
            if t_index >= t_len:
                return False
            s_index += 1
            t_index += 1
        return True


s="axc"
t="ahbgdc"
print(Solution().isSubsquence(s,t))
