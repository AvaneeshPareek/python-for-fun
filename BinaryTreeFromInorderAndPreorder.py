class Tree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = Tree(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.binaryTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.binaryTree(preorder[mid+1:], inorder[mid+1:])
        return


s = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
s.binaryTree(preorder, inorder)
stri = [1,2,3]
print(stri[1:1])