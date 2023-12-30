# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        def buildTreeHelper(stop=None):
            if inorder and inorder[0] != stop:
                root = TreeNode(preorder.popleft())
                root.left = buildTreeHelper(root.val)
                inorder.popleft()
                root.right = buildTreeHelper(stop)
                return root
        preorder = deque(preorder)
        inorder = deque(inorder)
        return buildTreeHelper()