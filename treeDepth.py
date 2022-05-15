class Tree:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

root = Tree(3)
nine = Tree(9)
twenty = Tree(20)
fifteen = Tree(15)
seven = Tree(7)

root.left = nine
root.right = twenty
twenty.left = fifteen
twenty.right = seven

s = Solution()
print(s.maxDepth(root))