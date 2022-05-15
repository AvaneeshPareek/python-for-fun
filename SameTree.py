class Tree:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


p = Tree(1)
p_two = Tree(2)
p_three = Tree(3)
p.left = p_two
p.right = p_three

q = Tree(1)
q_two = Tree(2)
q_three = Tree(3)
q.left = q_two
q.right = q_three

class Solution:
    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))

s = Solution()
print(s.sameTree(p,q))

