# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def dfs(node, _max):
            if node and node.val > _max:
                _max = node.val
            return (node.val == _max)+dfs(node.left, _max)+dfs(node.right, _max) if node else 0
        return dfs(root, -10000) # the minimum value is -10000 according to the constraints


