def reverse(x: int) -> int:
    if x == 0:
        return 0
    s = str(x)
    if s[0] != '-':
        s = s[::-1]
        while s[0] == '0':
            s = s[1:]

    else:
        s = s[1:]
        s = s[::-1]
        while s[0] == '0':
            s = s[1:]
        s = format('-%s' % s)
    return int(s) if -2 ** 31 <= int(s) <= 2 ** 31 - 1 else 0


class Solution:
    pass


print(reverse(-10))
