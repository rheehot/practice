#   https://leetcode.com/problems/range-sum-of-bst

#   https://leetcode.com/problems/range-sum-of-bst/solution


from TreeNode import TreeNode


class Solution:
    #   540ms, 9.17%
    def rangeSumBST0(self, root, L, R):
        self._sum = 0
        def add(node):
            if node is None:
                return
            if L <= node.val <= R:
                self._sum += node.val
            add(node.left)
            add(node.right)
        add(root)
        return self._sum

    #   572ms, 5.37%
    def rangeSumBST(self, root, L, R):
        if root is None:
            return 0
        q, _sum = [root], 0
        while q:
            n = q.pop(0)
            if L <= n.val <= R:
                _sum += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return _sum


s = Solution()

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.right = TreeNode(18)
print(s.rangeSumBST(root, 7, 15) == 32)

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(7)
root.left.right.left = TreeNode(6)
root.right = TreeNode(15)
root.right.left = TreeNode(13)
root.right.right = TreeNode(18)
print(s.rangeSumBST(root, 6, 10) == 23)
