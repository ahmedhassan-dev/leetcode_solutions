# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        leaf_seq_1 = []
        leaf_seq_2 = []
        
        def helper(node, container):
            if node:
                helper(node.left, container)
                if not node.left and not node.right:
                    container.append(node.val)
                helper(node.right, container)
        helper(root1, leaf_seq_1)
        helper(root2, leaf_seq_2)
        return leaf_seq_1 == leaf_seq_2
