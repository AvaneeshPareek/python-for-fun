class Tree:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

root = Tree(4)
root.left = Tree(2)
root.left.left = Tree(1)
root.left.right = Tree(3)
root.right = Tree(7)
root.right.left = Tree(6)
root.right.right = Tree(9)

class Solution:
    def fliptree(self, root):
        if not root:
            return

        temp = root.left
        root.left = root.right
        root.right = temp
        self.fliptree(root.left)
        self.fliptree(root.right)

    def printTree(self,root):
        if not root:
            return
        print(root.val,end=' ')
        self.printTree(root.left)
        self.printTree(root.right)

        


s = Solution()
print('before:')
s.printTree(root)
s.fliptree(root)
print('after:')
s.printTree(root)