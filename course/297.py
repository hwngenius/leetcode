# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        level = []
        level.append(root)
        ans = []

        def is_all_None(level):
            for node in level:
                if node is not None:
                    return False
            return True

        while True:
            level_t = []
            for node in level:
                if node is not None:
                    level_t.append(node.left)
                    level_t.append(node.right)
                    flag_t = True
                    ans.append(node.val)
                else:
                    level_t += [None] * 2
                    ans.append(None)
            level = level_t
            if is_all_None(level):
                break

        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        length=1
        while len(data)!=0:


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

print(Codec().serialize(root))
