class Tree:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def isSubTree(self, root, subRoot):
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubTree(root.left, subRoot) or self.isSubTree(root.right, subRoot))

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))

root = Tree(3)
root.left = Tree(4)
root.right = Tree(5)
root.left.left = Tree(1)
root.left.right = Tree(2)

subRoot = Tree(4)
subRoot.left = Tree(1)
subRoot.right = Tree(2)

s = Solution()
print(s.isSubTree(root,subRoot))