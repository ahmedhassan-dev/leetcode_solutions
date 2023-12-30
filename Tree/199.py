# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                # print(node.val, "depth ", depth, "view ",len(view))
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view
