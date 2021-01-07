class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.pre=None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.head.next=self.head
        self.head.pre=self.head
        self.size=0

    def get(self, key: int) -> int:
        if key not in self.cache:return -1
        node=self.cache[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            self.delete(node)
            self.cache[key]=Node(key,value)
            self.add(self.cache[key])
        else:
            self.size+=1
            if self.size>self.capacity:
                self.cache.pop(self.head.pre.key)
                self.removetail()
                self.size-=1
            self.cache[key]=Node(key,value)
            self.add(self.cache[key])
    def add(self,node):
        self.head.next.pre=node
        node.next=self.head.next
        node.pre=self.head
        self.head.next=node
    def delete(self,node):
        node.next.pre=node.pre
        node.pre.next=node.next
    def removetail(self):
        self.head.pre.pre.next=self.head
        self.head.pre=self.head.pre.pre
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# 执行用时：
# 188 ms
# , 在所有 Python3 提交中击败了
# 72.18%
# 的用户
# 内存消耗：
# 23.4 MB
# , 在所有 Python3 提交中击败了
# 12.99%
# 的用户