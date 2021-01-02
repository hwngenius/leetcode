class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_map,t_map={},{}
        for i in range(len(s)):
            if s[i] not in s_map and t[i] not in t_map:
                s_map[s[i]]=t[i]
                t_map[t[i]]=s[i]
            elif s[i] in s_map and t[i] in t_map:
                if s_map[s[i]]==t[i] and t_map[t[i]]==s[i]:
                    continue
                else:
                    return False
            else:
                return False

        return True


# 执行用时：
# 56 ms
# , 在所有 Python3 提交中击败了
# 34.79%
# 的用户
# 内存消耗：
# 14.9 MB
# , 在所有 Python3 提交中击败了
# 13.21%
# 的用户