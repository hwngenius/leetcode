class CQueue:

    def __init__(self):
        self.A = []
        self.B = []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if len(self.A) == 0 and len(self.B) == 0:
            return -1
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
        return self.B.pop()


# 执行用时：
# 584 ms
# , 在所有 Python3 提交中击败了
# 55.87%
# 的用户
# 内存消耗：
# 17 MB
# , 在所有 Python3 提交中击败了
# 100.00%
# 的用户