import collections

class Tree:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.right = right
        self.left = left


class Solution:
    def lot(self, root):
        res = []
        q = collections.deque()
        q.append(root)
        while q:
            log = []
            l = len(q)
            for i in range(l):
                
                node = q.popleft()
                if node:
                    log.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if log:
                res.append(log)
        return res

root = Tree(3)
right = Tree(20)
left = Tree(9)
root.left = left
root.right = right
root.right.right = Tree(7)
root.right.left = Tree(15)

s = Solution()
print(s.lot(root))