class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x = -x
        ans = 0
        while x > 0:
            t = x % 10
            x //= 10
            ans = ans * 10 + t
        if flag:
            ans=-ans
        print(ans)

        return 0 if ans<-2**31 or ans>2**31-1 else ans