# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        nodes = []

        def dfs(node):
            if not node: return

            if len(nodes) < k:
                dfs(node.left)
                nodes.append(node.val)
                dfs(node.right)

        dfs(root)
        return nodes[k - 1]