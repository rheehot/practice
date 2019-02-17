#   https://leetcode.com/problems/cousins-in-binary-tree

#   https://leetcode.com/problems/cousins-in-binary-tree/solution


from TreeNode import TreeNode
from collections import defaultdict

class Solution:
    #   runtime; 52ms, 100.00%
    #   memory; 12.5MB, 100.00%
    def isCousins(self, root, x, y):
        if root is None:
            return True
        if x == root.val or y == root.val:
            return False
        q, depthParentDict = [], defaultdict(list)
        if root.left:
            q.append((1, root, root.left))
        if root.right:
            q.append((1, root, root.right))
        while q:
            depth, parent, node = q.pop(0)
            depthParentDict[node.val] = [depth, parent.val]
            if x in depthParentDict and y in depthParentDict:
                xDepth, xParent = depthParentDict[x]
                yDepth, yParent = depthParentDict[y]
                if xDepth == yDepth and xParent != yParent:
                    return True
                else:
                    return False
            if node.left:
                q.append((depth + 1, node, node.left))
            if node.right:
                q.append((depth + 1, node, node.right))
        return False


s = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.right.right = TreeNode(5)
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.right = TreeNode(4)
data = [(root1, 4, 3, False),
        (root2, 5, 4, True),
        (root3, 2, 3, False),
        ]
for root, x, y, expected in data:
    real = s.isCousins(root, x, y)
    print('{}, {}, {}, expected {}, real {}, result {}'.format(root, x, y, expected, real, expected == real))
