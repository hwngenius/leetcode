class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        t_len = len(t)
        s_len = len(s)
        t_count = collections.Counter(t)
        s_count = collections.Counter(s[0:t_len])
        for k,_ in t_count.items():
            if k not in s_count:
                s_count[k]=0
        ans_len = s_len + 1
        ans = ""

        def is_contain():
            for k, v in t_count.items():
                if v > s_count[k]:
                    return False
            return True

        left, right = 0, t_len - 1
        while right-left+1>=t_len:
            if left>0:
                s_count[s[left-1]]-=1
            while is_contain() is not True and right + 1 < s_len:
                right += 1
                if s[right] not in s_count:
                    s_count[s[right]] = 1
                else:
                    s_count[s[right]] += 1
            if is_contain():
                if ans_len>right-left+1:
                    ans_len=right-left+1
                    ans=s[left:left+ans_len]
            left+=1
        return ans

# 执行用时 :
# 692 ms
# , 在所有 Python3 提交中击败了
# 15.42%
# 的用户
# 内存消耗 :
# 13.8 MB
# , 在所有 Python3 提交中击败了
# 7.69%
# 的用户
